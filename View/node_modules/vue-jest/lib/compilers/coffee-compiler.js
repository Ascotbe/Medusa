var ensureRequire = require('../ensure-require.js')
const throwError = require('../throw-error')
const loadBabelConfig = require('../load-babel-config.js')

module.exports = function (raw, vueJestConfig, filePath) {
  ensureRequire('coffee', ['coffeescript'])
  var coffee = require('coffeescript')
  var compiled
  var babelConfig = loadBabelConfig(vueJestConfig, filePath)

  // babel throws error if filename is undefined, "unknown" is default
  if (!babelConfig.filename) babelConfig.filename = 'unknown'

  try {
    compiled = coffee.compile(raw, {
      bare: true,
      sourceMap: true,
      transpile: babelConfig
    })

    return {
      code: compiled.js,
      map: compiled.v3SourceMap
    }
  } catch (err) {
    throwError(err)
  }
}
