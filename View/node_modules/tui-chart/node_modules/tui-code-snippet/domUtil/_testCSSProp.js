/**
 * @fileoverview Check specific CSS style is available.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

/**
 * Check specific CSS style is available.
 * @param {array} props property name to testing
 * @returns {(string|boolean)} return true when property is available
 * @private
 */
function testCSSProp(props) {
  var style = document.documentElement.style;
  var i, len;

  for (i = 0, len = props.length; i < len; i += 1) {
    if (props[i] in style) {
      return props[i];
    }
  }

  return false;
}

module.exports = testCSSProp;
