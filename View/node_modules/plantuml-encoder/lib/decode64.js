'use strict'

// Reverse of
// http://plantuml.sourceforge.net/codejavascript2.html

// It is described as being "a transformation close to base64"
// The code has been slightly modified to pass linters

function decode6bit (cc) {
  var c = cc.charCodeAt(0)
  if (cc === '_') return 63
  if (cc === '-') return 62
  if (c >= 97) return c - 61 // - 97 + 26 + 10
  if (c >= 65) return c - 55 // - 65 + 10
  if (c >= 48) return c - 48
  return '?'
}

function extract3bytes (data) {
  var c1 = decode6bit(data[0])
  var c2 = decode6bit(data[1])
  var c3 = decode6bit(data[2])
  var c4 = decode6bit(data[3])
  var b1 = c1 << 2 | (c2 >> 4) & 0x3F
  var b2 = (c2 << 4) & 0xF0 | (c3 >> 2) & 0xF
  var b3 = (c3 << 6) & 0xC0 | c4 & 0x3F

  return [b1, b2, b3]
}

module.exports = function (data) {
  var r = ''
  var i = 0
  for (i = 0; i < data.length; i += 4) {
    var t = extract3bytes(data.substring(i, i + 4))
    r = r + String.fromCharCode(t[0])
    r = r + String.fromCharCode(t[1])
    r = r + String.fromCharCode(t[2])
  }
  return r
}
