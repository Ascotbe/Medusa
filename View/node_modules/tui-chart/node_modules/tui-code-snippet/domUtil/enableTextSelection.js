/**
 * @fileoverview Transform the Array-like object to Array.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var off = require('../domEvent/off');
var preventDefault = require('../domEvent/preventDefault');
var getData = require('./getData');
var removeData = require('./removeData');
var testCSSProp = require('./_testCSSProp');

var SUPPORT_SELECTSTART = 'onselectstart' in document;
var KEY_PREVIOUS_USER_SELECT = 'prevUserSelect';
var userSelectProperty = testCSSProp([
  'userSelect',
  'WebkitUserSelect',
  'OUserSelect',
  'MozUserSelect',
  'msUserSelect'
]);

/**
 * Enable browser's text selection behaviors.
 * @param {HTMLElement} [el] - target element. if not supplied, use `document`
 * @memberof module:domUtil
 */
function enableTextSelection(el) {
  if (!el) {
    el = document;
  }

  if (SUPPORT_SELECTSTART) {
    off(el, 'selectstart', preventDefault);
  } else {
    el = (el === document) ? document.documentElement : el;
    el.style[userSelectProperty] = getData(el, KEY_PREVIOUS_USER_SELECT) || 'auto';
    removeData(el, KEY_PREVIOUS_USER_SELECT);
  }
}

module.exports = enableTextSelection;
