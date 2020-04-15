const throwError = require('./throw-error')

module.exports = function (name, deps) {
  var i, len
  var missing = []
  if (typeof deps === 'string') {
    deps = [deps]
  }
  for (i = 0, len = deps.length; i < len; i++) {
    var mis
    var req = deps[i]
    if (typeof req === 'string') {
      mis = req
    } else {
      mis = req[1]
      req = req[0]
    }
    try {
      // hack for babel-runtime because it does not expose "main" field
      if (req === 'babel-runtime') {
        req = 'babel-runtime/core-js'
      }
      require.resolve(req)
    } catch (e) {
      missing.push(mis)
    }
  }
  if (missing.length > 0) {
    var message = 'You are trying to use "' + name + '". '
    var npmInstall = 'npm install --save-dev ' + missing.join(' ')
    if (missing.length > 1) {
      var last = missing.pop()
      message += missing.join(', ') + ' and ' + last + ' are '
    } else {
      message += missing[0] + ' is '
    }
    message += 'missing.\n\nTo install run:\n' + npmInstall
    throwError(message)
  }
}
