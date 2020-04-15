'use strict'

// Encode code taken from the PlantUML website:
// http://plantuml.sourceforge.net/codejavascript2.html

// It is described as being "a transformation close to base64"
// The code has been slightly modified to pass linters

function encode6bit (b) {
  if (b < 10) {
    return String.fromCharCode(48 + b)
  }
  b -= 10
  if (b < 26) {
    return String.fromCharCode(65 + b)
  }
  b -= 26
  if (b < 26) {
    return String.fromCharCode(97 + b)
  }
  b -= 26
  if (b === 0) {
    return '-'
  }
  if (b === 1) {
    return '_'
  }
  return '?'
}

function append3bytes (b1, b2, b3) {
  var c1 = b1 >> 2
  var c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
  var c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
  var c4 = b3 & 0x3F
  var r = ''
  r += encode6bit(c1 & 0x3F)
  r += encode6bit(c2 & 0x3F)
  r += encode6bit(c3 & 0x3F)
  r += encode6bit(c4 & 0x3F)
  return r
}

module.exports = function (data) {
  var r = ''
  for (var i = 0; i < data.length; i += 3) {
    if (i + 2 === data.length) {
      r += append3bytes(data.charCodeAt(i), data.charCodeAt(i + 1), 0)
    } else if (i + 1 === data.length) {
      r += append3bytes(data.charCodeAt(i), 0, 0)
    } else {
      r += append3bytes(data.charCodeAt(i),
        data.charCodeAt(i + 1),
        data.charCodeAt(i + 2))
    }
  }
  return r
}
