/**
 * @fileoverview Bind DOM event. this event will unbind after invokes.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

var forEachOwnProperties = require('../collection/forEachOwnProperties');
var isObject = require('../type/isObject');
var on = require('./on');
var off = require('./off');

/**
 * Bind DOM event. this event will unbind after invokes.
 * @param {HTMLElement} element - HTMLElement to bind events.
 * @param {(string|object)} types - Space splitted events names or
 *  eventName:handler object.
 * @param {(function|object)} handler - handler function or context for handler method.
 * @param {object} [context] - context object for handler method.
 * @memberof module:domEvent
 */
function once(element, types, handler, context) {
  /**
     * Event handler for one time.
     */
  function onceHandler() {
    handler.apply(context || element, arguments);
    off(element, types, onceHandler, context);
  }

  if (isObject(types)) {
    forEachOwnProperties(types, function(fn, type) {
      once(element, type, fn, handler);
    });

    return;
  }

  on(element, types, onceHandler, context);
}

module.exports = once;
