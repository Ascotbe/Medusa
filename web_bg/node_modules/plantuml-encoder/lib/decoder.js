'use strict'

var inflate = require('./inflate')
var decode64 = require('./decode64')

module.exports.decode = function (encoded) {
  var deflated = decode64(encoded)
  return inflate(deflated)
}
