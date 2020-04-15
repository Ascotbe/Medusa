var ensureRequire = require('../ensure-require.js')
const throwError = require('../throw-error')

module.exports = function (raw) {
  var html
  ensureRequire('jade', 'jade')
  var jade = require('jade')
  try {
    html = jade.compile(raw)()
  } catch (err) {
    throwError(err)
  }
  return html
}
