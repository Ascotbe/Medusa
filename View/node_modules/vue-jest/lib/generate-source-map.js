const path = require('path')
const sourceMap = require('source-map')
const splitRE = /\r?\n/g

module.exports = function generateSourceMap (script, output, filePath, content, inputMap) {
  var hashedFilename = path.basename(filePath)
  var map = new sourceMap.SourceMapGenerator()
  map.setSourceContent(hashedFilename, content)
  // check input source map from babel/coffee etc
  var inputMapConsumer = inputMap && new sourceMap.SourceMapConsumer(inputMap)
  var generatedOffset = (output ? output.split(splitRE).length : 0) + 1
  script.split(splitRE).forEach(function (line, index) {
    var ln = index + 1
    var originalLine = inputMapConsumer
      ? inputMapConsumer.originalPositionFor({ line: ln, column: 0 }).line
      : ln
    if (originalLine) {
      map.addMapping({
        source: hashedFilename,
        generated: {
          line: ln + generatedOffset,
          column: 0
        },
        original: {
          line: originalLine,
          column: 0
        }
      })
    }
  })
  map._hashedFilename = hashedFilename
  return map
}
