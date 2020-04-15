const babel = require('babel-core')
const loadBabelConfig = require('../load-babel-config.js')

module.exports = function compileBabel (scriptContent, inputSourceMap, inlineConfig, vueJestConfig, filePath) {
  const babelConfig = inlineConfig || loadBabelConfig(vueJestConfig, filePath)

  if (!babelConfig) {
    return {
      code: scriptContent,
      sourceMap: inputSourceMap
    }
  }

  const sourceMapOptions = {
    sourceMaps: true,
    inputSourceMap: inputSourceMap
  }

  const babelOptions = Object.assign(sourceMapOptions, babelConfig)

  // babel throws error if filename is undefined, "unknown" is default
  if (!babelOptions.filename) babelOptions.filename = 'unknown'
  const res = babel.transform(scriptContent, babelOptions)

  return {
    code: res.code,
    sourceMap: res.map
  }
}

