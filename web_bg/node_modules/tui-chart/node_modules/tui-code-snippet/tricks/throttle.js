/**
 * @fileoverview Creates a throttled function that only invokes fn at most once per every interval milliseconds.
 * @author NHN FE Development Lab <dl_javascript.nhn.com>
 */

'use strict';

var debounce = require('./debounce');

/**
 * Creates a throttled function that only invokes fn at most once per every interval milliseconds.
 * You can use this throttle short time repeatedly invoking functions. (e.g MouseMove, Resize ...)
 * if you need reuse throttled method. you must remove slugs (e.g. flag variable) related with throttling.
 * @param {function} fn function to throttle
 * @param {number} [interval=0] the number of milliseconds to throttle invocations to.
 * @returns {function} throttled function
 * @memberof module:tricks
 * @example
 * var throttle = require('tui-code-snippet/tricks/throttle'); // node, commonjs
 *
 * function someMethodToInvokeThrottled() {}
 *
 * var throttled = throttle(someMethodToInvokeThrottled, 300);
 *
 * // invoke repeatedly
 * throttled();    // invoke (leading)
 * throttled();
 * throttled();    // invoke (near 300 milliseconds)
 * throttled();
 * throttled();
 * throttled();    // invoke (near 600 milliseconds)
 * // ...
 * // invoke (trailing)
 *
 * // if you need reuse throttled method. then invoke reset()
 * throttled.reset();
 */
function throttle(fn, interval) {
  var base;
  var isLeading = true;
  var tick = function(_args) {
    fn.apply(null, _args);
    base = null;
  };
  var debounced, stamp, args;

  /* istanbul ignore next */
  interval = interval || 0;

  debounced = debounce(tick, interval);

  function throttled() { // eslint-disable-line require-jsdoc
    args = Array.prototype.slice.call(arguments);

    if (isLeading) {
      tick(args);
      isLeading = false;

      return;
    }

    stamp = Number(new Date());

    base = base || stamp;

    // pass array directly because `debounce()`, `tick()` are already use
    // `apply()` method to invoke developer's `fn` handler.
    //
    // also, this `debounced` line invoked every time for implements
    // `trailing` features.
    debounced(args);

    if ((stamp - base) >= interval) {
      tick(args);
    }
  }

  function reset() { // eslint-disable-line require-jsdoc
    isLeading = true;
    base = null;
  }

  throttled.reset = reset;

  return throttled;
}

module.exports = throttle;
