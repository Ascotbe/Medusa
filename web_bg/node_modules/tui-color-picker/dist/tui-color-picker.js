/*!
 * TOAST UI Color Picker
 * @version 2.2.6
 * @author NHN FE Development Team <dl_javascript@nhn.com>
 * @license MIT
 */
(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory();
	else if(typeof define === 'function' && define.amd)
		define([], factory);
	else if(typeof exports === 'object')
		exports["colorPicker"] = factory();
	else
		root["tui"] = root["tui"] || {}, root["tui"]["colorPicker"] = factory();
})(window, function() {
return /******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "dist";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 33);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Extend the target object from other objects.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * @module object
 */

/**
 * Extend the target object from other objects.
 * @param {object} target - Object that will be extended
 * @param {...object} objects - Objects as sources
 * @returns {object} Extended object
 * @memberof module:object
 */
function extend(target, objects) { // eslint-disable-line no-unused-vars
  var hasOwnProp = Object.prototype.hasOwnProperty;
  var source, prop, i, len;

  for (i = 1, len = arguments.length; i < len; i += 1) {
    source = arguments[i];
    for (prop in source) {
      if (hasOwnProp.call(source, prop)) {
        target[prop] = source[prop];
      }
    }
  }

  return target;
}

module.exports = extend;


/***/ }),
/* 1 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check whether the given variable is an instance of Array or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Check whether the given variable is an instance of Array or not.
 * If the given variable is an instance of Array, return true.
 * @param {*} obj - Target for checking
 * @returns {boolean} Is array instance?
 * @memberof module:type
 */
function isArray(obj) {
  return obj instanceof Array;
}

module.exports = isArray;


/***/ }),
/* 2 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Execute the provided callback once for each property of object(or element of array) which actually exist.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var isArray = __webpack_require__(1);
var forEachArray = __webpack_require__(6);
var forEachOwnProperties = __webpack_require__(7);

/**
 * @module collection
 */

/**
 * Execute the provided callback once for each property of object(or element of array) which actually exist.
 * If the object is Array-like object(ex-arguments object), It needs to transform to Array.(see 'ex2' of example).
 * If the callback function returns false, the loop will be stopped.
 * Callback function(iteratee) is invoked with three arguments:
 *  1) The value of the property(or The value of the element)
 *  2) The name of the property(or The index of the element)
 *  3) The object being traversed
 * @param {Object} obj The object that will be traversed
 * @param {function} iteratee Callback function
 * @param {Object} [context] Context(this) of callback function
 * @memberof module:collection
 * @example
 * var forEach = require('tui-code-snippet/collection/forEach'); // node, commonjs
 *
 * var sum = 0;
 *
 * forEach([1,2,3], function(value){
 *     sum += value;
 * });
 * alert(sum); // 6
 *
 * // In case of Array-like object
 * var array = Array.prototype.slice.call(arrayLike); // change to array
 * forEach(array, function(value){
 *     sum += value;
 * });
 */
function forEach(obj, iteratee, context) {
  if (isArray(obj)) {
    forEachArray(obj, iteratee, context);
  } else {
    forEachOwnProperties(obj, iteratee, context);
  }
}

module.exports = forEach;


/***/ }),
/* 3 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check whether the given variable is undefined or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Check whether the given variable is undefined or not.
 * If the given variable is undefined, returns true.
 * @param {*} obj - Target for checking
 * @returns {boolean} Is undefined?
 * @memberof module:type
 */
function isUndefined(obj) {
  return obj === undefined; // eslint-disable-line no-undefined
}

module.exports = isUndefined;


/***/ }),
/* 4 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Utils for ColorPicker component
 * @author NHN. FE dev Lab. <dl_javascript@nhn.com>
 */


var browser = __webpack_require__(22);

var forEach = __webpack_require__(2);

var forEachArray = __webpack_require__(6);

var forEachOwnProperties = __webpack_require__(7);

var sendHostname = __webpack_require__(37);

var currentId = 0;
/**
 * Utils
 * @namespace util
 * @ignore
 */

var utils = {
  /**
   * Get the number of properties in the object.
   * @param {Object} obj - object
   * @returns {number}
   */
  getLength: function (obj) {
    var length = 0;
    forEachOwnProperties(obj, function () {
      length += 1;
    });
    return length;
  },

  /**
   * Constructs a new array by executing the provided callback function.
   * @param {Object|Array} obj - object or array to be traversed
   * @param {function} iteratee - callback function
   * @param {Object} context - context of callback function
   * @returns {Array}
   */
  map: function (obj, iteratee, context) {
    var result = [];
    forEach(obj, function () {
      result.push(iteratee.apply(context || null, arguments));
    });
    return result;
  },

  /**
   * Construct a new array with elements that pass the test by the provided callback function.
   * @param {Array|NodeList|Arguments} arr - array to be traversed
   * @param {function} iteratee - callback function
   * @param {Object} context - context of callback function
   * @returns {Array}
   */
  filter: function (arr, iteratee, context) {
    var result = [];
    forEachArray(arr, function (elem) {
      if (iteratee.apply(context || null, arguments)) {
        result.push(elem);
      }
    });
    return result;
  },

  /**
   * Create an unique id for a color-picker instance.
   * @returns {number}
   */
  generateId: function () {
    currentId += 1;
    return currentId;
  },

  /**
   * True when browser is below IE8.
   */
  isOldBrowser: function () {
    return browser.msie && browser.version < 9;
  }(),

  /**
   * send host name
   * @ignore
   */
  sendHostName: function () {
    sendHostname('color-picker', 'UA-129987462-1');
  }
};
module.exports = utils;

/***/ }),
/* 5 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/* eslint-disable complexity */
/**
 * @fileoverview Returns the first index at which a given element can be found in the array.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var isArray = __webpack_require__(1);

/**
 * @module array
 */

/**
 * Returns the first index at which a given element can be found in the array
 * from start index(default 0), or -1 if it is not present.
 * It compares searchElement to elements of the Array using strict equality
 * (the same method used by the ===, or triple-equals, operator).
 * @param {*} searchElement Element to locate in the array
 * @param {Array} array Array that will be traversed.
 * @param {number} startIndex Start index in array for searching (default 0)
 * @returns {number} the First index at which a given element, or -1 if it is not present
 * @memberof module:array
 * @example
 * var inArray = require('tui-code-snippet/array/inArray'); // node, commonjs
 *
 * var arr = ['one', 'two', 'three', 'four'];
 * var idx1 = inArray('one', arr, 3); // -1
 * var idx2 = inArray('one', arr); // 0
 */
function inArray(searchElement, array, startIndex) {
  var i;
  var length;
  startIndex = startIndex || 0;

  if (!isArray(array)) {
    return -1;
  }

  if (Array.prototype.indexOf) {
    return Array.prototype.indexOf.call(array, searchElement, startIndex);
  }

  length = array.length;
  for (i = startIndex; startIndex >= 0 && i < length; i += 1) {
    if (array[i] === searchElement) {
      return i;
    }
  }

  return -1;
}

module.exports = inArray;


/***/ }),
/* 6 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Execute the provided callback once for each element present in the array(or Array-like object) in ascending order.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Execute the provided callback once for each element present
 * in the array(or Array-like object) in ascending order.
 * If the callback function returns false, the loop will be stopped.
 * Callback function(iteratee) is invoked with three arguments:
 *  1) The value of the element
 *  2) The index of the element
 *  3) The array(or Array-like object) being traversed
 * @param {Array|Arguments|NodeList} arr The array(or Array-like object) that will be traversed
 * @param {function} iteratee Callback function
 * @param {Object} [context] Context(this) of callback function
 * @memberof module:collection
 * @example
 * var forEachArray = require('tui-code-snippet/collection/forEachArray'); // node, commonjs
 *
 * var sum = 0;
 *
 * forEachArray([1,2,3], function(value){
 *     sum += value;
 * });
 * alert(sum); // 6
 */
function forEachArray(arr, iteratee, context) {
  var index = 0;
  var len = arr.length;

  context = context || null;

  for (; index < len; index += 1) {
    if (iteratee.call(context, arr[index], index, arr) === false) {
      break;
    }
  }
}

module.exports = forEachArray;


/***/ }),
/* 7 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Execute the provided callback once for each property of object which actually exist.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Execute the provided callback once for each property of object which actually exist.
 * If the callback function returns false, the loop will be stopped.
 * Callback function(iteratee) is invoked with three arguments:
 *  1) The value of the property
 *  2) The name of the property
 *  3) The object being traversed
 * @param {Object} obj The object that will be traversed
 * @param {function} iteratee  Callback function
 * @param {Object} [context] Context(this) of callback function
 * @memberof module:collection
 * @example
 * var forEachOwnProperties = require('tui-code-snippet/collection/forEachOwnProperties'); // node, commonjs
 *
 * var sum = 0;
 *
 * forEachOwnProperties({a:1,b:2,c:3}, function(value){
 *     sum += value;
 * });
 * alert(sum); // 6
 */
function forEachOwnProperties(obj, iteratee, context) {
  var key;

  context = context || null;

  for (key in obj) {
    if (obj.hasOwnProperty(key)) {
      if (iteratee.call(context, obj[key], key, obj) === false) {
        break;
      }
    }
  }
}

module.exports = forEachOwnProperties;


/***/ }),
/* 8 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview The base class of views.
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var addClass = __webpack_require__(39);

var isFunction = __webpack_require__(13);

var isNumber = __webpack_require__(41);

var isUndefined = __webpack_require__(3);

var domUtil = __webpack_require__(9);

var Collection = __webpack_require__(19);

var util = __webpack_require__(4);
/**
 * Base class of views.
 *
 * All views create own container element inside supplied container element.
 * @constructor
 * @param {options} options The object for describe view's specs.
 * @param {HTMLElement} container Default container element for view. you can use this element for this.container syntax.
 * @ignore
 */


function View(options, container) {
  var id = util.generateId();
  options = options || {};

  if (isUndefined(container)) {
    container = domUtil.appendHTMLElement('div');
  }

  addClass(container, 'tui-view-' + id);
  /**
   * unique id
   * @type {number}
   */

  this.id = id;
  /**
   * base element of view.
   * @type {HTMLDIVElement}
   */

  this.container = container;
  /**
   * child views.
   * @type {Collection}
   */

  this.childs = new Collection(function (view) {
    return view.id;
  });
  /**
   * parent view instance.
   * @type {View}
   */

  this.parent = null;
}
/**
 * Add child views.
 * @param {View} view The view instance to add.
 * @param {function} [fn] Function for invoke before add. parent view class is supplied first arguments.
 */


View.prototype.addChild = function (view, fn) {
  if (fn) {
    fn.call(view, this);
  } // add parent view


  view.parent = this;
  this.childs.add(view);
};
/**
 * Remove added child view.
 * @param {(number|View)} id View id or instance itself to remove.
 * @param {function} [fn] Function for invoke before remove. parent view class is supplied first arguments.
 */


View.prototype.removeChild = function (id, fn) {
  var view = isNumber(id) ? this.childs.items[id] : id;

  if (fn) {
    fn.call(view, this);
  }

  this.childs.remove(view.id);
};
/**
 * Render view recursively.
 */


View.prototype.render = function () {
  this.childs.each(function (childView) {
    childView.render();
  });
};
/**
 * Invoke function recursively.
 * @param {function} fn - function to invoke child view recursively
 * @param {boolean} [skipThis=false] - set true then skip invoke with this(root) view.
 */


View.prototype.recursive = function (fn, skipThis) {
  if (!isFunction(fn)) {
    return;
  }

  if (!skipThis) {
    fn(this);
  }

  this.childs.each(function (childView) {
    childView.recursive(fn);
  });
};
/**
 * Resize view recursively to parent.
 */


View.prototype.resize = function () {
  var args = Array.prototype.slice.call(arguments);
  var parent = this.parent;

  while (parent) {
    if (isFunction(parent._onResize)) {
      parent._onResize.apply(parent, args);
    }

    parent = parent.parent;
  }
};
/**
 * Invoking method before destroying.
 */


View.prototype._beforeDestroy = function () {};
/**
 * Clear properties
 */


View.prototype._destroy = function () {
  this._beforeDestroy();

  this.container.innerHTML = '';
  this.id = this.parent = this.childs = this.container = null;
};
/**
 * Destroy child view recursively.
 * @param {boolean} isChildView - Whether it is the child view or not
 */


View.prototype.destroy = function (isChildView) {
  if (this.childs) {
    this.childs.each(function (childView) {
      childView.destroy(true);

      childView._destroy();
    });
    this.childs.clear();
  }

  if (isChildView) {
    return;
  }

  this._destroy();
};
/**
 * Calculate view's container element bound.
 * @returns {object} The bound of container element.
 */


View.prototype.getViewBound = function () {
  var bound = this.container.getBoundingClientRect();
  return {
    x: bound.left,
    y: bound.top,
    width: bound.right - bound.left,
    height: bound.bottom - bound.top
  };
};

module.exports = View;

/***/ }),
/* 9 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Utility modules for manipulate DOM elements.
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var domUtil = {
  /**
   * Create DOM element and return it.
   * @param {string} tagName Tag name to append.
   * @param {HTMLElement} [container] HTML element will be parent to created element.
   * if not supplied, will use **document.body**
   * @param {string} [className] Design class names to appling created element.
   * @returns {HTMLElement} HTML element created.
   */
  appendHTMLElement: function (tagName, container, className) {
    var el = document.createElement(tagName);
    el.className = className || '';

    if (container) {
      container.appendChild(el);
    } else {
      document.body.appendChild(el);
    }

    return el;
  }
};
module.exports = domUtil;

/***/ }),
/* 10 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview This module provides some functions for custom events. And it is implemented in the observer design pattern.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var extend = __webpack_require__(0);
var isExisty = __webpack_require__(20);
var isString = __webpack_require__(11);
var isObject = __webpack_require__(21);
var isArray = __webpack_require__(1);
var isFunction = __webpack_require__(13);
var forEach = __webpack_require__(2);

var R_EVENTNAME_SPLIT = /\s+/g;

/**
 * @class
 * @example
 * // node, commonjs
 * var CustomEvents = require('tui-code-snippet/customEvents/customEvents');
 */
function CustomEvents() {
  /**
     * @type {HandlerItem[]}
     */
  this.events = null;

  /**
     * only for checking specific context event was binded
     * @type {object[]}
     */
  this.contexts = null;
}

/**
 * Mixin custom events feature to specific constructor
 * @param {function} func - constructor
 * @example
 * var CustomEvents = require('tui-code-snippet/customEvents/customEvents'); // node, commonjs
 *
 * var model;
 * function Model() {
 *     this.name = '';
 * }
 * CustomEvents.mixin(Model);
 *
 * model = new Model();
 * model.on('change', function() { this.name = 'model'; }, this);
 * model.fire('change');
 * alert(model.name); // 'model';
 */
CustomEvents.mixin = function(func) {
  extend(func.prototype, CustomEvents.prototype);
};

/**
 * Get HandlerItem object
 * @param {function} handler - handler function
 * @param {object} [context] - context for handler
 * @returns {HandlerItem} HandlerItem object
 * @private
 */
CustomEvents.prototype._getHandlerItem = function(handler, context) {
  var item = {handler: handler};

  if (context) {
    item.context = context;
  }

  return item;
};

/**
 * Get event object safely
 * @param {string} [eventName] - create sub event map if not exist.
 * @returns {(object|array)} event object. if you supplied `eventName`
 *  parameter then make new array and return it
 * @private
 */
CustomEvents.prototype._safeEvent = function(eventName) {
  var events = this.events;
  var byName;

  if (!events) {
    events = this.events = {};
  }

  if (eventName) {
    byName = events[eventName];

    if (!byName) {
      byName = [];
      events[eventName] = byName;
    }

    events = byName;
  }

  return events;
};

/**
 * Get context array safely
 * @returns {array} context array
 * @private
 */
CustomEvents.prototype._safeContext = function() {
  var context = this.contexts;

  if (!context) {
    context = this.contexts = [];
  }

  return context;
};

/**
 * Get index of context
 * @param {object} ctx - context that used for bind custom event
 * @returns {number} index of context
 * @private
 */
CustomEvents.prototype._indexOfContext = function(ctx) {
  var context = this._safeContext();
  var index = 0;

  while (context[index]) {
    if (ctx === context[index][0]) {
      return index;
    }

    index += 1;
  }

  return -1;
};

/**
 * Memorize supplied context for recognize supplied object is context or
 *  name: handler pair object when off()
 * @param {object} ctx - context object to memorize
 * @private
 */
CustomEvents.prototype._memorizeContext = function(ctx) {
  var context, index;

  if (!isExisty(ctx)) {
    return;
  }

  context = this._safeContext();
  index = this._indexOfContext(ctx);

  if (index > -1) {
    context[index][1] += 1;
  } else {
    context.push([ctx, 1]);
  }
};

/**
 * Forget supplied context object
 * @param {object} ctx - context object to forget
 * @private
 */
CustomEvents.prototype._forgetContext = function(ctx) {
  var context, contextIndex;

  if (!isExisty(ctx)) {
    return;
  }

  context = this._safeContext();
  contextIndex = this._indexOfContext(ctx);

  if (contextIndex > -1) {
    context[contextIndex][1] -= 1;

    if (context[contextIndex][1] <= 0) {
      context.splice(contextIndex, 1);
    }
  }
};

/**
 * Bind event handler
 * @param {(string|{name:string, handler:function})} eventName - custom
 *  event name or an object {eventName: handler}
 * @param {(function|object)} [handler] - handler function or context
 * @param {object} [context] - context for binding
 * @private
 */
CustomEvents.prototype._bindEvent = function(eventName, handler, context) {
  var events = this._safeEvent(eventName);
  this._memorizeContext(context);
  events.push(this._getHandlerItem(handler, context));
};

/**
 * Bind event handlers
 * @param {(string|{name:string, handler:function})} eventName - custom
 *  event name or an object {eventName: handler}
 * @param {(function|object)} [handler] - handler function or context
 * @param {object} [context] - context for binding
 * //-- #1. Get Module --//
 * var CustomEvents = require('tui-code-snippet/customEvents/customEvents'); // node, commonjs
 *
 * //-- #2. Use method --//
 * // # 2.1 Basic Usage
 * CustomEvents.on('onload', handler);
 *
 * // # 2.2 With context
 * CustomEvents.on('onload', handler, myObj);
 *
 * // # 2.3 Bind by object that name, handler pairs
 * CustomEvents.on({
 *     'play': handler,
 *     'pause': handler2
 * });
 *
 * // # 2.4 Bind by object that name, handler pairs with context object
 * CustomEvents.on({
 *     'play': handler
 * }, myObj);
 */
CustomEvents.prototype.on = function(eventName, handler, context) {
  var self = this;

  if (isString(eventName)) {
    // [syntax 1, 2]
    eventName = eventName.split(R_EVENTNAME_SPLIT);
    forEach(eventName, function(name) {
      self._bindEvent(name, handler, context);
    });
  } else if (isObject(eventName)) {
    // [syntax 3, 4]
    context = handler;
    forEach(eventName, function(func, name) {
      self.on(name, func, context);
    });
  }
};

/**
 * Bind one-shot event handlers
 * @param {(string|{name:string,handler:function})} eventName - custom
 *  event name or an object {eventName: handler}
 * @param {function|object} [handler] - handler function or context
 * @param {object} [context] - context for binding
 */
CustomEvents.prototype.once = function(eventName, handler, context) {
  var self = this;

  if (isObject(eventName)) {
    context = handler;
    forEach(eventName, function(func, name) {
      self.once(name, func, context);
    });

    return;
  }

  function onceHandler() { // eslint-disable-line require-jsdoc
    handler.apply(context, arguments);
    self.off(eventName, onceHandler, context);
  }

  this.on(eventName, onceHandler, context);
};

/**
 * Splice supplied array by callback result
 * @param {array} arr - array to splice
 * @param {function} predicate - function return boolean
 * @private
 */
CustomEvents.prototype._spliceMatches = function(arr, predicate) {
  var i = 0;
  var len;

  if (!isArray(arr)) {
    return;
  }

  for (len = arr.length; i < len; i += 1) {
    if (predicate(arr[i]) === true) {
      arr.splice(i, 1);
      len -= 1;
      i -= 1;
    }
  }
};

/**
 * Get matcher for unbind specific handler events
 * @param {function} handler - handler function
 * @returns {function} handler matcher
 * @private
 */
CustomEvents.prototype._matchHandler = function(handler) {
  var self = this;

  return function(item) {
    var needRemove = handler === item.handler;

    if (needRemove) {
      self._forgetContext(item.context);
    }

    return needRemove;
  };
};

/**
 * Get matcher for unbind specific context events
 * @param {object} context - context
 * @returns {function} object matcher
 * @private
 */
CustomEvents.prototype._matchContext = function(context) {
  var self = this;

  return function(item) {
    var needRemove = context === item.context;

    if (needRemove) {
      self._forgetContext(item.context);
    }

    return needRemove;
  };
};

/**
 * Get matcher for unbind specific hander, context pair events
 * @param {function} handler - handler function
 * @param {object} context - context
 * @returns {function} handler, context matcher
 * @private
 */
CustomEvents.prototype._matchHandlerAndContext = function(handler, context) {
  var self = this;

  return function(item) {
    var matchHandler = (handler === item.handler);
    var matchContext = (context === item.context);
    var needRemove = (matchHandler && matchContext);

    if (needRemove) {
      self._forgetContext(item.context);
    }

    return needRemove;
  };
};

/**
 * Unbind event by event name
 * @param {string} eventName - custom event name to unbind
 * @param {function} [handler] - handler function
 * @private
 */
CustomEvents.prototype._offByEventName = function(eventName, handler) {
  var self = this;
  var andByHandler = isFunction(handler);
  var matchHandler = self._matchHandler(handler);

  eventName = eventName.split(R_EVENTNAME_SPLIT);

  forEach(eventName, function(name) {
    var handlerItems = self._safeEvent(name);

    if (andByHandler) {
      self._spliceMatches(handlerItems, matchHandler);
    } else {
      forEach(handlerItems, function(item) {
        self._forgetContext(item.context);
      });

      self.events[name] = [];
    }
  });
};

/**
 * Unbind event by handler function
 * @param {function} handler - handler function
 * @private
 */
CustomEvents.prototype._offByHandler = function(handler) {
  var self = this;
  var matchHandler = this._matchHandler(handler);

  forEach(this._safeEvent(), function(handlerItems) {
    self._spliceMatches(handlerItems, matchHandler);
  });
};

/**
 * Unbind event by object(name: handler pair object or context object)
 * @param {object} obj - context or {name: handler} pair object
 * @param {function} handler - handler function
 * @private
 */
CustomEvents.prototype._offByObject = function(obj, handler) {
  var self = this;
  var matchFunc;

  if (this._indexOfContext(obj) < 0) {
    forEach(obj, function(func, name) {
      self.off(name, func);
    });
  } else if (isString(handler)) {
    matchFunc = this._matchContext(obj);

    self._spliceMatches(this._safeEvent(handler), matchFunc);
  } else if (isFunction(handler)) {
    matchFunc = this._matchHandlerAndContext(handler, obj);

    forEach(this._safeEvent(), function(handlerItems) {
      self._spliceMatches(handlerItems, matchFunc);
    });
  } else {
    matchFunc = this._matchContext(obj);

    forEach(this._safeEvent(), function(handlerItems) {
      self._spliceMatches(handlerItems, matchFunc);
    });
  }
};

/**
 * Unbind custom events
 * @param {(string|object|function)} eventName - event name or context or
 *  {name: handler} pair object or handler function
 * @param {(function)} handler - handler function
 * @example
 * //-- #1. Get Module --//
 * var CustomEvents = require('tui-code-snippet/customEvents/customEvents'); // node, commonjs
 *
 * //-- #2. Use method --//
 * // # 2.1 off by event name
 * CustomEvents.off('onload');
 *
 * // # 2.2 off by event name and handler
 * CustomEvents.off('play', handler);
 *
 * // # 2.3 off by handler
 * CustomEvents.off(handler);
 *
 * // # 2.4 off by context
 * CustomEvents.off(myObj);
 *
 * // # 2.5 off by context and handler
 * CustomEvents.off(myObj, handler);
 *
 * // # 2.6 off by context and event name
 * CustomEvents.off(myObj, 'onload');
 *
 * // # 2.7 off by an Object.<string, function> that is {eventName: handler}
 * CustomEvents.off({
 *   'play': handler,
 *   'pause': handler2
 * });
 *
 * // # 2.8 off the all events
 * CustomEvents.off();
 */
CustomEvents.prototype.off = function(eventName, handler) {
  if (isString(eventName)) {
    // [syntax 1, 2]
    this._offByEventName(eventName, handler);
  } else if (!arguments.length) {
    // [syntax 8]
    this.events = {};
    this.contexts = [];
  } else if (isFunction(eventName)) {
    // [syntax 3]
    this._offByHandler(eventName);
  } else if (isObject(eventName)) {
    // [syntax 4, 5, 6]
    this._offByObject(eventName, handler);
  }
};

/**
 * Fire custom event
 * @param {string} eventName - name of custom event
 */
CustomEvents.prototype.fire = function(eventName) {  // eslint-disable-line
  this.invoke.apply(this, arguments);
};

/**
 * Fire a event and returns the result of operation 'boolean AND' with all
 *  listener's results.
 *
 * So, It is different from {@link CustomEvents#fire}.
 *
 * In service code, use this as a before event in component level usually
 *  for notifying that the event is cancelable.
 * @param {string} eventName - Custom event name
 * @param {...*} data - Data for event
 * @returns {boolean} The result of operation 'boolean AND'
 * @example
 * var map = new Map();
 * map.on({
 *     'beforeZoom': function() {
 *         // It should cancel the 'zoom' event by some conditions.
 *         if (that.disabled && this.getState()) {
 *             return false;
 *         }
 *         return true;
 *     }
 * });
 *
 * if (this.invoke('beforeZoom')) {    // check the result of 'beforeZoom'
 *     // if true,
 *     // doSomething
 * }
 */
CustomEvents.prototype.invoke = function(eventName) {
  var events, args, index, item;

  if (!this.hasListener(eventName)) {
    return true;
  }

  events = this._safeEvent(eventName);
  args = Array.prototype.slice.call(arguments, 1);
  index = 0;

  while (events[index]) {
    item = events[index];

    if (item.handler.apply(item.context, args) === false) {
      return false;
    }

    index += 1;
  }

  return true;
};

/**
 * Return whether at least one of the handlers is registered in the given
 *  event name.
 * @param {string} eventName - Custom event name
 * @returns {boolean} Is there at least one handler in event name?
 */
CustomEvents.prototype.hasListener = function(eventName) {
  return this.getListenerLength(eventName) > 0;
};

/**
 * Return a count of events registered.
 * @param {string} eventName - Custom event name
 * @returns {number} number of event
 */
CustomEvents.prototype.getListenerLength = function(eventName) {
  var events = this._safeEvent(eventName);

  return events.length;
};

module.exports = CustomEvents;


/***/ }),
/* 11 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check whether the given variable is a string or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Check whether the given variable is a string or not.
 * If the given variable is a string, return true.
 * @param {*} obj - Target for checking
 * @returns {boolean} Is string?
 * @memberof module:type
 */
function isString(obj) {
  return typeof obj === 'string' || obj instanceof String;
}

module.exports = isString;


/***/ }),
/* 12 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Utility methods to manipulate colors
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var hexRX = /(^#[0-9A-F]{6}$)|(^#[0-9A-F]{3}$)/i;
var colorUtil = {
  /**
   * pad left zero characters.
   * @param {number} number number value to pad zero.
   * @param {number} length pad length to want.
   * @returns {string} padded string.
   */
  leadingZero: function (number, length) {
    var zero = '';
    var i = 0;

    if ((number + '').length > length) {
      return number + '';
    }

    for (; i < length - 1; i += 1) {
      zero += '0';
    }

    return (zero + number).slice(length * -1);
  },

  /**
   * Check validate of hex string value is RGB
   * @param {string} str - rgb hex string
   * @returns {boolean} return true when supplied str is valid RGB hex string
   */
  isValidRGB: function (str) {
    return hexRX.test(str);
  },
  // @license RGB <-> HSV conversion utilities based off of http://www.cs.rit.edu/~ncs/color/t_convert.html

  /**
   * Convert color hex string to rgb number array
   * @param {string} hexStr - hex string
   * @returns {number[]} rgb numbers
   */
  hexToRGB: function (hexStr) {
    var r, g, b;

    if (!colorUtil.isValidRGB(hexStr)) {
      return false;
    }

    hexStr = hexStr.substring(1);
    r = parseInt(hexStr.substr(0, 2), 16);
    g = parseInt(hexStr.substr(2, 2), 16);
    b = parseInt(hexStr.substr(4, 2), 16);
    return [r, g, b];
  },

  /**
   * Convert rgb number to hex string
   * @param {number} r - red
   * @param {number} g - green
   * @param {number} b - blue
   * @returns {string|boolean} return false when supplied rgb number is not valid. otherwise, converted hex string
   */
  rgbToHEX: function (r, g, b) {
    var hexStr = '#' + colorUtil.leadingZero(r.toString(16), 2) + colorUtil.leadingZero(g.toString(16), 2) + colorUtil.leadingZero(b.toString(16), 2);

    if (colorUtil.isValidRGB(hexStr)) {
      return hexStr;
    }

    return false;
  },

  /**
   * Convert rgb number to HSV value
   * @param {number} r - red
   * @param {number} g - green
   * @param {number} b - blue
   * @returns {number[]} hsv value
   */
  rgbToHSV: function (r, g, b) {
    var max, min, h, s, v, d;
    r /= 255;
    g /= 255;
    b /= 255;
    max = Math.max(r, g, b);
    min = Math.min(r, g, b);
    v = max;
    d = max - min;
    s = max === 0 ? 0 : d / max;

    if (max === min) {
      h = 0;
    } else {
      switch (max) {
        case r:
          h = (g - b) / d + (g < b ? 6 : 0);
          break;

        case g:
          h = (b - r) / d + 2;
          break;

        case b:
          h = (r - g) / d + 4;
          break;
        // no default
      }

      h /= 6;
    }

    return [Math.round(h * 360), Math.round(s * 100), Math.round(v * 100)];
  },

  /**
   * Convert HSV number to RGB
   * @param {number} h - hue
   * @param {number} s - saturation
   * @param {number} v - value
   * @returns {number[]} rgb value
   */
  hsvToRGB: function (h, s, v) {
    var r, g, b;
    var i;
    var f, p, q, t;
    h = Math.max(0, Math.min(360, h));
    s = Math.max(0, Math.min(100, s));
    v = Math.max(0, Math.min(100, v));
    s /= 100;
    v /= 100;

    if (s === 0) {
      // Achromatic (grey)
      r = g = b = v;
      return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
    }

    h /= 60; // sector 0 to 5

    i = Math.floor(h);
    f = h - i; // factorial part of h

    p = v * (1 - s);
    q = v * (1 - s * f);
    t = v * (1 - s * (1 - f));

    switch (i) {
      case 0:
        r = v;
        g = t;
        b = p;
        break;

      case 1:
        r = q;
        g = v;
        b = p;
        break;

      case 2:
        r = p;
        g = v;
        b = t;
        break;

      case 3:
        r = p;
        g = q;
        b = v;
        break;

      case 4:
        r = t;
        g = p;
        b = v;
        break;

      default:
        r = v;
        g = p;
        b = q;
        break;
    }

    return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
  }
};
module.exports = colorUtil;

/***/ }),
/* 13 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check whether the given variable is a function or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Check whether the given variable is a function or not.
 * If the given variable is a function, return true.
 * @param {*} obj - Target for checking
 * @returns {boolean} Is function?
 * @memberof module:type
 */
function isFunction(obj) {
  return obj instanceof Function;
}

module.exports = isFunction;


/***/ }),
/* 14 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Bind DOM events
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var isString = __webpack_require__(11);
var forEach = __webpack_require__(2);

var safeEvent = __webpack_require__(26);

/**
 * Bind DOM events.
 * @param {HTMLElement} element - element to bind events
 * @param {(string|object)} types - Space splitted events names or eventName:handler object
 * @param {(function|object)} handler - handler function or context for handler method
 * @param {object} [context] context - context for handler method.
 * @memberof module:domEvent
 * @example
 * var div = document.querySelector('div');
 * 
 * // Bind one event to an element.
 * on(div, 'click', toggle);
 * 
 * // Bind multiple events with a same handler to multiple elements at once.
 * // Use event names splitted by a space.
 * on(div, 'mouseenter mouseleave', changeColor);
 * 
 * // Bind multiple events with different handlers to an element at once.
 * // Use an object which of key is an event name and value is a handler function.
 * on(div, {
 *   keydown: highlight,
 *   keyup: dehighlight
 * });
 * 
 * // Set a context for handler method.
 * var name = 'global';
 * var repository = {name: 'CodeSnippet'};
 * on(div, 'drag', function() {
 *  console.log(this.name);
 * }, repository);
 * // Result when you drag a div: "CodeSnippet"
 */
function on(element, types, handler, context) {
  if (isString(types)) {
    forEach(types.split(/\s+/g), function(type) {
      bindEvent(element, type, handler, context);
    });

    return;
  }

  forEach(types, function(func, type) {
    bindEvent(element, type, func, handler);
  });
}

/**
 * Bind DOM events
 * @param {HTMLElement} element - element to bind events
 * @param {string} type - events name
 * @param {function} handler - handler function or context for handler method
 * @param {object} [context] context - context for handler method.
 * @private
 */
function bindEvent(element, type, handler, context) {
  /**
     * Event handler
     * @param {Event} e - event object
     */
  function eventHandler(e) {
    handler.call(context || element, e || window.event);
  }

  if ('addEventListener' in element) {
    element.addEventListener(type, eventHandler);
  } else if ('attachEvent' in element) {
    element.attachEvent('on' + type, eventHandler);
  }
  memorizeHandler(element, type, handler, eventHandler);
}

/**
 * Memorize DOM event handler for unbinding.
 * @param {HTMLElement} element - element to bind events
 * @param {string} type - events name
 * @param {function} handler - handler function that user passed at on() use
 * @param {function} wrappedHandler - handler function that wrapped by domevent for implementing some features
 * @private
 */
function memorizeHandler(element, type, handler, wrappedHandler) {
  var events = safeEvent(element, type);
  var existInEvents = false;

  forEach(events, function(obj) {
    if (obj.handler === handler) {
      existInEvents = true;

      return false;
    }

    return true;
  });

  if (!existInEvents) {
    events.push({
      handler: handler,
      wrappedHandler: wrappedHandler
    });
  }
}

module.exports = on;


/***/ }),
/* 15 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Prevent default action
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Prevent default action
 * @param {Event} e - event object
 * @memberof module:domEvent
 */
function preventDefault(e) {
  if (e.preventDefault) {
    e.preventDefault();

    return;
  }

  e.returnValue = false;
}

module.exports = preventDefault;


/***/ }),
/* 16 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Convert kebab-case
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Convert kebab-case
 * @param {string} key - string to be converted to Kebab-case
 * @private
 */
function convertToKebabCase(key) {
  return key.replace(/([A-Z])/g, function(match) {
    return '-' + match.toLowerCase();
  });
}

module.exports = convertToKebabCase;


/***/ }),
/* 17 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Unbind DOM events
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var isString = __webpack_require__(11);
var forEach = __webpack_require__(2);

var safeEvent = __webpack_require__(26);

/**
 * Unbind DOM events
 * If a handler function is not passed, remove all events of that type.
 * @param {HTMLElement} element - element to unbind events
 * @param {(string|object)} types - Space splitted events names or eventName:handler object
 * @param {function} [handler] - handler function
 * @memberof module:domEvent
 * @example
 * // Following the example of domEvent#on
 * 
 * // Unbind one event from an element.
 * off(div, 'click', toggle);
 * 
 * // Unbind multiple events with a same handler from multiple elements at once.
 * // Use event names splitted by a space.
 * off(element, 'mouseenter mouseleave', changeColor);
 * 
 * // Unbind multiple events with different handlers from an element at once.
 * // Use an object which of key is an event name and value is a handler function.
 * off(div, {
 *   keydown: highlight,
 *   keyup: dehighlight
 * });
 * 
 * // Unbind events without handlers.
 * off(div, 'drag');
 */
function off(element, types, handler) {
  if (isString(types)) {
    forEach(types.split(/\s+/g), function(type) {
      unbindEvent(element, type, handler);
    });

    return;
  }

  forEach(types, function(func, type) {
    unbindEvent(element, type, func);
  });
}

/**
 * Unbind DOM events
 * If a handler function is not passed, remove all events of that type.
 * @param {HTMLElement} element - element to unbind events
 * @param {string} type - events name
 * @param {function} [handler] - handler function
 * @private
 */
function unbindEvent(element, type, handler) {
  var events = safeEvent(element, type);
  var index;

  if (!handler) {
    forEach(events, function(item) {
      removeHandler(element, type, item.wrappedHandler);
    });
    events.splice(0, events.length);
  } else {
    forEach(events, function(item, idx) {
      if (handler === item.handler) {
        removeHandler(element, type, item.wrappedHandler);
        index = idx;

        return false;
      }

      return true;
    });
    events.splice(index, 1);
  }
}

/**
 * Remove an event handler
 * @param {HTMLElement} element - An element to remove an event
 * @param {string} type - event type
 * @param {function} handler - event handler
 * @private
 */
function removeHandler(element, type, handler) {
  if ('removeEventListener' in element) {
    element.removeEventListener(type, handler);
  } else if ('detachEvent' in element) {
    element.detachEvent('on' + type, handler);
  }
}

module.exports = off;


/***/ }),
/* 18 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Provide a simple inheritance in prototype-oriented.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var createObject = __webpack_require__(50);

/**
 * Provide a simple inheritance in prototype-oriented.
 * Caution :
 *  Don't overwrite the prototype of child constructor.
 *
 * @param {function} subType Child constructor
 * @param {function} superType Parent constructor
 * @memberof module:inheritance
 * @example
 * var inherit = require('tui-code-snippet/inheritance/inherit'); // node, commonjs
 *
 * // Parent constructor
 * function Animal(leg) {
 *     this.leg = leg;
 * }
 * Animal.prototype.growl = function() {
 *     // ...
 * };
 *
 * // Child constructor
 * function Person(name) {
 *     this.name = name;
 * }
 *
 * // Inheritance
 * inherit(Person, Animal);
 *
 * // After this inheritance, please use only the extending of property.
 * // Do not overwrite prototype.
 * Person.prototype.walk = function(direction) {
 *     // ...
 * };
 */
function inherit(subType, superType) {
  var prototype = createObject(superType.prototype);
  prototype.constructor = subType;
  subType.prototype = prototype;
}

module.exports = inherit;


/***/ }),
/* 19 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Common collections.
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var forEachArray = __webpack_require__(6);

var forEachOwnProperties = __webpack_require__(7);

var extend = __webpack_require__(0);

var isArray = __webpack_require__(1);

var isExisty = __webpack_require__(20);

var isFunction = __webpack_require__(13);

var isObject = __webpack_require__(21);

var util = __webpack_require__(4);

var slice = Array.prototype.slice;
/**
 * Common collection.
 *
 * It need function for get model's unique id.
 *
 * if the function is not supplied then it use default function {@link Collection#getItemID}
 * @constructor
 * @param {function} [getItemIDFn] function for get model's id.
 * @ignore
 */

function Collection(getItemIDFn) {
  /**
   * @type {object.<string, *>}
   */
  this.items = {};
  /**
   * @type {number}
   */

  this.length = 0;

  if (isFunction(getItemIDFn)) {
    /**
     * @type {function}
     */
    this.getItemID = getItemIDFn;
  }
}
/**********
 * static props
 **********/

/**
 * Combind supplied function filters and condition.
 * @param {...function} filters - function filters
 * @returns {function} combined filter
 */


Collection.and = function (filters) {
  var cnt;
  filters = slice.call(arguments);
  cnt = filters.length;
  return function (item) {
    var i = 0;

    for (; i < cnt; i += 1) {
      if (!filters[i].call(null, item)) {
        return false;
      }
    }

    return true;
  };
};
/**
 * Combine multiple function filters with OR clause.
 * @param {...function} filters - function filters
 * @returns {function} combined filter
 */


Collection.or = function (filters) {
  var cnt;
  filters = slice.call(arguments);
  cnt = filters.length;
  return function (item) {
    var i = 1;
    var result = filters[0].call(null, item);

    for (; i < cnt; i += 1) {
      result = result || filters[i].call(null, item);
    }

    return result;
  };
};
/**
 * Merge several collections.
 *
 * You can\'t merge collections different _getEventID functions. Take case of use.
 * @param {...Collection} collections collection arguments to merge
 * @returns {Collection} merged collection.
 */


Collection.merge = function (firstCollection) {
  var newItems = {};
  var merged = new Collection(firstCollection.getItemID);
  forEachArray(arguments, function (col) {
    extend(newItems, col.items);
  });
  merged.items = newItems;
  merged.length = util.getLength(merged.items);
  return merged;
};
/**********
 * prototype props
 **********/

/**
 * get model's unique id.
 * @param {object} item model instance.
 * @returns {number} model unique id.
 */


Collection.prototype.getItemID = function (item) {
  return item._id + '';
};
/**
 * add models.
 * @param {...*} item models to add this collection.
 */


Collection.prototype.add = function (item) {
  var id, ownItems;

  if (arguments.length > 1) {
    forEachArray(slice.call(arguments), function (o) {
      this.add(o);
    }, this);
    return;
  }

  id = this.getItemID(item);
  ownItems = this.items;

  if (!ownItems[id]) {
    this.length += 1;
  }

  ownItems[id] = item;
};
/**
 * remove models.
 * @param {...(object|string|number)} id model instance or unique id to delete.
 * @returns {array} deleted model list.
 */


Collection.prototype.remove = function (id) {
  var removed = [];
  var ownItems, itemToRemove;

  if (!this.length) {
    return removed;
  }

  if (arguments.length > 1) {
    removed = util.map(slice.call(arguments), function (id) {
      return this.remove(id);
    }, this);
    return removed;
  }

  ownItems = this.items;

  if (isObject(id)) {
    id = this.getItemID(id);
  }

  if (!ownItems[id]) {
    return removed;
  }

  this.length -= 1;
  itemToRemove = ownItems[id];
  delete ownItems[id];
  return itemToRemove;
};
/**
 * remove all models in collection.
 */


Collection.prototype.clear = function () {
  this.items = {};
  this.length = 0;
};
/**
 * check collection has specific model.
 * @param {(object|string|number|function)} id model instance or id or filter function to check
 * @returns {boolean} is has model?
 */


Collection.prototype.has = function (id) {
  var isFilter, has;

  if (!this.length) {
    return false;
  }

  isFilter = isFunction(id);
  has = false;

  if (isFilter) {
    this.each(function (item) {
      if (id(item) === true) {
        has = true;
        return false;
      }

      return true;
    });
  } else {
    id = isObject(id) ? this.getItemID(id) : id;
    has = isExisty(this.items[id]);
  }

  return has;
};
/**
 * invoke callback when model exist in collection.
 * @param {(string|number)} id model unique id.
 * @param {function} fn the callback.
 * @param {*} [context] callback context.
 */


Collection.prototype.doWhenHas = function (id, fn, context) {
  var item = this.items[id];

  if (!isExisty(item)) {
    return;
  }

  fn.call(context || this, item);
};
/**
 * Search model. and return new collection.
 * @param {function} filter filter function.
 * @returns {Collection} new collection with filtered models.
 * @example
 * collection.find(function(item) {
 *     return item.edited === true;
 * });
 *
 * function filter1(item) {
 *     return item.edited === false;
 * }
 *
 * function filter2(item) {
 *     return item.disabled === false;
 * }
 *
 * collection.find(Collection.and(filter1, filter2));
 *
 * collection.find(Collection.or(filter1, filter2));
 */


Collection.prototype.find = function (filter) {
  var result = new Collection();

  if (this.hasOwnProperty('getItemID')) {
    result.getItemID = this.getItemID;
  }

  this.each(function (item) {
    if (filter(item) === true) {
      result.add(item);
    }
  });
  return result;
};
/**
 * Group element by specific key values.
 *
 * if key parameter is function then invoke it and use returned value.
 * @param {(string|number|function|array)} key key property or getter function. if string[] supplied, create each collection before grouping.
 * @param {function} [groupFunc] - function that return each group's key
 * @returns {object.<string, Collection>} grouped object
 * @example
 *
 * // pass `string`, `number`, `boolean` type value then group by property value.
 * collection.groupBy('gender');    // group by 'gender' property value.
 * collection.groupBy(50);          // group by '50' property value.
 *
 * // pass `function` then group by return value. each invocation `function` is called with `(item)`.
 * collection.groupBy(function(item) {
 *     if (item.score > 60) {
 *         return 'pass';
 *     }
 *     return 'fail';
 * });
 *
 * // pass `array` with first arguments then create each collection before grouping.
 * collection.groupBy(['go', 'ruby', 'javascript']);
 * // result: { 'go': empty Collection, 'ruby': empty Collection, 'javascript': empty Collection }
 *
 * // can pass `function` with `array` then group each elements.
 * collection.groupBy(['go', 'ruby', 'javascript'], function(item) {
 *     if (item.isFast) {
 *         return 'go';
 *     }
 *
 *     return item.name;
 * });
 */


Collection.prototype.groupBy = function (key, groupFunc) {
  var result = {};
  var keyIsFunc = isFunction(key);
  var getItemIDFn = this.getItemID;
  var collection, baseValue;

  if (isArray(key)) {
    forEachArray(key, function (k) {
      result[k + ''] = new Collection(getItemIDFn);
    });

    if (!groupFunc) {
      return result;
    }

    key = groupFunc;
    keyIsFunc = true;
  }

  this.each(function (item) {
    if (keyIsFunc) {
      baseValue = key(item);
    } else {
      baseValue = item[key];

      if (isFunction(baseValue)) {
        baseValue = baseValue.apply(item);
      }
    }

    collection = result[baseValue];

    if (!collection) {
      collection = result[baseValue] = new Collection(getItemIDFn);
    }

    collection.add(item);
  });
  return result;
};
/**
 * Return single item in collection.
 *
 * Returned item is inserted in this collection firstly.
 * @returns {object} item.
 */


Collection.prototype.single = function () {
  var result;
  this.each(function (item) {
    result = item;
    return false;
  }, this);
  return result;
};
/**
 * sort a basis of supplied compare function.
 * @param {function} compareFunction compareFunction
 * @returns {array} sorted array.
 */


Collection.prototype.sort = function (compareFunction) {
  var arr = [];
  this.each(function (item) {
    arr.push(item);
  });

  if (isFunction(compareFunction)) {
    arr = arr.sort(compareFunction);
  }

  return arr;
};
/**
 * iterate each model element.
 *
 * when iteratee return false then break the loop.
 * @param {function} iteratee iteratee(item, index, items)
 * @param {*} [context] context
 */


Collection.prototype.each = function (iteratee, context) {
  forEachOwnProperties(this.items, iteratee, context || this);
};
/**
 * return new array with collection items.
 * @returns {array} new array.
 */


Collection.prototype.toArray = function () {
  if (!this.length) {
    return [];
  }

  return util.map(this.items, function (item) {
    return item;
  });
};

module.exports = Collection;

/***/ }),
/* 20 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check whether the given variable is existing or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var isUndefined = __webpack_require__(3);
var isNull = __webpack_require__(36);

/**
 * Check whether the given variable is existing or not.
 * If the given variable is not null and not undefined, returns true.
 * @param {*} param - Target for checking
 * @returns {boolean} Is existy?
 * @memberof module:type
 * @example
 * var isExisty = require('tui-code-snippet/type/isExisty'); // node, commonjs
 *
 * isExisty(''); //true
 * isExisty(0); //true
 * isExisty([]); //true
 * isExisty({}); //true
 * isExisty(null); //false
 * isExisty(undefined); //false
*/
function isExisty(param) {
  return !isUndefined(param) && !isNull(param);
}

module.exports = isExisty;


/***/ }),
/* 21 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check whether the given variable is an object or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Check whether the given variable is an object or not.
 * If the given variable is an object, return true.
 * @param {*} obj - Target for checking
 * @returns {boolean} Is object?
 * @memberof module:type
 */
function isObject(obj) {
  return obj === Object(obj);
}

module.exports = isObject;


/***/ }),
/* 22 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview This module detects the kind of well-known browser and version.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Browser module
 * @module browser
 */

/**
 * This object has an information that indicate the kind of browser.
 * The list below is a detectable browser list.
 *  - ie8 ~ ie11
 *  - chrome
 *  - firefox
 *  - safari
 *  - edge
 * @memberof module:browser
 * @example
 * var browser = require('tui-code-snippet/browser/browser'); // node, commonjs
 *
 * browser.chrome === true; // chrome
 * browser.firefox === true; // firefox
 * browser.safari === true; // safari
 * browser.msie === true; // IE
 * browser.edge === true; // edge
 * browser.others === true; // other browser
 * browser.version; // browser version
 */
var browser = {
  chrome: false,
  firefox: false,
  safari: false,
  msie: false,
  edge: false,
  others: false,
  version: 0
};

if (window && window.navigator) {
  detectBrowser();
}

/**
 * Detect the browser.
 * @private
 */
function detectBrowser() {
  var nav = window.navigator;
  var appName = nav.appName.replace(/\s/g, '_');
  var userAgent = nav.userAgent;

  var rIE = /MSIE\s([0-9]+[.0-9]*)/;
  var rIE11 = /Trident.*rv:11\./;
  var rEdge = /Edge\/(\d+)\./;
  var versionRegex = {
    firefox: /Firefox\/(\d+)\./,
    chrome: /Chrome\/(\d+)\./,
    safari: /Version\/([\d.]+).*Safari\/(\d+)/
  };

  var key, tmp;

  var detector = {
    Microsoft_Internet_Explorer: function() { // eslint-disable-line camelcase
      var detectedVersion = userAgent.match(rIE);

      if (detectedVersion) { // ie8 ~ ie10
        browser.msie = true;
        browser.version = parseFloat(detectedVersion[1]);
      } else { // no version information
        browser.others = true;
      }
    },
    Netscape: function() { // eslint-disable-line complexity
      var detected = false;

      if (rIE11.exec(userAgent)) {
        browser.msie = true;
        browser.version = 11;
        detected = true;
      } else if (rEdge.exec(userAgent)) {
        browser.edge = true;
        browser.version = userAgent.match(rEdge)[1];
        detected = true;
      } else {
        for (key in versionRegex) {
          if (versionRegex.hasOwnProperty(key)) {
            tmp = userAgent.match(versionRegex[key]);
            if (tmp && tmp.length > 1) { // eslint-disable-line max-depth
              browser[key] = detected = true;
              browser.version = parseFloat(tmp[1] || 0);
              break;
            }
          }
        }
      }
      if (!detected) {
        browser.others = true;
      }
    }
  };

  var fn = detector[appName];

  if (fn) {
    detector[appName]();
  }
}

module.exports = browser;


/***/ }),
/* 23 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Get HTML element's design classes.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var isUndefined = __webpack_require__(3);

/**
 * Get HTML element's design classes.
 * @param {(HTMLElement|SVGElement)} element target element
 * @returns {string} element css class name
 * @memberof module:domUtil
 */
function getClass(element) {
  if (!element || !element.className) {
    return '';
  }

  if (isUndefined(element.className.baseVal)) {
    return element.className;
  }

  return element.className.baseVal;
}

module.exports = getClass;


/***/ }),
/* 24 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/* WEBPACK VAR INJECTION */(function(global) {/**
 * @fileoverview General drag handler
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var CustomEvents = __webpack_require__(10);

var disableTextSelection = __webpack_require__(42);

var enableTextSelection = __webpack_require__(44);

var getMouseButton = __webpack_require__(47);

var getTarget = __webpack_require__(28);

var off = __webpack_require__(17);

var on = __webpack_require__(14);

var preventDefault = __webpack_require__(15);

var extend = __webpack_require__(0);
/**
 * @constructor
 * @mixes CustomEvents
 * @param {object} options - options for drag handler
 * @param {number} [options.distance=10] - distance in pixels after mouse must move before dragging should start
 * @param {HTMLElement} container - container element to bind drag events
 * @ignore
 */


function Drag(options, container) {
  on(container, 'mousedown', this._onMouseDown, this);
  this.options = extend({
    distance: 10
  }, options);
  /**
   * @type {HTMLElement}
   */

  this.container = container;
  /**
   * @type {boolean}
   */

  this._isMoved = false;
  /**
   * dragging distance in pixel between mousedown and firing dragStart events
   * @type {number}
   */

  this._distance = 0;
  /**
   * @type {boolean}
   */

  this._dragStartFired = false;
  /**
   * @type {object}
   */

  this._dragStartEventData = null;
}
/**
 * Destroy method.
 */


Drag.prototype.destroy = function () {
  off(this.container, 'mousedown', this._onMouseDown);
  this.options = this.container = this._isMoved = this._distance = this._dragStartFired = this._dragStartEventData = null;
};
/**
 * Toggle events for mouse dragging.
 * @param {boolean} toBind - bind events related with dragging when supplied "true"
 */


Drag.prototype._toggleDragEvent = function (toBind) {
  var container = this.container;

  if (toBind) {
    disableTextSelection(container);
    on(window, 'dragstart', preventDefault);
    on(global.document, {
      mousemove: this._onMouseMove,
      mouseup: this._onMouseUp
    }, this);
  } else {
    enableTextSelection(container);
    off(window, 'dragstart', preventDefault);
    off(global.document, {
      mousemove: this._onMouseMove,
      mouseup: this._onMouseUp
    });
  }
};
/**
 * Normalize mouse event object.
 * @param {MouseEvent} mouseEvent - mouse event object.
 * @returns {object} normalized mouse event data.
 */


Drag.prototype._getEventData = function (mouseEvent) {
  return {
    target: getTarget(mouseEvent),
    originEvent: mouseEvent
  };
};
/**
 * MouseDown DOM event handler.
 * @param {MouseEvent} mouseDownEvent MouseDown event object.
 */


Drag.prototype._onMouseDown = function (mouseDownEvent) {
  // only primary button can start drag.
  if (getMouseButton(mouseDownEvent) !== 0) {
    return;
  }

  this._distance = 0;
  this._dragStartFired = false;
  this._dragStartEventData = this._getEventData(mouseDownEvent);

  this._toggleDragEvent(true);
};
/**
 * MouseMove DOM event handler.
 * @emits Drag#drag
 * @emits Drag#dragStart
 * @param {MouseEvent} mouseMoveEvent MouseMove event object.
 */


Drag.prototype._onMouseMove = function (mouseMoveEvent) {
  var distance = this.options.distance; // prevent automatic scrolling.

  preventDefault(mouseMoveEvent);
  this._isMoved = true;

  if (this._distance < distance) {
    this._distance += 1;
    return;
  }

  if (!this._dragStartFired) {
    this._dragStartFired = true;
    /**
     * Drag starts events. cancelable.
     * @event Drag#dragStart
     * @type {object}
     * @property {HTMLElement} target - target element in this event.
     * @property {MouseEvent} originEvent - original mouse event object.
     */

    if (!this.invoke('dragStart', this._dragStartEventData)) {
      this._toggleDragEvent(false);

      return;
    }
  }
  /**
   * Events while dragging.
   * @event Drag#drag
   * @type {object}
   * @property {HTMLElement} target - target element in this event.
   * @property {MouseEvent} originEvent - original mouse event object.
   */


  this.fire('drag', this._getEventData(mouseMoveEvent));
};
/**
 * MouseUp DOM event handler.
 * @param {MouseEvent} mouseUpEvent MouseUp event object.
 * @emits Drag#dragEnd
 * @emits Drag#click
 */


Drag.prototype._onMouseUp = function (mouseUpEvent) {
  this._toggleDragEvent(false); // emit "click" event when not emitted drag event between mousedown and mouseup.


  if (this._isMoved) {
    this._isMoved = false;
    /**
     * Drag end events.
     * @event Drag#dragEnd
     * @type {MouseEvent}
     * @property {HTMLElement} target - target element in this event.
     * @property {MouseEvent} originEvent - original mouse event object.
     */

    this.fire('dragEnd', this._getEventData(mouseUpEvent));
    return;
  }
  /**
   * Click events.
   * @event Drag#click
   * @type {MouseEvent}
   * @property {HTMLElement} target - target element in this event.
   * @property {MouseEvent} originEvent - original mouse event object.
   */


  this.fire('click', this._getEventData(mouseUpEvent));
};

CustomEvents.mixin(Drag);
module.exports = Drag;
/* WEBPACK VAR INJECTION */}.call(this, __webpack_require__(25)))

/***/ }),
/* 25 */
/***/ (function(module, exports) {

var g;

// This works in non-strict mode
g = (function() {
	return this;
})();

try {
	// This works if eval is allowed (see CSP)
	g = g || new Function("return this")();
} catch (e) {
	// This works if the window reference is available
	if (typeof window === "object") g = window;
}

// g can still be undefined, but nothing to do about it...
// We return undefined, instead of nothing here, so it's
// easier to handle this case. if(!global) { ...}

module.exports = g;


/***/ }),
/* 26 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Get event collection for specific HTML element
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var EVENT_KEY = '_feEventKey';

/**
 * Get event collection for specific HTML element
 * @param {HTMLElement} element - HTML element
 * @param {string} type - event type
 * @returns {array}
 * @private
 */
function safeEvent(element, type) {
  var events = element[EVENT_KEY];
  var handlers;

  if (!events) {
    events = element[EVENT_KEY] = {};
  }

  handlers = events[type];
  if (!handlers) {
    handlers = events[type] = [];
  }

  return handlers;
}

module.exports = safeEvent;


/***/ }),
/* 27 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check specific CSS style is available.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Check specific CSS style is available.
 * @param {array} props property name to testing
 * @returns {(string|boolean)} return true when property is available
 * @private
 */
function testCSSProp(props) {
  var style = document.documentElement.style;
  var i, len;

  for (i = 0, len = props.length; i < len; i += 1) {
    if (props[i] in style) {
      return props[i];
    }
  }

  return false;
}

module.exports = testCSSProp;


/***/ }),
/* 28 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Get a target element from an event object.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Get a target element from an event object.
 * @param {Event} e - event object
 * @returns {HTMLElement} - target element
 * @memberof module:domEvent
 */
function getTarget(e) {
  return e.target || e.srcElement;
}

module.exports = getTarget;


/***/ }),
/* 29 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Color palette view
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var CustomEvents = __webpack_require__(10);

var getTarget = __webpack_require__(28);

var off = __webpack_require__(17);

var on = __webpack_require__(14);

var hasClass = __webpack_require__(30);

var extend = __webpack_require__(0);

var inherit = __webpack_require__(18);

var domUtil = __webpack_require__(9);

var colorUtil = __webpack_require__(12);

var View = __webpack_require__(8);

var tmpl = __webpack_require__(51);
/**
 * @constructor
 * @extends {View}
 * @mixes CustomEvents
 * @param {object} options - options for color palette view
 * @param {string[]} options.preset - color list
 * @param {HTMLDivElement} container - container element
 * @ignore
 */


function Palette(options, container) {
  /**
   * option object
   * @type {object}
   */
  this.options = extend({
    cssPrefix: 'tui-colorpicker-',
    preset: ['#181818', '#282828', '#383838', '#585858', '#B8B8B8', '#D8D8D8', '#E8E8E8', '#F8F8F8', '#AB4642', '#DC9656', '#F7CA88', '#A1B56C', '#86C1B9', '#7CAFC2', '#BA8BAF', '#A16946'],
    detailTxt: 'Detail'
  }, options);
  container = domUtil.appendHTMLElement('div', container, this.options.cssPrefix + 'palette-container');
  View.call(this, options, container);
}

inherit(Palette, View);
/**
 * Mouse click event handler
 * @fires Palette#_selectColor
 * @fires Palette#_toggleSlider
 * @param {MouseEvent} clickEvent - mouse event object
 */

Palette.prototype._onClick = function (clickEvent) {
  var options = this.options;
  var target = getTarget(clickEvent);
  var eventData = {};

  if (hasClass(target, options.cssPrefix + 'palette-button')) {
    eventData.color = target.value;
    /**
     * @event Palette#_selectColor
     * @type {object}
     * @property {string} color - selected color value
     */

    this.fire('_selectColor', eventData);
    return;
  }

  if (hasClass(target, options.cssPrefix + 'palette-toggle-slider')) {
    /**
     * @event Palette#_toggleSlider
     */
    this.fire('_toggleSlider');
  }
};
/**
 * Textbox change event handler
 * @fires Palette#_selectColor
 * @param {Event} changeEvent - change event object
 */


Palette.prototype._onChange = function (changeEvent) {
  var options = this.options;
  var target = getTarget(changeEvent);
  var eventData = {};

  if (hasClass(target, options.cssPrefix + 'palette-hex')) {
    eventData.color = target.value;
    /**
     * @event Palette#_selectColor
     * @type {object}
     * @property {string} color - selected color value
     */

    this.fire('_selectColor', eventData);
  }
};
/**
 * Invoke before destory
 * @override
 */


Palette.prototype._beforeDestroy = function () {
  this._toggleEvent(false);
};
/**
 * Toggle view DOM events
 * @param {boolean} [toBind=false] - true to bind event.
 */


Palette.prototype._toggleEvent = function (toBind) {
  var options = this.options;
  var container = this.container;
  var handleEvent = toBind ? on : off;
  var hexTextBox;
  handleEvent(container, 'click', this._onClick, this);
  hexTextBox = container.querySelector('.' + options.cssPrefix + 'palette-hex', container);

  if (hexTextBox) {
    handleEvent(hexTextBox, 'change', this._onChange, this);
  }
};
/**
 * Render palette
 * @override
 */


Palette.prototype.render = function (color) {
  var options = this.options;
  var html = '';

  this._toggleEvent(false);

  html = tmpl({
    cssPrefix: options.cssPrefix,
    preset: options.preset,
    detailTxt: options.detailTxt,
    color: color,
    isValidRGB: colorUtil.isValidRGB,
    getItemClass: function (itemColor) {
      return !itemColor ? ' ' + options.cssPrefix + 'color-transparent' : '';
    },
    isSelected: function (itemColor) {
      return itemColor === color ? ' ' + options.cssPrefix + 'selected' : '';
    }
  });
  this.container.innerHTML = html;

  this._toggleEvent(true);
};

CustomEvents.mixin(Palette);
module.exports = Palette;

/***/ }),
/* 30 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check element has specific css class
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var inArray = __webpack_require__(5);
var getClass = __webpack_require__(23);

/**
 * Check element has specific css class
 * @param {(HTMLElement|SVGElement)} element - target element
 * @param {string} cssClass - css class
 * @returns {boolean}
 * @memberof module:domUtil
 */
function hasClass(element, cssClass) {
  var origin;

  if (element.classList) {
    return element.classList.contains(cssClass);
  }

  origin = getClass(element).split(/\s+/);

  return inArray(cssClass, origin) > -1;
}

module.exports = hasClass;


/***/ }),
/* 31 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Slider view
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var CustomEvents = __webpack_require__(10);

var getMousePosition = __webpack_require__(53);

var closest = __webpack_require__(54);

var hasClass = __webpack_require__(30);

var extend = __webpack_require__(0);

var inherit = __webpack_require__(18);

var domUtil = __webpack_require__(9);

var svgvml = __webpack_require__(32);

var colorUtil = __webpack_require__(12);

var View = __webpack_require__(8);

var Drag = __webpack_require__(24);

var tmpl = __webpack_require__(57); // Limitation position of point element inside of colorslider and hue bar
// Minimum value can to be negative because that using color point of handle element is center point. not left, top point.


var COLORSLIDER_POS_LIMIT_RANGE = [-7, 112];
var HUEBAR_POS_LIMIT_RANGE = [-3, 115];
var HUE_WHEEL_MAX = 359.99;
/**
 * @constructor
 * @extends {View}
 * @mixes CustomEvents
 * @param {object} options - options for view
 *  @param {string} options.cssPrefix - design css prefix
 * @param {HTMLElement} container - container element
 * @ignore
 */

function Slider(options, container) {
  container = domUtil.appendHTMLElement('div', container, options.cssPrefix + 'slider-container');
  container.style.display = 'none';
  View.call(this, options, container);
  /**
   * @type {object}
   */

  this.options = extend({
    color: '#f8f8f8',
    cssPrefix: 'tui-colorpicker-'
  }, options);
  /**
   * Cache immutable data in click, drag events.
   *
   * (i.e. is event related with colorslider? or huebar?)
   * @type {object}
   * @property {boolean} isColorSlider
   * @property {number[]} containerSize
   */

  this._dragDataCache = {};
  /**
   * Color slider handle element
   * @type {SVG|VML}
   */

  this.sliderHandleElement = null;
  /**
   * hue bar handle element
   * @type {SVG|VML}
   */

  this.huebarHandleElement = null;
  /**
   * Element that render base color in colorslider part
   * @type {SVG|VML}
   */

  this.baseColorElement = null;
  /**
   * @type {Drag}
   */

  this.drag = new Drag({
    distance: 0
  }, container); // bind drag events

  this.drag.on({
    dragStart: this._onDragStart,
    drag: this._onDrag,
    dragEnd: this._onDragEnd,
    click: this._onClick
  }, this);
}

inherit(Slider, View);
/**
 * @override
 */

Slider.prototype._beforeDestroy = function () {
  this.drag.off();
  this.drag = this.options = this._dragDataCache = this.sliderHandleElement = this.huebarHandleElement = this.baseColorElement = null;
};
/**
 * Toggle slider view
 * @param {boolean} onOff - set true then reveal slider view
 */


Slider.prototype.toggle = function (onOff) {
  this.container.style.display = !!onOff ? 'block' : 'none';
};
/**
 * Get slider display status
 * @returns {boolean} return true when slider is visible
 */


Slider.prototype.isVisible = function () {
  return this.container.style.display === 'block';
};
/**
 * Render slider view
 * @override
 * @param {string} colorStr - hex string color from parent view (Layout)
 */


Slider.prototype.render = function (colorStr) {
  var container = this.container;
  var options = this.options;
  var html = tmpl.layout;
  var rgb, hsv;

  if (!colorUtil.isValidRGB(colorStr)) {
    return;
  }

  html = html.replace(/{{slider}}/, tmpl.slider);
  html = html.replace(/{{huebar}}/, tmpl.huebar);
  html = html.replace(/{{cssPrefix}}/g, options.cssPrefix);
  html = html.replace(/{{id}}/g, options.id);
  this.container.innerHTML = html;
  this.sliderHandleElement = container.querySelector('.' + options.cssPrefix + 'slider-handle');
  this.huebarHandleElement = container.querySelector('.' + options.cssPrefix + 'huebar-handle');
  this.baseColorElement = container.querySelector('.' + options.cssPrefix + 'slider-basecolor');
  rgb = colorUtil.hexToRGB(colorStr);
  hsv = colorUtil.rgbToHSV.apply(null, rgb);
  this.moveHue(hsv[0], true);
  this.moveSaturationAndValue(hsv[1], hsv[2], true);
};
/**
 * Move colorslider by newLeft(X), newTop(Y) value
 * @private
 * @param {number} newLeft - left pixel value to move handle
 * @param {number} newTop - top pixel value to move handle
 * @param {boolean} [silent=false] - set true then not fire custom event
 */


Slider.prototype._moveColorSliderHandle = function (newLeft, newTop, silent) {
  var handle = this.sliderHandleElement;
  var handleColor; // Check position limitation.

  newTop = Math.max(COLORSLIDER_POS_LIMIT_RANGE[0], newTop);
  newTop = Math.min(COLORSLIDER_POS_LIMIT_RANGE[1], newTop);
  newLeft = Math.max(COLORSLIDER_POS_LIMIT_RANGE[0], newLeft);
  newLeft = Math.min(COLORSLIDER_POS_LIMIT_RANGE[1], newLeft);
  svgvml.setTranslateXY(handle, newLeft, newTop);
  handleColor = newTop > 50 ? 'white' : 'black';
  svgvml.setStrokeColor(handle, handleColor);

  if (!silent) {
    this.fire('_selectColor', {
      color: colorUtil.rgbToHEX.apply(null, this.getRGB())
    });
  }
};
/**
 * Move colorslider by supplied saturation and values.
 *
 * The movement of color slider handle follow HSV cylinder model. {@link https://en.wikipedia.org/wiki/HSL_and_HSV}
 * @param {number} saturation - the percent of saturation (0% ~ 100%)
 * @param {number} value - the percent of saturation (0% ~ 100%)
 * @param {boolean} [silent=false] - set true then not fire custom event
 */


Slider.prototype.moveSaturationAndValue = function (saturation, value, silent) {
  var absMin, maxValue, newLeft, newTop;
  saturation = saturation || 0;
  value = value || 0;
  absMin = Math.abs(COLORSLIDER_POS_LIMIT_RANGE[0]);
  maxValue = COLORSLIDER_POS_LIMIT_RANGE[1]; // subtract absMin value because current color position is not left, top of handle element.
  // The saturation. from left 0 to right 100

  newLeft = saturation * maxValue / 100 - absMin; // The Value. from top 100 to bottom 0. that why newTop subtract by maxValue.

  newTop = maxValue - value * maxValue / 100 - absMin;

  this._moveColorSliderHandle(newLeft, newTop, silent);
};
/**
 * Move color slider handle to supplied position
 *
 * The number of X, Y must be related value from color slider container
 * @private
 * @param {number} x - the pixel value to move handle
 * @param {number} y - the pixel value to move handle
 */


Slider.prototype._moveColorSliderByPosition = function (x, y) {
  var offset = COLORSLIDER_POS_LIMIT_RANGE[0];

  this._moveColorSliderHandle(x + offset, y + offset);
};
/**
 * Get saturation and value value.
 * @returns {number[]} saturation and value
 */


Slider.prototype.getSaturationAndValue = function () {
  var absMin = Math.abs(COLORSLIDER_POS_LIMIT_RANGE[0]);
  var maxValue = absMin + COLORSLIDER_POS_LIMIT_RANGE[1];
  var position = svgvml.getTranslateXY(this.sliderHandleElement);
  var saturation, value;
  saturation = (position[1] + absMin) / maxValue * 100; // The value of HSV color model is inverted. top 100 ~ bottom 0. so subtract by 100

  value = 100 - (position[0] + absMin) / maxValue * 100;
  return [saturation, value];
};
/**
 * Move hue handle supplied pixel value
 * @private
 * @param {number} newTop - pixel to move hue handle
 * @param {boolean} [silent=false] - set true then not fire custom event
 */


Slider.prototype._moveHueHandle = function (newTop, silent) {
  var hueHandleElement = this.huebarHandleElement;
  var baseColorElement = this.baseColorElement;
  var newGradientColor, hexStr;
  newTop = Math.max(HUEBAR_POS_LIMIT_RANGE[0], newTop);
  newTop = Math.min(HUEBAR_POS_LIMIT_RANGE[1], newTop);
  svgvml.setTranslateY(hueHandleElement, newTop);
  newGradientColor = colorUtil.hsvToRGB(this.getHue(), 100, 100);
  hexStr = colorUtil.rgbToHEX.apply(null, newGradientColor);
  svgvml.setGradientColorStop(baseColorElement, hexStr);

  if (!silent) {
    this.fire('_selectColor', {
      color: colorUtil.rgbToHEX.apply(null, this.getRGB())
    });
  }
};
/**
 * Move hue bar handle by supplied degree
 * @param {number} degree - (0 ~ 359.9 degree)
 * @param {boolean} [silent=false] - set true then not fire custom event
 */


Slider.prototype.moveHue = function (degree, silent) {
  var newTop = 0;
  var absMin, maxValue;
  absMin = Math.abs(HUEBAR_POS_LIMIT_RANGE[0]);
  maxValue = absMin + HUEBAR_POS_LIMIT_RANGE[1];
  degree = degree || 0;
  newTop = maxValue * degree / HUE_WHEEL_MAX - absMin;

  this._moveHueHandle(newTop, silent);
};
/**
 * Move hue bar handle by supplied percent
 * @private
 * @param {number} y - pixel value to move hue handle
 */


Slider.prototype._moveHueByPosition = function (y) {
  var offset = HUEBAR_POS_LIMIT_RANGE[0];

  this._moveHueHandle(y + offset);
};
/**
 * Get huebar handle position by color degree
 * @returns {number} degree (0 ~ 359.9 degree)
 */


Slider.prototype.getHue = function () {
  var handle = this.huebarHandleElement;
  var position = svgvml.getTranslateXY(handle);
  var absMin, maxValue;
  absMin = Math.abs(HUEBAR_POS_LIMIT_RANGE[0]);
  maxValue = absMin + HUEBAR_POS_LIMIT_RANGE[1]; // maxValue : 359.99 = pos.y : x

  return (position[0] + absMin) * HUE_WHEEL_MAX / maxValue;
};
/**
 * Get HSV value from slider
 * @returns {number[]} hsv values
 */


Slider.prototype.getHSV = function () {
  var sv = this.getSaturationAndValue();
  var h = this.getHue();
  return [h].concat(sv);
};
/**
 * Get RGB value from slider
 * @returns {number[]} RGB value
 */


Slider.prototype.getRGB = function () {
  return colorUtil.hsvToRGB.apply(null, this.getHSV());
};
/**********
 * Drag event handler
 **********/

/**
 * Cache immutable data when dragging or click view
 * @param {object} event - Click, DragStart event.
 * @returns {object} cached data.
 */


Slider.prototype._prepareColorSliderForMouseEvent = function (event) {
  var options = this.options;
  var sliderPart = closest(event.target, '.' + options.cssPrefix + 'slider-part');
  var cache;
  cache = this._dragDataCache = {
    isColorSlider: hasClass(sliderPart, options.cssPrefix + 'slider-left'),
    parentElement: sliderPart
  };
  return cache;
};
/**
 * Click event handler
 * @param {object} clickEvent - Click event from Drag module
 */


Slider.prototype._onClick = function (clickEvent) {
  var cache = this._prepareColorSliderForMouseEvent(clickEvent);

  var mousePos = getMousePosition(clickEvent.originEvent, cache.parentElement);

  if (cache.isColorSlider) {
    this._moveColorSliderByPosition(mousePos[0], mousePos[1]);
  } else {
    this._moveHueByPosition(mousePos[1]);
  }

  this._dragDataCache = null;
};
/**
 * DragStart event handler
 * @param {object} dragStartEvent - dragStart event data from Drag#dragStart
 */


Slider.prototype._onDragStart = function (dragStartEvent) {
  this._prepareColorSliderForMouseEvent(dragStartEvent);
};
/**
 * Drag event handler
 * @param {Drag#drag} dragEvent - drag event data
 */


Slider.prototype._onDrag = function (dragEvent) {
  var cache = this._dragDataCache;
  var mousePos = getMousePosition(dragEvent.originEvent, cache.parentElement);

  if (cache.isColorSlider) {
    this._moveColorSliderByPosition(mousePos[0], mousePos[1]);
  } else {
    this._moveHueByPosition(mousePos[1]);
  }
};
/**
 * Drag#dragEnd event handler
 */


Slider.prototype._onDragEnd = function () {
  this._dragDataCache = null;
};

CustomEvents.mixin(Slider);
module.exports = Slider;

/***/ }),
/* 32 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview module for manipulate SVG or VML object
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var isOldBrowser = __webpack_require__(4).isOldBrowser;

var PARSE_TRANSLATE_NUM_REGEX = /[\.\-0-9]+/g;
var SVG_HUE_HANDLE_RIGHT_POS = -6;
/* istanbul ignore next */

var svgvml = {
  /**
   * Get translate transform value
   * @param {SVG|VML} obj - svg or vml object that want to know translate x, y
   * @returns {number[]} translated coordinates [x, y]
   */
  getTranslateXY: function (obj) {
    var temp;

    if (isOldBrowser) {
      temp = obj.style;
      return [parseFloat(temp.top), parseFloat(temp.left)];
    }

    temp = obj.getAttribute('transform');

    if (!temp) {
      return [0, 0];
    }

    temp = temp.match(PARSE_TRANSLATE_NUM_REGEX); // need caution for difference of VML, SVG coordinates system.
    // translate command need X coords in first parameter. but VML is use CSS coordinate system(top, left)

    return [parseFloat(temp[1]), parseFloat(temp[0])];
  },

  /**
   * Set translate transform value
   * @param {SVG|VML} obj - SVG or VML object to setting translate transform.
   * @param {number} x - translate X value
   * @param {number} y - translate Y value
   */
  setTranslateXY: function (obj, x, y) {
    if (isOldBrowser) {
      obj.style.left = x + 'px';
      obj.style.top = y + 'px';
    } else {
      obj.setAttribute('transform', 'translate(' + x + ',' + y + ')');
    }
  },

  /**
   * Set translate only Y value
   * @param {SVG|VML} obj - SVG or VML object to setting translate transform.
   * @param {number} y - translate Y value
   */
  setTranslateY: function (obj, y) {
    if (isOldBrowser) {
      obj.style.top = y + 'px';
    } else {
      obj.setAttribute('transform', 'translate(' + SVG_HUE_HANDLE_RIGHT_POS + ',' + y + ')');
    }
  },

  /**
   * Set stroke color to SVG or VML object
   * @param {SVG|VML} obj - SVG or VML object to setting stroke color
   * @param {string} colorStr - color string
   */
  setStrokeColor: function (obj, colorStr) {
    if (isOldBrowser) {
      obj.strokecolor = colorStr;
    } else {
      obj.setAttribute('stroke', colorStr);
    }
  },

  /**
   * Set gradient stop color to SVG, VML object.
   * @param {SVG|VML} obj - SVG, VML object to applying gradient stop color
   * @param {string} colorStr - color string
   */
  setGradientColorStop: function (obj, colorStr) {
    if (isOldBrowser) {
      obj.color = colorStr;
    } else {
      obj.setAttribute('stop-color', colorStr);
    }
  }
};
module.exports = svgvml;

/***/ }),
/* 33 */
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(34);
module.exports = __webpack_require__(35);


/***/ }),
/* 34 */
/***/ (function(module, exports, __webpack_require__) {

// extracted by mini-css-extract-plugin

/***/ }),
/* 35 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var Collection = __webpack_require__(19);

var View = __webpack_require__(8);

var Drag = __webpack_require__(24);

var create = __webpack_require__(48);

var Palette = __webpack_require__(29);

var Slider = __webpack_require__(31);

var colorUtil = __webpack_require__(12);

var svgvml = __webpack_require__(32);

var colorPicker = {
  Collection: Collection,
  View: View,
  Drag: Drag,
  create: create,
  Palette: Palette,
  Slider: Slider,
  colorutil: colorUtil,
  svgvml: svgvml
};
module.exports = colorPicker;

/***/ }),
/* 36 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check whether the given variable is null or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Check whether the given variable is null or not.
 * If the given variable(arguments[0]) is null, returns true.
 * @param {*} obj - Target for checking
 * @returns {boolean} Is null?
 * @memberof module:type
 */
function isNull(obj) {
  return obj === null;
}

module.exports = isNull;


/***/ }),
/* 37 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Send hostname on DOMContentLoaded.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var isUndefined = __webpack_require__(3);
var imagePing = __webpack_require__(38);

var ms7days = 7 * 24 * 60 * 60 * 1000;

/**
 * Check if the date has passed 7 days
 * @param {number} date - milliseconds
 * @returns {boolean}
 * @private
 */
function isExpired(date) {
  var now = new Date().getTime();

  return now - date > ms7days;
}

/**
 * Send hostname on DOMContentLoaded.
 * To prevent hostname set tui.usageStatistics to false.
 * @param {string} appName - application name
 * @param {string} trackingId - GA tracking ID
 * @ignore
 */
function sendHostname(appName, trackingId) {
  var url = 'https://www.google-analytics.com/collect';
  var hostname = location.hostname;
  var hitType = 'event';
  var eventCategory = 'use';
  var applicationKeyForStorage = 'TOAST UI ' + appName + ' for ' + hostname + ': Statistics';
  var date = window.localStorage.getItem(applicationKeyForStorage);

  // skip if the flag is defined and is set to false explicitly
  if (!isUndefined(window.tui) && window.tui.usageStatistics === false) {
    return;
  }

  // skip if not pass seven days old
  if (date && !isExpired(date)) {
    return;
  }

  window.localStorage.setItem(applicationKeyForStorage, new Date().getTime());

  setTimeout(function() {
    if (document.readyState === 'interactive' || document.readyState === 'complete') {
      imagePing(url, {
        v: 1,
        t: hitType,
        tid: trackingId,
        cid: hostname,
        dp: hostname,
        dh: appName,
        el: appName,
        ec: eventCategory
      });
    }
  }, 1000);
}

module.exports = sendHostname;


/***/ }),
/* 38 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Request image ping.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var forEachOwnProperties = __webpack_require__(7);

/**
 * @module request
 */

/**
 * Request image ping.
 * @param {String} url url for ping request
 * @param {Object} trackingInfo infos for make query string
 * @returns {HTMLElement}
 * @memberof module:request
 * @example
 * var imagePing = require('tui-code-snippet/request/imagePing'); // node, commonjs
 *
 * imagePing('https://www.google-analytics.com/collect', {
 *     v: 1,
 *     t: 'event',
 *     tid: 'trackingid',
 *     cid: 'cid',
 *     dp: 'dp',
 *     dh: 'dh'
 * });
 */
function imagePing(url, trackingInfo) {
  var trackingElement = document.createElement('img');
  var queryString = '';
  forEachOwnProperties(trackingInfo, function(value, key) {
    queryString += '&' + key + '=' + value;
  });
  queryString = queryString.substring(1);

  trackingElement.src = url + '?' + queryString;

  trackingElement.style.display = 'none';
  document.body.appendChild(trackingElement);
  document.body.removeChild(trackingElement);

  return trackingElement;
}

module.exports = imagePing;


/***/ }),
/* 39 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Add css class to element
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var forEach = __webpack_require__(2);
var inArray = __webpack_require__(5);
var getClass = __webpack_require__(23);
var setClassName = __webpack_require__(40);

/**
 * domUtil module
 * @module domUtil
 */

/**
 * Add css class to element
 * @param {(HTMLElement|SVGElement)} element - target element
 * @param {...string} cssClass - css classes to add
 * @memberof module:domUtil
 */
function addClass(element) {
  var cssClass = Array.prototype.slice.call(arguments, 1);
  var classList = element.classList;
  var newClass = [];
  var origin;

  if (classList) {
    forEach(cssClass, function(name) {
      element.classList.add(name);
    });

    return;
  }

  origin = getClass(element);

  if (origin) {
    cssClass = [].concat(origin.split(/\s+/), cssClass);
  }

  forEach(cssClass, function(cls) {
    if (inArray(cls, newClass) < 0) {
      newClass.push(cls);
    }
  });

  setClassName(element, newClass);
}

module.exports = addClass;


/***/ }),
/* 40 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Set className value
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var isArray = __webpack_require__(1);
var isUndefined = __webpack_require__(3);

/**
 * Set className value
 * @param {(HTMLElement|SVGElement)} element - target element
 * @param {(string|string[])} cssClass - class names
 * @private
 */
function setClassName(element, cssClass) {
  cssClass = isArray(cssClass) ? cssClass.join(' ') : cssClass;

  cssClass = cssClass.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, '');

  if (isUndefined(element.className.baseVal)) {
    element.className = cssClass;

    return;
  }

  element.className.baseVal = cssClass;
}

module.exports = setClassName;


/***/ }),
/* 41 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check whether the given variable is a number or not.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * Check whether the given variable is a number or not.
 * If the given variable is a number, return true.
 * @param {*} obj - Target for checking
 * @returns {boolean} Is number?
 * @memberof module:type
 */
function isNumber(obj) {
  return typeof obj === 'number' || obj instanceof Number;
}

module.exports = isNumber;


/***/ }),
/* 42 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Disable browser's text selection behaviors.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var on = __webpack_require__(14);
var preventDefault = __webpack_require__(15);
var setData = __webpack_require__(43);
var testCSSProp = __webpack_require__(27);

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


/***/ }),
/* 43 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Set data attribute to target element
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var convertToKebabCase = __webpack_require__(16);

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


/***/ }),
/* 44 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Transform the Array-like object to Array.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var off = __webpack_require__(17);
var preventDefault = __webpack_require__(15);
var getData = __webpack_require__(45);
var removeData = __webpack_require__(46);
var testCSSProp = __webpack_require__(27);

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


/***/ }),
/* 45 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Get data value from data-attribute
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var convertToKebabCase = __webpack_require__(16);

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


/***/ }),
/* 46 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Remove data property
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var convertToKebabCase = __webpack_require__(16);

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


/***/ }),
/* 47 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Normalize mouse event's button attributes.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var browser = __webpack_require__(22);
var inArray = __webpack_require__(5);

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


/***/ }),
/* 48 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview ColorPicker factory module
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var CustomEvents = __webpack_require__(10);

var extend = __webpack_require__(0);

var util = __webpack_require__(4);

var colorUtil = __webpack_require__(12);

var Layout = __webpack_require__(49);

var Palette = __webpack_require__(29);

var Slider = __webpack_require__(31);
/**
 * Create an unique id for a color-picker instance.
 * @private
 */


var currentId = 0;

function generateId() {
  currentId += 1;
  return currentId;
}
/**
 * @constructor
 * @param {object} options - options for colorpicker component
 *  @param {HTMLDivElement} options.container - container element
 *  @param {string} [options.color='#ffffff'] - default selected color
 *  @param {string[]} [options.preset] - color preset for palette (use base16 palette if not supplied)
 *  @param {string} [options.cssPrefix='tui-colorpicker-'] - css prefix text for each child elements
 *  @param {string} [options.detailTxt='Detail'] - text for detail button.
 *  @param {boolean} [options.usageStatistics=true] - Let us know the hostname. If you don't want to send the hostname, please set to false.
 * @example
 * var colorPicker = tui.colorPicker; // or require('tui-color-picker')
 *
 * var instance = colorPicker.create({
 *   container: document.getElementById('color-picker')
 * });
 */


function ColorPicker(options) {
  var layout;

  if (!(this instanceof ColorPicker)) {
    return new ColorPicker(options);
  }
  /**
   * Option object
   * @type {object}
   * @private
   */


  options = this.options = extend({
    container: null,
    color: '#f8f8f8',
    preset: ['#181818', '#282828', '#383838', '#585858', '#b8b8b8', '#d8d8d8', '#e8e8e8', '#f8f8f8', '#ab4642', '#dc9656', '#f7ca88', '#a1b56c', '#86c1b9', '#7cafc2', '#ba8baf', '#a16946'],
    cssPrefix: 'tui-colorpicker-',
    detailTxt: 'Detail',
    id: generateId(),
    usageStatistics: true
  }, options);

  if (!options.container) {
    throw new Error('ColorPicker(): need container option.');
  }
  /**********
   * Create layout view
   **********/

  /**
   * @type {Layout}
   * @private
   */


  layout = this.layout = new Layout(options, options.container);
  /**********
   * Create palette view
   **********/

  this.palette = new Palette(options, layout.container);
  this.palette.on({
    _selectColor: this._onSelectColorInPalette,
    _toggleSlider: this._onToggleSlider
  }, this);
  /**********
   * Create slider view
   **********/

  this.slider = new Slider(options, layout.container);
  this.slider.on('_selectColor', this._onSelectColorInSlider, this);
  /**********
   * Add child views
   **********/

  layout.addChild(this.palette);
  layout.addChild(this.slider);
  this.render(options.color);

  if (options.usageStatistics) {
    util.sendHostName();
  }
}
/**
 * Handler method for Palette#_selectColor event
 * @private
 * @fires ColorPicker#selectColor
 * @param {object} selectColorEventData - event data
 */


ColorPicker.prototype._onSelectColorInPalette = function (selectColorEventData) {
  var color = selectColorEventData.color;
  var opt = this.options;

  if (!colorUtil.isValidRGB(color) && color !== '') {
    this.render();
    return;
  }
  /**
   * @event ColorPicker#selectColor
   * @type {object}
   * @property {string} color - selected color (hex string)
   * @property {string} origin - flags for represent the source of event fires.
   */


  this.fire('selectColor', {
    color: color,
    origin: 'palette'
  });

  if (opt.color === color) {
    return;
  }

  opt.color = color;
  this.render(color);
};
/**
 * Handler method for Palette#_toggleSlider event
 * @private
 */


ColorPicker.prototype._onToggleSlider = function () {
  this.slider.toggle(!this.slider.isVisible());
};
/**
 * Handler method for Slider#_selectColor event
 * @private
 * @fires ColorPicker#selectColor
 * @param {object} selectColorEventData - event data
 */


ColorPicker.prototype._onSelectColorInSlider = function (selectColorEventData) {
  var color = selectColorEventData.color;
  var opt = this.options;
  /**
   * @event ColorPicker#selectColor
   * @type {object}
   * @property {string} color - selected color (hex string)
   * @property {string} origin - flags for represent the source of event fires.
   * @ignore
   */

  this.fire('selectColor', {
    color: color,
    origin: 'slider'
  });

  if (opt.color === color) {
    return;
  }

  opt.color = color;
  this.palette.render(color);
};
/**********
 * PUBLIC API
 **********/

/**
 * Set color to colorpicker instance.<br>
 * The string parameter must be hex color value
 * @param {string} hexStr - hex formatted color string
 * @example
 * instance.setColor('#ffff00');
 */


ColorPicker.prototype.setColor = function (hexStr) {
  if (!colorUtil.isValidRGB(hexStr)) {
    throw new Error('ColorPicker#setColor(): need valid hex string color value');
  }

  this.options.color = hexStr;
  this.render(hexStr);
};
/**
 * Get hex color string of current selected color in colorpicker instance.
 * @returns {string} hex string formatted color
 * @example
 * instance.setColor('#ffff00');
 * instance.getColor(); // '#ffff00';
 */


ColorPicker.prototype.getColor = function () {
  return this.options.color;
};
/**
 * Toggle colorpicker element. set true then reveal colorpicker view.
 * @param {boolean} [isShow=false] - A flag to show
 * @example
 * instance.toggle(false); // hide
 * instance.toggle(); // hide
 * instance.toggle(true); // show
 */


ColorPicker.prototype.toggle = function (isShow) {
  this.layout.container.style.display = !!isShow ? 'block' : 'none';
};
/**
 * Render colorpicker
 * @param {string} [color] - selected color
 * @ignore
 */


ColorPicker.prototype.render = function (color) {
  this.layout.render(color || this.options.color);
};
/**
 * Destroy colorpicker instance.
 * @example
 * instance.destroy(); // DOM-element is removed
 */


ColorPicker.prototype.destroy = function () {
  this.layout.destroy();
  this.options.container.innerHTML = '';
  this.layout = this.slider = this.palette = this.options = null;
};

CustomEvents.mixin(ColorPicker);
module.exports = ColorPicker;

/***/ }),
/* 49 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview ColorPicker layout module
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var extend = __webpack_require__(0);

var inherit = __webpack_require__(18);

var domUtil = __webpack_require__(9);

var View = __webpack_require__(8);
/**
 * @constructor
 * @extends {View}
 * @param {object} options - option object
 *  @param {string} options.cssPrefix - css prefix for each child elements
 * @param {HTMLDivElement} container - container
 * @ignore
 */


function Layout(options, container) {
  /**
   * option object
   * @type {object}
   */
  this.options = extend({
    cssPrefix: 'tui-colorpicker-'
  }, options);
  container = domUtil.appendHTMLElement('div', container, this.options.cssPrefix + 'container');
  View.call(this, options, container);
  this.render();
}

inherit(Layout, View);
/**
 * @override
 * @param {string} [color] - selected color
 */

Layout.prototype.render = function (color) {
  this.recursive(function (view) {
    view.render(color);
  }, true);
};

module.exports = Layout;

/***/ }),
/* 50 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Create a new object with the specified prototype object and properties.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



/**
 * @module inheritance
 */

/**
 * Create a new object with the specified prototype object and properties.
 * @param {Object} obj This object will be a prototype of the newly-created object.
 * @returns {Object}
 * @memberof module:inheritance
 */
function createObject(obj) {
  function F() {} // eslint-disable-line require-jsdoc
  F.prototype = obj;

  return new F();
}

module.exports = createObject;


/***/ }),
/* 51 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Palette view template
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var template = __webpack_require__(52);

module.exports = function (context) {
  var item = ['<li><input class="{{cssPrefix}}palette-button{{isSelected @this}}{{getItemClass @this}}" type="button"', '{{if isValidRGB @this}}', ' style="background-color:{{@this}};color:{{@this}}"', '{{/if}}', ' title="{{@this}}" value="{{@this}}" /></li>'].join('');
  var layout = ['<ul class="{{cssPrefix}}clearfix">', '{{each preset}}', item, '{{/each}}', '</ul>', '<div class="{{cssPrefix}}clearfix" style="overflow:hidden">', '<input type="button" class="{{cssPrefix}}palette-toggle-slider" value="{{detailTxt}}" />', '<input type="text" class="{{cssPrefix}}palette-hex" value="{{color}}" maxlength="7" />', '<span class="{{cssPrefix}}palette-preview" style="background-color:{{color}};color:{{color}}">{{color}}</span>', '</div>'].join('\n');
  return template(layout, context);
};

/***/ }),
/* 52 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Convert text by binding expressions with context.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var inArray = __webpack_require__(5);
var forEach = __webpack_require__(2);
var isArray = __webpack_require__(1);
var isString = __webpack_require__(11);
var extend = __webpack_require__(0);

// IE8 does not support capture groups.
var EXPRESSION_REGEXP = /{{\s?|\s?}}/g;
var BRACKET_NOTATION_REGEXP = /^[a-zA-Z0-9_@]+\[[a-zA-Z0-9_@"']+\]$/;
var BRACKET_REGEXP = /\[\s?|\s?\]/;
var DOT_NOTATION_REGEXP = /^[a-zA-Z_]+\.[a-zA-Z_]+$/;
var DOT_REGEXP = /\./;
var STRING_NOTATION_REGEXP = /^["']\w+["']$/;
var STRING_REGEXP = /"|'/g;
var NUMBER_REGEXP = /^-?\d+\.?\d*$/;

var EXPRESSION_INTERVAL = 2;

var BLOCK_HELPERS = {
  'if': handleIf,
  'each': handleEach,
  'with': handleWith
};

var isValidSplit = 'a'.split(/a/).length === 3;

/**
 * Split by RegExp. (Polyfill for IE8)
 * @param {string} text - text to be splitted\
 * @param {RegExp} regexp - regular expression
 * @returns {Array.<string>}
 */
var splitByRegExp = (function() {
  if (isValidSplit) {
    return function(text, regexp) {
      return text.split(regexp);
    };
  }

  return function(text, regexp) {
    var result = [];
    var prevIndex = 0;
    var match, index;

    if (!regexp.global) {
      regexp = new RegExp(regexp, 'g');
    }

    match = regexp.exec(text);
    while (match !== null) {
      index = match.index;
      result.push(text.slice(prevIndex, index));

      prevIndex = index + match[0].length;
      match = regexp.exec(text);
    }
    result.push(text.slice(prevIndex));

    return result;
  };
})();

/**
 * Find value in the context by an expression.
 * @param {string} exp - an expression
 * @param {object} context - context
 * @returns {*}
 * @private
 */
// eslint-disable-next-line complexity
function getValueFromContext(exp, context) {
  var splitedExps;
  var value = context[exp];

  if (exp === 'true') {
    value = true;
  } else if (exp === 'false') {
    value = false;
  } else if (STRING_NOTATION_REGEXP.test(exp)) {
    value = exp.replace(STRING_REGEXP, '');
  } else if (BRACKET_NOTATION_REGEXP.test(exp)) {
    splitedExps = exp.split(BRACKET_REGEXP);
    value = getValueFromContext(splitedExps[0], context)[getValueFromContext(splitedExps[1], context)];
  } else if (DOT_NOTATION_REGEXP.test(exp)) {
    splitedExps = exp.split(DOT_REGEXP);
    value = getValueFromContext(splitedExps[0], context)[splitedExps[1]];
  } else if (NUMBER_REGEXP.test(exp)) {
    value = parseFloat(exp);
  }

  return value;
}

/**
 * Extract elseif and else expressions.
 * @param {Array.<string>} ifExps - args of if expression
 * @param {Array.<string>} sourcesInsideBlock - sources inside if block
 * @returns {object} - exps: expressions of if, elseif, and else / sourcesInsideIf: sources inside if, elseif, and else block.
 * @private
 */
function extractElseif(ifExps, sourcesInsideBlock) {
  var exps = [ifExps];
  var sourcesInsideIf = [];
  var otherIfCount = 0;
  var start = 0;

  // eslint-disable-next-line complexity
  forEach(sourcesInsideBlock, function(source, index) {
    if (source.indexOf('if') === 0) {
      otherIfCount += 1;
    } else if (source === '/if') {
      otherIfCount -= 1;
    } else if (!otherIfCount && (source.indexOf('elseif') === 0 || source === 'else')) {
      exps.push(source === 'else' ? ['true'] : source.split(' ').slice(1));
      sourcesInsideIf.push(sourcesInsideBlock.slice(start, index));
      start = index + 1;
    }
  });

  sourcesInsideIf.push(sourcesInsideBlock.slice(start));

  return {
    exps: exps,
    sourcesInsideIf: sourcesInsideIf
  };
}

/**
 * Helper function for "if". 
 * @param {Array.<string>} exps - array of expressions split by spaces
 * @param {Array.<string>} sourcesInsideBlock - array of sources inside the if block
 * @param {object} context - context
 * @returns {string}
 * @private
 */
function handleIf(exps, sourcesInsideBlock, context) {
  var analyzed = extractElseif(exps, sourcesInsideBlock);
  var result = false;
  var compiledSource = '';

  forEach(analyzed.exps, function(exp, index) {
    result = handleExpression(exp, context);
    if (result) {
      compiledSource = compile(analyzed.sourcesInsideIf[index], context);
    }

    return !result;
  });

  return compiledSource;
}

/**
 * Helper function for "each".
 * @param {Array.<string>} exps - array of expressions split by spaces
 * @param {Array.<string>} sourcesInsideBlock - array of sources inside the each block
 * @param {object} context - context
 * @returns {string}
 * @private
 */
function handleEach(exps, sourcesInsideBlock, context) {
  var collection = handleExpression(exps, context);
  var additionalKey = isArray(collection) ? '@index' : '@key';
  var additionalContext = {};
  var result = '';

  forEach(collection, function(item, key) {
    additionalContext[additionalKey] = key;
    additionalContext['@this'] = item;
    extend(context, additionalContext);

    result += compile(sourcesInsideBlock.slice(), context);
  });

  return result;
}

/**
 * Helper function for "with ... as"
 * @param {Array.<string>} exps - array of expressions split by spaces
 * @param {Array.<string>} sourcesInsideBlock - array of sources inside the with block
 * @param {object} context - context
 * @returns {string}
 * @private
 */
function handleWith(exps, sourcesInsideBlock, context) {
  var asIndex = inArray('as', exps);
  var alias = exps[asIndex + 1];
  var result = handleExpression(exps.slice(0, asIndex), context);

  var additionalContext = {};
  additionalContext[alias] = result;

  return compile(sourcesInsideBlock, extend(context, additionalContext)) || '';
}

/**
 * Extract sources inside block in place.
 * @param {Array.<string>} sources - array of sources
 * @param {number} start - index of start block
 * @param {number} end - index of end block
 * @returns {Array.<string>}
 * @private
 */
function extractSourcesInsideBlock(sources, start, end) {
  var sourcesInsideBlock = sources.splice(start + 1, end - start);
  sourcesInsideBlock.pop();

  return sourcesInsideBlock;
}

/**
 * Handle block helper function
 * @param {string} helperKeyword - helper keyword (ex. if, each, with)
 * @param {Array.<string>} sourcesToEnd - array of sources after the starting block
 * @param {object} context - context
 * @returns {Array.<string>}
 * @private
 */
function handleBlockHelper(helperKeyword, sourcesToEnd, context) {
  var executeBlockHelper = BLOCK_HELPERS[helperKeyword];
  var helperCount = 1;
  var startBlockIndex = 0;
  var endBlockIndex;
  var index = startBlockIndex + EXPRESSION_INTERVAL;
  var expression = sourcesToEnd[index];

  while (helperCount && isString(expression)) {
    if (expression.indexOf(helperKeyword) === 0) {
      helperCount += 1;
    } else if (expression.indexOf('/' + helperKeyword) === 0) {
      helperCount -= 1;
      endBlockIndex = index;
    }

    index += EXPRESSION_INTERVAL;
    expression = sourcesToEnd[index];
  }

  if (helperCount) {
    throw Error(helperKeyword + ' needs {{/' + helperKeyword + '}} expression.');
  }

  sourcesToEnd[startBlockIndex] = executeBlockHelper(
    sourcesToEnd[startBlockIndex].split(' ').slice(1),
    extractSourcesInsideBlock(sourcesToEnd, startBlockIndex, endBlockIndex),
    context
  );

  return sourcesToEnd;
}

/**
 * Helper function for "custom helper".
 * If helper is not a function, return helper itself.
 * @param {Array.<string>} exps - array of expressions split by spaces (first element: helper)
 * @param {object} context - context
 * @returns {string}
 * @private
 */
function handleExpression(exps, context) {
  var result = getValueFromContext(exps[0], context);

  if (result instanceof Function) {
    return executeFunction(result, exps.slice(1), context);
  }

  return result;
}

/**
 * Execute a helper function.
 * @param {Function} helper - helper function
 * @param {Array.<string>} argExps - expressions of arguments
 * @param {object} context - context
 * @returns {string} - result of executing the function with arguments
 * @private
 */
function executeFunction(helper, argExps, context) {
  var args = [];
  forEach(argExps, function(exp) {
    args.push(getValueFromContext(exp, context));
  });

  return helper.apply(null, args);
}

/**
 * Get a result of compiling an expression with the context.
 * @param {Array.<string>} sources - array of sources split by regexp of expression.
 * @param {object} context - context
 * @returns {Array.<string>} - array of sources that bind with its context
 * @private
 */
function compile(sources, context) {
  var index = 1;
  var expression = sources[index];
  var exps, firstExp, result;

  while (isString(expression)) {
    exps = expression.split(' ');
    firstExp = exps[0];

    if (BLOCK_HELPERS[firstExp]) {
      result = handleBlockHelper(firstExp, sources.splice(index, sources.length - index), context);
      sources = sources.concat(result);
    } else {
      sources[index] = handleExpression(exps, context);
    }

    index += EXPRESSION_INTERVAL;
    expression = sources[index];
  }

  return sources.join('');
}

/**
 * Convert text by binding expressions with context.
 * <br>
 * If expression exists in the context, it will be replaced.
 * ex) '{{title}}' with context {title: 'Hello!'} is converted to 'Hello!'.
 * An array or object can be accessed using bracket and dot notation.
 * ex) '{{odds\[2\]}}' with context {odds: \[1, 3, 5\]} is converted to '5'.
 * ex) '{{evens\[first\]}}' with context {evens: \[2, 4\], first: 0} is converted to '2'.
 * ex) '{{project\["name"\]}}' and '{{project.name}}' with context {project: {name: 'CodeSnippet'}} is converted to 'CodeSnippet'.
 * <br>
 * If replaced expression is a function, next expressions will be arguments of the function.
 * ex) '{{add 1 2}}' with context {add: function(a, b) {return a + b;}} is converted to '3'.
 * <br>
 * It has 3 predefined block helpers '{{helper ...}} ... {{/helper}}': 'if', 'each', 'with ... as ...'.
 * 1) 'if' evaluates conditional statements. It can use with 'elseif' and 'else'.
 * 2) 'each' iterates an array or object. It provides '@index'(array), '@key'(object), and '@this'(current element).
 * 3) 'with ... as ...' provides an alias.
 * @param {string} text - text with expressions
 * @param {object} context - context
 * @returns {string} - text that bind with its context
 * @memberof module:domUtil
 * @example
 * var template = require('tui-code-snippet/domUtil/template');
 * 
 * var source = 
 *     '<h1>'
 *   +   '{{if isValidNumber title}}'
 *   +     '{{title}}th'
 *   +   '{{elseif isValidDate title}}'
 *   +     'Date: {{title}}'
 *   +   '{{/if}}'
 *   + '</h1>'
 *   + '{{each list}}'
 *   +   '{{with addOne @index as idx}}'
 *   +     '<p>{{idx}}: {{@this}}</p>'
 *   +   '{{/with}}'
 *   + '{{/each}}';
 * 
 * var context = {
 *   isValidDate: function(text) {
 *     return /^\d{4}-(0|1)\d-(0|1|2|3)\d$/.test(text);
 *   },
 *   isValidNumber: function(text) {
 *     return /^\d+$/.test(text);
 *   }
 *   title: '2019-11-25',
 *   list: ['Clean the room', 'Wash the dishes'],
 *   addOne: function(num) {
 *     return num + 1;
 *   }
 * };
 * 
 * var result = template(source, context);
 * console.log(result); // <h1>Date: 2019-11-25</h1><p>1: Clean the room</p><p>2: Wash the dishes</p>
 */
function template(text, context) {
  return compile(splitByRegExp(text, EXPRESSION_REGEXP), context);
}

module.exports = template;


/***/ }),
/* 53 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Get mouse position from mouse event
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var isArray = __webpack_require__(1);

/**
 * Get mouse position from mouse event
 *
 * If supplied relatveElement parameter then return relative position based on
 *  element
 * @param {(MouseEvent|object|number[])} position - mouse position object
 * @param {HTMLElement} relativeElement HTML element that calculate relative
 *  position
 * @returns {number[]} mouse position
 * @memberof module:domEvent
 */
function getMousePosition(position, relativeElement) {
  var positionArray = isArray(position);
  var clientX = positionArray ? position[0] : position.clientX;
  var clientY = positionArray ? position[1] : position.clientY;
  var rect;

  if (!relativeElement) {
    return [clientX, clientY];
  }

  rect = relativeElement.getBoundingClientRect();

  return [
    clientX - rect.left - relativeElement.clientLeft,
    clientY - rect.top - relativeElement.clientTop
  ];
}

module.exports = getMousePosition;


/***/ }),
/* 54 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Find parent element recursively
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var matches = __webpack_require__(55);

/**
 * Find parent element recursively
 * @param {HTMLElement} element - base element to start find
 * @param {string} selector - selector string for find
 * @returns {HTMLElement} - element finded or null
 * @memberof module:domUtil
 */
function closest(element, selector) {
  var parent = element.parentNode;

  if (matches(element, selector)) {
    return element;
  }

  while (parent && parent !== document) {
    if (matches(parent, selector)) {
      return parent;
    }

    parent = parent.parentNode;
  }

  return null;
}

module.exports = closest;


/***/ }),
/* 55 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Check element match selector
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var inArray = __webpack_require__(5);
var toArray = __webpack_require__(56);

var elProto = Element.prototype;
var matchSelector = elProto.matches ||
    elProto.webkitMatchesSelector ||
    elProto.mozMatchesSelector ||
    elProto.msMatchesSelector ||
    function(selector) {
      var doc = this.document || this.ownerDocument;

      return inArray(this, toArray(doc.querySelectorAll(selector))) > -1;
    };

/**
 * Check element match selector
 * @param {HTMLElement} element - element to check
 * @param {string} selector - selector to check
 * @returns {boolean} is selector matched to element?
 * @memberof module:domUtil
 */
function matches(element, selector) {
  return matchSelector.call(element, selector);
}

module.exports = matches;


/***/ }),
/* 56 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/**
 * @fileoverview Transform the Array-like object to Array.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */



var forEachArray = __webpack_require__(6);

/**
 * Transform the Array-like object to Array.
 * In low IE (below 8), Array.prototype.slice.call is not perfect. So, try-catch statement is used.
 * @param {*} arrayLike Array-like object
 * @returns {Array} Array
 * @memberof module:collection
 * @example
 * var toArray = require('tui-code-snippet/collection/toArray'); // node, commonjs
 *
 * var arrayLike = {
 *     0: 'one',
 *     1: 'two',
 *     2: 'three',
 *     3: 'four',
 *     length: 4
 * };
 * var result = toArray(arrayLike);
 *
 * alert(result instanceof Array); // true
 * alert(result); // one,two,three,four
 */
function toArray(arrayLike) {
  var arr;
  try {
    arr = Array.prototype.slice.call(arrayLike);
  } catch (e) {
    arr = [];
    forEachArray(arrayLike, function(value) {
      arr.push(value);
    });
  }

  return arr;
}

module.exports = toArray;


/***/ }),
/* 57 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/* WEBPACK VAR INJECTION */(function(global) {/**
 * @fileoverview Slider template
 * @author NHN. FE Development Team <dl_javascript@nhn.com>
 */


var isOldBrowser = __webpack_require__(4).isOldBrowser;

var layout = ['<div class="{{cssPrefix}}slider-left {{cssPrefix}}slider-part">{{slider}}</div>', '<div class="{{cssPrefix}}slider-right {{cssPrefix}}slider-part">{{huebar}}</div>'].join('\n');
var SVGSlider = ['<svg class="{{cssPrefix}}svg {{cssPrefix}}svg-slider">', '<defs>', '<linearGradient id="{{cssPrefix}}svg-fill-color-{{id}}" x1="0%" y1="0%" x2="100%" y2="0%">', '<stop offset="0%" stop-color="rgb(255,255,255)" />', '<stop class="{{cssPrefix}}slider-basecolor" offset="100%" stop-color="rgb(255,0,0)" />', '</linearGradient>', '<linearGradient id="{{cssPrefix}}svn-fill-black-{{id}}" x1="0%" y1="0%" x2="0%" y2="100%">', '<stop offset="0%" style="stop-color:rgb(0,0,0);stop-opacity:0" />', '<stop offset="100%" style="stop-color:rgb(0,0,0);stop-opacity:1" />', '</linearGradient>', '</defs>', '<rect width="100%" height="100%" fill="url(#{{cssPrefix}}svg-fill-color-{{id}})"></rect>', '<rect width="100%" height="100%" fill="url(#{{cssPrefix}}svn-fill-black-{{id}})"></rect>', '<path transform="translate(0,0)" class="{{cssPrefix}}slider-handle" d="M0 7.5 L15 7.5 M7.5 15 L7.5 0 M2 7 a5.5 5.5 0 1 1 0 1 Z" stroke="black" stroke-width="0.75" fill="none" />', '</svg>'].join('\n');
var VMLSlider = ['<div class="{{cssPrefix}}vml-slider">', '<v:rect strokecolor="none" class="{{cssPrefix}}vml {{cssPrefix}}vml-slider-bg">', '<v:fill class="{{cssPrefix}}vml {{cssPrefix}}slider-basecolor" type="gradient" method="none" color="#ff0000" color2="#fff" angle="90" />', '</v:rect>', '<v:rect strokecolor="#ccc" class="{{cssPrefix}}vml {{cssPrefix}}vml-slider-bg">', '<v:fill type="gradient" method="none" color="black" color2="white" o:opacity2="0%" class="{{cssPrefix}}vml" />', '</v:rect>', '<v:shape class="{{cssPrefix}}vml {{cssPrefix}}slider-handle" coordsize="1 1" style="width:1px;height:1px;"' + 'path="m 0,7 l 14,7 m 7,14 l 7,0 ar 12,12 2,2 z" filled="false" stroked="true" />', '</div>'].join('\n');
var SVGHuebar = ['<svg class="{{cssPrefix}}svg {{cssPrefix}}svg-huebar">', '<defs>', '<linearGradient id="g-{{id}}" x1="0%" y1="0%" x2="0%" y2="100%">', '<stop offset="0%" stop-color="rgb(255,0,0)" />', '<stop offset="16.666%" stop-color="rgb(255,255,0)" />', '<stop offset="33.333%" stop-color="rgb(0,255,0)" />', '<stop offset="50%" stop-color="rgb(0,255,255)" />', '<stop offset="66.666%" stop-color="rgb(0,0,255)" />', '<stop offset="83.333%" stop-color="rgb(255,0,255)" />', '<stop offset="100%" stop-color="rgb(255,0,0)" />', '</linearGradient>', '</defs>', '<rect width="18px" height="100%" fill="url(#g-{{id}})"></rect>', '<path transform="translate(-6,-3)" class="{{cssPrefix}}huebar-handle" d="M0 0 L4 4 L0 8 L0 0 Z" fill="black" stroke="none" />', '</svg>'].join('\n');
var VMLHuebar = ['<div class="{{cssPrefix}}vml-huebar">', '<v:rect strokecolor="#ccc" class="{{cssPrefix}}vml {{cssPrefix}}vml-huebar-bg">', '<v:fill type="gradient" method="none" colors="' + '0% rgb(255,0,0), 16.666% rgb(255,255,0), 33.333% rgb(0,255,0), 50% rgb(0,255,255), 66.666% rgb(0,0,255), 83.333% rgb(255,0,255), 100% rgb(255,0,0)' + '" angle="180" class="{{cssPrefix}}vml" />', '</v:rect>', '<v:shape class="{{cssPrefix}}vml {{cssPrefix}}huebar-handle" coordsize="1 1" style="width:1px;height:1px;position:absolute;z-index:1;right:22px;top:-3px;"' + 'path="m 0,0 l 4,4 l 0,8 l 0,0 z" filled="true" fillcolor="black" stroked="false" />', '</div>'].join('\n');

if (isOldBrowser) {
  global.document.namespaces.add('v', 'urn:schemas-microsoft-com:vml');
}

module.exports = {
  layout: layout,
  slider: isOldBrowser ? VMLSlider : SVGSlider,
  huebar: isOldBrowser ? VMLHuebar : SVGHuebar
};
/* WEBPACK VAR INJECTION */}.call(this, __webpack_require__(25)))

/***/ })
/******/ ]);
});