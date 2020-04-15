const merge = require('deepmerge');
const defaults = require('./config');
const utils = require('./utils');

const loaderDefaults = defaults.loader;
const isomorphicSpriteModule = 'svg-sprite-loader/runtime/sprite.build';
const isomorphicSymbolModule = 'svg-baker-runtime/symbol';

const isTargetBrowser = target => target === 'web' || target === 'electron-renderer';

/**
 * @param {Object} params
 * @param {Object} [params.config] Parsed loader config {@see SVGSpriteLoaderConfig}
 * @param {LoaderContext} context Loader context {@see https://webpack.js.org/api/loaders/#the-loader-context}
 * @return {Object}
 */
module.exports = function configurator({ config, context, target }) {
  const module = context._module;
  const compiler = context._compiler;
  const compilerName = compiler.name;

  const autoConfigured = {
    spriteModule: isTargetBrowser(target) ? loaderDefaults.spriteModule : isomorphicSpriteModule,
    symbolModule: isTargetBrowser(target) ? loaderDefaults.symbolModule : isomorphicSymbolModule,
    extract: utils.isModuleShouldBeExtracted(module),
    esModule: context.version && context.version >= 2
  };

  const finalConfig = merge.all([loaderDefaults, autoConfigured, config || {}]);

  /**
   * esModule should be `false` when compiles via extract-text-webpack-plugin or html-webpack-plugin.
   * Because this compilers executes module as usual node module so export should be always in commonjs style.
   * This could be dropped when Node.js will support ES modules natively :)
   * @see https://git.io/vS7Sn
   * @see https://git.io/v9w60
   */
  if (compilerName && (
      compilerName.includes('extract-text-webpack-plugin') ||
      compilerName.includes('html-webpack-plugin')
    )) {
    finalConfig.esModule = false;
  }

  return finalConfig;
};
