'use strict'

var deflate = require('./deflate')
var encode64 = require('./encode64')

module.exports.encode = function (puml) {
  var deflated = deflate(puml)
  return encode64(deflated)
}
