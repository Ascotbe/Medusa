/* eslint-disable max-len */
const fs = require('fs');
const PACKAGE_NAME = require('../package.json').name;

module.exports = {
  PACKAGE_NAME,
  NAMESPACE: fs.realpathSync(__dirname),
  EXTRACTABLE_MODULE_ISSUER_PATTERN: /\.(css|sass|scss|less|styl|html)$/i,
  SPRITE_PLACEHOLDER_PATTERN: /\{\{sprite-filename\|([^}}]*)\}\};?/gi,

  /**
   * Overridable loader options
   * @typedef {Object} SVGSpriteLoaderConfig
   */
  loader: {
    /**
     * How `<symbol id>` should be named.
     * Full list of supported patterns see at [loader-utils#interpolatename docs](https://github.com/webpack/loader-utils#interpolatename).
     * @type {string}
     */
    symbolId: '[name]',

    /**
     * Regular expression passed to interpolateName.
     * Supports the interpolateName [N] pattern inserting the N-th match.
     * @type {string}
     */
    symbolRegExp: '',

    /**
     * Path to Node.js module which generates client runtime.
     * @type {string}
     */
    runtimeGenerator: require.resolve('./runtime-generator'),

    /**
     * Arbitrary data passed to runtime generator.
     * @type {*}
     */
    runtimeOptions: undefined,

    /**
     * Should runtime be compatible with earlier v0.* loader versions.
     * Will be removed in 3 version.
     * @type {boolean}
     * @deprecated
     */
    runtimeCompat: false,

    /**
     * Path to sprite module which will be compiled and executed at runtime.
     * By default depends on 'target' webpack config option:
     * - `svg-sprite-loader/runtime/browser-sprite.build` for 'web' target.
     * - `svg-sprite-loader/runtime/sprite.build` for all other targets.
     * @type {string}
     * @autoconfigured
     */
    spriteModule: 'svg-sprite-loader/runtime/browser-sprite.build',

    /**
     * Path to symbol module.
     * By default depends on 'target' webpack config option:
     * - `svg-baker-runtime/browser-symbol` for 'web' target.
     * - `svg-baker-runtime/symbol` for all other targets.
     * @type {string}
     * @autoconfigured
     */
    symbolModule: 'svg-baker-runtime/browser-symbol',

    /**
     * Generated export format:
     * - when `true` loader will produce `export default ...`.
     * - when `false` the result is `module.exports = ...`.
     * By default depends on used webpack version. `true` for Webpack >= 2, `false` otherwise.
     * @type {boolean}
     * @autoconfigured
     */
    esModule: true,

    /**
     * Turns loader in extract mode.
     * Enables automatically if SVG image was imported from css/scss/sass/less/styl/html.
     * @type {boolean}
     * @autoconfigured
     */
    extract: false,

    /**
     * Filename for generated sprite. `[chunkname]` placeholder can be used.
     * @type {string}
     */
    spriteFilename: 'sprite.svg'
  }
};
