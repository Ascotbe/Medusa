/**
 * @fileoverview Generate an integer Array containing an arithmetic progression.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var isUndefined = require('../type/isUndefined');

/**
 * Generate an integer Array containing an arithmetic progression.
 * @param {number} start - start index
 * @param {number} stop - stop index
 * @param {number} step - next visit index = current index + step
 * @returns {Array}
 * @memberof module:array
 * @example
 * var range = require('tui-code-snippet/array/range'); // node, commonjs
 *
 * range(5); // [0, 1, 2, 3, 4]
 * range(1, 5); // [1,2,3,4]
 * range(2, 10, 2); // [2,4,6,8]
 * range(10, 2, -2); // [10,8,6,4]
 */
function range(start, stop, step) {
  var arr = [];
  var flag;

  if (isUndefined(stop)) {
    stop = start || 0;
    start = 0;
  }

  step = step || 1;
  flag = step < 0 ? -1 : 1;
  stop *= flag;

  for (; start * flag < stop; start += step) {
    arr.push(start);
  }

  return arr;
}

module.exports = range;
