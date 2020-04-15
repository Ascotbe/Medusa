const path = require('path')
const fs = require('fs')
const ensureRequire = require('../ensure-require')
const getVueJestConfig = require('../get-vue-jest-config')
const logger = require('../logger')

const applyModuleNameMapper = require('./helpers/module-name-mapper-helper')

/**
 * This module is meant to compile scss
 *
 * @param {String} content - the content of the scss string that should be compiled
 * @param {String} filePath - the path of the file holding the scss
 * @param {Object} jestConfig - the complete jest config
 * @returns {String} styles - the compiled scss
 */
module.exports = (content, filePath, jestConfig = {}) => {
  const vueJestConfig = getVueJestConfig(jestConfig)

  ensureRequire('scss', ['node-sass'])
  const sass = require('node-sass')

  let scssResources = ''
  if (vueJestConfig.resources && vueJestConfig.resources.scss) {
    scssResources = vueJestConfig.resources.scss
      .map(scssResource => path.resolve(process.cwd(), scssResource))
      .filter(scssResourcePath => fs.existsSync(scssResourcePath))
      .map(scssResourcePath => fs.readFileSync(scssResourcePath).toString())
      .join('\n')
  }

  try {
    return sass.renderSync({
      data: scssResources + content,
      outputStyle: 'compressed',
      importer: (url, prev, done) => ({ file: applyModuleNameMapper(url, prev === 'stdin' ? filePath : prev, jestConfig) })
    }).css.toString()
  } catch (err) {
    if (!vueJestConfig.hideStyleWarn) {
      logger.warn(`There was an error rendering the SCSS in ${filePath}. SCSS is fully supported by vue-jest. Still some features might throw errors. Webpack aliases are a common cause of errors. If you use Webpack aliases, please use jest's suggested way via moduleNameMapper which is supported.`)
      logger.warn(`Error while compiling styles: ${err}`)
    }
  }

  return ''
}
