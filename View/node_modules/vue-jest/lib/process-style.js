const getVueJestConfig = require('./get-vue-jest-config')
const cssExtract = require('extract-from-css')

module.exports = function processStyle (stylePart, filePath, jestConfig = {}) {
  const vueJestConfig = getVueJestConfig(jestConfig)

  if (!stylePart || vueJestConfig.experimentalCSSCompile === false) {
    return {}
  }

  const processStyleByLang = lang => require('./compilers/' + lang + '-compiler')(stylePart.content, filePath, jestConfig)

  let cssCode = stylePart.content
  switch (stylePart.lang) {
    case 'styl':
    case 'stylus':
      cssCode = processStyleByLang('stylus')
      break
    case 'scss':
      cssCode = processStyleByLang('scss')
      break
    case 'sass':
      cssCode = processStyleByLang('sass')
      break
  }

  const cssNames = cssExtract.extractClasses(cssCode)

  const obj = {}
  for (let i = 0, l = cssNames.length; i < l; i++) {
    obj[cssNames[i]] = cssNames[i]
  }

  return obj
}
