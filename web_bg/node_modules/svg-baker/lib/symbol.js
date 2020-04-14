const { renderer } = require('posthtml-svg-mode');
const { getRoot, getHash } = require('./utils');
const defaultFactory = require('./symbol-factory');
const FileRequest = require('./request');
const clone = require('clone');

class SpriteSymbol {
  constructor({ id, tree, request }) {
    this.id = id;
    this._tree = tree;
    this.request = request;
  }

  /**
   * @param {Object} options
   * @param {string} options.id
   * @param {string} options.content
   * @param {string|FileRequest} options.request
   * @param {Function<Promise<PostHTMLProcessingResult>>} [options.factory]
   * @return {Promise<SpriteSymbol>}
   */
  static create(options) {
    const { content, factory = defaultFactory } = options;
    const request = typeof options.request === 'string' ? new FileRequest(options.request) : options.request;
    const id = typeof options.id === 'undefined' ? getHash(`${request.toString()}_${content}`) : options.id;

    return factory({ content, request, id })
      .then(({ tree }) => new SpriteSymbol({ id, request, tree }));
  }

  /**
   * @return {string}
   */
  get viewBox() {
    const root = getRoot(this.tree);
    return root.attrs ? root.attrs.viewBox : null;
  }

  get tree() {
    return clone(this._tree);
  }

  /**
   * @return {string}
   */
  get useId() {
    return `${this.id}-usage`;
  }

  /**
   * @return {string}
   */
  render() {
    return renderer(this.tree);
  }
}

module.exports = SpriteSymbol;
