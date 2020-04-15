/**
 * @fileoverview Check whether the given variable is a boolean or not. (for multiple frame environments)
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

/**
 * Check whether the given variable is a boolean or not.
 * If the given variable is a boolean, return true.
 * (It is used for multiple frame environments)
 * @param {*} obj - Target for checking
 * @returns {boolean} Is a boolean?
 * @memberof module:type
 */
function isBooleanSafe(obj) {
  return Object.prototype.toString.call(obj) === '[object Boolean]';
}

module.exports = isBooleanSafe;
