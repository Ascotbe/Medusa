module.exports.info = function info (msg) {
  console.info('\n[vue-jest]: ' + (msg) + '\n')
}

module.exports.warn = function warn (msg) {
  console.warn('\n[vue-jest]: ' + (msg) + '\n')
}

module.exports.shouldLogStyleWarn = true
