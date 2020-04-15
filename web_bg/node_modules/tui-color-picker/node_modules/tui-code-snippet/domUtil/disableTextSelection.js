/**
 * @fileoverview Disable browser's text selection behaviors.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var on = require('../domEvent/on');
var preventDefault = require('../domEvent/preventDefault');
var setData = require('./setData');
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
 * Disable browser's text selection behaviors.
 * @param {HTMLElement} [el] - target element. if not supplied, use `document`
 * @memberof module:domUtil
 */
function disableTextSelection(el) {
  if (!el) {
    el = document;
  }

  if (SUPPORT_SELECTSTART) {
    on(el, 'selectstart', preventDefault);
  } else {
    el = (el === document) ? document.documentElement : el;
    setData(el, KEY_PREVIOUS_USER_SELECT, el.style[userSelectProperty]);
    el.style[userSelectProperty] = 'none';
  }
}

module.exports = disableTextSelection;
