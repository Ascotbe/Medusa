/**
 * @fileoverview Transform the given HTML Entity string into plain string.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

/**
 * @module string
 */

/**
 * Transform the given HTML Entity string into plain string.
 * @param {String} htmlEntity - HTML Entity type string
 * @returns {String} Plain string
 * @memberof module:string
 * @example
 * var decodeHTMLEntity = require('tui-code-snippet/string/decodeHTMLEntity'); // node, commonjs
 *
 * var htmlEntityString = "A &#39;quote&#39; is &lt;b&gt;bold&lt;/b&gt;"
 * var result = decodeHTMLEntity(htmlEntityString); //"A 'quote' is <b>bold</b>"
 */
function decodeHTMLEntity(htmlEntity) {
  var entities = {
    '&quot;': '"',
    '&amp;': '&',
    '&lt;': '<',
    '&gt;': '>',
    '&#39;': '\'',
    '&nbsp;': ' '
  };

  return htmlEntity.replace(/&amp;|&lt;|&gt;|&quot;|&#39;|&nbsp;/g, function(m0) {
    return entities[m0] ? entities[m0] : m0;
  });
}

module.exports = decodeHTMLEntity;
