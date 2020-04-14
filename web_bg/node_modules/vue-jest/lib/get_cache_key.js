var crypto = require('crypto')

module.exports = function getCacheKey (fileData, filename, configString) {
  return crypto.createHash('md5')
    .update(fileData + filename + configString, 'utf8')
    .digest('hex')
}
