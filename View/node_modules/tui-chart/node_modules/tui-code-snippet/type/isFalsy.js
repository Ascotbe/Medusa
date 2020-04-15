/**
 * @fileoverview Check whether the given variable is falsy or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var isTruthy = require('./isTruthy');

/**
 * Check whether the given variable is falsy or not.
 * If the given variable is null or undefined or false, returns true.
 * @param {*} obj - Target for checking
 * @returns {boolean} Is falsy?
 * @memberof module:type
 */
function isFalsy(obj) {
  return !isTruthy(obj);
}

module.exports = isFalsy;
