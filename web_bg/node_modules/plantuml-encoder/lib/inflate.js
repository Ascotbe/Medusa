'use strict'

const zlib = require('zlib')

module.exports = function (data) {
  return zlib.inflateRawSync(Buffer.from(data, 'binary')).toString()
}
