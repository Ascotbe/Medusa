var chalk = require('chalk')
var vueCompiler = require('vue-template-compiler')
var transpile = require('vue-template-es2015-compiler')
var compilePug = require('./compilers/pug-compiler')
var compileJade = require('./compilers/jade-compiler')
var compileHaml = require('./compilers/haml-compiler')
const throwError = require('./throw-error')

function getTemplateContent (templatePart, config) {
  if (templatePart.lang === 'pug') {
    return compilePug(templatePart, config)
  }
  if (templatePart.lang === 'jade') {
    return compileJade(templatePart.content)
  }
  if (templatePart.lang === 'haml') {
    return compileHaml(templatePart.content)
  }
  return templatePart.content
}

module.exports = function compileTemplate (templatePart, config) {
  var templateContent = getTemplateContent(templatePart, config)
  var compiled = vueCompiler.compile(templateContent)
  if (compiled.errors.length) {
    compiled.errors.forEach(function (msg) {
      console.error('\n' + chalk.red(msg) + '\n')
    })
    throwError('Vue template compilation failed')
  } else {
    return compile(compiled, templatePart.attrs.functional)
  }
}

function compile (compiled, isFunctional) {
  function toFunction (code) {
    var renderArgs = isFunctional ? '_h, _vm' : ''
    return transpile('function render (' + renderArgs + ') {' + code + '}', {
      transforms: { stripWithFunctional: isFunctional }
    })
  }

  return {
    render: toFunction(compiled.render),
    staticRenderFns: '[' + compiled.staticRenderFns.map(toFunction).join(',') + ']'
  }
}
