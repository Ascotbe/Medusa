const splitRE = /\r?\n/g

module.exports = function addTemplateMapping (content, parts, output, map, beforeLines) {
  var afterLines = output.split(splitRE).length
  var templateLine = content.slice(0, parts.template.start).split(splitRE).length
  for (; beforeLines < afterLines; beforeLines++) {
    map.addMapping({
      source: map._hashedFilename,
      generated: {
        line: beforeLines,
        column: 0
      },
      original: {
        line: templateLine,
        column: 0
      }
    })
  }
}
