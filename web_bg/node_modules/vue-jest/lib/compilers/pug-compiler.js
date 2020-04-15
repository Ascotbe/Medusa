var ensureRequire = require('../ensure-require.js')
const throwError = require('../throw-error')

module.exports = function (templatePart, config) {
  const options = (config && config['pug']) || {}
  if (templatePart.filename) {
    options.filename = templatePart.filename
  }
  var html
  ensureRequire('pug', 'pug')
  var jade = require('pug')
  try {
    html = jade.compile(templatePart.content, options)()
  } catch (err) {
    throwError(err)
  }
  return html
}
