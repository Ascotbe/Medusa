module.exports = function error (msg) {
  throw new Error('\n[vue-jest] Error: ' + (msg) + '\n')
}
