const ensureRequire = require('../ensure-require')
const compileBabel = require('./babel-compiler')
const loadBabelConfig = require('../load-babel-config.js')
const { loadTypescriptConfig } = require('../load-typescript-config')

module.exports = function compileTypescript (scriptContent, vueJestConfig, filePath) {
  ensureRequire('typescript', ['typescript'])
  const typescript = require('typescript')
  const tsConfig = loadTypescriptConfig(vueJestConfig)

  const res = typescript.transpileModule(scriptContent, tsConfig)
  const inputSourceMap = (res.sourceMapText !== undefined)
    ? JSON.parse(res.sourceMapText)
    : false // inputSourceMap must be a boolean, object, or undefined as per babel requirements

  // handle ES modules in TS source code in case user uses non commonjs module
  // output and there is no .babelrc.
  let inlineBabelConfig
  if (tsConfig.compilerOptions.module !== 'commonjs' && !loadBabelConfig(vueJestConfig, filePath)) {
    inlineBabelConfig = {
      plugins: [
        require('babel-plugin-transform-es2015-modules-commonjs')
      ]
    }
  }

  return compileBabel(res.outputText, inputSourceMap, inlineBabelConfig, vueJestConfig)
}

