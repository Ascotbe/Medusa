'use strict'

var pako = require('pako/lib/inflate.js')

module.exports = function (data) {
  return pako.inflateRaw(data, { to: 'string' })
}
