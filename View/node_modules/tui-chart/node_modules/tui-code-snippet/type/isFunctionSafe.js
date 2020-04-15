/**
 * @fileoverview Check whether the given variable is a function or not. (for multiple frame environments)
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

/**
 * Check whether the given variable is a function or not.
 * If the given variable is a function, return true.
 * (It is used for multiple frame environments)
 * @param {*} obj - Target for checking
 * @returns {boolean} Is a function?
 * @memberof module:type
 */
function isFunctionSafe(obj) {
  return Object.prototype.toString.call(obj) === '[object Function]';
}

module.exports = isFunctionSafe;
