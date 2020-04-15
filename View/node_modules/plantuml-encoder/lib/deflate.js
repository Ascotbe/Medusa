'use strict'

const zlib = require('zlib')

module.exports = function (data) {
  return zlib.deflateRawSync(data, { level: 9 }).toString('binary')
}
