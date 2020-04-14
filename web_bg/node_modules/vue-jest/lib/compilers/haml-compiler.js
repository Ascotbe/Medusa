var ensureRequire = require('../ensure-require.js')
const throwError = require('../throw-error')

module.exports = function (raw) {
  var html
  ensureRequire('hamljs', 'hamljs')
  var haml = require('hamljs')
  try {
    html = haml.render(raw)
  } catch (err) {
    throwError(err)
  }
  return html
}
