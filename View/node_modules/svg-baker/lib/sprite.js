const { renderer } = require('posthtml-svg-mode');
const defaultFactory = require('./sprite-factory');

class Sprite {
  constructor({ tree, filename }) {
    this.tree = tree;
    this.filename = filename;
  }

  /**
   * @param {Object} options
   * @param {Array<SpriteSymbol>} options.symbols
   * @param {string} options.filename Output sprite filename
   * @param {Function<Promise<PostHTMLProcessingResult>>} [options.factory]
   * @return {Promise<Sprite>}
   */
  static create(options) {
    const { symbols, filename, factory = defaultFactory } = options;
    return factory({ symbols }).then(({ tree }) => new Sprite({ tree, filename }));
  }

  /**
   * @return {string}
   */
  render() {
    return renderer(this.tree);
  }
}

module.exports = Sprite;
