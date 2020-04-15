/**
 * @fileoverview Normalize mouse event's button attributes.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var browser = require('../browser/browser');
var inArray = require('../array/inArray');

var primaryButton = ['0', '1', '3', '5', '7'];
var secondaryButton = ['2', '6'];
var wheelButton = ['4'];

/**
 * @module domEvent
 */

/**
 * Normalize mouse event's button attributes.
 *
 * Can detect which button is clicked by this method.
 *
 * Meaning of return numbers
 *
 * - 0: primary mouse button
 * - 1: wheel button or center button
 * - 2: secondary mouse button
 * @param {MouseEvent} mouseEvent - The mouse event object want to know.
 * @returns {number} - The value of meaning which button is clicked?
 * @memberof module:domEvent
 */
function getMouseButton(mouseEvent) {
  if (browser.msie && browser.version <= 8) {
    return getMouseButtonIE8AndEarlier(mouseEvent);
  }

  return mouseEvent.button;
}

/**
 * Normalize return value of mouseEvent.button
 * Make same to standard MouseEvent's button value
 * @param {DispCEventObj} mouseEvent - mouse event object
 * @returns {number|null} - id indicating which mouse button is clicked
 * @private
 */
function getMouseButtonIE8AndEarlier(mouseEvent) {
  var button = String(mouseEvent.button);

  if (inArray(button, primaryButton) > -1) {
    return 0;
  }

  if (inArray(button, secondaryButton) > -1) {
    return 2;
  }

  if (inArray(button, wheelButton) > -1) {
    return 1;
  }

  return null;
}

module.exports = getMouseButton;
