/**
 * @fileoverview Check whether the given variable is a HTML tag or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

/**
 * Check whether the given variable is a HTML tag or not.
 * If the given variables is a HTML tag, return true.
 * @param {*} html - Target for checking
 * @returns {boolean} Is HTML tag?
 * @memberof module:type
 */
function isHTMLTag(html) {
  if (typeof HTMLElement === 'object') {
    return (html && (html instanceof HTMLElement));
  }

  return !!(html && html.nodeType && html.nodeType === 1);
}

module.exports = isHTMLTag;
