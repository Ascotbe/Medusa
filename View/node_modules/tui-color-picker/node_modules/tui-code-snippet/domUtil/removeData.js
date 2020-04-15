/**
 * @fileoverview Remove data property
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var convertToKebabCase = require('./_convertToKebabCase');

/**
 * Remove data property
 * @param {HTMLElement} element - target element
 * @param {string} key - key
 * @memberof module:domUtil
 */
function removeData(element, key) {
  if (element.dataset) {
    delete element.dataset[key];

    return;
  }

  element.removeAttribute('data-' + convertToKebabCase(key));
}

module.exports = removeData;
