/* eslint-disable complexity */
/**
 * @fileoverview Check whether the given variable is empty(null, undefined, or empty array, empty object) or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var isString = require('./isString');
var isExisty = require('./isExisty');
var isArray = require('./isArray');
var isArguments = require('./isArguments');
var isObject = require('./isObject');
var isFunction = require('./isFunction');

/**
 * Check whether given argument is empty string
 * @param {*} obj - Target for checking
 * @returns {boolean} whether given argument is empty string
 * @private
 */
function _isEmptyString(obj) {
  return isString(obj) && obj === '';
}

/**
 * Check whether given argument has own property
 * @param {Object} obj - Target for checking
 * @returns {boolean} - whether given argument has own property
 * @private
 */
function _hasOwnProperty(obj) {
  var key;
  for (key in obj) {
    if (obj.hasOwnProperty(key)) {
      return true;
    }
  }

  return false;
}

/**
 * Check whether the given variable is empty(null, undefined, or empty array, empty object) or not.
 *  If the given variables is empty, return true.
 * @param {*} obj - Target for checking
 * @returns {boolean} Is empty?
 * @memberof module:type
 */
function isEmpty(obj) {
  if (!isExisty(obj) || _isEmptyString(obj)) {
    return true;
  }

  if (isArray(obj) || isArguments(obj)) {
    return obj.length === 0;
  }

  if (isObject(obj) && !isFunction(obj)) {
    return !_hasOwnProperty(obj);
  }

  return true;
}

module.exports = isEmpty;
