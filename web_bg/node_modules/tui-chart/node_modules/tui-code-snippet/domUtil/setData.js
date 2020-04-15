/**
 * @fileoverview Set data attribute to target element
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var convertToKebabCase = require('./_convertToKebabCase');

/**
 * Set data attribute to target element
 * @param {HTMLElement} element - element to set data attribute
 * @param {string} key - key
 * @param {string} value - value
 * @memberof module:domUtil
 */
function setData(element, key, value) {
  if (element.dataset) {
    element.dataset[key] = value;

    return;
  }

  element.setAttribute('data-' + convertToKebabCase(key), value);
}

module.exports = setData;
