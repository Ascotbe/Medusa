const { stringifyRequest } = require('loader-utils');
const {
  stringify,
  stringifySymbol,
  generateImport,
  generateExport,
  generateSpritePlaceholder
} = require('./utils');

/**
 * @param {Object} params
 * @param {SpriteSymbol} params.symbol - Sprite symbol instance {@see https://git.io/v9k8g}
 * @param {SVGSpriteLoaderConfig} params.config - Parsed loader config
 * @param {string} params.context - Context folder of current processing module
 * @param {Object} params.loaderContext {@see https://webpack.js.org/api/loaders/#the-loader-context}
 * @return {string}
 */
function runtimeGenerator(params) {
  const { symbol, config, context } = params;
  const { extract, esModule, spriteModule, symbolModule, runtimeCompat, publicPath } = config;
  let runtime;

  if (extract) {
    const spritePlaceholder = generateSpritePlaceholder(symbol.request.file);
    const path = stringify(publicPath) || '__webpack_public_path__';
    const data = `{
      id: ${stringify(symbol.useId)},
      viewBox: ${stringify(symbol.viewBox)},
      url: ${path} + ${stringify(spritePlaceholder)},
      toString: function () {
        return this.url;
      }
    }`;
    runtime = generateExport(data, esModule);
  } else {
    const spriteModuleImport = stringifyRequest({ context }, spriteModule);
    const symbolModuleImport = stringifyRequest({ context }, symbolModule);

    runtime = [
      generateImport('SpriteSymbol', symbolModuleImport, esModule),
      generateImport('sprite', spriteModuleImport, esModule),

      `var symbol = new SpriteSymbol(${stringifySymbol(symbol)})`,
      'var result = sprite.add(symbol)',

      generateExport(runtimeCompat ? '"#" + symbol.id' : 'symbol', esModule)
    ].join(';\n');
  }

  return runtime;
}

module.exports = runtimeGenerator;
