'use strict'

var pako = require('pako/lib/deflate.js')

module.exports = function (data) {
  return pako.deflateRaw(data, { level: 9, to: 'string' })
}
