/**
 * @fileoverview Convert kebab-case
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

/**
 * Convert kebab-case
 * @param {string} key - string to be converted to Kebab-case
 * @private
 */
function convertToKebabCase(key) {
  return key.replace(/([A-Z])/g, function(match) {
    return '-' + match.toLowerCase();
  });
}

module.exports = convertToKebabCase;
