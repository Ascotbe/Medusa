/**
 * @fileoverview Toggle css class
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var forEach = require('../collection/forEach');
var inArray = require('../array/inArray');
var getClass = require('./getClass');
var setClassName = require('./_setClassName');

/**
 * Toggle css class
 * @param {(HTMLElement|SVGElement)} element - target element
 * @param {...string} cssClass - css classes to toggle
 * @memberof module:domUtil
 */
function toggleClass(element) {
  var cssClass = Array.prototype.slice.call(arguments, 1);
  var newClass;

  if (element.classList) {
    forEach(cssClass, function(name) {
      element.classList.toggle(name);
    });

    return;
  }

  newClass = getClass(element).split(/\s+/);

  forEach(cssClass, function(name) {
    var idx = inArray(name, newClass);

    if (idx > -1) {
      newClass.splice(idx, 1);
    } else {
      newClass.push(name);
    }
  });

  setClassName(element, newClass);
}

module.exports = toggleClass;
