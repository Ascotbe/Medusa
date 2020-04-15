/**
 * @fileoverview Get data value from data-attribute
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var convertToKebabCase = require('./_convertToKebabCase');

/**
 * Get data value from data-attribute
 * @param {HTMLElement} element - target element
 * @param {string} key - key
 * @returns {string} value
 * @memberof module:domUtil
 */
function getData(element, key) {
  if (element.dataset) {
    return element.dataset[key];
  }

  return element.getAttribute('data-' + convertToKebabCase(key));
}

module.exports = getData;
