// TODO refactor this smelly code!
const loaderDefaults = require('../config').loader;
const getAllModules = require('./get-all-modules');
const isModuleShouldBeExtracted = require('./is-module-should-be-extracted');
const getModuleChunk = require('./get-module-chunk');
const interpolate = require('./interpolate');
const getMatchedRule = require('./get-matched-rule');

class MappedListItem {
  /**
   * @param {SpriteSymbol} symbol
   * @param {NormalModule} module
   * @param {string} spriteFilename
   */
  constructor(symbol, module, spriteFilename) {
    this.symbol = symbol;
    this.module = module;
    this.resource = symbol.request.file;
    this.spriteFilename = spriteFilename;
  }

  get url() {
    return `${this.spriteFilename}#${this.symbol.id}`;
  }

  get useUrl() {
    return `${this.spriteFilename}#${this.symbol.useId}`;
  }
}

class MappedList {
  /**
   * @param {SpriteSymbol[]} symbols
   * @param {Compilation} compilation
   */
  constructor(symbols, compilation, shouldLog = false) {
    const { compiler } = compilation;

    this.symbols = symbols;
    this.rule = getMatchedRule(compiler);
    this.allModules = getAllModules(compilation);
    this.spriteModules = this.allModules.filter(isModuleShouldBeExtracted);
    this.shouldLog = shouldLog;
    this.items = this.create();
  }

  /**
   * @param {MappedListItem[]} data
   * @return {Object<string, MappedListItem>}
   */
  static groupItemsBySpriteFilename(data) {
    return data
      .map(item => item.spriteFilename)
      .filter((value, index, self) => self.indexOf(value) === index)
      .reduce((acc, spriteFilename) => {
        acc[spriteFilename] = data.filter(item => item.spriteFilename === spriteFilename);
        return acc;
      }, {});
  }

  /**
   * @param {MappedListItem[]} data
   * @param {Function} [mapper] Custom grouper function
   * @return {Object<string, MappedListItem>}
   */
  static groupItemsBySymbolFile(data, mapper) {
    return data.reduce((acc, item) => {
      if (mapper) {
        mapper(acc, item);
      } else {
        acc[item.resource] = item;
      }
      return acc;
    }, {});
  }

  /**
   * @return {MappedListItem[]}
   */
  create() {
    const { symbols, spriteModules, allModules, rule } = this;

    const data = symbols.reduce((acc, symbol) => {
      const resource = symbol.request.file;
      const module = spriteModules.find((m) => {
        return 'resource' in m ? m.resource.split('?')[0] === resource : false;
      });

      let spriteFilename = rule.spriteFilename || loaderDefaults.spriteFilename;

      const chunk = module ? getModuleChunk(module, allModules) : null;

      if (typeof spriteFilename !== 'function' && chunk && chunk.name) {
        spriteFilename = spriteFilename.replace('[chunkname]', chunk.name);
      } else if (typeof spriteFilename === 'function') {
        spriteFilename = spriteFilename(resource);
      }

      if (rule && module) {
        acc.push(new MappedListItem(symbol, module, spriteFilename));
      }

      return acc;
    }, []);

    // Additional pass to interpolate [hash] in spriteFilename
    const itemsBySpriteFilename = MappedList.groupItemsBySpriteFilename(data);
    const filenames = Object.keys(itemsBySpriteFilename);

    filenames.forEach((filename) => {
      if (!filename.includes('hash')) {
        return;
      }

      const items = itemsBySpriteFilename[filename];
      const spriteSymbols = items.map(item => item.symbol);
      const content = spriteSymbols.map(s => s.render()).join('');
      const interpolatedName = interpolate(filename, {
        resourcePath: filename,
        content
      });

      items
        .filter(item => item.spriteFilename !== interpolatedName)
        .forEach(item => item.spriteFilename = interpolatedName);
    });

    return data;
  }

  /**
   * @return {Object<string, MappedListItem>}
   */
  groupItemsBySpriteFilename() {
    return MappedList.groupItemsBySpriteFilename(this.items);
  }

  /**
   * @param {Function} [mapper] Custom grouper function
   * @return {Object<string, MappedListItem>}
   */
  groupItemsBySymbolFile(mapper) {
    return MappedList.groupItemsBySymbolFile(this.items, mapper);
  }
}

module.exports = MappedList;
