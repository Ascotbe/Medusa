/******/ (function(modules) { // webpackBootstrap
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
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
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
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 3);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

/* WEBPACK VAR INJECTION */(function(global) {(function (global, factory) {
	 true ? module.exports = factory() :
	typeof define === 'function' && define.amd ? define(factory) :
	(global.BrowserSpriteSymbol = factory());
}(this, (function () { 'use strict';

var SpriteSymbol = function SpriteSymbol(ref) {
  var id = ref.id;
  var viewBox = ref.viewBox;
  var content = ref.content;

  this.id = id;
  this.viewBox = viewBox;
  this.content = content;
};

/**
 * @return {string}
 */
SpriteSymbol.prototype.stringify = function stringify () {
  return this.content;
};

/**
 * @return {string}
 */
SpriteSymbol.prototype.toString = function toString () {
  return this.stringify();
};

SpriteSymbol.prototype.destroy = function destroy () {
    var this$1 = this;

  ['id', 'viewBox', 'content'].forEach(function (prop) { return delete this$1[prop]; });
};

/**
 * @param {string} content
 * @return {Element}
 */
var parse = function (content) {
  var hasImportNode = !!document.importNode;
  var doc = new DOMParser().parseFromString(content, 'image/svg+xml').documentElement;

  /**
   * Fix for browser which are throwing WrongDocumentError
   * if you insert an element which is not part of the document
   * @see http://stackoverflow.com/a/7986519/4624403
   */
  if (hasImportNode) {
    return document.importNode(doc, true);
  }

  return doc;
};

var commonjsGlobal = typeof window !== 'undefined' ? window : typeof global !== 'undefined' ? global : typeof self !== 'undefined' ? self : {};





function createCommonjsModule(fn, module) {
	return module = { exports: {} }, fn(module, module.exports), module.exports;
}

var index = createCommonjsModule(function (module, exports) {
(function (root, factory) {
    if (false) {
        undefined(factory);
    } else {
        module.exports = factory();
    }
}(commonjsGlobal, function () {

function isMergeableObject(val) {
    var nonNullObject = val && typeof val === 'object';

    return nonNullObject
        && Object.prototype.toString.call(val) !== '[object RegExp]'
        && Object.prototype.toString.call(val) !== '[object Date]'
}

function emptyTarget(val) {
    return Array.isArray(val) ? [] : {}
}

function cloneIfNecessary(value, optionsArgument) {
    var clone = optionsArgument && optionsArgument.clone === true;
    return (clone && isMergeableObject(value)) ? deepmerge(emptyTarget(value), value, optionsArgument) : value
}

function defaultArrayMerge(target, source, optionsArgument) {
    var destination = target.slice();
    source.forEach(function(e, i) {
        if (typeof destination[i] === 'undefined') {
            destination[i] = cloneIfNecessary(e, optionsArgument);
        } else if (isMergeableObject(e)) {
            destination[i] = deepmerge(target[i], e, optionsArgument);
        } else if (target.indexOf(e) === -1) {
            destination.push(cloneIfNecessary(e, optionsArgument));
        }
    });
    return destination
}

function mergeObject(target, source, optionsArgument) {
    var destination = {};
    if (isMergeableObject(target)) {
        Object.keys(target).forEach(function (key) {
            destination[key] = cloneIfNecessary(target[key], optionsArgument);
        });
    }
    Object.keys(source).forEach(function (key) {
        if (!isMergeableObject(source[key]) || !target[key]) {
            destination[key] = cloneIfNecessary(source[key], optionsArgument);
        } else {
            destination[key] = deepmerge(target[key], source[key], optionsArgument);
        }
    });
    return destination
}

function deepmerge(target, source, optionsArgument) {
    var array = Array.isArray(source);
    var options = optionsArgument || { arrayMerge: defaultArrayMerge };
    var arrayMerge = options.arrayMerge || defaultArrayMerge;

    if (array) {
        return Array.isArray(target) ? arrayMerge(target, source, optionsArgument) : cloneIfNecessary(source, optionsArgument)
    } else {
        return mergeObject(target, source, optionsArgument)
    }
}

deepmerge.all = function deepmergeAll(array, optionsArgument) {
    if (!Array.isArray(array) || array.length < 2) {
        throw new Error('first argument should be an array with at least two elements')
    }

    // we are sure there are at least 2 values, so it is safe to have no initial value
    return array.reduce(function(prev, next) {
        return deepmerge(prev, next, optionsArgument)
    })
};

return deepmerge

}));
});

var namespaces_1 = createCommonjsModule(function (module, exports) {
var namespaces = {
  svg: {
    name: 'xmlns',
    uri: 'http://www.w3.org/2000/svg'
  },
  xlink: {
    name: 'xmlns:xlink',
    uri: 'http://www.w3.org/1999/xlink'
  }
};

exports.default = namespaces;
module.exports = exports.default;
});

/**
 * @param {Object} attrs
 * @return {string}
 */
var objectToAttrsString = function (attrs) {
  return Object.keys(attrs).map(function (attr) {
    var value = attrs[attr].toString().replace(/"/g, '&quot;');
    return (attr + "=\"" + value + "\"");
  }).join(' ');
};

var svg = namespaces_1.svg;
var xlink = namespaces_1.xlink;

var defaultAttrs = {};
defaultAttrs[svg.name] = svg.uri;
defaultAttrs[xlink.name] = xlink.uri;

/**
 * @param {string} [content]
 * @param {Object} [attributes]
 * @return {string}
 */
var wrapInSvgString = function (content, attributes) {
  if ( content === void 0 ) content = '';

  var attrs = index(defaultAttrs, attributes || {});
  var attrsRendered = objectToAttrsString(attrs);
  return ("<svg " + attrsRendered + ">" + content + "</svg>");
};

var BrowserSpriteSymbol = (function (SpriteSymbol$$1) {
  function BrowserSpriteSymbol () {
    SpriteSymbol$$1.apply(this, arguments);
  }

  if ( SpriteSymbol$$1 ) BrowserSpriteSymbol.__proto__ = SpriteSymbol$$1;
  BrowserSpriteSymbol.prototype = Object.create( SpriteSymbol$$1 && SpriteSymbol$$1.prototype );
  BrowserSpriteSymbol.prototype.constructor = BrowserSpriteSymbol;

  var prototypeAccessors = { isMounted: {} };

  prototypeAccessors.isMounted.get = function () {
    return !!this.node;
  };

  /**
   * @param {Element} node
   * @return {BrowserSpriteSymbol}
   */
  BrowserSpriteSymbol.createFromExistingNode = function createFromExistingNode (node) {
    return new BrowserSpriteSymbol({
      id: node.getAttribute('id'),
      viewBox: node.getAttribute('viewBox'),
      content: node.outerHTML
    });
  };

  BrowserSpriteSymbol.prototype.destroy = function destroy () {
    if (this.isMounted) {
      this.unmount();
    }
    SpriteSymbol$$1.prototype.destroy.call(this);
  };

  /**
   * @param {Element|string} target
   * @return {Element}
   */
  BrowserSpriteSymbol.prototype.mount = function mount (target) {
    if (this.isMounted) {
      return this.node;
    }

    var mountTarget = typeof target === 'string' ? document.querySelector(target) : target;
    var node = this.render();
    this.node = node;

    mountTarget.appendChild(node);

    return node;
  };

  /**
   * @return {Element}
   */
  BrowserSpriteSymbol.prototype.render = function render () {
    var content = this.stringify();
    return parse(wrapInSvgString(content)).childNodes[0];
  };

  BrowserSpriteSymbol.prototype.unmount = function unmount () {
    this.node.parentNode.removeChild(this.node);
  };

  Object.defineProperties( BrowserSpriteSymbol.prototype, prototypeAccessors );

  return BrowserSpriteSymbol;
}(SpriteSymbol));

return BrowserSpriteSymbol;

})));

/* WEBPACK VAR INJECTION */}.call(exports, __webpack_require__(2)))

/***/ }),
/* 1 */
/***/ (function(module, exports, __webpack_require__) {

/* WEBPACK VAR INJECTION */(function(global) {(function (global, factory) {
	 true ? module.exports = factory() :
	typeof define === 'function' && define.amd ? define(factory) :
	(global.BrowserSprite = factory());
}(this, (function () { 'use strict';

var commonjsGlobal = typeof window !== 'undefined' ? window : typeof global !== 'undefined' ? global : typeof self !== 'undefined' ? self : {};





function createCommonjsModule(fn, module) {
	return module = { exports: {} }, fn(module, module.exports), module.exports;
}

var index = createCommonjsModule(function (module, exports) {
(function (root, factory) {
    if (false) {
        undefined(factory);
    } else {
        module.exports = factory();
    }
}(commonjsGlobal, function () {

function isMergeableObject(val) {
    var nonNullObject = val && typeof val === 'object';

    return nonNullObject
        && Object.prototype.toString.call(val) !== '[object RegExp]'
        && Object.prototype.toString.call(val) !== '[object Date]'
}

function emptyTarget(val) {
    return Array.isArray(val) ? [] : {}
}

function cloneIfNecessary(value, optionsArgument) {
    var clone = optionsArgument && optionsArgument.clone === true;
    return (clone && isMergeableObject(value)) ? deepmerge(emptyTarget(value), value, optionsArgument) : value
}

function defaultArrayMerge(target, source, optionsArgument) {
    var destination = target.slice();
    source.forEach(function(e, i) {
        if (typeof destination[i] === 'undefined') {
            destination[i] = cloneIfNecessary(e, optionsArgument);
        } else if (isMergeableObject(e)) {
            destination[i] = deepmerge(target[i], e, optionsArgument);
        } else if (target.indexOf(e) === -1) {
            destination.push(cloneIfNecessary(e, optionsArgument));
        }
    });
    return destination
}

function mergeObject(target, source, optionsArgument) {
    var destination = {};
    if (isMergeableObject(target)) {
        Object.keys(target).forEach(function (key) {
            destination[key] = cloneIfNecessary(target[key], optionsArgument);
        });
    }
    Object.keys(source).forEach(function (key) {
        if (!isMergeableObject(source[key]) || !target[key]) {
            destination[key] = cloneIfNecessary(source[key], optionsArgument);
        } else {
            destination[key] = deepmerge(target[key], source[key], optionsArgument);
        }
    });
    return destination
}

function deepmerge(target, source, optionsArgument) {
    var array = Array.isArray(source);
    var options = optionsArgument || { arrayMerge: defaultArrayMerge };
    var arrayMerge = options.arrayMerge || defaultArrayMerge;

    if (array) {
        return Array.isArray(target) ? arrayMerge(target, source, optionsArgument) : cloneIfNecessary(source, optionsArgument)
    } else {
        return mergeObject(target, source, optionsArgument)
    }
}

deepmerge.all = function deepmergeAll(array, optionsArgument) {
    if (!Array.isArray(array) || array.length < 2) {
        throw new Error('first argument should be an array with at least two elements')
    }

    // we are sure there are at least 2 values, so it is safe to have no initial value
    return array.reduce(function(prev, next) {
        return deepmerge(prev, next, optionsArgument)
    })
};

return deepmerge

}));
});

//      
// An event handler can take an optional event argument
// and should not return a value
                                          
// An array of all currently registered event handlers for a type
                                            
// A map of event types and their corresponding event handlers.
                        
                                   
  

/** Mitt: Tiny (~200b) functional event emitter / pubsub.
 *  @name mitt
 *  @returns {Mitt}
 */
function mitt(all                 ) {
	all = all || Object.create(null);

	return {
		/**
		 * Register an event handler for the given type.
		 *
		 * @param  {String} type	Type of event to listen for, or `"*"` for all events
		 * @param  {Function} handler Function to call in response to given event
		 * @memberOf mitt
		 */
		on: function on(type        , handler              ) {
			(all[type] || (all[type] = [])).push(handler);
		},

		/**
		 * Remove an event handler for the given type.
		 *
		 * @param  {String} type	Type of event to unregister `handler` from, or `"*"`
		 * @param  {Function} handler Handler function to remove
		 * @memberOf mitt
		 */
		off: function off(type        , handler              ) {
			if (all[type]) {
				all[type].splice(all[type].indexOf(handler) >>> 0, 1);
			}
		},

		/**
		 * Invoke all handlers for the given type.
		 * If present, `"*"` handlers are invoked after type-matched handlers.
		 *
		 * @param {String} type  The event type to invoke
		 * @param {Any} [evt]  Any value (object is recommended and powerful), passed to each handler
		 * @memberof mitt
		 */
		emit: function emit(type        , evt     ) {
			(all[type] || []).map(function (handler) { handler(evt); });
			(all['*'] || []).map(function (handler) { handler(type, evt); });
		}
	};
}

var namespaces_1 = createCommonjsModule(function (module, exports) {
var namespaces = {
  svg: {
    name: 'xmlns',
    uri: 'http://www.w3.org/2000/svg'
  },
  xlink: {
    name: 'xmlns:xlink',
    uri: 'http://www.w3.org/1999/xlink'
  }
};

exports.default = namespaces;
module.exports = exports.default;
});

/**
 * @param {Object} attrs
 * @return {string}
 */
var objectToAttrsString = function (attrs) {
  return Object.keys(attrs).map(function (attr) {
    var value = attrs[attr].toString().replace(/"/g, '&quot;');
    return (attr + "=\"" + value + "\"");
  }).join(' ');
};

var svg = namespaces_1.svg;
var xlink = namespaces_1.xlink;

var defaultAttrs = {};
defaultAttrs[svg.name] = svg.uri;
defaultAttrs[xlink.name] = xlink.uri;

/**
 * @param {string} [content]
 * @param {Object} [attributes]
 * @return {string}
 */
var wrapInSvgString = function (content, attributes) {
  if ( content === void 0 ) content = '';

  var attrs = index(defaultAttrs, attributes || {});
  var attrsRendered = objectToAttrsString(attrs);
  return ("<svg " + attrsRendered + ">" + content + "</svg>");
};

var svg$1 = namespaces_1.svg;
var xlink$1 = namespaces_1.xlink;

var defaultConfig = {
  attrs: ( obj = {
    style: ['position: absolute', 'width: 0', 'height: 0'].join('; ')
  }, obj[svg$1.name] = svg$1.uri, obj[xlink$1.name] = xlink$1.uri, obj )
};
var obj;

var Sprite = function Sprite(config) {
  this.config = index(defaultConfig, config || {});
  this.symbols = [];
};

/**
 * Add new symbol. If symbol with the same id exists it will be replaced.
 * @param {SpriteSymbol} symbol
 * @return {boolean} `true` - symbol was added, `false` - replaced
 */
Sprite.prototype.add = function add (symbol) {
  var ref = this;
    var symbols = ref.symbols;
  var existing = this.find(symbol.id);

  if (existing) {
    symbols[symbols.indexOf(existing)] = symbol;
    return false;
  }

  symbols.push(symbol);
  return true;
};

/**
 * Remove symbol & destroy it
 * @param {string} id
 * @return {boolean} `true` - symbol was found & successfully destroyed, `false` - otherwise
 */
Sprite.prototype.remove = function remove (id) {
  var ref = this;
    var symbols = ref.symbols;
  var symbol = this.find(id);

  if (symbol) {
    symbols.splice(symbols.indexOf(symbol), 1);
    symbol.destroy();
    return true;
  }

  return false;
};

/**
 * @param {string} id
 * @return {SpriteSymbol|null}
 */
Sprite.prototype.find = function find (id) {
  return this.symbols.filter(function (s) { return s.id === id; })[0] || null;
};

/**
 * @param {string} id
 * @return {boolean}
 */
Sprite.prototype.has = function has (id) {
  return this.find(id) !== null;
};

/**
 * @return {string}
 */
Sprite.prototype.stringify = function stringify () {
  var ref = this.config;
    var attrs = ref.attrs;
  var stringifiedSymbols = this.symbols.map(function (s) { return s.stringify(); }).join('');
  return wrapInSvgString(stringifiedSymbols, attrs);
};

/**
 * @return {string}
 */
Sprite.prototype.toString = function toString () {
  return this.stringify();
};

Sprite.prototype.destroy = function destroy () {
  this.symbols.forEach(function (s) { return s.destroy(); });
};

var SpriteSymbol = function SpriteSymbol(ref) {
  var id = ref.id;
  var viewBox = ref.viewBox;
  var content = ref.content;

  this.id = id;
  this.viewBox = viewBox;
  this.content = content;
};

/**
 * @return {string}
 */
SpriteSymbol.prototype.stringify = function stringify () {
  return this.content;
};

/**
 * @return {string}
 */
SpriteSymbol.prototype.toString = function toString () {
  return this.stringify();
};

SpriteSymbol.prototype.destroy = function destroy () {
    var this$1 = this;

  ['id', 'viewBox', 'content'].forEach(function (prop) { return delete this$1[prop]; });
};

/**
 * @param {string} content
 * @return {Element}
 */
var parse = function (content) {
  var hasImportNode = !!document.importNode;
  var doc = new DOMParser().parseFromString(content, 'image/svg+xml').documentElement;

  /**
   * Fix for browser which are throwing WrongDocumentError
   * if you insert an element which is not part of the document
   * @see http://stackoverflow.com/a/7986519/4624403
   */
  if (hasImportNode) {
    return document.importNode(doc, true);
  }

  return doc;
};

var BrowserSpriteSymbol = (function (SpriteSymbol$$1) {
  function BrowserSpriteSymbol () {
    SpriteSymbol$$1.apply(this, arguments);
  }

  if ( SpriteSymbol$$1 ) BrowserSpriteSymbol.__proto__ = SpriteSymbol$$1;
  BrowserSpriteSymbol.prototype = Object.create( SpriteSymbol$$1 && SpriteSymbol$$1.prototype );
  BrowserSpriteSymbol.prototype.constructor = BrowserSpriteSymbol;

  var prototypeAccessors = { isMounted: {} };

  prototypeAccessors.isMounted.get = function () {
    return !!this.node;
  };

  /**
   * @param {Element} node
   * @return {BrowserSpriteSymbol}
   */
  BrowserSpriteSymbol.createFromExistingNode = function createFromExistingNode (node) {
    return new BrowserSpriteSymbol({
      id: node.getAttribute('id'),
      viewBox: node.getAttribute('viewBox'),
      content: node.outerHTML
    });
  };

  BrowserSpriteSymbol.prototype.destroy = function destroy () {
    if (this.isMounted) {
      this.unmount();
    }
    SpriteSymbol$$1.prototype.destroy.call(this);
  };

  /**
   * @param {Element|string} target
   * @return {Element}
   */
  BrowserSpriteSymbol.prototype.mount = function mount (target) {
    if (this.isMounted) {
      return this.node;
    }

    var mountTarget = typeof target === 'string' ? document.querySelector(target) : target;
    var node = this.render();
    this.node = node;

    mountTarget.appendChild(node);

    return node;
  };

  /**
   * @return {Element}
   */
  BrowserSpriteSymbol.prototype.render = function render () {
    var content = this.stringify();
    return parse(wrapInSvgString(content)).childNodes[0];
  };

  BrowserSpriteSymbol.prototype.unmount = function unmount () {
    this.node.parentNode.removeChild(this.node);
  };

  Object.defineProperties( BrowserSpriteSymbol.prototype, prototypeAccessors );

  return BrowserSpriteSymbol;
}(SpriteSymbol));

var defaultConfig$1 = {
  /**
   * Should following options be automatically configured:
   * - `syncUrlsWithBaseTag`
   * - `locationChangeAngularEmitter`
   * - `moveGradientsOutsideSymbol`
   * @type {boolean}
   */
  autoConfigure: true,

  /**
   * Default mounting selector
   * @type {string}
   */
  mountTo: 'body',

  /**
   * Fix disappearing SVG elements when <base href> exists.
   * Executes when sprite mounted.
   * @see http://stackoverflow.com/a/18265336/796152
   * @see https://github.com/everdimension/angular-svg-base-fix
   * @see https://github.com/angular/angular.js/issues/8934#issuecomment-56568466
   * @type {boolean}
   */
  syncUrlsWithBaseTag: false,

  /**
   * Should sprite listen custom location change event
   * @type {boolean}
   */
  listenLocationChangeEvent: true,

  /**
   * Custom window event name which should be emitted to update sprite urls
   * @type {string}
   */
  locationChangeEvent: 'locationChange',

  /**
   * Emit location change event in Angular automatically
   * @type {boolean}
   */
  locationChangeAngularEmitter: false,

  /**
   * Selector to find symbols usages when updating sprite urls
   * @type {string}
   */
  usagesToUpdate: 'use[*|href]',

  /**
   * Fix Firefox bug when gradients and patterns don't work if they are within a symbol.
   * Executes when sprite is rendered, but not mounted.
   * @see https://bugzilla.mozilla.org/show_bug.cgi?id=306674
   * @see https://bugzilla.mozilla.org/show_bug.cgi?id=353575
   * @see https://bugzilla.mozilla.org/show_bug.cgi?id=1235364
   * @type {boolean}
   */
  moveGradientsOutsideSymbol: false
};

/**
 * @param {*} arrayLike
 * @return {Array}
 */
var arrayFrom = function (arrayLike) {
  return Array.prototype.slice.call(arrayLike, 0);
};

var ua = navigator.userAgent;

var browser = {
  isChrome: /chrome/i.test(ua),
  isFirefox: /firefox/i.test(ua),

  // https://msdn.microsoft.com/en-us/library/ms537503(v=vs.85).aspx
  isIE: /msie/i.test(ua) || /trident/i.test(ua),
  isEdge: /edge/i.test(ua)
};

/**
 * @param {string} name
 * @param {*} data
 */
var dispatchEvent = function (name, data) {
  var event = document.createEvent('CustomEvent');
  event.initCustomEvent(name, false, false, data);
  window.dispatchEvent(event);
};

/**
 * IE doesn't evaluate <style> tags in SVGs that are dynamically added to the page.
 * This trick will trigger IE to read and use any existing SVG <style> tags.
 * @see https://github.com/iconic/SVGInjector/issues/23
 * @see https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/10898469/
 *
 * @param {Element} node DOM Element to search <style> tags in
 * @return {Array<HTMLStyleElement>}
 */
var evalStylesIEWorkaround = function (node) {
  var updatedNodes = [];

  arrayFrom(node.querySelectorAll('style'))
    .forEach(function (style) {
      style.textContent += '';
      updatedNodes.push(style);
    });

  return updatedNodes;
};

/**
 * @param {string} [url] If not provided - current URL will be used
 * @return {string}
 */
var getUrlWithoutFragment = function (url) {
  return (url || window.location.href).split('#')[0];
};

/* global angular */
/**
 * @param {string} eventName
 */
var locationChangeAngularEmitter = function (eventName) {
  angular.module('ng').run(['$rootScope', function ($rootScope) {
    $rootScope.$on('$locationChangeSuccess', function (e, newUrl, oldUrl) {
      dispatchEvent(eventName, { oldUrl: oldUrl, newUrl: newUrl });
    });
  }]);
};

var defaultSelector = 'linearGradient, radialGradient, pattern';

/**
 * @param {Element} svg
 * @param {string} [selector]
 * @return {Element}
 */
var moveGradientsOutsideSymbol = function (svg, selector) {
  if ( selector === void 0 ) selector = defaultSelector;

  arrayFrom(svg.querySelectorAll('symbol')).forEach(function (symbol) {
    arrayFrom(symbol.querySelectorAll(selector)).forEach(function (node) {
      symbol.parentNode.insertBefore(node, symbol);
    });
  });
  return svg;
};

/**
 * @param {NodeList} nodes
 * @param {Function} [matcher]
 * @return {Attr[]}
 */
function selectAttributes(nodes, matcher) {
  var attrs = arrayFrom(nodes).reduce(function (acc, node) {
    if (!node.attributes) {
      return acc;
    }

    var arrayfied = arrayFrom(node.attributes);
    var matched = matcher ? arrayfied.filter(matcher) : arrayfied;
    return acc.concat(matched);
  }, []);

  return attrs;
}

/**
 * @param {NodeList|Node} nodes
 * @param {boolean} [clone=true]
 * @return {string}
 */

var xLinkNS = namespaces_1.xlink.uri;
var xLinkAttrName = 'xlink:href';

// eslint-disable-next-line no-useless-escape
var specialUrlCharsPattern = /[{}|\\\^\[\]`"<>]/g;

function encoder(url) {
  return url.replace(specialUrlCharsPattern, function (match) {
    return ("%" + (match[0].charCodeAt(0).toString(16).toUpperCase()));
  });
}

/**
 * @param {NodeList} nodes
 * @param {string} startsWith
 * @param {string} replaceWith
 * @return {NodeList}
 */
function updateReferences(nodes, startsWith, replaceWith) {
  arrayFrom(nodes).forEach(function (node) {
    var href = node.getAttribute(xLinkAttrName);
    if (href && href.indexOf(startsWith) === 0) {
      var newUrl = href.replace(startsWith, replaceWith);
      node.setAttributeNS(xLinkNS, xLinkAttrName, newUrl);
    }
  });

  return nodes;
}

/**
 * List of SVG attributes to update url() target in them
 */
var attList = [
  'clipPath',
  'colorProfile',
  'src',
  'cursor',
  'fill',
  'filter',
  'marker',
  'markerStart',
  'markerMid',
  'markerEnd',
  'mask',
  'stroke',
  'style'
];

var attSelector = attList.map(function (attr) { return ("[" + attr + "]"); }).join(',');

/**
 * Update URLs in svg image (like `fill="url(...)"`) and update referencing elements
 * @param {Element} svg
 * @param {NodeList} references
 * @param {string|RegExp} startsWith
 * @param {string} replaceWith
 * @return {void}
 *
 * @example
 * const sprite = document.querySelector('svg.sprite');
 * const usages = document.querySelectorAll('use');
 * updateUrls(sprite, usages, '#', 'prefix#');
 */
var updateUrls = function (svg, references, startsWith, replaceWith) {
  var startsWithEncoded = encoder(startsWith);
  var replaceWithEncoded = encoder(replaceWith);

  var nodes = svg.querySelectorAll(attSelector);
  var attrs = selectAttributes(nodes, function (ref) {
    var localName = ref.localName;
    var value = ref.value;

    return attList.indexOf(localName) !== -1 && value.indexOf(("url(" + startsWithEncoded)) !== -1;
  });

  attrs.forEach(function (attr) { return attr.value = attr.value.replace(startsWithEncoded, replaceWithEncoded); });
  updateReferences(references, startsWithEncoded, replaceWithEncoded);
};

/**
 * Internal emitter events
 * @enum
 * @private
 */
var Events = {
  MOUNT: 'mount',
  SYMBOL_MOUNT: 'symbol_mount'
};

var BrowserSprite = (function (Sprite$$1) {
  function BrowserSprite(cfg) {
    var this$1 = this;
    if ( cfg === void 0 ) cfg = {};

    Sprite$$1.call(this, index(defaultConfig$1, cfg));

    var emitter = mitt();
    this._emitter = emitter;
    this.node = null;

    var ref = this;
    var config = ref.config;

    if (config.autoConfigure) {
      this._autoConfigure(cfg);
    }

    if (config.syncUrlsWithBaseTag) {
      var baseUrl = document.getElementsByTagName('base')[0].getAttribute('href');
      emitter.on(Events.MOUNT, function () { return this$1.updateUrls('#', baseUrl); });
    }

    var handleLocationChange = this._handleLocationChange.bind(this);
    this._handleLocationChange = handleLocationChange;

    // Provide way to update sprite urls externally via dispatching custom window event
    if (config.listenLocationChangeEvent) {
      window.addEventListener(config.locationChangeEvent, handleLocationChange);
    }

    // Emit location change event in Angular automatically
    if (config.locationChangeAngularEmitter) {
      locationChangeAngularEmitter(config.locationChangeEvent);
    }

    // After sprite mounted
    emitter.on(Events.MOUNT, function (spriteNode) {
      if (config.moveGradientsOutsideSymbol) {
        moveGradientsOutsideSymbol(spriteNode);
      }
    });

    // After symbol mounted into sprite
    emitter.on(Events.SYMBOL_MOUNT, function (symbolNode) {
      if (config.moveGradientsOutsideSymbol) {
        moveGradientsOutsideSymbol(symbolNode.parentNode);
      }

      if (browser.isIE || browser.isEdge) {
        evalStylesIEWorkaround(symbolNode);
      }
    });
  }

  if ( Sprite$$1 ) BrowserSprite.__proto__ = Sprite$$1;
  BrowserSprite.prototype = Object.create( Sprite$$1 && Sprite$$1.prototype );
  BrowserSprite.prototype.constructor = BrowserSprite;

  var prototypeAccessors = { isMounted: {} };

  /**
   * @return {boolean}
   */
  prototypeAccessors.isMounted.get = function () {
    return !!this.node;
  };

  /**
   * Automatically configure following options
   * - `syncUrlsWithBaseTag`
   * - `locationChangeAngularEmitter`
   * - `moveGradientsOutsideSymbol`
   * @param {Object} cfg
   * @private
   */
  BrowserSprite.prototype._autoConfigure = function _autoConfigure (cfg) {
    var ref = this;
    var config = ref.config;

    if (typeof cfg.syncUrlsWithBaseTag === 'undefined') {
      config.syncUrlsWithBaseTag = typeof document.getElementsByTagName('base')[0] !== 'undefined';
    }

    if (typeof cfg.locationChangeAngularEmitter === 'undefined') {
      config.locationChangeAngularEmitter = 'angular' in window;
    }

    if (typeof cfg.moveGradientsOutsideSymbol === 'undefined') {
      config.moveGradientsOutsideSymbol = browser.isFirefox;
    }
  };

  /**
   * @param {Event} event
   * @param {Object} event.detail
   * @param {string} event.detail.oldUrl
   * @param {string} event.detail.newUrl
   * @private
   */
  BrowserSprite.prototype._handleLocationChange = function _handleLocationChange (event) {
    var ref = event.detail;
    var oldUrl = ref.oldUrl;
    var newUrl = ref.newUrl;
    this.updateUrls(oldUrl, newUrl);
  };

  /**
   * Add new symbol. If symbol with the same id exists it will be replaced.
   * If sprite already mounted - `symbol.mount(sprite.node)` will be called.
   * @fires Events#SYMBOL_MOUNT
   * @param {BrowserSpriteSymbol} symbol
   * @return {boolean} `true` - symbol was added, `false` - replaced
   */
  BrowserSprite.prototype.add = function add (symbol) {
    var sprite = this;
    var isNewSymbol = Sprite$$1.prototype.add.call(this, symbol);

    if (this.isMounted && isNewSymbol) {
      symbol.mount(sprite.node);
      this._emitter.emit(Events.SYMBOL_MOUNT, symbol.node);
    }

    return isNewSymbol;
  };

  /**
   * Attach to existing DOM node
   * @param {string|Element} target
   * @return {Element|null} attached DOM Element. null if node to attach not found.
   */
  BrowserSprite.prototype.attach = function attach (target) {
    var this$1 = this;

    var sprite = this;

    if (sprite.isMounted) {
      return sprite.node;
    }

    /** @type Element */
    var node = typeof target === 'string' ? document.querySelector(target) : target;
    sprite.node = node;

    // Already added symbols needs to be mounted
    this.symbols.forEach(function (symbol) {
      symbol.mount(sprite.node);
      this$1._emitter.emit(Events.SYMBOL_MOUNT, symbol.node);
    });

    // Create symbols from existing DOM nodes, add and mount them
    arrayFrom(node.querySelectorAll('symbol'))
      .forEach(function (symbolNode) {
        var symbol = BrowserSpriteSymbol.createFromExistingNode(symbolNode);
        symbol.node = symbolNode; // hack to prevent symbol mounting to sprite when adding
        sprite.add(symbol);
      });

    this._emitter.emit(Events.MOUNT, node);

    return node;
  };

  BrowserSprite.prototype.destroy = function destroy () {
    var ref = this;
    var config = ref.config;
    var symbols = ref.symbols;
    var _emitter = ref._emitter;

    symbols.forEach(function (s) { return s.destroy(); });

    _emitter.off('*');
    window.removeEventListener(config.locationChangeEvent, this._handleLocationChange);

    if (this.isMounted) {
      this.unmount();
    }
  };

  /**
   * @fires Events#MOUNT
   * @param {string|Element} [target]
   * @param {boolean} [prepend=false]
   * @return {Element|null} rendered sprite node. null if mount node not found.
   */
  BrowserSprite.prototype.mount = function mount (target, prepend) {
    if ( target === void 0 ) target = this.config.mountTo;
    if ( prepend === void 0 ) prepend = false;

    var sprite = this;

    if (sprite.isMounted) {
      return sprite.node;
    }

    var mountNode = typeof target === 'string' ? document.querySelector(target) : target;
    var node = sprite.render();
    this.node = node;

    if (prepend && mountNode.childNodes[0]) {
      mountNode.insertBefore(node, mountNode.childNodes[0]);
    } else {
      mountNode.appendChild(node);
    }

    this._emitter.emit(Events.MOUNT, node);

    return node;
  };

  /**
   * @return {Element}
   */
  BrowserSprite.prototype.render = function render () {
    return parse(this.stringify());
  };

  /**
   * Detach sprite from the DOM
   */
  BrowserSprite.prototype.unmount = function unmount () {
    this.node.parentNode.removeChild(this.node);
  };

  /**
   * Update URLs in sprite and usage elements
   * @param {string} oldUrl
   * @param {string} newUrl
   * @return {boolean} `true` - URLs was updated, `false` - sprite is not mounted
   */
  BrowserSprite.prototype.updateUrls = function updateUrls$1 (oldUrl, newUrl) {
    if (!this.isMounted) {
      return false;
    }

    var usages = document.querySelectorAll(this.config.usagesToUpdate);

    updateUrls(
      this.node,
      usages,
      ((getUrlWithoutFragment(oldUrl)) + "#"),
      ((getUrlWithoutFragment(newUrl)) + "#")
    );

    return true;
  };

  Object.defineProperties( BrowserSprite.prototype, prototypeAccessors );

  return BrowserSprite;
}(Sprite));

var ready$1 = createCommonjsModule(function (module) {
/*!
  * domready (c) Dustin Diaz 2014 - License MIT
  */
!function (name, definition) {

  { module.exports = definition(); }

}('domready', function () {

  var fns = [], listener
    , doc = document
    , hack = doc.documentElement.doScroll
    , domContentLoaded = 'DOMContentLoaded'
    , loaded = (hack ? /^loaded|^c/ : /^loaded|^i|^c/).test(doc.readyState);


  if (!loaded)
  { doc.addEventListener(domContentLoaded, listener = function () {
    doc.removeEventListener(domContentLoaded, listener);
    loaded = 1;
    while (listener = fns.shift()) { listener(); }
  }); }

  return function (fn) {
    loaded ? setTimeout(fn, 0) : fns.push(fn);
  }

});
});

var spriteNodeId = '__SVG_SPRITE_NODE__';
var spriteGlobalVarName = '__SVG_SPRITE__';
var isSpriteExists = !!window[spriteGlobalVarName];

// eslint-disable-next-line import/no-mutable-exports
var sprite;

if (isSpriteExists) {
  sprite = window[spriteGlobalVarName];
} else {
  sprite = new BrowserSprite({ attrs: { id: spriteNodeId } });
  window[spriteGlobalVarName] = sprite;
}

var loadSprite = function () {
  /**
   * Check for page already contains sprite node
   * If found - attach to and reuse it's content
   * If not - render and mount the new sprite
   */
  var existing = document.getElementById(spriteNodeId);

  if (existing) {
    sprite.attach(existing);
  } else {
    sprite.mount(document.body, true);
  }
};

if (document.body) {
  loadSprite();
} else {
  ready$1(loadSprite);
}

var sprite$1 = sprite;

return sprite$1;

})));

/* WEBPACK VAR INJECTION */}.call(exports, __webpack_require__(2)))

/***/ }),
/* 2 */
/***/ (function(module, exports) {

var g;

// This works in non-strict mode
g = (function() {
	return this;
})();

try {
	// This works if eval is allowed (see CSP)
	g = g || Function("return this")() || (1,eval)("this");
} catch(e) {
	// This works if the window reference is available
	if(typeof window === "object")
		g = window;
}

// g can still be undefined, but nothing to do about it...
// We return undefined, instead of nothing here, so it's
// easier to handle this case. if(!global) { ...}

module.exports = g;


/***/ }),
/* 3 */
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(4);
__webpack_require__(5);
module.exports = __webpack_require__(6);


/***/ }),
/* 4 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build__ = __webpack_require__(1);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build__);


var symbol = new __WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol___default.a({
  "id": "facebook",
  "use": "facebook-usage",
  "viewBox": "0 0 1000 1000",
  "content": "<symbol viewBox=\"0 0 1000 1000\" id=\"facebook\"><path d=\"M990 500c0-270.6-219.4-490-490-490S10 229.4 10 500s219.4 490 490 490 490-219.4 490-490zm-935.5 0C54.5 254 254 54.5 500 54.5S945.5 254 945.5 500 746.1 945.5 500 945.5C254 945.5 54.5 746 54.5 500z\" /><path d=\"M518.8 782.8V500h93.3l14.7-93.7h-108v-47c0-24.5 8-47.8 43.1-47.8h70.2V218h-99.6c-83.7 0-106.6 55.1-106.6 131.6v56.7h-57.5V500h57.5v282.8h92.9z\" /></symbol>"
});
var result = __WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build___default.a.add(symbol);
/* harmony default export */ __webpack_exports__["default"] = (symbol);

/***/ }),
/* 5 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build__ = __webpack_require__(1);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build__);


var symbol = new __WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol___default.a({
  "id": "twitter",
  "use": "twitter-usage",
  "viewBox": "0 0 273.4 222.2",
  "content": "<symbol viewBox=\"0 0 273.4 222.2\" id=\"twitter\"><path d=\"M273.4 26.3c-10.1 4.5-20.9 7.5-32.2 8.8 11.6-6.9 20.5-17.9 24.7-31-10.9 6.4-22.9 11.1-35.7 13.6A55.919 55.919 0 0 0 189.3 0c-31 0-56.1 25.1-56.1 56.1 0 4.4.5 8.7 1.5 12.8C88 66.5 46.7 44.2 19 10.3c-4.8 8.3-7.6 17.9-7.6 28.2 0 19.5 9.9 36.6 25 46.7-9.2-.3-17.8-2.8-25.4-7v.7c0 27.2 19.3 49.8 45 55-4.7 1.3-9.7 2-14.8 2-3.6 0-7.1-.4-10.6-1 7.1 22.3 27.9 38.5 52.4 39-19.2 15-43.4 24-69.7 24-4.5 0-9-.3-13.4-.8 24.8 15.9 54.3 25.2 86 25.2 103.2 0 159.6-85.5 159.6-159.6 0-2.4-.1-4.9-.2-7.3 11.1-8 20.6-17.9 28.1-29.1z\" /></symbol>"
});
var result = __WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build___default.a.add(symbol);
/* harmony default export */ __webpack_exports__["default"] = (symbol);

/***/ }),
/* 6 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build__ = __webpack_require__(1);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build__);


var symbol = new __WEBPACK_IMPORTED_MODULE_0_svg_baker_runtime_browser_symbol___default.a({
  "id": "wikipedia",
  "use": "wikipedia-usage",
  "viewBox": "-254 350 103 94",
  "content": "<symbol viewBox=\"-254 350 103 94\" id=\"wikipedia\"><title>Wikipedia logo version 2</title><radialGradient id=\"wikipedia_a\" cx=\"-9.429\" cy=\"1569.139\" r=\"68.687\" gradientTransform=\"translate(-213.764 -1178.502)\" gradientUnits=\"userSpaceOnUse\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\".483\" stop-color=\"#EAEAEB\" /><stop offset=\".945\" stop-color=\"#A9ABAE\" /><stop offset=\"1\" stop-color=\"#999B9E\" /></radialGradient><path d=\"M-204.1 367c0-.6-.4-1.3-.4-1.3v-.1s-.5-.9-1.3-1.2c-.8-.3-1.5.3-1.5.3s-.1.1-.4.5c-.3.4-.5.7-1.2.9-.7.3-1.4.2-1.7 0-.4-.2-.5-.5-.5-.5s-.2-.7-.3-1c-.1-.3-.3-1.7-.3-1.7s-.5-2.7-.5-3.3c0 0 1.5-.1 3.7-.8 2.3-.7 3-1.2 3-1.2s-.4-.2-.5-.7c-.1-.5-.1-1.2-.1-1.2s-.1-.5.5-1.1c.6-.6 1.4-.9 1.8-1 .4-.1 1.3-.2 2.1-.1.8 0 1.3.1 1.6.3.3.2.4.6.4.6v1.1s0 .4.3.5c0 0 .5.3 2.2.1 0 0 .7-.1 1.8-.5 1.1-.3 4.1-1.2 4.6-1.3.4-.1 1-.3 1.6-.5.7-.2 2-.6 2.3-.7.3-.1 1.8-.6 2.9-.8 1.1-.2 2.2-.2 2.8.1 0 0 .4.3.5.7.2.4.5.9.9 1.1.5.2.8.4 1.9.3 0 0 0-.1-.4-.4-.4-.3-1-.7-1-.7s-.3-.2-.4-.4c-.1-.2 0-.3 0-.3l.9-1.4s0-.2.5-.2c.5-.1 1.1-.1 1.7-.3.7-.2.8-.3.8-.3l.6.2s3.5 2.9 4.7 3.6l.2-.2s.4 0 .8.2 1 .6 1 .6 1.6 1.3 2.1 2.2l.2.7-.1.2s.9 1.3 2.1 2.6c0 0 1.2 1.7 1.7 2.1l-.2-.8.3-.2.2-.1.6.3c3.6 4.8 6.4 10.4 8.1 16.3l-.1.5.4.5c1.1 4.2 1.7 8.6 1.7 13.2 0 1.1 0 2.2-.1 3.3l-.3.5.2.6c-2.2 26.1-24.1 46.6-50.8 46.6-18.5 0-34.7-9.9-43.6-24.6l-.1-.4-.2-.2c-3.4-5.7-5.7-12.2-6.6-19.1l.2-.5-.3-.5c-.2-1.9-.3-3.8-.3-5.8 0-3 .3-5.9.7-8.8l.3-.6-.1-.3c1.2-6.1 3.4-11.7 6.5-16.8l.7-.4h.1s.2-.2.4-.2h.1s1.2-2 1.6-2.6c0 0 .5-.3.7-.4 0 0 .1 0 .2.1 0 0 .5-.4 1.7-2.1 0 0-.1-.1-.1-.2s.1-.6.2-.7c.1-.1.1-.2.1-.2s1.7-2 3.2-3.2c0 0 .3-.2.7-.3 0 0 1.5-.6 3.3-2.2 0 0 .1-.3.5-.9.4-.6 1.5-1.2 2.2-1.3.8-.2.9 0 .9 0l.1.1.5.8s.6-.3 1.4-.6c.8-.3 1-.3 1-.3l.8 1.3-1 2s-.6 1.4-1.7 2.2c0 0-.5.3-1.1.1-.6-.2-1.1.3-1.1.3l-.2.1s.1 0 .3-.1c0 0 .2.1.3.2.1.2.9 1.2.9 1.2s0 .8-.4 1.9c-.4 1.1-1.5 2.9-1.5 2.9s-.7 1.4-1.1 2.3-.5 1.8-.5 2.3c0 0 .2.1.7-.2.7-.3 1.1 0 1.1 0s.7.5 1 .9c.3.3.8 1.8.2 3.2 0 0-.4 1-1.4 1.7 0 0-.2.3-1.5.2-.4 0-.6-.3-1.4-.2-.8.1-1.2.8-1.2.8-.7 1-1.2 2.5-1.2 2.5l-.1.2s-.2.5-.3 1.8c-.1 1.3.3 3.1.3 3.1s7.9-1.4 9.9-.1l.6.5v.4c-.1.2-.4.7-1 1.1-.6.4-1.2 1.6-.3 2.3 1 .8 1.7.8 3.4.5 1.7-.3 2.9-1.3 2.9-1.3s1-.7.8-1.6c-.2-.9-1-1.2-1-1.2s-.7-.4-.1-1.2c0 0 .1-.7 2.6-1.3 2.4-.6 6.8-1.5 10.6-2 0 0-2.5-8.2-.7-9.3 0 0 .4-.3 1.2-.4h1.5c.5 0 1 .1 1.7-.4.3-.7.4-1 .4-.9\" fill=\"url(#wikipedia_a)\" /><linearGradient id=\"wikipedia_b\" gradientUnits=\"userSpaceOnUse\" x1=\"202.276\" y1=\"-64.159\" x2=\"248.778\" y2=\"-136.911\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#8A8A8A\" /><stop offset=\".569\" stop-color=\"#606060\" /><stop offset=\".591\" stop-color=\"#FFF\" /><stop offset=\".612\" stop-color=\"#585858\" /><stop offset=\"1\" stop-color=\"#303030\" /></linearGradient><path d=\"M-171.6 429.3l.5.2c0 .1-.1.1-.1.2-.9 1.6-.9 1.9-1.4 2.3-.4.3-.6.5-1.4.7-.9.2-1.8 1.2-1.8 1.2s-.9.8-.5.9c.4 0 1.2-.6 1.2-.6s.5-.4.6-.3c.1.1-.5.8-.5.8s-1.2 1.2-2.5 2l-.4.2s1.9-1.4 2.8-2.4c0 0 .2-.3-.2.1-.4.3-1.3.8-1.7.8-.4 0 0-.6 0-.6s.6-.8 1.8-1.8c1.2-1 2.2-.9 2.2-.9s.2 0 .3-.3c0-.3.3-.9.3-.9s.5-1 1.7-2.7c1.2-1.7 1.8-2.2 1.8-2.2s1.6-1.6 2.4-3.3c0 0 .6-1-.4-.3-1 .8-2.2 1.7-3.4 2-1.2.3-1.3-.8-1.3-.8s-.3-1.9 1-3.3c1.2-1.3 2.5-1.3 3.7-1.4 1.2-.1 2.2-1.6 2.2-1.6s.8-.9 1.3-3.8c.2-1.3.1-2.2-.1-2.8v-.6h-.4c-.1-.1-.1-.2-.1-.2s-.3-.3-.6-.5-.7-.6-1.1-1.5c0 0-1-2.1-.8-5.2.2-3 2.8-2.8 2.8-2.8s1.5.1 1.8-.3c.3-.4.6-1 .6-2.2.1-1.2-.4-2.4-.4-2.4s-.2-.6-1-.7c-.9-.1-1.1.2-1.1.2s-.3.1-.7 1.1c-.5 1-.8 1.5-1.6 1.7-.8.2-2 .1-2.5-1s-1.8-3.7-2.4-5.8l.1-.7-.3-.5c-.1-.4-.1-.8-.1-1.2 0-1-.3-2.1-.6-3.2s-1.5-3-1.7-3.4c-.3-.7-.6-.9-1-.9-.4.1-.3.1-.5.1s-.3.2-.3.4-.4 1.3-1.1 1.8c-.8.5-1.1.7-2.4.9 0 0-1.5.1-2.7-2.1-1.2-2.2-.9-3.6-.8-4.1.1-.5.5-1.2 1.2-1.4.7-.1 1.1-.2 1.1-.2s1.1 0 1.6-.1c.6-.1.3-1 .3-1s-.4-2.4-2.3-4.3l-.1-.5-.8-.4c-1.9-2-4.4-5.4-4.4-5.4s-1.1-1-.2-2.5c0 0 .4-1 1.7-.8.4.1.5.1.8.2.5.1 1 .2 1.5-.4 0 0 .4-.8-.3-1.8s-.9-1.7-1.8-1.7c0 0-.4-.1-.8.4-.4.4-1.4.7-2 .8-.7.1-2.3-.5-3.2-2.1-.5-.9-.8-1.4-.9-1.6l.2-.3.7.1c.2.4.5 1.1 1 1.8.6 1 1 1.1 1.4 1.3.3.1 1-.1 1.4-.3.4-.2.8-.7 1.4-.7.7 0 1.6.1 2.3.8.7.7 1.5 2.2 1.5 2.9-.1.7-.1 1.4-1 1.7-.9.3-1.3 0-1.9-.1-.6-.1-.9-.1-1.1.2-.2.3-.5.9-.4 1.2.1.3.2.5.8 1.3.6.8 3.5 4.3 4 4.8l-.2.7 1 .2c.6.7 1.4 1.7 1.7 2.3.5.9.8 2.3.8 3 0 .7-.3 1-.3 1s-.3.5-2 .5c-1.5 0-1.6.3-1.6.3s-.5.5-.4 1.6c.1 1.1.6 2.3 1.6 3.4.8.9 2.3 0 2.7-.3.5-.3.8-1.3.8-1.3s.1-1.2 1.4-1.2c1.4 0 2 1.3 2 1.3s1 1.3 1.9 4.1c.5 1.4.6 2.3.6 2.3l.1 1.7-.5.9.7.3c.1.5.3 1.2.7 2 0 0 1 2.4 1.4 3.3.4.9.9.8 1.3.8 0 0 .9.1 1.2-.3.3-.4.6-1.1.6-1.1s.7-1.8 2.1-1.7c1.5.2 1.8 1.1 2.1 2.2.3 1.1.3 3.2-.5 4.5-.8 1.3-1.7 1.1-1.7 1.1s-1.8-.2-2.2.2c-.4.4-.6.7-.7 1.6-.1.9 0 2.3.8 4.1.6 1.5 1.1 1.4 1.4 1.7.3.4 1.2 1.2 1.1 3.3-.1 2.1-.8 4.1-1.6 5.4-.8 1.3-2 2.1-2 2.1s-.3.2-1.1.3c-.7.1-1.8.1-2.5.5-.8.4-1 1.5-1.1 2-.1.5-.1 1.5.9 1.4 1-.1 2.6-1.4 2.6-1.4s1.5-1.1 1.7-.8c.2.4-.6 1.8-.6 1.8s-1 1.6-1.9 2.5c-.7.8-1.6 1.9-2.4 3.1l-.8.4z\" opacity=\".69\" fill=\"url(#wikipedia_b)\" /><linearGradient id=\"wikipedia_c\" gradientUnits=\"userSpaceOnUse\" x1=\"171.286\" y1=\"-56.951\" x2=\"191.786\" y2=\"-152.661\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#A8A9AB\" /><stop offset=\"1\" stop-color=\"#636668\" /></linearGradient><path d=\"M-230.6 372.7s0 .1 0 0c0 .1 0 0 0 0z\" fill=\"url(#wikipedia_c)\" /><linearGradient id=\"wikipedia_d\" gradientUnits=\"userSpaceOnUse\" x1=\"167.068\" y1=\"-58.37\" x2=\"187.068\" y2=\"-151.743\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#A8A9AB\" /><stop offset=\"1\" stop-color=\"#636668\" /></linearGradient><path d=\"M-215.8 439.7h.2c-.2-.1-.4-.3-.6-.4-.7-.4-3.7-2.4-4.7-3-.9-.6-2.6-1.7-3.3-1.5-.6.2-.5.4-.8.6-.3.2-.7.1-1.5-.4-.8-.4-1.4-.7-3-2.2-1.2-1.2 1.6-.1 1.6-.1s.6.3.3-.4c-.3-.6-1.7-2.3-3-3.7-1.1-1.1-1.7-1.9-2.4-3l-.6-.7v-.2s0-.1-.1-.1c0 0-1.9-3.4-1.7-4.6 0 0 .1-.8 1.2-1.2.8-.3.7.5 3.1 1 0 0 2.1.6 2.6-.9s-.6-3.4-.6-3.4-1.4-2.7-3.2-2.8c-.9-.1-.7.6-2.1.9 0 0-1.9.2-2.5-1-.7-1.4-1-3-1-4s.1-1.1.1-1.4c0-.2.2-.6.3-1.1l-.1-.7.2-.5v-.8c-.1-1.7-.2-4.2-.4-5.7s-.6-3.8-2-3.9c0 0-.7-.1-1.6.9-.9.9-1.7-.7-1.7-1.7-.1-1.1.1-2.3.4-2.8.3-.5 1-.6 1.2-.6.1 0 .6.2 1 .5.5.3 1.2.3 1.6-.1.4-.4.9-.9 1.2-2.6.2-1.7.2-3.5 0-5.7l-.2-.5 1.3-.3V378.6c.1-1.2.3-1.8.3-1.8l.1-.2s.5-1.5 1.2-2.5c0 0 .4-.7 1.2-.8.8-.1 1 .2 1.4.2h.9c.3-.2.6-.5.8-.8 0-.1.1-.1.1-.2v-.1c.1-.1.1-.2.1-.2.6-1.5.1-2.9-.2-3.2-.3-.4-1-.9-1-.9s-.4-.4-1.1 0c-.5.3-.7.2-.7.2 0-.5.1-1.4.5-2.3.3-.8 1.1-2.3 1.1-2.3s1-1.8 1.5-2.9c.4-1.1.4-1.9.4-1.9s-.8-1-.9-1.2c-.1-.2-.3-.2-.3-.2-.2.1-.3.1-.3.1l.2-.1s.4-.5 1.1-.3c.6.2 1.1-.1 1.1-.1 1-.8 1.7-2.2 1.7-2.2l1-2-.8-1.3s-.1 0-1 .3c0 0-.8 1.9-1.7 3.1 0 0-.4.6-.7.4-.3-.1-.6-.1-.9-.1-.3.1-1.2.3-1.9 1.4-.8 1.1-.9 1.9-.5 2.1s1-.1 1.4-.4c.4-.3.6-.5.8-.5.1 0 .1.3.1.4 0 .1-.2 1.4-1.6 3.9-.4.6-.8 1.6-1.1 2l.6.4-1 .5c-.3.8-.6 1.9-.5 2.6.2 1 1.2 1 1.2 1s.6 0 1.3-.3c.7-.4.9 1.2.9 1.5 0 .3 0 1.7-1 2.4 0 0-.4.3-1 .3s-1-.2-1-.2-1-.3-1.6.1c-.6.4-1.3 1.1-1.9 2.2-.6 1.1-1 3-1 4.4 0 1.1.2 2.2.3 2.9l.7.4-.5.6c.1 1.1.2 3.4.2 4.1 0 .9-.2 2.8-1.1 3.3 0 0-.3.2-.9-.2-.5-.4-1.1-.4-1.4-.4-.2 0-1.3.2-1.7 1.3-.4 1.1-.4 2.7-.3 3.6.1.9.9 2.5 1.9 2.5 0 0 .5 0 1.1-.6.6-.6.9-.6 1.2-.6.3 0 .7.3 1.1 2.9.3 2.4.4 4.4.4 6.7l.6.4-.8.8c0 .2-.1.4-.1.6-.2.7-.2 1.4 0 2.6.2 1.2.8 3.7 1.8 4.4 1.3.9 2.1.9 2.9.8.8-.1 1.4-.7 1.4-.7s.3-.3.7-.2c.4.1 1.3.7 2.1 2.1.7 1.4.9 3-.3 3.3-1.2.3-3.2-.8-3.2-.8s-1.2-.6-2.1.1c-1 .7-1 1.8-.5 3.1.3.7.8 1.9 1.5 3.2l.7.3-.2.6c.5.7 1.1 1.5 1.7 2.1 0 0 2.5 2.7 3.8 4.5 0 0 .1.2-.2 0-.2-.1-1.3-.6-1.8-.6-.6.1-.4.4-.4.4s.2 1.3 4 3.4c0 0 1.4.8 2.2.8 0 0 .3 0 .6-.3.3-.4.4-.3.7-.3.2.1.6.2 1.7 1.1 1.2.9 3.5 2.2 4.3 2.7.8.6.8.7.6 1.1-.2.4.6.6.6.6s1.9.9 2.9.8c1 0 1.5-.1 2.1 0 .6.1 1.3.3 1.3.3.1.1-.3 0-.3 0s-2.4-.3-2.5-.2c-.1.1 0 .2 1 .4 1.2.2 2.5.4 3.8.5-.5-.1-2.5-.3-3.8-.7 0 0-.1-.1.2 0 .3.1 2 .2 2.5.2.4-.1-.1-.3-.1-.3s-.9-.4-2.9-.6c0 0-.8-.1-1.5 0s-1.4-.3-1.4-.3-1-.3-.8-.6c.1-.2.1-.3.1-.5l-.4-1z\" opacity=\".45\" fill=\"url(#wikipedia_d)\" /><linearGradient id=\"wikipedia_e\" gradientUnits=\"userSpaceOnUse\" x1=\"190.76\" y1=\"-104.815\" x2=\"219.842\" y2=\"-104.815\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#231F20\" /><stop offset=\"1\" stop-color=\"#474747\" /></linearGradient><path d=\"M-191.7 436.2l-.4.6c.1.7-.1.9-.3 1.1-.2.3-.6.6-.4 1.2.2.6 1.7.4 2.5.1.9-.3 1.6-.5 2.1-.7.6-.2.7.1.7.1s.2.2-.6.6c-.8.4-2.3.6-3.1.7-.7.1-.5 0-1.6.3-1.1.4-.1.7-.1.7 2.4.6 4.2.1 4.2.1l.3-.1c.3-.1.5-.2.8-.2-2 .5-3.3.1-3.7.1-.4-.1-.8-.1-.9-.4-.1-.2.5-.2.5-.2s1.7-.2 3.2-.7c1.6-.5 1.9-1 1.9-1.3-.1-.4-.8-.3-1.8 0-.9.3-2.3.8-2.7.8-.3.1-.7.1-.8-.1-.1-.2-.2-.5.1-.9.4-.4.4-.7.4-.7.1-.3.1-.5 0-.8l-.3-.3.5-.1c-.3-1.1-1.1-2.2-1.3-2.6-.3-.5-.8-.8-2.4-.5-1.6.3-3.4 1-3.4 1s-1.9 1-3.3.8c-1.4-.2-1.7-1.6-1.7-2.1 0-.4.3-.8 1-1.1.7-.3 2.5-.7 5-.8 2.5-.1 3.5-1.8 3.5-1.8.3-.5.9-1.5-.5-2.3-1.4-.8-1.4-.6-2.1-1.1-.7-.5-1.4-1.2-1.7-2 0-.1-.1-.2-.1-.3l-.8-.6.4-.4c-.3-.7-.7-1.3-.7-1.3s-1.3-1.9-.2-3.7c1-1.8 2.7-2.3 2.7-2.3s1.5-.3 3 0c1.4.3 2.1-.2 2.1-.2s.9-.4 1.1-2.1c.3-1.7 0-4.9-2.3-5.6-2.3-.6-3.5.6-3.5.6s-1.2 1.4-1.6 1.6c-.4.2-1 .6-1 .6s-.9.5-1.5.6c-.4.1-1.8-1.8-1.9-3.2-.1-1.3-.4-2.4-.3-5.1l-.5-.6.5-.5c.1-3-.4-5.1-1.2-6.5-.8-1.4-2.1-2.2-2.8-2.5-.6-.3-2.1-.5-3.2-.1-1 .4-1.2.7-1.6 1.3-.4.6-.8.6-.8.6s-1.4 0-1.9-2.1c-.6-3 .4-4 .4-4s.3-.5 1.4-.6c1.1-.1 1.7.1 2.5.3.8.2 1.4.1 2.4-.4s1.4-1.3 1.2-2.7c-.2-1.4-.3-1.7-1.5-6l-.9-.5.6-.6c-1.2-4.3-1.3-7-1.3-7-.1-1 0-1.3.6-1.5.6-.3 1.1-.2 1.9-.1.8.1 1.4-.1 1.8-.3s1.6-.9 1.5-2.2c-.1-1.3-1.1-2.8-2-3.4-.8-.5-2-.3-2.6.1-.6.4-.8 1-1.2 1.2-.4.2-.9.6-1.5.5-.6-.1-.6-1.4-.8-2.8-.2-.9-.3-1.6-.3-2l-.7-.3c0 .6.5 3.3.5 3.3s.2 1.4.3 1.7c.1.3.3 1 .3 1s.1.4.5.5c.4.2 1.1.2 1.7 0 .7-.3.9-.6 1.2-.9.3-.4.4-.5.4-.5s.7-.6 1.5-.3 1.3 1.2 1.3 1.2v.1s.4.7.4 1.3v-.1s0 .3-.7.8-1.2.5-1.7.4c-.5 0-.7-.1-.8 0h-.7c-.8.1-1.2.4-1.2.4-1.8 1.1.7 9.3.7 9.3l-.3.6s.5 2.1.9 3.4c.4 1.3.6 2.6.6 2.9.1.3 0 .8-.3 1.1-.4.3-1.2.5-1.4.6-.2 0-.5 0-1-.2s-.9-.2-.9-.2-1.1-.2-2.3.2c-1.2.4-2.1 1.6-2.1 3.1-.1 1.5-.1 2.3.5 3.6.6 1.3 1.7 2.1 2.5 2.1s1.5-.4 1.9-1.1c.5-.6.6-.8.6-.8.5-.3 1.9-.4 2.7-.2.7.3 2 1.1 2.7 2.7.6 1.3.8 2.8.7 5.4l.6.4-.6.7v.8c-.1 3.9.7 5.9.7 5.9.5 1.1 1 1.8 1.7 2.3.7.5 1.7.2 2 0 .3-.2 1.2-.6 1.9-1 .7-.5.7-.7 1.6-1.5.9-.8 2.1-.6 2.1-.6s1.1 0 1.7 1.3c.6 1.3.5 3.1.3 3.8-.2.7-.4 1.1-1.1 1-.6-.1-1.6-.2-2-.2-.4 0-1.4 0-2.4.2-.9.2-2.2.9-3.4 2.9-.9 1.5-.5 3-.3 3.6.2.5.6 1.1 1 1.9l.8.3-.3.7c.4 1 .7 1.5 1.3 2.2.6.7 1.7 1.3 2.9 1.7 1.2.5.7 1.3.7 1.3-.7 1.5-2.8 1.6-3.4 1.6-.6.1-1.9.2-3.1.4-1.2.3-2.3.4-3 1.2-.7.8-.4 1.6 0 2.4.4.8 1.4 1.3 2.9 1.2 1.4-.1 2.3-.5 3.2-.9.9-.4 2.4-.8 2.8-.9.4-.1 1.1-.4 1.5.3.5.7 1 1.7 1.2 2.4l1.2-.1z\" opacity=\".35\" fill=\"url(#wikipedia_e)\" /><path d=\"M-152.4 401.2s.3-3.2.5-4.4v-.5l-.1-.2c-.5 5.8-.9 7.7-.9 7.7v-.1c.2-.9.3-1.7.5-2.5zm-10.3-38.6l.3.4.3.5c1 1.6 2.8 4.3 2.8 4.3s.7 1 .9 1c.2 0-.1-.7-.1-.7s-.3-1 .5.3c.7 1.2 1.2 2.4 1.3 2.7.1.4 0 .4 0 .4s-.1.1-.1.3c0 .5.5 1.7.5 1.7s1.5 3.9 2.1 5.6c.5 1.6 1.1 4.4 1.1 4.4s.2.8.2 1.2c0 .4-.1.4-.2.2-.2-.2-.3-.1-.3-.1s-.2.1-.2.8c0 .7.1 2.3.2 3.6.2 1.5.6 2.1.6 2.1s.4.6.5-.6c.1-1 .2-.2.2-.2.2 1.6.1 4.5 0 5v.6l.1-.2c.2-3 .1-5.4.1-5.4s-.1-1.3-.3-1.3c-.2 0-.2.7-.2.7s-.1.5-.2.5-.4 0-.6-1.4c-.2-1.4-.2-2.9-.2-2.9v-.2c.1 0 .2.1.2.1s.1.2.3 0c.2-.2.2-.6-.3-3.1-.3-1.5-.7-2.9-1-3.8l-.3-.3-.1-.7s-.3-.9-1-2.7c-.7-1.8-.8-2.5-.8-2.5s0-.2.1-.2.1-.2.1-.2 0-.2-.3-1c-.3-.7-.4-1.3-1.4-2.9-.9-1.5-1.1-1.6-1.1-1.6s-.4-.2-.1.6c.3.8-.1.2-.1.2-.9-1.2-2.8-4.3-2.8-4.3l-.5-.4-.5-1.3m-89.5 20.9l-.2.4c-.5 2.5-.6 5.1-.6 5.3 0 .2 0 .2-.1.2v-.2c-.1 0-.1.2-.1.2 0 .3 0 .6-.1.9.1-.1.1 0 .1 0s0 .1.1.1c.1-.1.2-1.4.2-1.4s0-2.8.8-6.1 1.3-4.3 1.3-4.3.2-.4.1-.1c0 .3.2.4.2.4.4-.1.8-1.1 1.3-2.5.4-1.4.7-2.6.7-2.7 0-.1-.1-.2-.2-.1s-.1 0-.1 0c0-.2.4-1.1.4-1.1 1.3-3.2 3.1-5.7 3.1-5.7l.1-.5c-.2.3-.3.4-.4.7-.1.1 0 .3 0 .3-.2.2-.4.3-.5.5-2.7 4.5-3.1 6.6-3.1 6.6 0 .2 0 .3.1.3s.3-.3.1.4c-.1.5-.5 1.7-.7 2.2-.2.5-.4.9-.5.8-.1 0-.1-.2-.1-.2s0-.5-.4.2c-.4.8-.7 1.9-1.4 4.7 0 .1-.1.3-.1.4v.3zm3.3 29.9c-.2-.4-.3-.7-.2-.6.1.1.2.4.5.7.3.3.4-.2-.6-3.1-1.1-2.9-1.4-3-1.4-3.1 0-.1-.2-.2-.2.2s0 .7-.5-1.1-1-4.8-1-5.1c0-.2-.2-1.8-.4-3.6s-.2-3.7-.2-4.3c0-.5-.1-.8-.1-.8-.1 0-.1 0-.1.3 0 .2 0 .4-.1.4s-.1-.5-.1-.5v1.1c0 .6.1.4.1.2v-.3s.1-.9.1 0 .2 4.6.2 4.6c0 .2 0 .5.1.7l.1.1v.1c.3 2.4.8 5.1.8 5.1.5 2.4 1.1 3.8 1.3 4.3.2.4.2.1.2-.3-.1-.4.5.7.9 1.7.3 1 .6 1.8.6 1.8s.3.8.1.8c-.1 0-.3-.3-.3-.3s-.5-.8-.3-.2c.4 1.2 1.6 3.8 1.6 3.8l1.4 2.5c-1-1.9-2.3-4.7-2.5-5.1zm2.5 5c.1.1.1.2.2.4l-.2-.4zm13.4-64.7c-.2.3-.2.5-.2.5l.2-.2v-.3zm-3.5 2.7c-.4 0-.7.3-.7.3s.4-.1.7-.3zm66.8-.7h.3c.1 0 .1-.2.1-.2s-.3-.4-.3-.6c-.3-.1-.6-.1-.6-.1v.3c-.1.1.4.5.5.6zm3.5 3l.1-.2-.2-.7c0 .1 0 .1-.2.1 0 0-.1 0 0 .2 0 .2.2.4.3.6z\" opacity=\".1\" fill=\"#232323\" /><path d=\"M-152.4 401.2s.3-3.2.5-4.4v-.5l-.1-.2c-.5 5.8-.9 7.7-.9 7.7v-.1c.2-.9.3-1.7.5-2.5z\" opacity=\".1\" fill=\"#232323\" /><linearGradient id=\"wikipedia_f\" gradientUnits=\"userSpaceOnUse\" x1=\"12.492\" y1=\"1537.278\" x2=\"41.964\" y2=\"1627.035\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\".009\" stop-color=\"#FCFCFC\" /><stop offset=\".066\" stop-color=\"#EEE\" /><stop offset=\".134\" stop-color=\"#E5E5E5\" /><stop offset=\".252\" stop-color=\"#E3E3E3\" /><stop offset=\".336\" stop-color=\"#8A8A8A\" /><stop offset=\".442\" stop-color=\"#B8B8B8\" /><stop offset=\"1\" stop-color=\"#3B3B3B\" /></linearGradient><path d=\"M-175 434.5s.7-.7.5-.8c-.1-.1-.6.3-.6.3s-.1.1-.2.1l.4-.3s0 .2-.4.6c0 0-.1.1-.3.2-1 .9-2.4 2-2.4 2l.4-.2c1.4-.7 2.6-1.9 2.6-1.9z\" opacity=\".5\" fill=\"url(#wikipedia_f)\" /><linearGradient id=\"wikipedia_g\" gradientUnits=\"userSpaceOnUse\" x1=\"206.463\" y1=\"-66.556\" x2=\"255.589\" y2=\"-127.306\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#EFF0F0\" /><stop offset=\".591\" stop-color=\"#F0F1F2\" /><stop offset=\".599\" stop-color=\"#787878\" /><stop offset=\".646\" stop-color=\"#EEEFF0\" /><stop offset=\"1\" stop-color=\"#D8D9DB\" /></linearGradient><path d=\"M-171 389.7l.5-.9-.1-1.7s-.1-.9-.6-2.3c-1-2.8-1.9-4.1-1.9-4.1s-.6-1.3-2-1.3c-1.3 0-1.4 1.2-1.4 1.2s-.3 1-.8 1.3c-.5.3-2 1.1-2.7.3-.9-1-1.5-2.2-1.6-3.4-.1-1.1.4-1.6.4-1.6s.1-.3 1.6-.3c1.7 0 2-.5 2-.5s.3-.3.3-1-.3-2.1-.8-3c-.3-.6-1.1-1.5-1.7-2.3l-1-.2.1-.7c-.6-.5-3.5-4-4-4.8-.6-.8-.7-1-.8-1.3-.1-.3.2-.9.4-1.2.2-.3.5-.3 1.1-.2.6.1 1 .4 1.9.1.9-.3 1-1 1-1.7.1-.7-.8-2.2-1.5-2.9-.7-.7-1.6-.8-2.3-.8-.7 0-1 .5-1.4.7-.4.2-1.1.4-1.4.3-.3-.1-.8-.3-1.4-1.3-.4-.8-.8-1.5-1-1.8l-.7-.1s.6 1.7 1.6 2.8c1 1.2 2.3.9 2.3.9s.8-.1 1.5-.8c.7-.7 1.8-.1 2 0 .3.2.9.9 1.5 2.1.6 1.2-.4 2.1-.4 2.1s-.6.5-1.7.1-1.8.3-2 .6c-.2.4-.5 1 .1 1.7s3.2 4.3 4.9 5.9c1.7 1.7 2.3 3 2.7 4.3.4 1.3.1 1.9-.5 2-.6.1-1.1 0-2.1.2-.9.2-1.3.4-1.5 1.7-.2 1.3.6 3.4 1.7 4.4 1.1 1 2.3.4 2.8.2.4-.2 1.4-.7 1.7-2 .2-.8.9-.7.9-.7s.6-.1.9.1c.3.2.6.5 1.4 1.9.8 1.3 1.5 3.1 1.7 4.7.2 2 0 2.2.3 3.3.3 1.1 1.1 3.2 1.5 4.1.4.8.8 1.7 1 2.1.2.4.5.8 1.4.8.9 0 1.3-.2 1.5-.7.3-.4.6-1.1.7-1.3.1-.2.5-.9 1.1-1 .7-.1 1.8 0 2.1 1.2.3 1.1.8 2.6-.2 4.5-.6 1.3-1.1.9-2.5.9 0 0-1.2 0-1.8.9-.6.9-.4 2.6-.3 3.9.1 1.3 1 3.1 1.6 3.6.6.4.9.8 1.1 1.3.2.4.5 1.2.2 3.3-.3 2.1-1 3.7-1.9 4.5 0 0-.1 0-.1.1l-.2.2c-.5.5-.4.5-.9.8-.6.3-1 .2-2 .4s-1.6.3-2.1.8-1.2 1.4-1 3.2c.1 1 1.3.6 2.2.1-.3.1-.6.2-.8.2-1 .1-1-.9-.9-1.4.1-.5.3-1.5 1.1-2s1.8-.4 2.5-.5c.7-.1 1.1-.3 1.1-.3s1.2-.8 2-2.1 1.5-3.4 1.6-5.4c.1-2.1-.8-2.9-1.1-3.3-.3-.4-.8-.2-1.4-1.7-.7-1.7-.8-3.2-.8-4.1.1-.9.3-1.2.7-1.6.4-.4 2.2-.2 2.2-.2s.9.2 1.7-1.1c.8-1.3.7-3.5.5-4.5-.3-1.1-.6-2-2.1-2.2-1.5-.2-2.1 1.7-2.1 1.7s-.3.7-.6 1.1c-.3.4-1.2.3-1.2.3-.4 0-.8.1-1.3-.8-.4-.9-1.4-3.3-1.4-3.3-.3-.8-.6-1.5-.7-2.1l-.4-.4z\" opacity=\".73\" fill=\"url(#wikipedia_g)\" /><linearGradient id=\"wikipedia_h\" gradientUnits=\"userSpaceOnUse\" x1=\"18.871\" y1=\"1534.826\" x2=\"48.469\" y2=\"1624.965\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\"1\" stop-color=\"#E4E5E6\" /></linearGradient><path d=\"M-171.5 429.3l.8-.5c.8-1.2 1.7-2.3 2.4-3.1.9-1 1.9-2.5 1.9-2.5s.8-1.4.6-1.8c-.1-.2-.7 0-1.7.8-3.7 2.7-4 1.2-4 1.2.4 2.4 4.7-1.6 5.1-1.4-.1.6-.5 1.2-1.3 2.3 0 0-.4.6-.8 1l-.6.6-.1.1c-.5.5-1 1.2-1.6 2l-.1.1c-.1.5-.3.8-.6 1.2-.3.4-.4.7-.5 1v.1s-.3.7-.5 1.1c-.1.4-.1.5-.6.6-.5.1-.3-.1-1 .2 0 0-.4.2-.9.6 0 0-.1 0-.1.1-.7.6-1.2 1.1-1.5 1.4-.1.1-.1.1-.1.2 0 0-.2.2.1.2.2 0 .6 0 1-.2l.1-.1c-.2.1-.4.2-.5.2-.4 0 .5-.9.5-.9s.9-1 1.8-1.2c.9-.2 1-.4 1.4-.7.4-.3.5-.7 1.4-2.3 0-.1.1-.1.1-.2l-.7-.1z\" opacity=\".53\" fill=\"url(#wikipedia_h)\" /><linearGradient id=\"wikipedia_i\" gradientUnits=\"userSpaceOnUse\" x1=\"190.694\" y1=\"-64.955\" x2=\"215.725\" y2=\"-146.069\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\".747\" stop-color=\"#F9F9F9\" /><stop offset=\"1\" stop-color=\"#D5D7D8\" /></linearGradient><path d=\"M-198.9 422.7l.4-.4c-.3-.7-.7-1.3-.7-1.3s-1.3-1.9-.2-3.7c1-1.8 2.7-2.3 2.7-2.3s1.5-.3 3 0c1.4.3 2.1-.2 2.1-.2s.9-.4 1.1-2.1c.3-1.7 0-4.9-2.3-5.6-2.3-.6-3.5.6-3.5.6s-1.2 1.4-1.6 1.6c-.4.2-1 .6-1 .6s-.9.5-1.5.6c-.4.1-1.8-1.8-1.9-3.2-.1-1.3-.4-2.4-.3-5.1l-.5-.6.5-.5c.1-3-.4-5.1-1.2-6.5-.8-1.4-2.1-2.2-2.8-2.5-.6-.3-2.1-.5-3.2-.1-1 .4-1.2.7-1.6 1.3-.4.7-.8.6-.8.6s-1.4 0-1.9-2.1c-.6-3 .4-4 .4-4s.3-.5 1.4-.6c1.1-.1 1.7.1 2.5.3.8.2 1.4.1 2.4-.4s1.4-1.3 1.2-2.7c-.2-1.4-.2-1.7-1.5-6l-.9-.5.6-.6c-1.2-4.3-1.3-7-1.3-7-.1-1 0-1.3.6-1.5.6-.3 1.1-.2 1.9-.1.8.1 1.4-.1 1.8-.3.4-.2 1.6-.9 1.5-2.2-.1-1.3-1.1-2.8-2-3.3-.8-.5-2-.3-2.6.1-.6.4-.8 1-1.2 1.2-.4.2-.9.6-1.5.5-.6-.1-.6-1.4-.8-2.8-.2-.9-.3-1.6-.3-2l-.7-.3c0 .6.5 3.3.5 3.3l.3 1.6c0 .1 0 .2.1.3.1.2.4.5.9.5 1.1.1 1.8-.5 2-.7.3-.2.9-.9.9-.9s.3-.6 1.3-.5c.9.1 1.2.8 1.4 1 .2.2 1.6 2 .7 2.9 0 0-.1.1-.2.1l-.4.4c-.7.5-1.2.5-1.7.4-.5 0-.7-.1-.8 0h-.7c-.8.1-1.2.4-1.2.4-1.8 1.1.7 9.3.7 9.3s.7 2 1 3c.3.9.5 1.6.8 3.3.3 1.6-.2 2.1-.5 2.3-.3.2-1 .6-1.8.6s-1-.4-2.4-.4c-1.3-.1-2.2.3-2.7.9-.4.6-.9 1.9-.7 3.4.2 1.5.5 2.1 1.1 2.7.6.7 1.2 1 2 .7.8-.3.8-.8 1.2-1.2.5-.5.9-.8 2.1-.8 1.2 0 2 .3 2.6.8.6.5 1.9 1.6 2.3 3.4.4 1.7.4 2.3.4 3.7s-.1 3-.1 4.4c0 1.4.2 2.8.6 3.8.4 1 .9 1.8 1.4 2.2.5.4.9.4 1.4.3.5-.2 1.5-.8 2.4-1.3.9-.6.8-1 1.6-1.5.9-.6 1.8-.6 2.5-.5.7.1 1.7.6 2.1 1.9.4 1.3.4 2.7.4 2.7s0 1.2-.4 1.9c-.5.7-1.3.6-1.6.5-.4-.1-1.1-.1-1.1-.1s-1.5-.2-2.6.1c-1.1.3-2.1 1.1-2.7 1.9-.7.8-.9 1.6-1 2.2 0 .6 0 1.6.6 2.6s.7 1.4 1.4 2.8 2.1 2.2 2.2 2.2c0 0 1.4.5 1.9.9s.6.8.4 1.2c-.1.4-.4 1.1-1.6 1.6-1.2.5-2.6.5-3.5.6-.9.1-2.7.3-3.7.8s-1 1.5-1 1.5 0 1.6 1.3 2c1.4.4 2.6 0 3.2-.2.6-.2 1.5-.6 1.5-.6s1.8-.6 2.8-.8c1-.2 1.5-.3 2.2.8.7 1.2 1 1.9 1.1 2.6.1.7-.2 1.1-.5 1.4-.3.3-.2.5-.2.5-.1.9 1.2.8 1.2.8h.1c-.3 0-.5 0-.6-.2-.1-.2-.2-.5.1-.9.4-.4.4-.7.4-.7.3-1.4-1-3.4-1.4-3.9-.3-.5-.8-.8-2.4-.5-1.6.3-3.4 1-3.4 1s-1.9 1-3.3.8c-1.4-.2-1.7-1.6-1.7-2.1 0-.4.3-.8 1-1.1.7-.3 2.5-.7 5-.8 2.5-.1 3.5-1.8 3.5-1.8.3-.5.9-1.5-.5-2.3-1.4-.8-1.4-.6-2.1-1.1-.7-.5-1.4-1.2-1.7-2 0-.1-.1-.2-.1-.3l-.6-.7z\" opacity=\".96\" fill=\"url(#wikipedia_i)\" /><path d=\"M-162 363.4c1 1.6 2.8 4.3 2.8 4.3s.3.3.5.6c0-.4-.1-.6-.1-.6l-.1-.3c0-.4.4.1.6.3-.5-.8-.7-.8-.7-.8s-.4-.2-.1.6c.3.8-.1.2-.1.2-.9-1.2-2.8-4.3-2.8-4.3l-.6-.4.6.4zm9.5 38V401.1c.1.1.1.2 0 .3zm-.7-15.7c.1 0 .2.1.2.1s.1.2.3 0c.1-.1.2-.4 0-1.3 0 .2-.1.4-.1.6-.1.3-.3 0-.4-.1-.1-.1-.2.1-.2.1v.2c0 .7.1 2.3.2 3.6.1.6.2 1.1.3 1.4v.1c.1.1.2.3.3.3.1-.1.3-.6.3-.6l.1-.6c.2.1.3.5.3 1v-.1s-.1-1.3-.3-1.3c-.2 0-.2.7-.2.7s-.1.5-.2.5-.4 0-.6-1.4c-.2-1.4-.2-2.9-.2-2.9s.1-.3.2-.3zm-1.1-7.1l.3.3c.5 1.5 1 3.8 1.1 4.3 0-.1-.1-.3-.1-.4-.3-1.5-.7-2.9-1-3.8l-.3-.4-.1-.7s-.3-.9-1-2.7c-.7-1.8-.8-2.5-.8-2.5s0-.2.1-.2.1-.2.1-.2 0-.2-.3-1c-.2-.5-.3-.9-.7-1.6.3.6.5 1.1.5 1.3v.1s.1.1.1.6c0 .4-.1.5-.1.5v.1c.1.5.4 1.2.4 1.2s1.1 2.7 1.7 4.5l.1.6z\" opacity=\".1\" fill=\"#232323\" /><linearGradient id=\"wikipedia_j\" gradientUnits=\"userSpaceOnUse\" x1=\"20.534\" y1=\"1538.158\" x2=\"1.209\" y2=\"1632.194\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\"1\" stop-color=\"#E4E5E6\" /></linearGradient><path d=\"M-211 441.5c.9.2 1.7.4 1.9.4-.4-.1-1-.2-1.9-.4z\" fill=\"url(#wikipedia_j)\" /><linearGradient id=\"wikipedia_k\" gradientUnits=\"userSpaceOnUse\" x1=\"168.559\" y1=\"-72.757\" x2=\"173.288\" y2=\"-132.177\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\".22\" stop-color=\"#989A9C\" /><stop offset=\".253\" stop-color=\"#FFF\" /></linearGradient><path d=\"M-233.6 424.9v-.2l-.1-.1s-1.9-3.4-1.7-4.6c0 0 .1-.8 1.2-1.2.8-.3.7.5 3.1 1 0 0 2.1.6 2.6-.9s-.6-3.4-.6-3.4-1.4-2.7-3.2-2.8c-.9-.1-.7.6-2.1.9 0 0-1.9.2-2.5-1-.7-1.4-1-3-1-4 0-1.1 0-1 .1-1.4 0-.2.2-.5.2-1.1l-.1-.7.2-.5v-.8c-.1-1.7-.2-4.2-.4-5.7s-.6-3.8-2-3.9c0 0-.7-.1-1.6.9-.9.9-1.7-.7-1.7-1.7-.1-1.1.1-2.3.4-2.8.3-.5 1-.6 1.2-.6.1 0 .6.2 1 .5.5.3 1.2.3 1.6-.1.4-.4.9-.9 1.2-2.6.2-1.7.2-3.5 0-5.7l-.2-.5 1.3-.3V378.5c.1-1.2.3-1.8.3-1.8l.1-.2s.5-1.5 1.2-2.5c0 0 .4-.7 1.2-.8.8-.1 1 .2 1.4.2h.9c.3-.2.6-.5.8-.8v-.2c0-.1.1-.1.1-.2v-.1c.1-.1.1-.2.1-.2.6-1.5.1-2.9-.2-3.2-.3-.4-1-.9-1-.9s-.3-.2-.8-.1c.3 0 .8.1 1 .6.3.7.4 1.3.2 2.3 0 0-.3 1.4-1.4 2.2-1.1.8-1.9.1-2.9.1s-1.5.7-1.8 1.2c-.3.5-1.4 2.2-1.3 5.1.1 2.9.3 4.3.3 5.6 0 1.2.2 4-.6 5.3-.8 1.3-1.6.6-2.2.3-.6-.3-1.2-.2-1.7.1-.5.4-.8 1.1-.8 3.3 0 2.4 1.5 2.6 1.5 2.6s.3.1.9-.5c0 0 .7-.7 1.3-.6.6.1 1 .7 1.3 1.8.3 1.1.8 5.6.7 8.7 0 1.3-.6 1.3-.4 3.6 0 0 .4 3.1 1.4 4.1 1 1 2.4.8 2.7.8.3 0 .7-.3.7-.3s.3-.2.5-.4.5-.4 1-.3c.5.1 1.6.9 2.6 2.6.9 1.7.5 3.3-.3 3.5-.7.2-.8.2-2-.1-1.1-.3-1.5-.6-2-.8-.5-.2-1-.3-1.5.1s-1.3 1.1-.3 3.3c1 2.2 1.7 3.8 3.5 5.6-.5-.6-1-1.2-1.4-1.9v-.7z\" fill=\"url(#wikipedia_k)\" /><linearGradient id=\"wikipedia_l\" gradientUnits=\"userSpaceOnUse\" x1=\"-16.628\" y1=\"1530.36\" x2=\"-35.153\" y2=\"1620.502\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\"1\" stop-color=\"#E4E5E6\" /></linearGradient><path d=\"M-231.5 357.4c-.1 0 0 0 0 0z\" fill=\"url(#wikipedia_l)\" /><linearGradient id=\"wikipedia_m\" gradientUnits=\"userSpaceOnUse\" x1=\"5.906\" y1=\"1621.338\" x2=\"5.898\" y2=\"1621.375\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\"1\" stop-color=\"#E4E5E6\" /></linearGradient><path d=\"M-208 442.9h.4c-.1 0-.3 0-.6-.1.1 0 .2 0 .2.1z\" fill=\"url(#wikipedia_m)\" /><path d=\"M-229.9 355.5c-.6.4-.7 0-1.1 0-.4 0-1 .2-1.6 1-.6.8-.6 1.9.3 1.4 0 0 .4-.4.8-.6.1 0 .2-.1.4-.2l.1-.1s.4-.5 1.1-.3c.6.2 1.1-.1 1.1-.1 1-.8 1.7-2.2 1.7-2.2l1-2-.8-1.3s-.7 1.5-1.4 2.5c-.7 1.1-.7 1.4-1.6 1.9z\" fill=\"#9FA2A3\" /><path d=\"M-234.1 366.3s-.4 1.9 1.2 1.6h-.1c0-.5.1-1.4.5-2.3.3-.8 1.1-2.3 1.1-2.3s1-1.8 1.5-2.9c.4-1.1.4-1.9.4-1.9s-.8-1-.9-1.2c-.1-.2-.3-.2-.3-.2-.1 0-.1 0-.1.1.1 0 .2 0 .3.1.2.3-.4 2-.4 2s-.5 1.2-1.5 3c-1.2 1.9-1.7 4-1.7 4z\" fill=\"#9FA2A3\" /><linearGradient id=\"wikipedia_n\" gradientUnits=\"userSpaceOnUse\" x1=\"14.903\" y1=\"1536.638\" x2=\"-4.504\" y2=\"1631.072\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\"1\" stop-color=\"#E4E5E6\" /></linearGradient><path d=\"M-215.8 439.7h.2c-.1-.1-.3-.2-.5-.3.2.1.5.4.3.7-.2.4 0 .5.5.9h.1c-.2-.1-.3-.2-.2-.4.1-.2.1-.3.1-.5l-.5-.4z\" fill=\"url(#wikipedia_n)\" /><linearGradient id=\"wikipedia_o\" gradientUnits=\"userSpaceOnUse\" x1=\".457\" y1=\"1533.599\" x2=\"-18.966\" y2=\"1628.111\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\"1\" stop-color=\"#E4E5E6\" /></linearGradient><path d=\"M-229.6 432.7c-1.2-1.2 1.6-.1 1.6-.1s.6.3.3-.4c-.2-.6-1.4-2-2.5-3.2l.1.2s2.3 2.7 2.2 3c-.2.2-1.1-.3-1.1-.3s-1.4-.5-1.2.1c.1.5 1.1 1.3 1.5 1.6l-.9-.9z\" fill=\"url(#wikipedia_o)\" /><linearGradient id=\"wikipedia_p\" gradientUnits=\"userSpaceOnUse\" x1=\"8.651\" y1=\"1534.969\" x2=\"-10.844\" y2=\"1629.835\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\"1\" stop-color=\"#E4E5E6\" /></linearGradient><path d=\"M-227 434.7c.4.3.9.5 1.4.7 0 0 .8.3 1.3-.1s.5-.6 1.2-.2c0 0 1.4.7 2.4 1.4s3.6 2.3 4.4 2.8c-.8-.4-3.7-2.4-4.6-3-.9-.6-2.6-1.7-3.3-1.5-.6.2-.5.4-.8.6-.3.2-.7.1-1.5-.4-.2-.1-.4-.2-.5-.3z\" fill=\"url(#wikipedia_p)\" /><linearGradient id=\"wikipedia_q\" gradientUnits=\"userSpaceOnUse\" x1=\"17.547\" y1=\"1532.957\" x2=\"-2.811\" y2=\"1632.017\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\"1\" stop-color=\"#E4E5E6\" /></linearGradient><path d=\"M-214.1 441.4c.4.1.7.1.8 0-.7 0-1.4-.3-1.4-.3s-.1 0-.2-.1c.3.3.6.4.8.4z\" fill=\"url(#wikipedia_q)\" /><linearGradient id=\"wikipedia_r\" gradientUnits=\"userSpaceOnUse\" x1=\"20.658\" y1=\"1537.844\" x2=\"1.256\" y2=\"1632.257\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\"1\" stop-color=\"#E4E5E6\" /></linearGradient><path d=\"M-209.7 442.2s-1.3-.2-1.9-.2c0 0 0 .1.2.2h.2c.3.1 2 .2 2.5.2.4-.1-.1-.3-.1-.3s-.1 0-.3-.1c-.3.2-.6.2-.6.2z\" fill=\"url(#wikipedia_r)\" /><path d=\"M-249.3 412c.1.1.2.4.5.7.1.2.3.1.2-.5-.3-.2-.4-.3-.5-.4-.1 0-.3-.3-.3-.3s-.5-.8-.3-.2c.4 1.2 1.6 3.8 1.6 3.8l1.4 2.5c-1-1.8-2.3-4.6-2.4-5-.2-.4-.3-.7-.2-.6zm-3.2-29.3v-.6c0-.1.1-.2.1-.4.7-2.8 1.1-3.9 1.4-4.6.4-.8.4-.2.4-.2s0 .2.1.2.3-.3.5-.8.6-1.7.7-2.2c.1-.7-.1-.4-.1-.4-.1 0-.1-.1-.1-.3 0 0 .4-2.1 3.1-6.6.2-.2.3-.3.5-.4-.1-.1 0-.3 0-.3.1-.2.3-.4.4-.7l-.1.5s-1.9 2.5-3.1 5.7c0 0-.3.8-.4 1.1 0 .2-.1.7.2.6h.1c-.1.5-.3 1.4-.6 2.3-.3.9-.6 1.6-.8 2.1-.1.1-.1 0-.1-.2s-.1-.2-.1-.2c-.2 0-.3.2-.4.4 0 .1-.1.2-.1.2s-.5.9-1.3 4.3c-.8 3.3-.8 6.1-.8 6.1s-.1 1.3-.2 1.4c-.1.1-.1-.1-.1-.1s0-.1-.1 0v-.9s0-.2.1-.2 0 .1 0 .2c0 0 .1 0 .1-.2s.1-2.8.6-5.3l.1-.5zm-1.1 9.3v.4c.1.4.2.4.2.4 0-.1.1-.3.2-.5v.4c0 .5 0 2.5.2 4.3.2 1.8.4 3.3.4 3.6 0 .2.5 3.3 1 5.1.3 1 .4 1.3.5 1.4 0 0 .1.2.3.3 0 0 .1-.1.1-.4 0 0 0 .1.1.1-.1.3-.1.4-.1.4s-.1 0 0 0c.1.4 0 .7-.2.3-.2-.4-.8-1.8-1.3-4.3 0 0-.5-2.7-.8-5.1v-.1l-.1-.1c0-.2 0-.5-.1-.7 0 0-.3-3.7-.2-4.6 0-.9-.1 0-.1 0v.3c0 .1-.1.4-.1-.2.1.3 0-.7 0-1zm24.3-40l-.5-.8-.1-.1s-.1-.1-.9 0h-.1s.4-.1.2.2c-.2.3-.6.5-1.2 1.1-.6.7-.4.8 0 .7.4 0 1.1-.4 2.6-1.1zm-1.6-.8z\" opacity=\".1\" fill=\"#232323\" /><path d=\"M-230.4 351.8c.3-.3.4-.5.5-.6 0 0-.1-.1-.9 0h-.1c.1 0 .3 0 .1.2-.2.3-.6.5-1.2 1.2s-.4.8 0 .7c.1 0 .2-.1.4-.2.2-.3.6-.8 1.2-1.3zm59.9 2.3l-.2.2s.1.1.2.1l-.1-.1s0-.1.1-.2h.1-.1z\" opacity=\".1\" fill=\"#232323\" /><path d=\"M-191.4 440.3s1.7-.2 3.2-.7c1.6-.5 1.9-1 1.9-1.3 0-.2-.4-.3-.9-.2.3 0 .5 0 .4.3-.3.6-.9.8-.9.8s-.3.2-.9.4c-.8.2-1.8.4-2.3.4-.7.1-.5 0-1.5.3h-.1c-.3.2 1.1.5 1.1.5s1.3.4 3.3.2h.1c.3-.1.5-.2.8-.2-2 .5-3.3.1-3.7.1-.4-.1-.8-.1-.9-.4-.2-.2.4-.2.4-.2z\" opacity=\".53\" fill=\"#FFF\" /><path d=\"M-190.7 354.4l.7.1c1.4-.4 2.7-.8 2.7-.8s1.3-.4 1.9-.6c.6-.2 1.1-.3 1.7-.4.6-.1 1.3-.1 1.7-.1.4 0 .5.1.5.1s.2.1.2.3c.1.1.7 1.9 3 2 2.2.1 2.3-1.1 2.1-1.5-.2-.4-.9-.9-.9-.9s-.9-.6-1.1-.8c-.2-.3 0-.4.1-.4s2.4-.5 2.7-.6l-.6-.2s-.1.1-.8.3c-.7.2-1.2.2-1.7.3-.5.1-.5.2-.5.2l-.9 1.4v.3c.1.2.4.4.4.4s.6.4 1 .7c.4.3.4.4.4.4-1.1.1-1.4 0-1.9-.3-.4-.2-.8-.7-.9-1.1-.2-.4-.5-.7-.5-.7-.6-.3-1.7-.3-2.8-.1-1.1.2-2.7.7-2.9.8-.3.1-1.6.6-2.3.7-.7.2-1.2.4-1.6.5-.4.1-3.4 1-4.6 1.3-1.1.3-1.8.5-1.8.5-1.7.2-2.2-.1-2.2-.1-.3-.1-.3-.5-.3-.5v-1.1s0-.4-.4-.6c-.3-.2-.8-.3-1.6-.3s-1.7 0-2.1.1c-.4.1-1.2.3-1.8 1-.6.6-.5 1.1-.5 1.1s0 .7.1 1.2.5.7.5.7-.7.5-3 1.2c-2.2.6-3.7.8-3.7.8l.7.3s5.5-1 7.1-2.6c0 0 .6-.3 0-.9-.6-.6-.9-.8-.9-.8s-.4-.2 0-.8c.4-.5.9-.8 1.4-.9s1.8-.3 2.9-.1c0 0 .5 0 .5.4s-.1.9-.1 1c0 .2 0 .5.4.8.4.3 1.1.5 1.1.5s1.3.2 2.8-.2c1.6-.4 3.6-1.1 5.4-1.6l.4-.4z\" opacity=\".1\" fill=\"#232323\" /><path d=\"M-205.5 356.6c.3.2.5.2.5.4.1.3-.6.6-.6.6s-.4-.2-.5-.7c-.1-.5-.1-1.2-.1-1.2v.3c.2.3.3.4.7.6z\" fill=\"#616161\" /><path d=\"M-171.6 429.3l.5.2c1.1-.6 1.5-.8 1.8-1 1.2-.7 2.6-1.6 3-1.9 0 0 .8-.5.1.2-.6.7-1 1-1 1s-.6.6-.5.8c0 0 .2.2 1.2-.7 1-.9 2.2-2.3 2.3-2.4.1-.2.1-.3.1-.3s.1-.2.3-.4c.1-.1 1.4-1.5 2-2.1.3-.4.5-.7.8-1.1-.4.4-1.7 1.8-2.5 2.7 0 0-.7.8-.9 1.1-.2.3-.2.5-.2.5s-.1.2-.4.5l-1.2 1.2s-.6.5-.8.5c-.2 0 .4-.5.4-.5s.6-.6 1-1.1c.4-.5.1-.5.1-.5s-.2 0-1 .5-1.4.9-1.4.9-1.7 1-2.8 1.6c-1.1.6-3.6 1.9-5 2.5-1.4.6-2.2.7-2 .5.1-.2.5-.5.5-.5s.4-.4.4-.8c0 0 .1-.6-1.6-.2-1.7.4-3.3 1.2-3.3 1.2s-2.6 1.2-2 1.9c0 0 .1.2.6.4s-.9.6-.9.6c-1.4.4-2.4.7-3.7.9-2 .4-3.6.8-4.2.9-.2 0-.3.1-.3.1s-1.2.3-3.2 1.1-6 1.4-6 1.4-2.5.3-2.8.6c-.2.3.2.5.2.5s.4.2 1.7.3h.5s0 .1-.2.2c-.3.1-.9.3-2.8.6-1.9.2-1.9-.1-1.9-.1s0-.1.1-.2 0-.4-.3-.5c0 0-.4-.3-1.8-.3s-4.2 0-6.8-.1c-2.4-.1-5.6-.6-6.1-.7 0 0-.1 0-.2-.1s-.6-.4-1.2-.7c-.5-.3-2.1-.9-2.1-.9s-2-.8-1.9-.5c0 .1.1.2.3.2.4.2.7.4 1.1.6 0 0-.7-.4-.5-.4.2 0 .4.1.4.1s1.2.3 2 .7c.8.4 1.4.8 1.4.8s.9.5 2.3.7c1.3.2 3.2.4 3.8.4l.6-.3.4.4c1.1.1 2.6.1 2.6.1s3 .1 4.6 0c.7-.1.5.3.5.3s-.2.4.2.5c0 0 .8.4 3.3.2 2.6-.3 3.1-.9 3.1-.9s.3-.3-.4-.4c-.5-.1-.5-.1-1.2-.1-.7-.1-1-.2-.6-.3.4-.1 1.2-.2 1.2-.2s2.2-.3 4.1-.8c0 0 1.9-.5 3.9-1.1.8-.3 1.4-.5 1.9-.6l.4-.6.6.4h.1s2.3-.5 3.3-.7c1-.2 3.2-.6 4.1-1.1.9-.4 1.4-.8 1.5-1.1.1-.3-.4-.4-.4-.4s-.6-.1-.5-.3c.1-.2.3-.4 1.2-.8.9-.4 2.1-.9 3.2-1.1 1.2-.3.7.2.7.2s-.7.7-.8 1c-.1.3 0 .3.1.3.1.1.6 0 1-.1s3.5-1.3 5.3-2.3l.1-.1.5-1z\" opacity=\".17\" fill=\"#FFF\" /><linearGradient id=\"wikipedia_s\" gradientUnits=\"userSpaceOnUse\" x1=\"-32.817\" y1=\"1596.566\" x2=\"-32.627\" y2=\"1596.566\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"gray\" /><stop offset=\".087\" stop-color=\"#7A7A7A\" /><stop offset=\".36\" stop-color=\"#6B6B6B\" /><stop offset=\".519\" stop-color=\"#686868\" /><stop offset=\".638\" stop-color=\"#5F5F5F\" /><stop offset=\".743\" stop-color=\"#4E4E4E\" /><stop offset=\".841\" stop-color=\"#383838\" /><stop offset=\".932\" stop-color=\"#1B1B1B\" /><stop offset=\"1\" /></linearGradient><path d=\"M-246.6 418l.2.1c-.1-.1-.2-.1-.2-.1z\" opacity=\".68\" fill=\"url(#wikipedia_s)\" /><linearGradient id=\"wikipedia_t\" gradientUnits=\"userSpaceOnUse\" x1=\"-32.594\" y1=\"1591.799\" x2=\"62.024\" y2=\"1591.799\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"gray\" /><stop offset=\".087\" stop-color=\"#7A7A7A\" /><stop offset=\".382\" stop-color=\"#828282\" /><stop offset=\".518\" stop-color=\"gray\" /><stop offset=\".568\" stop-color=\"#797979\" /><stop offset=\".603\" stop-color=\"#6E6E6E\" /><stop offset=\".608\" stop-color=\"#6B6B6B\" /><stop offset=\"1\" stop-color=\"#4E4E4E\" /></linearGradient><path d=\"M-163.6 410h-.4c-1.8 1.5-2.3 1.9-3.8 3 0 0-1.6 1.2-3.4 2.2-1.8 1-3.9.9-3.9.9s-.6-.1-.3-.5.6-1.4.8-1.9c.1-.5.4-1.8-.6-2.2-1-.4-3 .2-3 .2s-4.5 1.2-6.4 3.2c-1.8 2-.3 2.8-.3 2.8s.7.5 1.4.7c.6.2.5.4.4.6 0 0-2 1.3-4.4 2 0 0-3.3 1-6.4 1.2-3.2.2-4.5.3-4.5.3l-.4.4-.8-.3c-1.3.2-3.5.5-5.6 1-2.6.6-5.1 1.1-6.9 2.3 0 0-1.3.9-.6 1.7.8.9 1.6 1.2 1.6 1.2s.5.2.5.3c0 .2 0 .3-.4.5 0 0-1.4.8-4.1.9-2.7 0-3.9 0-4.7-.7-.7-.6.2-1.8.2-1.8s.3-.6 0-1.5c-.3-.8-2.2-.9-2.2-.9l-2.6-.1c-3.1-.1-7.2-.4-9-.7v.2l-.7-.3c-1.1-.2-3.2-.7-4.1-1.1-.8-.4-1.2-.3-1.1-1.1.1-.8-.8-1.8-.8-1.8s-1.2-1.3-2.3-2.1c-1.1-.8-1.5-.6-1.5-.6s-.5.3 0 1.3c.4 1 .9 1.4.9 1.4s.2.2.1.3c-.1.1-.5-.2-.8-.5-.3-.2-1.9-1.7-2.5-2.3l.1.4s0 .1.1.1c.2.3.9 1.3 2.2 2.3 1.5 1.2 1.6.7 1.6.7s.1-.4-.3-.8-.9-1.4-.8-1.7c.1-.3.3-.3.3-.3s.1-.1.6.3 1.5 1.1 2 1.7c.5.6.5 1.2.5 1.2s-.1.6.5 1.2 1.7 1.7 5.9 2.4h.1l.2-.6.6.7c3.6.5 5.6.6 5.6.6s4.7.2 6 .2c1.3 0 1 .7 1 .7s-.1.4-.2.6c-.2.3-.5 1.4-.1 1.9 0 0 .6 1.4 4.4 1.5 0 0 3.3.3 5.6-.7s.2-2.3.2-2.3-.8-.5-1.1-.7c-.3-.2-.2-.5-.1-.6.1-.2.3-.4.6-.5.3-.1 1.2-.7 5.4-1.7 4.1-1.1 6.6-1.2 6.6-1.2h.1l.3-.7.9.6c.7-.1 1.7-.1 2.5-.2 1.7-.1 4.3-.5 5.9-.8 1.5-.3 3.9-1.1 5.6-2 1.7-.9 1.8-1.5 1.8-1.5s.3-.5-.4-1-1-.4-1.7-1c-.6-.6.6-1.6.6-1.6s.6-.9 4-2.2c3.4-1.3 4-.9 4.2-.7.2.1.2.6.1.9l-.7 2.1c-.2.6-.3 1.4.6 1.6.9.2 2.2 0 3.4-.4 2.9-1 3.8-2.3 8.5-5.8l-.6-.9.7.1c2-1.6 3.9-3.6 3.9-3.6s1.3-1.3 1.9-2.4c.6-1 0 .9 0 .9s-.3 1.5.2 2.1c.4.4 1.6-.8 1.6-.8s.7-.8 1-2.1c.4-1.9.2-2.2.2-2.2s-.2-.4-.1-.9c.2-.5 1.2-3 2-4l.5-.6-.2-.6.3-.5s-.3.3-1.4 2.2c-1.3 2.1-1.5 3.8-1.5 3.8s-.1.7-.1 1c.1.4.2.5.2.6 0 .1-.1 1-.5 1.8s-.8 1-.8 1-.8.5-.9.2c-.1-.4-.1-.7 0-1 0-.2.3-1.6.3-2.1s-.5-.1-.5-.1-.1.1-.3.4-1.3 1.6-1.7 2.1c-1 1.2-1.9 2-4.3 3.9l-.5.8z\" opacity=\".43\" fill=\"url(#wikipedia_t)\" /><linearGradient id=\"wikipedia_u\" gradientUnits=\"userSpaceOnUse\" x1=\"-39.407\" y1=\"1573.355\" x2=\"60.406\" y2=\"1573.355\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#555\" /><stop offset=\"1\" stop-color=\"#231F20\" /></linearGradient><path d=\"M-252.8 398.5l.1 1c.2.3.6.7 1.1 1.2 1.1 1.1 1.4.4 1.4.4s.3-.7-.1-2c-.3-1.3-.3-2 .3-2s2.3.4 2.8 1.8c0 0 .2.6 0 1.5-.2.8-.2 1.6 0 2.3.1.7.8 1.4 1.5 2 .7.6 2.7 1.5 4.7 1.7 2 .1 2.6 0 2.6 0l.7-.8.1.7c.8-.1 2.1-.2 3.6-.4 2.5-.3 4.2-.5 5.8-.3 1.6.2 2.1 1.5 2.1 1.5s.1.3-.3.5c-.3.2-.7.5-.9.9-.2.3-.4 1.1.2 2 .6 1 2.1 1.6 3.5 1.4 1.3-.2 3.3-.7 4.5-1 1.3-.3 2.4-1 2.6-2 .1-1-1.5-2.3-1.5-2.3s-.8-.6-.9-.8c-.1-.1.1-.2.1-.2s.9-.2 1.4-.4c.4-.2 1.5-.6 3.4-1.2 1.8-.6 5.6-1.2 5.6-1.2s2.1-.3 4.7-.5l.6-.7.5.6c.4 0 .8 0 1.2-.1 3.6-.1 5.3-.6 7.2-1 1.9-.4 4.6-2 5-2.3.4-.3 1.2-.7 1.4-2 .2-1.3-1.4-2.2-1.4-2.2s-1.2-.6-1.5-.9c-.3-.3 0-.6 0-.6s.7-1.5 2.9-2.4c2.2-.9 3.7-1.1 4.6-1.2.9-.1 1.2.2 1.4.4.1.2.1.5 0 .8-.1.3-.4 1-.6 1.4-.2.4-.5 1.2-.3 1.6.2.4.8.6 1.7.4.8-.1 3-.8 4.9-1.6s5.1-2.3 5.1-2.3l.1-.7.7.3c1-.6 2.8-1.6 4-2.6 1.9-1.6 3.7-3.2 4.2-3.6.5-.4.9-.8 1.3-.7.4 0 .7.3 1 1.4.3 1.1.3 2 .4 2.6.1.5.3 1.2.9 1.3.6.1 1.5-.4 1.8-.7.3-.3.9-1.2.9-2.4 0 0 .1-1.6-.8-3.1 0 0-.4-.6-.5-.8-.1-.1-.2-.2 0-.5.1-.3.5-.8 1.1-1.2.4-.3.9-.3 1.1-.4 0 0 .3-.1.6-.3l-.1-.4.3.3c.4-.2.7 0 .7 0l-.4-.5.1-.5s-.3-.2-.7-.1c-.4.1-.4.4-1 .5-.6.1-1.3.3-1.9 1.3-.7 1 0 2.3 0 2.3s.4.6.5.9c.2.3 1.1 2.2 0 3.6 0 0-.6.6-1.5.9-.9.2-.6-.8-.7-1.4 0 0-.1-2.3-1.2-3.6-1-1.1-2.7.9-3.6 1.6-.8.6-3.2 3.1-6.7 4.9l-.5.9-.3-.5c-1.7.8-5.4 2.7-7.9 3.5 0 0-1.9.8-2.6.8 0 0-.2 0 0-.2.1-.2.3-.3.5-.7.2-.4.6-1.4.6-2.3 0-1-1.1-1.9-2.7-1.7-1.6.2-3.1.6-4.8 1.3-1.8.7-3.3 2.2-3.6 3.4-.2 1.2 1.1 1.9 1.1 1.9s1.5.8 1.7 1.2c.2.4 0 .8 0 .8s-.1.4-.8.8c-.6.4-2.4 1.3-2.4 1.3s-2.2 1.2-5.6 1.5c0 0-3.1.3-4.8.3h-.1l-.5.5-.6-.4c-1.6.1-3.5.4-3.5.4s-4.3.6-8.2 1.8c-3.3 1-4 1.6-4 1.6s-.7.6-.1 1.5c0 0 .3.5 1 1.1.7.5 1.2 1.1 1.2 1.3-.1.3-.3.4-.3.4s-1 .9-4.9 1.5c0 0-2.5.5-3.3-.3-.8-.8-.4-1.3-.4-1.3s.1-.2.6-.5c0 0 1-.6.6-1.7-.3-1.1-2.1-2.5-4.1-2.5 0 0-2.3 0-8.2.8l-.2.5-.6-.4c-.3 0-.7.1-1.1.1-1 .1-2.5-.1-4.3-.6-1.8-.5-3-1.5-3.1-2.1-.1-.4 0-1 0-1s.3-1.3.1-2.4c-.2-1.1-.6-1.9-1.6-2.6-1-.6-1.6-.5-1.6-.5s-.9-.1-.9 1.4c0 1.6.2 2.3.2 2.3s.2.6-.1.6c-.3.1-.7-.4-.7-.4s-1-.9-1.6-1.7v.1l-.2.5s.1.1.3.4l-.1-.8z\" opacity=\".31\" fill=\"url(#wikipedia_u)\" /><linearGradient id=\"wikipedia_v\" gradientUnits=\"userSpaceOnUse\" x1=\"-39.103\" y1=\"1552.882\" x2=\"52.501\" y2=\"1552.882\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#A0A0A0\" /><stop offset=\".077\" stop-color=\"#656767\" /><stop offset=\"1\" stop-color=\"#717375\" /></linearGradient><path d=\"M-162.9 361.7l.2.8s-.6.3-1.7.6-2.2.8-2.2.8-.9.3-.6 1c.3.7.8 1.1.8 1.1s.7.7.7 1.2-.2.8-.8 1.1c-.6.3-1.1.4-1.1.4s-1.3.2-2-.4c-.7-.6-.8-1.7-.8-1.7s-.1-.9-1.1-1.3c-1.1-.4-2.5.4-2.5.4s-1.1.6-2.2 1.3c-1.1.7-3.3 1.6-4.6 2.1l-.2.7-.8-.4c-1.4.5-3.3 1.1-3.3 1.1s-2.5.9-4.2 1.2c-1.6.2-2 0-2.2-.2-.2-.2 0-1 0-1s.7-1.4.3-2.1c-.3-.7-2.5-.9-2.5-.9s-2.3-.3-4.5.9c-1.9 1.1-2.1 1.6-2.1 1.6s-.6.9.1 1.9c.8 1.1 1.9 1.1 1.9 1.1s1 .1 1.3.4c.2.3.1.6.1.6s-.3.9-2.2 1.3c0 0-3.2.9-9.1 1.8l-.6.6c-3.7.5-8.1 1.4-10.6 2-2.4.6-2.6 1.3-2.6 1.3-.5.8.1 1.2.1 1.2s.8.3 1 1.2c.2.9-.8 1.6-.8 1.6s-1.2 1-2.9 1.3-2.4.4-3.4-.5c-.9-.7-.3-1.9.3-2.3.6-.4.9-.9 1-1.1.1-.2 0-.4 0-.4l-.6-.5c-2-1.3-9.9.1-9.9.1l-1.3.3-.7-.4s-2.3.6-4.9.6c-2.7 0-1.3-2.1-1.3-2.1s.6-1.1.8-1.8c0 0 .2-1.7-1.4-1.6-1.6.1-2 1.5-2 1.5s-.1.8-.1 1.4c0 .6 0 1.8-.7 2.6-.7.7-1.5.5-1.5.5s-1.3-.6-1.6-.7c-.3-.1-.5-.2-.8-.1h-.1l-.2.8v-.6c-.2.2-.3.4-.3.4l.1.3-.2.6.2-.4.2-.4-.1.2c.1 0 .1-.1.2-.1.3 0 .6.2.6.2s1.1.6 1.6.7c.5.1.9-.1 1.2-.3.5-.4 1.1-1.1 1.4-1.8.2-.6.3-2.4.3-2.4v-.5c0-.1-.1-.6.2-.8.3-.2.5-.3 1.1-.4.7 0 .9.4.9.4s.2.3.2.5-.1.3-.1.3-.4.6-.5.9c-.1.3-.6 1.3-.5 2.2.1.9 1.5 1.3 1.5 1.3s1.1.3 2.6 0l3.1-.5.5-.6.2.5c.8-.1 2.1-.4 3.6-.5 2.3-.2 4.8-.3 5.8-.1 0 0 .5.1.4.2l-.4.4-.7.7s-.7 1.2-.7 1.7.5 2 2.4 2.4c1.9.4 4.1-.3 4.1-.3s1.4-.3 2.8-1.7 0-3.1 0-3.1-.2-.3-.6-.4c0 0-.2 0-.1-.2.1-.1.4-.6 1.4-.9 1-.3 4-1.2 11.1-2.1l.3-.6.9.5c2.7-.4 4.6-.7 7.8-1.5 0 0 3-.5 3.7-1.7.4-.6 1-1.5 0-2.4 0 0-.1-.2-.8-.3-.7-.2-1.2-.3-1.7-.7-.6-.4-.6-.9-.6-.9s0-.4.9-1c0 0 .9-.6 2.5-1.2 1.7-.5 3.6-.3 3.6-.3s.8.1.7.6c-.1.6-.6 1.5-.6 2s0 1 .9 1.4c.9.4 2.3.3 2.3.3s1.4-.1 3.6-.8c2.3-.7 4.6-1.6 4.6-1.6l-.1-.5 1 .2c.6-.2 1.4-.5 2.3-.9 1.8-.8 2.7-1.5 3.5-2 0 0 1.8-1.1 2.9-1.1 0 0 .3 0 .3.3s.1.8.2 1.1c.1.3.7 1.8 2.7 2 2 .2 2.8-1.1 2.8-1.1s.7-1-.5-2.3c0 0-1-1-1-1.1 0 0-.1-.2.2-.2.3-.1 3.2-.9 4.3-1.4l-.3-.5.5.4c.2-.1.4-.2.5-.4.2-.3-.1-.8-.1-.8-.1-.2-.3-.4-.4-.5l-.6-.3h-.1l.4.6\" opacity=\".34\" fill=\"url(#wikipedia_v)\" /><path d=\"M-245.9 366.3l-.3.4c.1 0 .2-.1.2-.1s.4-.1 1.1.1c.9.2 2.1-.5 2.1-.5s.9-.5 1.3-1.4l.4-1s.3-1 1.1-1.3c0 0 .3-.2.8-.2s.4.4.4.4-.1.2-.6.9-.7 1.2-.7 1.2-.3.7.2 1c0 0 .2.1.9-.1s3-.8 4.4-1.1l1-.5-.6-.4c-2.4.4-4.2 1-4.8 1.2-.6.2-.6.1-.6.1-.2-.2.4-1 .4-1s.7-.9.9-1.7c.3-.8-.9-.7-.9-.7-.8.1-1.3.5-1.9 1.2-.5.6-.8 1.4-.9 1.8-.1.3-.2.5-.2.5s-.1.2-.4.3c-.4.2-1.2.4-1.2.4s-.5 0-.9-.1c-.2-.1-.9 0-.9 0l.1-.5h-.1l-.7.4-.3.6c-.1.1-.2.5 0 .5h.2l.5-.4zm5.2-7.1s.3-.3.3 0c0 .2-.3.7-.3.7s-.1.1-.2.1c0 0 0-.5.2-.8zm-2.7 3.3s-.4.5 0 .5l.8-.8s-.1-.1-.2-.1c.1 0-.4.2-.6.4z\" opacity=\".1\" fill=\"#232323\" /><path d=\"M-176.2 435.7s-1.8.8-3.4 1.6c-1.6.8-2.3 1.1-2.3 1.1s-.1 0 0 .1c.1 0 0 .1 0 .1-.8.4-2.7 1.1-2.7 1.1s-.2.1-.2 0l.2-.1s.4-.1.3-.2c-.1-.1-1.2.3-1.2.3s-1.9.6-2.9.9c-.9.3-2.8.7-2.8.7-1.2.3-3.8.8-4.3.9-.6.1-.4.1-.4.1s.5-.2-.4-.2c-1.1-.1-2.4.1-3.6.3-1.3.2-1.2.3-1.2.3s0 .2.7.1h.5c-1.4.2-4.2.2-4.2.2h3.2c.2 0 1.5-.1 1.9-.2.5-.1-.1-.1-.1-.1h-.7s-.8 0-.1-.2c.7-.1 1.8-.2 2.4-.3.8-.1.5.1.5.1s0 .1.5.1 4.7-.8 7.1-1.5c2.3-.7 4.1-1.3 4.1-1.3s.2-.1.1 0-.5.2-.5.2-.6.3.8-.1c.1 0 .1 0 .2-.1l3.6-1.5s.1-.1 0-.1c-.2.1 0-.1.2-.1.2-.1 2.3-1.2 3.4-1.6.5-.1.9-.3 1.3-.6z\" opacity=\".3\" fill=\"#FFF\" /><linearGradient id=\"wikipedia_w\" gradientUnits=\"userSpaceOnUse\" x1=\"-36.343\" y1=\"1578.751\" x2=\"-36.343\" y2=\"1578.751\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\".078\" stop-color=\"#F4F4F4\" /><stop offset=\".381\" stop-color=\"#CECECE\" /><stop offset=\".54\" stop-color=\"#BFBFBF\" /><stop offset=\".836\" stop-color=\"#7C7C7C\" /><stop offset=\".9\" stop-color=\"#A8A8A8\" /><stop offset=\".909\" stop-color=\"#9A9A9A\" /><stop offset=\".933\" stop-color=\"#7D7D7D\" /><stop offset=\".956\" stop-color=\"#686868\" /><stop offset=\".979\" stop-color=\"#5B5B5B\" /><stop offset=\"1\" stop-color=\"#575757\" /></linearGradient><linearGradient id=\"wikipedia_x\" gradientUnits=\"userSpaceOnUse\" x1=\"-39.674\" y1=\"1578.511\" x2=\"68.872\" y2=\"1566.485\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\".078\" stop-color=\"#F4F4F4\" /><stop offset=\".381\" stop-color=\"#CECECE\" /><stop offset=\".54\" stop-color=\"#BFBFBF\" /><stop offset=\".836\" stop-color=\"#7C7C7C\" /><stop offset=\".9\" stop-color=\"#A8A8A8\" /><stop offset=\".909\" stop-color=\"#9A9A9A\" /><stop offset=\".933\" stop-color=\"#7D7D7D\" /><stop offset=\".956\" stop-color=\"#686868\" /><stop offset=\".979\" stop-color=\"#5B5B5B\" /><stop offset=\"1\" stop-color=\"#575757\" /></linearGradient><path d=\"M-252.8 398.5l.1 1c.2.3.6.7 1.1 1.2 1.1 1.1 1.4.4 1.4.4s.1-.2.1-.6c0 .2-.2.4-.8-.1-.3-.2-.7-.6-1.1-1-.3-.3-.7-.7-1-1.1v.1l-.2.5s.1.1.3.4l.1-.8z\" fill=\"url(#wikipedia_x)\" /><linearGradient id=\"wikipedia_y\" gradientUnits=\"userSpaceOnUse\" x1=\"-40.111\" y1=\"1578.477\" x2=\"82.882\" y2=\"1564.851\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\".078\" stop-color=\"#F4F4F4\" /><stop offset=\".381\" stop-color=\"#CECECE\" /><stop offset=\".54\" stop-color=\"#BFBFBF\" /><stop offset=\".836\" stop-color=\"#7C7C7C\" /><stop offset=\".9\" stop-color=\"#A8A8A8\" /><stop offset=\".909\" stop-color=\"#9A9A9A\" /><stop offset=\".933\" stop-color=\"#7D7D7D\" /><stop offset=\".956\" stop-color=\"#686868\" /><stop offset=\".979\" stop-color=\"#5B5B5B\" /><stop offset=\"1\" stop-color=\"#575757\" /></linearGradient><path d=\"M-250.3 399.1v.2s.1.4.1.8c.1-.3 0-.6-.1-1z\" fill=\"url(#wikipedia_y)\" /><linearGradient id=\"wikipedia_z\" gradientUnits=\"userSpaceOnUse\" x1=\"157.253\" y1=\"-110.999\" x2=\"253.236\" y2=\"-91.625\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#EDEDEE\" /><stop offset=\".418\" stop-color=\"#FFF\" /><stop offset=\".626\" stop-color=\"#F8F9F9\" /><stop offset=\"1\" stop-color=\"#BFC0C2\" /></linearGradient><path d=\"M-154.3 378.6l.3.3c.4-.2.7 0 .7 0l-.4-.5c-.4.1-1.1.3-2.2.6 0 0-1.4.6-1.6 1.5 0 .3 0 .6.1.9.8 1.4.9 1.7.9 1.7.5 1.1.4 2 .3 2.8-.2.9-1.2 1.7-1.8 1.8-.6.2-1 0-1.1-.5-.2-.5-.2-.8-.4-2.3-.3-1.5-.7-2.2-1.2-2.4-.6-.2-1.3.5-1.7.8-.4.3-2.4 2.2-2.4 2.2s-2.3 2.1-5.7 4c-3.4 1.9-7.7 3.4-7.7 3.4s-2.8 1.1-3.5 1c-.7-.1-.5-.7-.3-1.1.2-.4.5-.9.8-1.5.3-.8.2-1.7-.4-2-.6-.3-1.2-.5-3.5.1s-3.2 1.1-3.8 1.5c-.6.4-1.6 1.2-1.8 1.7-.3.5-.6 1 .1 1.6.7.6.8.5 1.6 1 .8.6.9.6 1 1.5 0 .8-.8 1.3-.8 1.3s-3.1 2.1-6.6 2.8c-2.3.5-6.8.6-6.8.6s-1.3 0-5.4.5c-4.1.6-6.8 1.5-7.7 1.9-1 .3-2.3.8-3.1 1.2-.8.4-.4.9-.2 1 .2.1 1.2 1.1 1.5 1.4.3.3 1.5 1.3.1 2.1s-3.6 1.3-3.6 1.3-3.1.7-4.1.2c-1-.4-1.2-.8-1.5-1.4-.3-.7 0-1.3.8-1.8s.5-1.2.5-1.2c-1-1.9-3.1-2.1-4.8-1.9-2.7.2-5.4.5-7.4.7-3.1.4-4.5-.1-6-.5-1.5-.5-3-1.5-3.2-2.5v-.3c-.1-.8.1-1.1.2-1.8.1-.6 0-1.5-.1-1.8v-.1c-.5-1.3-1.7-1.9-2.7-2.1-1-.2-1 .9-1 .9.1-.2.2-.3.4-.3.6 0 2.3.4 2.8 1.8 0 0 .2.6 0 1.5-.2.8-.2 1.6 0 2.3.1.7.8 1.4 1.5 2 .7.6 2.7 1.5 4.7 1.7 1.8.1 2.5 0 2.6 0l.8-.8.1.7c.8-.1 2.1-.2 3.6-.4 2.5-.3 4.2-.5 5.8-.3 1.6.2 2.1 1.5 2.1 1.5s.1.3-.3.5c-.3.2-.8.5-.9.9-.2.3-.4 1.1.2 2 .6 1 2.1 1.6 3.5 1.4 1.3-.2 3.3-.7 4.5-1 1.3-.3 2.4-1 2.6-2 .1-1-1.5-2.3-1.5-2.3s-.8-.6-.9-.8c-.1-.1.1-.2.1-.2s1-.2 1.4-.4c.4-.2 1.5-.6 3.4-1.2 1.8-.6 5.6-1.2 5.6-1.2s2.1-.3 4.7-.5l.6-.7.5.6c.4 0 .8 0 1.2-.1 3.6-.1 5.3-.6 7.2-1 1.9-.4 4.6-2 5-2.3.4-.3 1.2-.7 1.4-2 .2-1.3-1.4-2.2-1.4-2.2s-1.2-.6-1.5-.9c-.3-.3 0-.6 0-.6s.7-1.5 2.9-2.4c2.2-.9 3.7-1.1 4.6-1.2.9-.1 1.2.2 1.4.4.1.2.1.5 0 .8-.1.3-.4 1-.6 1.4-.2.4-.5 1.2-.3 1.6.2.4.8.6 1.7.4.8-.1 3-.8 4.9-1.6 1.9-.8 5.1-2.3 5.1-2.3l.1-.7.7.3c1-.6 2.8-1.6 4-2.6 1.9-1.6 3.7-3.2 4.2-3.6.5-.4.9-.8 1.3-.7.4 0 .7.3 1 1.4.3 1.1.3 2 .4 2.6.1.5.3 1.2.9 1.3.6.1 1.5-.4 1.8-.7.3-.3.9-1.2.9-2.4 0 0 .1-1.6-.8-3.1 0 0-.3-.6-.5-.8-.1-.1-.2-.2 0-.5.1-.3.5-.8 1.1-1.2.4-.3.9-.3 1.1-.4 0 0 .3-.1.6-.3h-.7z\" fill=\"url(#wikipedia_z)\" /><path d=\"M-252.5 382.7l-.1.2c.1 0 .1-.1.2-.1.3 0 .6.2.6.2s1.1.6 1.6.7c.5.1.9-.1 1.2-.3.3-.2.5-.4.8-.7-.3.3-.7.5-1.4.6 0 0-.6 0-1.4-.6-.8-.5-1.3-.2-1.7.1l-.2.6.2-.4.2-.3z\" fill=\"#FFF\" /><path d=\"M-247.6 382c.1-.1.1-.2.2-.4 0-.1.1-.3.1-.5-.1.4-.2.7-.2.7s-.1.1-.1.2zm.4-3.3v1.5c0-.5.1-.9.1-.9-.1-.1-.1-.5-.1-.6z\" opacity=\".73\" fill=\"#FFF\" /><linearGradient id=\"wikipedia_A\" gradientUnits=\"userSpaceOnUse\" x1=\"159.514\" y1=\"-70.412\" x2=\"163.999\" y2=\"-70.412\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#E2E3E4\" /><stop offset=\".505\" stop-color=\"#FFF\" /></linearGradient><path d=\"M-245.9 366.3l-.3.4c.1 0 .1 0 .2-.1 0 0 .4-.1 1.1.1.9.2 2.1-.5 2.1-.5s.3-.2.6-.5c-.4.2-1.4.8-2.1.6-1-.2-1 0-1.3 0-.3 0-.3-.1-.3-.3v-.1c.1-.3.3-.7.3-.7l-.7.4-.3.6c-.1.1-.2.5 0 .5h.2l.5-.4z\" fill=\"url(#wikipedia_A)\" /><path d=\"M-237 365c-1 .3-2 .7-2.5.6-.4-.1-.1-.8 0-1 .1-.1.2-.3.2-.4.3-.5.8-1.4.8-1.4v-.1c.1-.2.1-.5-.5-.6-.8-.1-1.6.6-1.6.6s-.5.3-.8 1.4l.1-.3s.3-1 1.1-1.3c0 0 .3-.2.8-.2s.4.4.4.4-.1.2-.6.9-.7 1.2-.7 1.2-.3.7.2 1c0 0 .2.1.9-.1s3-.8 4.4-1.1l1-.5c-.4.2-2.2.7-3.2.9z\" fill=\"#FFF\" /><path d=\"M-163.4 424.2zm.2-.2c0-.1 0-.1 0 0 0-.1 0-.1 0 0zm-.1 0z\" opacity=\".1\" fill=\"#231F20\" /><path d=\"M-166.1 426.7l-.2.2c-.6.7-1 1-1 1l-.2.3s.2 0 .6-.2c-.1 0-.1.1-.2.1-.2 0 .4-.5.4-.5s.6-.6 1-1.1c.4-.5.1-.5.1-.5s-.1 0-.4.1c.1-.1.3.1-.1.6z\" opacity=\".25\" fill=\"#231F20\" /><path d=\"M-181.1 431.2s2.2-.9 3.4-.8c0 0 .6.1-.1.7-.7.7-.9 1.2.4.8 0 0 .1 0 .2-.1-.5.1-.7.1-.7 0 .1-.2.5-.5.5-.5s.4-.4.4-.8c0 0 .1-.6-1.6-.2-.9.3-1.8.6-2.5.9z\" opacity=\".22\" fill=\"#231F20\" /><path d=\"M-181.8 431.6zm15.9-5.6c-.1 0-.1 0 0 0-.1 0-.1 0 0 0z\" opacity=\".1\" fill=\"#231F20\" /><path d=\"M-175.7 431.3c1.4-.5 3.9-1.9 5-2.5-1.1.6-3.6 1.9-5 2.5z\" opacity=\".28\" fill=\"#231F20\" /><path d=\"M-166.5 426.3s.1 0 0 0c.1 0 0 0 0 0zm4.1-3.2zm-.2.2s.1 0 0 0c.1 0 0 0 0 0zm.1-.1zm-.6.7zm-19.7 8.2zm20.1-8.7c.1 0 .1 0 0 0 .1 0 .1 0 0 0zm-.2.3zm.2-.2zm-.3.3zm.2-.2zm-19.4 8.2zm.2-.2s0 .1 0 0c0 .1 0 0 0 0zm-.7.5zm.7-.4zm.1-.1zm-.1.1zm.2-.1zm-.1 0zm-.2.1zm.3-.1zm0 0zm-.1 0zm-.2.1s-.1 0 0 0c-.1 0 0 0 0 0zm-.3.2c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm.6-.3zm-.8.4zm0 0s-.1 0 0 0c-.1 0 0 0 0 0zm.1-.1c0 .1 0 .1 0 0 0 .1 0 .1 0 0zm.3-.1s-.1 0 0 0zm19.9-8.8zm-20 8.8zm0 0c0 .1-.1.1 0 0-.1.1 0 .1 0 0zm-.1.1zm20.8-9.7zm0 .1c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm.1-.2s0 .1 0 0c0 .1 0 0 0 0zm-.7.8zm.5-.5s-.1 0 0 0c-.1 0 0 0 0 0zm.3-.3zm.2-.2zm-.1 0zm-4.8 4.2zm4.7-4.1zm-4.9 4.2c-.1 0-.1.1 0 0-.1.1-.1 0 0 0zm-39.5 14.8zm-.1 0zm0 0zm-.1 0zm-.1 0zm40-14.9s-.1 0 0 0c-.1 0 0 0 0 0zm-.1 0c0 .1 0 .1 0 0 0 .1 0 .1 0 0zm-.1.1zm.3-.1s0-.1 0 0c0-.1 0 0 0 0zm-.3 1.4s-.1.1-.2.1c.1 0 .2 0 .2-.1zm4.5-5zm-64.1 14.5c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm43-4.8c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm-25.2 7.7c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm-18.2-3zm-.1-.1h.1c-.1.1-.1.1-.1 0zm.3.1h-.1.1zm64-14.1zm-63.8 14.2h.1-.1zm63.9-14.3zm.1-.1zM-226 437s-.1 0 0 0c-.1 0 0 0 0 0zm43.1-4.8c.1-.1.1-.1 0 0 .1-.1.1-.1 0 0zm-24.7 7.7c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm24.7-7.7zm-24.7 7.7zm.1.1c0-.1 0-.1 0 0 0-.1 0-.1 0 0zm-.4-.1h-.1.1zm.2 0s-.1 0 0 0c-.1 0 0 0 0 0zm-.1 0s-.1 0 0 0c-.1 0 0 0 0 0zm-.2 0c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm-18.1-2.9zm19.5 4zm0 0zm0 0zm.1 0zm-.1 0zm-.1 0zm-.7-1zm.2 0s-.1 0 0 0c-.1 0 0 0 0 0zm2.2 1zm-2.3-1c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm1.1 1zm0 0zm-2.6-1.1zm2.5 1.1z\" opacity=\".1\" fill=\"#231F20\" /><path d=\"M-207.2 440s.2 0 .1.3.1.5.5.6c-.1 0-.1-.1-.1-.1s0-.1.1-.2 0-.4-.3-.5c-.1 0-.1 0-.3-.1z\" opacity=\".36\" fill=\"#231F20\" /><path d=\"M-206.1 441zm-.4 0zm.2 0zm-.2 0zm.1 0zm0 0zm-.9-1zm-18-2.7s0-.1 0 0zm.1 0zm-.1-.1zm17 2.7zm-16.9-2.6zm-1.4-.5zm.1 0zm1.3.5zm-.2-.1z\" opacity=\".1\" fill=\"#231F20\" /><path d=\"M-226.3 437.2c-.3-.2-.4-.5-.4-.5h.1c-.3-.1-.5-.1-.5 0s.1.2.3.2c.1.2.3.3.5.3z\" opacity=\".38\" fill=\"#231F20\" /><path d=\"M-225.3 437.2zm-.1 0zm.2.1zm-.6-.2zm17.3 2.8c.1 0 .1 0 0 0 .1 0 .1 0 0 0zm-.1 0s.1 0 0 0c.1 0 0 0 0 0zm-17.1-2.8h-.1.1zm.2.1zm-.1-.1zm.2.1c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm-.1-.1c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm41.5-2.7zm.8-.3zm0 0zm-.1 0zm0 0zm-.3.1zm0 .1zm.3-.2zm-.4.2zm0 0zm.1 0zm-21.5 6.7zm21.4-6.7zm.5-1.9zm.2-.1zm-.1 0z\" opacity=\".1\" fill=\"#231F20\" /><path d=\"M-183.1 433.8c.2.1.1.2-.1.3h.1s.8-.4.5-.6c-.3-.2-1.1-.3-.6-1-.4.3-.8.7-.5 1 0-.1.1.1.6.3z\" opacity=\".19\" fill=\"#231F20\" /><path d=\"M-183.4 434.2zm0 0zm0 0zm-.1 0zm0 0zm.3-1.8c.1 0 .1-.1 0 0 .1-.1.1 0 0 0zm-22.5 8.6zm.1 0zm0 0z\" opacity=\".1\" fill=\"#231F20\" /><path d=\"M-204 439.9s.4.2 1.7.3h.5s0 .1-.1.1c.1 0 .8-.3.5-.4H-201.7c-.1 0-.3 0-.4-.1h-.2s-.5 0-.7-.3c-.1-.2.5-.3.5-.3s1-.2 1.9-.3c0 0-2.5.3-2.8.6-1 .2-.6.4-.6.4z\" opacity=\".25\" fill=\"#231F20\" /><path d=\"M-184 434.4zm0 0zm-21.2 6.6zm-.1 0zm-.1 0zm0 0c-.1 0-.1 0 0 0-.1 0-.1 0 0 0zm21.5-6.6s0-.1 0 0c0-.1 0 0 0 0zm0 0zm.1-.1zm-.1.1zm.1-.1zm-.2.1zm0 0zm2.2-2.8zm-2.1 2.8zm-.1 0z\" opacity=\".1\" fill=\"#231F20\" /><linearGradient id=\"wikipedia_B\" gradientUnits=\"userSpaceOnUse\" x1=\"160.245\" y1=\"-122.267\" x2=\"255.006\" y2=\"-99.729\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#EDEDEE\" /><stop offset=\".418\" stop-color=\"#FFF\" /><stop offset=\".626\" stop-color=\"#F8F9F9\" /><stop offset=\".951\" stop-color=\"#B2B4B6\" /></linearGradient><path d=\"M-246.4 418.1l-.1-.1.1.1z\" fill=\"url(#wikipedia_B)\" /><linearGradient id=\"wikipedia_C\" gradientUnits=\"userSpaceOnUse\" x1=\"162.699\" y1=\"-132.563\" x2=\"257.822\" y2=\"-109.938\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#EDEDEE\" /><stop offset=\".418\" stop-color=\"#FFF\" /><stop offset=\".626\" stop-color=\"#F8F9F9\" /><stop offset=\".951\" stop-color=\"#B2B4B6\" /></linearGradient><path d=\"M-163.6 410l.7.1c2-1.6 3.9-3.6 3.9-3.6s1.3-1.3 1.9-2.4c.2-.4.3-.4.3-.2 0-.1.1-.5 0-.7-.1-.2-.4.3-.8.9-.1 0-2.2 2.9-6 5.9-3.7 2.9-4.7 3.7-8 5.6 0 0-2.3 1-3.9.7-1.2-.3 0-1.5.3-2.7.3-1.1.1-1.6-.2-1.8-.3-.2-.9-.4-2.1-.1 0 0-4.7 1.3-6.8 3.3-1.9 1.9.5 2.6 1 2.9 0 0 .8.3.7.7-.1.3-.5.6-.7.8-.2.2-3.3 2-8.3 2.8-4 .6-3.3.3-7.1.7-3.9.4-5 .7-8.1 1.5-3.1.7-4.9 1.5-5.4 2.3-.3.7.5 1.1 1 1.4.5.3 1.4.8 1.1 1.3-.3.5-1.6 1.3-4.9 1.4-3.2.1-4.6-.3-5.2-1-.5-.6-.1-1.3.1-1.9 0 0 .4-.8.2-1.2-.2-.4-.7-.5-1.3-.6-.5-.1-3.2-.2-5.3-.3-2.4-.1-5.2-.2-8.6-.9 0 0-2.2-.4-3.7-1.3-.1-.1-.2-.1-.3-.2-.1-.1-.2-.1-.3-.2-.4-.4 0-.7-.2-1.2-.1-.4-.4-.9-.9-1.5l-.7-.7c-.1-.1-.2-.1-.3-.2-1.3-1-1.4-1.1-2-1.2-.5 0-.2.9-.1 1.2 0 .1.1.3.2.5-.2-.4-.3-.7-.3-.9.1-.3.3-.3.3-.3s.1-.1.6.3 1.5 1.1 2 1.7c.5.6.5 1.2.5 1.2s-.1.6.5 1.2 1.7 1.7 5.9 2.3h.1l.2-.5.6.7c3.6.5 5.5.6 5.5.6s4.7.2 6 .2c1.3 0 1 .7 1 .7s-.1.4-.2.6c-.2.3-.5 1.4-.1 1.9 0 0 .6 1.4 4.4 1.5 0 0 3.3.3 5.6-.7s.2-2.3.2-2.3-.8-.5-1.1-.7c-.3-.2-.2-.5-.1-.6.1-.2.3-.4.6-.5.3-.1 1.2-.7 5.4-1.7 4.1-1.1 6.6-1.2 6.6-1.2h.1l.3-.7.8.6c.7-.1 1.7-.1 2.5-.2 1.7-.1 4.3-.5 5.9-.8 1.5-.3 3.9-1.1 5.6-2 1.7-.9 1.8-1.5 1.8-1.5s.3-.5-.4-1-1-.4-1.7-1c-.6-.6.6-1.6.6-1.6s.6-.9 4-2.2c3.4-1.3 4-.9 4.2-.7.2.1.2.6.1.9l-.7 2.1c-.2.6-.3 1.4.6 1.6.9.2 2.2 0 3.4-.4 2.9-1 3.8-2.3 8.5-5.8v-.9z\" opacity=\".83\" fill=\"url(#wikipedia_C)\" /><linearGradient id=\"wikipedia_D\" gradientUnits=\"userSpaceOnUse\" x1=\"161.474\" y1=\"-127.42\" x2=\"256.587\" y2=\"-104.797\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#EDEDEE\" /><stop offset=\".418\" stop-color=\"#FFF\" /><stop offset=\".626\" stop-color=\"#F8F9F9\" /><stop offset=\".951\" stop-color=\"#B2B4B6\" /></linearGradient><path d=\"M-153.1 397.6c-.6 1.2-1.2 2.6-1.4 3.5 0 .2-.1.3-.1.3s-.1.7-.1 1c0 .2.1.3.1.4 0 .1 0 .1.1.1v.1c0 .1 0 .6-.3 1.2-.1.2-.1.4-.2.5 0 .1-.1.1-.1.1-.5.8-1.1 1.5-1.6 1.5-.3 0-.5-.1-.6-.4 0 .4.1.7.3 1 .4.4 1.6-.8 1.6-.8s.7-.8 1-2.1c.4-1.9.2-2.2.2-2.2s-.2-.4-.1-.9c.2-.5 1.2-3 2-4l.5-.6-.2-.5c-.1.1-.3.3-.4.5-.2.5-.4.8-.7 1.3z\" fill=\"url(#wikipedia_D)\" /><linearGradient id=\"wikipedia_E\" gradientUnits=\"userSpaceOnUse\" x1=\"160.775\" y1=\"-124.479\" x2=\"255.87\" y2=\"-101.862\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#EDEDEE\" /><stop offset=\".418\" stop-color=\"#FFF\" /><stop offset=\".626\" stop-color=\"#F8F9F9\" /><stop offset=\".951\" stop-color=\"#B2B4B6\" /></linearGradient><path d=\"M-243.4 420.8c-.1-.1-.3-.2-.5-.4-.1-.1-.6-.6-1.2-1.1-.2-.2-.4-.4-.6-.5-.3-.3-.5-.5-.7-.6l.1.4s0 .1.1.1c.2.3.9 1.3 2.2 2.3 1.5 1.2 1.6.7 1.6.7s.1-.4-.3-.8c-.1-.1-.1-.2-.2-.3-.1-.1.9 1.4-.5.2z\" fill=\"url(#wikipedia_E)\" /><linearGradient id=\"wikipedia_F\" gradientUnits=\"userSpaceOnUse\" x1=\"160.915\" y1=\"-125.065\" x2=\"256.04\" y2=\"-102.44\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#EDEDEE\" /><stop offset=\".418\" stop-color=\"#FFF\" /><stop offset=\".626\" stop-color=\"#F8F9F9\" /><stop offset=\".951\" stop-color=\"#B2B4B6\" /></linearGradient><path d=\"M-243.3 420c.1.2.2.4.3.5 0 0-.2-.2-.3-.5z\" fill=\"url(#wikipedia_F)\" /><linearGradient id=\"wikipedia_G\" gradientUnits=\"userSpaceOnUse\" x1=\"162.103\" y1=\"-130.065\" x2=\"257.229\" y2=\"-107.44\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#EDEDEE\" /><stop offset=\".418\" stop-color=\"#FFF\" /><stop offset=\".626\" stop-color=\"#F8F9F9\" /><stop offset=\".951\" stop-color=\"#B2B4B6\" /></linearGradient><path d=\"M-157.1 405s.2-.8.2-1.1-.5 1.4-.3 2.2c0-.5.1-1.1.1-1.1z\" fill=\"url(#wikipedia_G)\" /><path d=\"M-190.7 354.4l.7.1c1.4-.4 2.6-.8 2.6-.8s1.3-.4 1.9-.6c.6-.2 1.1-.3 1.7-.4.6-.1 1.3-.1 1.7-.1.4 0 .5.1.5.1s.2.1.2.3c.1.1.7 1.9 3 2 2.2.1 2.3-1.1 2.1-1.5-.2-.4-.9-.9-.9-.9s-.9-.6-1.1-.8c-.2-.3 0-.4.1-.4s2.4-.5 2.7-.6l-.6-.2s-.1.1-.8.3c-.7.2-1.2.2-1.7.3-.5.1-.5.2-.5.2l-.1.1c0 .1-.1.3.4.6.5.4 1.2.8 1.4 1 .3.3.6.8 0 1.1-.3.2-.5.2-.8.3h-.8c-.5 0-.7-.1-1.1-.3-.4-.2-.8-.7-.9-1.1-.2-.4-.5-.7-.5-.7-.6-.3-1.7-.3-2.8-.1-1.1.2-2.7.7-2.9.8-.3.1-1.6.6-2.3.7-.7.2-1.2.4-1.6.5-.4.1-3.4 1-4.6 1.3-1.1.3-1.8.5-1.8.5-1.7.2-2.2-.1-2.2-.1-.3-.1-.3-.5-.3-.5v-1.1s0-.4-.4-.6c-.3-.2-.8-.3-1.6-.3s-1.7 0-2.1.1c-.4.1-1.2.3-1.8 1-.6.6-.5 1.1-.5 1.1v.2c.2.2.4.5.9.7 1 .5-1.1 1.3-1.1 1.3-.5.2-1.2.5-2.2.8-2.2.6-3.7.8-3.7.8l.7.3s5.5-1 7.1-2.6c0 0 .6-.3 0-.9-.6-.6-.9-.8-.9-.8s-.4-.2 0-.8c.4-.5.9-.8 1.4-.9.4-.1 1.8-.2 2.9-.1 0 0 .5 0 .5.4s-.1.9-.1 1c0 .2 0 .5.4.8.4.3 1.1.5 1.1.5s1.3.2 2.8-.2c1.6-.4 3.6-1.1 5.4-1.6l.5-.2z\" opacity=\".1\" fill=\"#232323\" /><linearGradient id=\"wikipedia_H\" gradientUnits=\"userSpaceOnUse\" x1=\"158.615\" y1=\"-89.399\" x2=\"247.586\" y2=\"-68.884\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#FFF\" /><stop offset=\".654\" stop-color=\"#FFF\" /><stop offset=\"1\" stop-color=\"#CBCCCE\" /></linearGradient><path d=\"M-162.4 363l.3.5c-1.1.5-4 1.3-4.3 1.4-.3.1-.2.2-.2.2 0 .1 1 1.1 1 1.1 1.2 1.2.5 2.3.5 2.3s-.9 1.3-2.8 1.1c-2-.2-2.6-1.8-2.7-2-.1-.3-.2-.8-.2-1.1 0-.3-.3-.3-.3-.3-1.1 0-2.9 1.1-2.9 1.1-.8.5-1.7 1.1-3.5 2-.9.4-1.7.7-2.3.9l-1-.2.1.5h-.1s-2.3.8-4.5 1.6c-2.3.7-3.7.8-3.7.8s-1.3.1-2.3-.3c-.9-.4-1-.9-.9-1.4 0-.5.5-1.4.6-2 .1-.6-.7-.6-.7-.6s-2-.2-3.7.3c-1.7.5-2.5 1.2-2.5 1.2-.9.5-.9 1-.9 1s0 .5.6.9 1.1.5 1.7.7c.7.1.8.3.8.3 1.1.9.4 1.8 0 2.4-.6 1.1-3.7 1.7-3.7 1.7-3.3.8-5.1 1.1-7.8 1.5l-.9-.5-.3.6c-7.1.9-10.1 1.9-11.1 2.1-1 .3-1.3.8-1.4.9-.1.1.1.2.1.2.4.1.6.4.6.4s1.4 1.7 0 3.1c-1.4 1.4-2.8 1.7-2.8 1.7s-2.2.7-4.1.3c-1.9-.4-2.4-1.9-2.4-2.4s.2-1.1.7-1.7c.5-.6.7-.7.7-.7s.4-.3.4-.4c.1-.2-.4-.2-.4-.2-1-.1-3.5-.1-5.8.1-1.4.1-2.8.4-3.6.5l-.2-.5-.5.6-3.1.5c-1.5.2-2.6 0-2.6 0s-1.3-.4-1.5-1.3c-.1-.9.4-1.9.5-2.2.1-.3.5-.9.5-.9s.1-.1.1-.3c0-.2-.2-.5-.2-.5s-.2-.4-.9-.4-.9.1-1.1.4l-.1.1c0-.1 0-.1.1-.2.2-.3.7-.7 1.4-.7s1 .2 1 .2c.7.8.1 1.8-.4 2.8-.1.1-.2.3-.2.5 0 .1-.1.2-.1.2-.4 1.1.3 1.6.7 1.7.4.1 1.1.6 4.3 0 3.1-.6 3.6-.7 3.6-.7s6.1-1.1 9-.4c0 0 1.3.4.3 1.3-1 1-1.7 1.6-1.5 2.4.2.8 1.3 1.9 3.6 1.6 0 0 .8-.1 1.1-.2 1.7-.3 2.9-1.3 2.9-1.3s1-.7.8-1.6c-.2-.9-1-1.2-1-1.2s-.7-.4-.1-1.2c0 0 .1-.7 2.6-1.3 2.4-.6 6.8-1.5 10.6-2 3.5-.4 9.7-1.6 10.9-2.1 1.2-.5 1.5-1.4 1.5-1.7 0-.3.1-.8-1.1-1.1-1.2-.3-1.8-.7-1.9-.8-.2-.1-.5-.5-.5-1.3s1.6-1.7 3.4-2.4c1.8-.6 3.9-.3 3.9-.3 1.9.2.9 2 .9 2-.1.3-.9 1.8.5 2.2 1.5.4 4.2-.3 5.2-.7.8-.3 3.1-1.1 4.7-1.6.4-.1.7-.2.9-.3 1.7-.6 3-1.2 3.8-1.7.8-.5 2.1-1.3 2.1-1.3s1.4-.7 1.8-.8c.5-.1 1.6-.3 1.8.8.2 1.1.6 1.9 1.4 2.3.8.4 2.1.5 3.2-.2 1.2-.8.4-1.9.4-1.9s0-.1-.1-.1c-.2-.3-.4-.5-.5-.6-.4-.5-.7-.8-.7-.8-.3-.4.1-.7.4-.8.4-.1 2.4-.8 2.4-.8 1.2-.4 1.6-.6 2.1-1 .4-.4-.2-1.3-.2-1.4l.6.3c.1.2.3.4.4.5 0 0 .2.5.1.8-.1.1-.3.3-.5.4l-.8-.6z\" fill=\"url(#wikipedia_H)\" /><path d=\"M-196.5 442.3c-.1-.1-.1-.1 0 0 0-.1.1-.1.1-.2 0 0-1.2-.1-2.1.1-1 .1-1.9.3-1.9.3l.3.1s.1-.1 1-.2 1.3-.1 1.3-.1.8-.1 1-.1c.2 0 .1.1.1.1s-.1.1.4.1c0 0 .7 0 1.3-.2-.2.1-1.3.3-1.5.1zm-3 .4s.1.3-2.9.4c0 0 1.8.1 3.3-.2 1.1-.2-.4-.2-.4-.2zm-41.4-82.8v.1l.1.1s.3-.5.2-.4c0 0-.1.2-.2.2l-.1.1v-.1zm-2.5 2.6s-.4.5 0 .5l.5-.5s.1-.2.1-.4c.1 0-.4.2-.6.4z\" opacity=\".1\" fill=\"#232323\" /><path d=\"M-232.9 373.7c1.2.1 1.5-.1 1.5-.2.3 0 1.5 0 2.9-.2 1.7-.2 3.6-.9 3.6-.9s1.6-.6 2.1-1.2c0 0-.7-.6-1.1-1.1 0 0-.3-.6 0-1 .3-.5.8-1 2.3-1.6 1.5-.6 2.4-.5 2.4-.5s.6 0 1 .4c.4.5.6 1 .6 1s0 .4-.1.6c-.1.3-.2.3-.2.3h.4c.3 0 1.2-.1 2.7-.5 1.5-.4 3.4-1 3.4-1s4.9-1.6 5.4-1.7c.5-.1 1.4-.4 1.4-.4v.1s.4.7.4 1.3v-.1s0 .3-.7.8-1.2.5-1.7.4c-.5 0-.7-.1-.8 0h-.7c-.8.1-1.2.4-1.2.4-1.8 1.1.7 9.3.7 9.3-3.7.5-8.1 1.4-10.6 2-2.4.6-2.6 1.3-2.6 1.3-.5.8.1 1.2.1 1.2s.8.3 1 1.2c.2.9-.8 1.6-.8 1.6s-1.2 1-2.9 1.3c-1.7.3-2.4.4-3.4-.5-.9-.7-.3-1.9.3-2.3.6-.4.9-.9 1-1.1s0-.4 0-.4l-.6-.5c-2-1.3-9.9.1-9.9.1-.2-1.2-.4-1.2-.3-3.1.1-1.2.3-1.8.3-1.8l.1-.2s.4-1.4 1.1-2.4c0 0 .6-.2 1.4-.3l1.5-.3z\" fill=\"#6B6B6B\" /><linearGradient id=\"wikipedia_I\" gradientUnits=\"userSpaceOnUse\" x1=\"-22.768\" y1=\"1549.871\" x2=\"9.619\" y2=\"1549.871\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#696969\" /><stop offset=\".37\" stop-color=\"#2E2E2E\" /><stop offset=\".455\" stop-color=\"#424242\" /><stop offset=\".601\" stop-color=\"#303030\" /><stop offset=\".695\" stop-color=\"#4A4A4A\" /><stop offset=\"1\" stop-color=\"#666\" /></linearGradient><path d=\"M-204.1 366.9s-4.1 1.3-3.9 1.3c0 0-.4.1-.7.2-.3.1-.5.2-.5.2s-3.3 1.2-6.4 1.8c-3.1.6-3-.4-2.7-.8.2-.4.8-1.1-.2-1.3-1-.1-1.8.3-2.2.4-.4.2-3.2 1.4-1.3 2.3 0 0 1.4.6-.4 1.8 0 0-1.8 1.2-5.4 1.8 0 0-.6.1-1.9.1-1.3 0-2.6.2-4.1.7-1.4.4-2 .6-2.7 1.1l.2-.5.2-.5c1.1-.5 3.7-1.3 5.7-1.4 2-.1 2.9-.2 4.7-.6 2.1-.5 2.7-1 2.9-1.2.2-.1.8-.5.5-.6-.4-.2-.9-.7-.9-.7-.2-.3-.4-.4-.2-1 .4-1 2.2-1.6 2.2-1.6s1-.5 2.3-.5c1.3 0 1.3.8 1.3.8s.1.3-.3.8c0 0-.5.6 0 .7.5.1 1.6.2 5.5-1s8.1-2.6 8.1-2.6.2.1.2.3z\" opacity=\".45\" fill=\"url(#wikipedia_I)\" /><linearGradient id=\"wikipedia_J\" gradientUnits=\"userSpaceOnUse\" x1=\"-22.377\" y1=\"1549.063\" x2=\"9.494\" y2=\"1549.063\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#525252\" /><stop offset=\".186\" stop-color=\"#333\" /><stop offset=\".354\" stop-color=\"#AEAEAE\" /><stop offset=\".42\" stop-color=\"#ADADAD\" /><stop offset=\".428\" stop-color=\"#9D9D9D\" /><stop offset=\".443\" stop-color=\"#818181\" /><stop offset=\".461\" stop-color=\"#6A6A6A\" /><stop offset=\".481\" stop-color=\"#585858\" /><stop offset=\".506\" stop-color=\"#4C4C4C\" /><stop offset=\".539\" stop-color=\"#444\" /><stop offset=\".617\" stop-color=\"#424242\" /><stop offset=\".668\" stop-color=\"#454545\" /><stop offset=\"1\" stop-color=\"#BDBDBD\" /></linearGradient><path d=\"M-222.9 371.3c-.5.6-2.1 1.2-2.1 1.2s-1.9.7-3.6.9c-1.6.2-2.8.2-2.8.2h-.1c-.2.1-.5.2-.7.2h-.8s-2.2.4-2.6.6c0 0-.3.4-.3.5-.1.1-.3.6-.3.6 1.1-.5 3.7-1.3 5.7-1.4 2-.1 2.9-.2 4.7-.6 2.1-.5 2.7-1 2.9-1.2.2-.1.8-.5.5-.6-.4-.2-.9-.7-.9-.7-.2-.3-.4-.4-.2-1 .4-1 2.2-1.6 2.2-1.6s1-.5 2.3-.5c1.3 0 1.3.8 1.3.8s.1.3-.3.8c0 0-.5.6 0 .7.5.1 1.6.2 5.5-1s8.1-2.6 8.1-2.6c-.1-.3-.3-.7-.3-.7s-.8.3-1.4.4c-.5.1-5.4 1.7-5.4 1.7s-1.9.6-3.4 1-2.3.5-2.7.5h-.4l.2-.3c.1-.2.1-.6.1-.6s-.2-.5-.6-1c-.4-.5-1-.5-1-.5s-.8-.1-2.4.5c-1.5.6-2 1.2-2.3 1.6-.3.5 0 1 0 1 .5.5 1.2 1.1 1.1 1.1\" fill=\"url(#wikipedia_J)\" /><linearGradient id=\"wikipedia_K\" gradientUnits=\"userSpaceOnUse\" x1=\"-17.084\" y1=\"1559.333\" x2=\"-18.113\" y2=\"1552.527\" gradientTransform=\"translate(-213.764 -1178.502)\"><stop offset=\"0\" stop-color=\"#969696\" /><stop offset=\"1\" /></linearGradient><path d=\"M-232.4 381.2s-.1-.3.2-.9c.2-.6.9-.6 1.4-.5.5.1.8.3 1.5-.1.6-.4.5-1.6 0-2.9-.4-1.3-.3-2.1-.3-2.1l-.6-.6-.2.7c0 1.3.7 3.2.8 3.8.2.5.3.8-.7.5-1-.3-1.5.1-1.5.1-1.3.9-1.1 2.2-1.1 2.2l.5-.2z\" opacity=\".2\" fill=\"url(#wikipedia_K)\" /><path d=\"M-226.5 386.6c-.3-1.8-.9-2.7-.9-2.7-.3.2-.5.7-.5.7s.2.2.5 1.6c0 0 .1.1.4.3.3.1.5.1.5.1zm5.7-3.7s-.8.9-.4 2.3c0 0 .5-.4.6-.7 0 0-.1-.5.1-1 0 0-.1-.4-.3-.6z\" opacity=\".5\" fill=\"#141414\" /><linearGradient id=\"wikipedia_L\" gradientUnits=\"userSpaceOnUse\" x1=\"174.78\" y1=\"-86.053\" x2=\"175.53\" y2=\"-78.469\" gradientTransform=\"matrix(1 0 0 -1 -406.164 295.68)\"><stop offset=\"0\" stop-color=\"#333\" /><stop offset=\".431\" /><stop offset=\"1\" stop-color=\"#2E2E2E\" /></linearGradient><path d=\"M-232.8 381.3c0-1.3.5-1.5.9-1.8.4-.3 1.3 0 1.3 0s.7.2 1-.1c.4-.3 0-1.5-.2-2.1-.2-.7-.4-1.6-.4-2.3 0-.5-.1-.7-.1-.8l-.2.6c0 1.3.7 3.2.8 3.8.2.5.3.8-.7.5-1-.3-1.5.1-1.5.1-1.3.9-1.1 2.2-1.1 2.2l.2-.1z\" opacity=\".18\" fill=\"url(#wikipedia_L)\" /><path d=\"M-227.8 384.3c0 .1.4.6.7 2.1.3.2.5.2.5.2-.3-1.8-.9-2.7-.9-2.7 0 .1-.2.2-.3.4zm7-1.4s-.8.9-.4 2.3c0 0 .1-.1.3-.2v-.1c-.3-1 .3-1.8.3-1.8-.1 0-.2-.1-.2-.2z\" opacity=\".3\" fill=\"#505050\" /><path d=\"M-236.8 358.2h.1c-.2.5-.8 1.1-1.1 1.6-.2.2-.3.6-.5.8.1.1.8-.1.9-.2h.1c0 .1-.5 1-.6 1.1.2 0 .5-.1.6-.2.4-.3.5-.9.8-1.3v-.2c-.2 0-.7 0-.9.2.1-.5.9-1.3 1.1-1.7.5-.6.9-1.3 1.3-1.9.2-.3.6-.6.8-.9.3-.4.6-.9.9-1.1v-.1h-.2c-.2.1-.7.2-.9.4 0 .1 0 .1.1.2-.1.4-.6.7-.8 1-.4.5-.8 1-1.1 1.5-.1.2-.2.4-.4.6-.2.2-.9.2-1.2.4h-.1c.1-.3.9-1.4 1.1-1.6-.4.1-.7.3-1 .5 0 .1 0 .1.1.1-.1.2-.4.4-.5.6-.2.3-.3.6-.5.9v.1c.6-.4 1.7-.7 1.9-.8zm34.7 5.3c.2.1.4.1.6.2h.4c0-.7-.4-.9-.6-1.3-.1-.2-.2-.5-.4-.7.1-.2.7-.3 1-.4.6-.2 1.4-.4 2-.6.3-.1.7-.1.9-.2.1 0 .2 0 .3.1.1.2.3 1.7.2 2.1-.4 1.7-.9 3-1.9 4 .4-.1.6-.4.8-.6 1.1-.8 1.8-2 2.1-3.4.2-.9-.1-1.7.2-2.5-.1-.2-1.1-.6-1.4-.6-.2.2-.4.4-.6.5-.4.2-.8.1-1.1.3-.3 0-.5-.6-.3-.8v-.2c-.2-.2-.8-.2-1.3-.2-.1.1-.3.1-.3.4v.1h.2c.4 0 .4.6.7.8v.1c-.2.1-1.3.5-1.5.5-.2 0-.4-.1-.6-.1-.3 0-.6.2-.8.3.1.2.4.1.6.3.3.6.5 1.3.8 1.9zm7.9-.5c.2.1.2.3.3.5l.6 1.2v.3c.1.3.4.3.6.4.2 0 .2-.1.3-.1-.1-.8-.5-1.4-.8-2-.1-.2-.2-.5-.2-.6 0-.1.1-.2 0-.3l-.2-.2c-.1 0 0 0 0-.1.1-.1.2-.3.3-.4.1-.3.1-.6.4-.8 0-.4-.6-.5-1.1-.4-.1 0-.2.1-.2.1l.2.2c.1 1.2-.7 2.2-1.2 2.9-.2.3-.6.5-.8.8.4 0 1.5-1.1 1.8-1.5zm-47.4 9.8h-.1c-.3.1-.8 1.4-1.3 1.1-.3 0-.3-.1-.5-.2 0-.4.7-1.1.9-1.2 0-.6.2-1.3.1-1.8h-.1c-.1 0-.3.2-.4.3l-.9.9c-.3 0-1.4 0-1.6.1h-.1c.1-.3.9-1.1.6-1.5v-.1c-.7 0-1.6 1.3-1.8 1.8-.1.3-.1.6-.3.8.5-.1 1.1-.1 1.6-.2.2 0 .5.1.6 0h.6c.1-.1.2-.2.3-.4.3-.3.8-.7 1-1.1h.1v.6c-.3.3-.8.7-.9 1.1v.3c-.2.9.2 1.3 1 1.3.5-.4 1.3-.8 1.2-1.8 0 0 0 .1 0 0zm-4.6-.7h-.2c.1-.4.5-.9 1.1-1v.2c-.2.2-.4.5-.6.7-.1.1-.2.1-.3.1zm85.2.2c-.2-.4-.3-.7-.5-1.1-.3-.6-.6-1.4-1.5-1.4-.2.2-.4.3-.6.6-.8 1.8.8 3.7 1.5 4.7.3.3.6.7.9.9-.1 1.4-1.3 1.8-2.5 1.3-.9-.4-1.6-1.2-2.2-2l-.7-.7c-.2-.2-.3-.5-.5-.7h-.1c.1.4.4.8.5 1.2.7 1.5 1.5 2.6 2.8 3.5.6.4 1.6 1.1 2.5.5 1.8-1.2 1.1-5.2.4-6.8zm-.1 1.9c-.1.1-.5-.4-.6-.5-.4-.4-1.3-1.2-.8-2h.2c.4.4.7.8 1 1.3.1.4.1.9.2 1.2 0 0 .1 0 0 0zm-26.2 7.9v-.4c.2-.8.1-1.8.3-2.6.2-1.1-.1-2.1 1-2.4 0-.1.1-.1 0-.2v-.1h-.1c-.3.2-1.1.4-1.5.5-.3.1-.6 0-.9.2h-.1v.2c.5.1.9 0 1.1.4.1.3.1 1.2 0 1.5-.3 1.2-.1 2.5-.4 3.6-.1.4 0 1.2-.2 1.5v.1c-.2-.1-.4-.4-.6-.6-.4-.5-.9-.8-1.2-1.3-.2-.3-.4-.6-.7-.8 0-.8.3-1.6.4-2.3.1-.5.1-1 .4-1.4.1-.2.5-.4.8-.5V377.2c-.5.1-1 .3-1.5.5-.5.1-.9.1-1.3.3v.3c1.4-.1 1.2.7.9 1.7-.1.3 0 .8-.2 1v.1c-.3-.4-.7-.9-1.1-1.2l-.4-.4c-.1-.1-.2-.3-.3-.4 0-.4.4-.5.7-.7 0-.2-.1-.2-.1-.3-1 .2-1.9.7-3.1.8v.3c.2 0 .6-.1.8 0 .4.1.8.6 1.1 1 .4.5 1 .9 1.4 1.5.2.3.4.6.7.8 0 .7-.2 1.4-.4 2.1-.1.3 0 .7-.2 1v.1c-.4-.7-1.1-1.3-1.6-1.9-.9-1.2-1.9-2.3-2.9-3.5 0-.2 0-.3.1-.4.1-.2.4-.4.6-.5V379.1c-.8.1-1.5.5-2.3.7-.4.1-.9.1-1.2.3h-.1c0 .2.1.2.1.3.3 0 .6-.1.9 0 .8.2 1.4 1.1 1.8 1.7.2.3.5.5.7.8.8 1.1 1.8 2.1 2.6 3.3.3.4.8.8 1.1 1.3.2 0 .2 0 .3-.1.2-.9.3-1.9.6-2.8.1-.4.3-.9.3-1.4.3.1.6.6.8.9.6.8 1.5 1.5 2.1 2.4.2 0 .2 0 .3-.1.2-1.6.3-2.9.5-4.3zm-62.4 6.8c0 2.5-.1 6.3 1.8 6.8.7.2 1.1-.3 1.3-.6.8-1.2.6-3.4-.2-4.4-.3 0-.8.8-1 1.1h-.1c-.1 0-.1-.1-.2-.1-.1-.9.1-1.8.2-2.7 1 .1 1.9.7 3 .8 0-.2 0-.4.1-.6v-.2c-.1-.1-.9-.3-1.2-.3.1-1.2-.2-2.1-1-2.4-.4-.1-.9-.2-1.3-.2-.2-.1-.3-.3-.5-.4-.1-.4-.1-.8.2-1 0-.1 0-.2-.1-.2-.1.2-.2.5-.3.8-.2 1 .3 1.8.9 2 .4.1.8.1 1.2.2.3.1.5.4.7.6 0 .5-.5.6-.9.4-.6-.2-1.3-.4-2-.6-.2-.1-.3-.2-.6-.2 0 .3-.1.5-.1.8.6.2 1.1.3 1.7.5 0 1.4-.6 3.1.1 4.2.1 0 .1 0 .2.1.8-.1.9-.7 1.3-1.1.3.8.1 2.3-.7 2.5-.3.2-.8-.1-1-.2-.6-.6-.8-1.5-1-2.5-.1-.3 0-1-.1-1.3-.2-.8-.1-1.6-.4-1.8zm95 6.6c-.1-.7.1-1.5-.1-2.1v-.6c-.1-.5-.1-1.1-.2-1.5-.2-.9 0-1.9-.4-2.7-.2 0-.4-.1-.7-.1-.1.1-.2.2-.2.3.1.4.5.4.7.8v.5c.1.6.1 1.3.2 1.9v.5c.1.3.2 1 .1 1.3-.1.4-.6.8-.9 1.1-.8.8-1.6 1.7-3 1.9v.1c0 .5.5.4.8.6h.2c.1-.1.2-.2.3-.4.2-.3.6-.4.8-.7v3.7h.1c.3-1.2.3-2.6.2-4 .5-.5.9-1.2 1.4-1.7v-.1 3.8c0 .4-.1 1.4 0 1.5v.2h.1c.1-.4.1-1 .2-1.5v-.7c.6-.5.5-1.5.4-2.1zm-71 2.6c-.3-.1-.8-.5-1-.8-.6-.9-1.3-2.9-.9-4.5.4-1.3 1.2-2.1 2.5-2.5.7-.2 1.4.1 1.8.3 1.2.6 1.7 1.5 2.1 3 .5 1.9-.1 3.6-1.4 4.2.1.8.2 1.5.2 2.3.4 0 .9-.1 1.2-.2.6-.2 1.3-.2 1.9-.3.4-.1 1.1 0 1.4-.2.1-.2-.2-1.4-.3-1.6-.1-.2 0-.5-.1-.6v-.2h-.3c0 1.2-.8 1-1.8 1.3-.5.1-1 .3-1.6.3v-.5c0-.1.7-.4.9-.5.5-.3.9-.8 1.2-1.3.2-.3.4-.8.5-1.1.1-.5.2-1.2 0-1.7-.1-.3 0-.6-.2-.9-.4-1.2-1.3-2.1-2.5-2.5-.5-.2-1.1-.2-1.7-.4-.5-.1-1.5.1-1.9.2-1.9.6-3.2 1.5-3.8 3.3-.2.7-.2 1.7 0 2.4.5 1.6 1.8 3 3.7 3 .1.1.1.3.1.4v.1c-.2.1-.4.1-.6.1-.5.1-2 .5-2.3.2-.2-.1-.4-.4-.4-.6h-.3c.1.8.3 1.5.4 2.3 1.4-.2 2.8-.5 4.2-.7-.2-.7-.4-1.5-.6-2.2.2-.1-.2 0-.4-.1zm67.7-4.4c.1.2.3.6.4.7.1.1.1 0 .2.1 1.3.1 1.8-2.1 1.3-3.4-.1-.2-.5-.9-.9-.6h-.1v-.1c0-.2 0-.3-.1-.4H-157.5c0 .2.1.2.1.5-.5.6-1.1 2-.6 3.2zm.4-2.1c.1-.2.3-.4.4-.5h.1c.3 0 .4.1.6.2.3.7.3 2-.2 2.5-.1.1-.2.1-.3.2-.8-.2-.9-1.7-.6-2.4zm-18.3 15.6c-.4-.3-.5-1.7-.7-2.3-.3-1.2-.5-2.5-.8-3.7-.2-.8-.5-1.6-.4-2.6.1-.1.2-.3.4-.4.2-.2.6-.2.8-.4v-.2c-.5.1-.9.4-1.3.5-.8.3-1.6.5-2.4.9-.3.1-.5.3-.8.3v.2h.1s1-.4 1.3-.1c.4.1.3.6.5.9-.1.6-.7 1.6-.9 2.1-.6 1.3-1.2 2.6-1.8 3.8-.2.5-.5 1.3-.9 1.7-.2-.3-.2-1.1-.3-1.5-.4-1.2-.6-2.6-1-3.8-.1-.2-.3-1.3-.2-1.5.1-.5.8-.8 1.3-1v-.3c-.7.1-1.4.5-2.1.7-.6.2-1.1.3-1.7.5-.3.1-.6.3-1 .3 0 .1 0 .2.1.2.2.1 1-.4 1.4-.1.6.2.6 1.1.8 1.7.5 1.6.7 3.3 1.2 4.9.1.4.4 1.7.1 2-.1.4-.9.6-1.3.8v.2c.6-.1 1.2-.4 1.7-.6 1.1-.4 2.1-.6 3.1-1v-.3c-.4.1-.8.2-1.4.2-.1-.1-.2-.1-.2-.2-.1-.2-.1-.4-.2-.6 0-.5.7-1.4.9-1.9.7-1.3 1.3-2.6 1.9-4 .2-.5.8-1.3.8-1.9.2.1.1.4.2.7.1.5.2 1 .4 1.5.3 1 .4 2.1.7 3.1.1.4.3 1 .1 1.5-.2.4-.8.7-1.3.8 0 .1 0 .2.1.2 0 0 .9-.3 1.1-.4 1.1-.5 2.2-1 3.4-1.4v-.3c-.7.6-1.3 1-1.7.8zm18.7 3.3c-.1.1-.4.2-.5.3-.5.4-1 1-1.4 1.5-.3.4-.5.8-.8 1.3-.1.2-.1.4-.3.6v.1c.3-.1.5-.3.8-.4.7-.4 1.2-.8 1.9-1.2.3-.2.5-.6.8-.8 0-.5.1-.8-.1-1.2-.1-.2-.2-.2-.4-.2zm-.5 1.4c-.2.2-.5.4-.7.6-.2.1-.5.2-.6.4.1-.4.8-1.1 1.1-1.3l.6-.3h.2l.1.1c-.2.3-.5.4-.7.5zm-85.5 1.6c-.2-.5-.3-1-.4-1.5-.1-.2-.1-.5-.2-.7v-.1c.3.1.7.1.9.2h.2c0-.2-.1-.6-.2-.7-.1-.2-.9-.2-1.1-.4-.3-.2-.6-.9-.8-1.3-.6-.9-1.3-1.8-2.1-2.5-.4-.3-.8-.7-1.5-.7-.1.1-.2.1-.3.2-.2.8.1 2.2.6 2.6v.1c-.2-.1-.4-.2-.5-.3 0 .2.1.5.2.7 0 .2.4.4.6.4.2 1 .6 2.1.9 3 .3.8.4 1.5.8 2.2.2.4.5.6.6 1h.1c-.1-.3-.3-.6-.4-.9-.4-.9-.7-1.8-1-2.7-.2-.6-.3-1.1-.5-1.7-.1-.2 0-.4-.2-.6.3 0 .4.2.6.3.5.2.9.3 1.4.5.4.1.8.3 1.2.4 0 .4.3 1.3.4 1.5v.1c-.6-.4-.6-1-1.7-.9l-.2.2c-.1.2-.1.6 0 .9.3.6 1.1 2 1.7 2.2.3.2.6 0 .8-.2.2.1.3.7.4 1 .2.6.5 1.3 1 1.5h.1c-.1-.4-.3-.9-.5-1.2-.3-.9-.6-1.8-.9-2.6zm-1.1-3.2c-.4 0-.8-.2-1.1-.3-.9-.3-1.7-.6-2.5-1-.1-.4-.8-1.6-.4-2.1l.1-.1h.1c1.2.1 2.4 1.6 3 2.5.3.2.5.7.8 1zm.6 3.4c-.1.1-.2.3-.4.4-.1.1-.2.1-.3.2-.7 0-.7-.7-1-1.1 0-.4.2-.4.3-.6h.2c.6 0 .8.3 1.1.5.1.2.1.3.1.6zm23.3 6.1c-.2-.3-.5-.3-.7-.6h-.1c.5-.3 1.1-.6 1.6-.8.1.2.8.8 1 .7h.1v-.7c-.5-.5-1.2-.9-2.1-1.1.1.3.4.5.6.7v.1c-.5.1-.9.3-1.3.4-.3.1-.6.1-.9.2h-.1c.2-.5.7-.9 1-1.3.6-.8 1-1.7 1.9-2.2 0-.4-1.1-1.1-1.5-.9l-.1.1c-.1.1.1.3.1.6-.1.3-.8 1.7-1 1.9-.4-.1-.7-.5-1.1-.7.1-.4.4-.6.6-.9.5-.7.8-1.3 1.5-1.8 0-.5-.9-1.1-1.4-1.1 0 .2.1.4.1.6-.1.6-.4 1.3-.7 1.9-.2.4-.2.8-.5 1.1-.1 0-.5 0-.6-.1h-.4v.1c.7.6 1.4.9 2.3 1.3-.1.7-.8 1.1-1.1 1.6-.2 0-.3 0-.4-.1h-.2c0 .6.5 1.1 1 1.2.3-.4.7-.5 1.2-.8.4.5.6 1.1.8 1.9.1.3 0 .7 0 1 .2.5.4.7.7 1h.3c.2-.9-.3-1.8-.5-2.6 0-.1-.1-.4-.1-.7zm62.5-6.7c-.2.2-.6.3-.8.5-.4.3-.8.7-1.1.9-.2.1-.4.3-.6.4-.2.3-.2.8-.4 1.1v.2c.3-.1.5-.5.7-.7.3-.2.6-.5.9-.8.2-.1.4-.2.6-.4.1 0 .1 0 .2.1 0 1-.5 1.7-.9 2.5-.1.2-.1.6-.3.7-.1.1-.2.1-.3.2-.3.3-.5.6-.8.9-.3.3-.4.8-.6 1.1v.3s.1.1.2.1c.5-.5 1-.9 1.4-1.5.7-.9 1-2 1.5-3.1.3-.7.7-1.4.7-2.3 0 0-.1-.1-.1-.2h-.3zm-2.8 6.3c0-.4.4-.6.6-.9h.1c-.1.3-.4.7-.7.9zm-59.1.6c-.1.3.8 1.1 1 1.3.1.1.3.3.5.2h.2c0-.1.1-.2 0-.4 0-.5-1.3-1-1.7-1.1zm3.8 3h.2c.1-.1.1-.3.2-.5.2-.2.6-.1.9-.2.8-.2 1.8-.2 2.6-.4.4-.1 1.1.2 1.5 0h.1c0-.5-1-.7-1.5-.6-.2.1-.5.2-.8.3h-.6c-.1-.6-.4-1.1-.4-1.8.6 0 1.3-.1 1.7-.3 0-.2 0-.2-.1-.3-.5-.1-1.2-.1-1.6.1h-.2c-.2-.3-.1-.9-.3-1.1v-.2c.4-.1 1.1-.2 1.3-.5v-.1l-.1-.1c-.6-.2-.9 0-1.4.2-.2-.5 0-1-.5-1.1.1-.2.5-.2.8-.3.4-.1.8-.3 1.1-.5v-.1c0-.2-.1-.2-.2-.3-.6 0-1 0-1.3.3h-.1c0-.3.2-.7.4-.9.1-.2.3-.1.4-.4-.1-.1-.2-.2-.2-.3-.2-.1-.5-.1-.6-.3-.3 0-.5 0-.7.1 0 .2.1.2.1.4.1.4-.3 1.7-.4 1.9-.1.2-1.6.7-1.9.6-.1 0-.4-.2-.4-.2v-.1c.6-.5 1-1.7 1.7-1.9v-.2c-.2-.2-1.1-1.2-1.6-.9h-.1c0 .3.2.6.1.9-.2.7-.6 1.6-.9 2.1-.2.4-.7.7-.7 1.2.6-.1.8-.7 1.3-.9l.4.4c.2.3.2.8.3 1.2.2.9.4 1.7.6 2.6 0 .4.1.8.1 1.3 0 .2.4.8.8.9zm1.2-3c0 .4.3 1.4.4 1.7v.1c-.5.1-1 .2-1.5.2-.1-.6-.4-1.1-.4-1.7.7 0 1-.2 1.5-.3zm-2.3-3.2c.1-.1 1.1-.3 1.2-.2.4.2.3.8.5 1.2-.1.2-1 .5-1.3.5 0-.5-.1-1.3-.4-1.5zm1.9 1.5c.1.4.2 1 .4 1.3-.1.3-1 .3-1.3.5-.1-.1-.3-1.1-.3-1.3.2-.1.9-.4 1.2-.5zm-6.9 2.2c-.1.1-.1.4-.1.5-.3.8-.5 1 .1 1.8.2 0 .3 0 .4-.1.1-.6.2-1.9-.4-2.2zm45.1.2c-1.2-.3-2.1.3-3.3.2-.1-.1-.2-.2-.3-.4-.8 0-1.8 1.9-.9 2.5.5.3 1.7.1 2.3 0 .3-.1.8-.1 1 0 .3.2.3 1.2.2 1.7-.1 1-.3 2-.4 2.9-.1.6-.2 1.2-.4 1.8.6 0 1.2-.6 1.3-1.1.1-.3 0-.5.1-.8.2-.8.2-1.8.4-2.7.1-.6 0-1.1.2-1.6.1-.4.1-1.7 0-2.1.1 0-.1-.2-.2-.4zm-54.1 12c-.1-.1-.2-.3-.4-.4l-1.5-1.2c-.4-.3-1-.5-1.4-.8 0-.1.1-.3 0-.5-.3-.9-1.6-1.9-2.4-2.4-.4-.2-1-.3-1.3-.6-.2 0-.4 0-.4.2-.1.2.2.5.3.7.3.4.6.8.9 1.1.3.2.6.4.8.6h.1c-.2-.4-.6-.7-.9-.9-.3-.2-.4-.6-.7-.9 0-.1 0-.1.1-.2 1.1 0 1.8 1 2.3 1.7.2.3.6.5.6 1h-.4c.2.5.8.5 1.3.8.9.5 1.6 1.4 2.4 2.1.3.2.7.5.8.9-.5 0-.9-.3-1.3-.6-.6-.4-1.6-1.1-2-1.7-.1-.1-.1-.3-.2-.4-.1-.1-.3-.1-.4-.3h-.2c0 .4.4.7.7.9.8.8 1.7 1.4 2.7 2 .4.2 1.1.5 1.5.3 0-.7-.7-1.1-1-1.4zm24.3 2.6c-2-1.4-5-2.8-8.4-2.7-.2.1-.5 0-.7.1-.3.1-.5.2-.7.4 0 1 1.4 1.5 2.3 1.7.5.1.9-.1 1.2-.2.2-.8-.8-.9-1.2-1.3h-.1c3-.1 5.3.7 7 2 .4.3.9.8 1.1 1.3.1.2.1.5 0 .7-.2.4-.7.4-1.2.5-1.2.3-2.8-.4-3.3-.9-.1.2 0 .5-.1.7-.2.5-.8.4-1.3.5-.9.2-2.4-.3-2.9-.6l-.4-.4v-.2c.1-.1.2-.2.2-.3 1.1-.1 1.7 0 2.4.6v.1c-.1.2-.2.2-.5.2v.1c.4 0 .6-.1.8-.2v-.2c-.1-.1-.2-.3-.4-.4-.6-.4-2-.6-2.7-.2-.1.6.2.9.6 1.1.6.5 1.2.8 2.1 1 .3.1.5 0 .9.1.3.1.8.1 1.1 0 .5-.1 1.2-.7.6-1.3.3.1.5.4.8.6.8.4 2 .7 3.2.5.6-.1 1.1-.1 1.3-.6.2-.3-.1-.7-.2-.8-.4-1-.9-1.5-1.5-1.9zm-7.3-1.8c.1.1.2.3.4.4v.2c-.3.7-1.7.2-2.1-.1-.1-.1-.2-.2-.2-.4v-.1c.1-.3.4-.2.7-.4.4.1.9.2 1.2.4zm36.7.4h-.4c-.3.2-.7.2-1 .4-.3.1-.6.3-.8.5-.2.1-.3.4-.5.6 0 .2 0 .2.2.3h.1l.1-.1v-.2c.4-.4.7-.6 1.2-.8.1-.1.4-.2.6-.1h.1c0 .4-.9 1.6-1.2 1.8v.1c.7-.2 1.2-1.6 1.7-2.2-.1-.2 0-.2-.1-.3zm-3.1 2.9c-.2.2-.8.2-1.1.4.1-.1.3-.2.4-.4.1-.1.1-.2.2-.3v-.2c-1.2-.2-3.1.8-3.7 1.3-.2.1-.2.3-.4.5v.2c.7 0 2-.4 2.2-.9v-.1c-.5 0-1.1.1-1.4.4.3-.4 1.2-.7 1.7-.9.2-.1.6-.1.7 0h.1c-.1.4-.7.8-1 .9v.1c.6-.1 1.2-.4 1.7-.6.4-.1.8-.2 1.1-.4.2-.1 1-1.2 1.1-1.5-1 .1-1.1 1-1.6 1.5zm-3.2.8v.1c-.1 0-.1.2-.2.2-.2.1-.5.1-.7.2h-.2c.2-.3.8-.5 1.1-.5zm-16.5 3.7v-.1c-1 0-2-.1-2.9-.1-.1.1-.3 0-.5.1s-.4.1-.6.2v.1c.2.2 1.6.2 1.9 0h.1v-.1c-.4-.1-1.2.2-1.5 0 1.1-.1 2.2 0 3.3 0-.1.1-.3.1-.4.1h-.1v.1c.2 0 .5.1.7.1-.3.2-1.3.1-1.6 0v-.1c-.2-.1-1 .1-1.1.1h-.4c-.2 0-.2 0-.3.1 0 .1 0 .1.1.2.3.1.7.1 1 .2-.1-.1-.6 0-.7-.1h-.1c.1-.1 1.4-.3 1.7-.1h.1c-.2 0-.4.1-.6.1v.1h.3c0 .1-.1.1-.1.2v.1c.6 0 1-.1 1.5-.2.3-.1.6.1.8-.1h.3v-.1c-.5 0-1.9-.1-2.2.2h-.1c.2-.2.5-.1.8-.2.4-.1 1.2-.3 1.5 0 .1.1 0 0 0 .1h.5v-.2c-.4-.1-.9-.3-1.2-.4.1-.1.1-.3-.2-.3zm-40.2-72.9c-.1.3-.3.6-.4.9-.3.6-.5 1.2-.8 1.8-.2.5-.3 1.3-.6 1.7v.1c.4-.1.7-.5.9-.8.6-.6 1.9-2.2 1.9-3.4-.1-.1-.1-.2-.2-.2-.1-.1-.4-.1-.8-.1zm.2 1.6c-.2.3-.3.6-.5.9-.2.3-.5.5-.6.7.1-.3.2-.5.3-.8.2-.6.4-1.1.7-1.6.2 0 .3 0 .4.1l.1.1c-.1.1-.3.5-.4.6zm70.2-12.1c-.4-.4-.7-.9-1.1-1.3-.2.1-.9.7-1 .9-.3-.1-.4-.4-.6-.5-.7-.5-1.3-1.2-2.5-1.1-.1.1-.4.1-.6.2-.5.2-1.1.7-1.3 1.2-.2.6 0 1.5.2 1.9.4.9 1 1.7 1.6 2.4.5.6 1 1.3 1.8 1.5 1 .2 1.4-.9 1.8-1.3.4-.4 1.2-.5 1.5-1.1.1-.2 0-.6 0-.8-.2-.4-1.1-1.6-1.4-1.9 0-.2.1-.2.2-.4.2.1.3.5.5.7.2.3.5.4.8.6.4 0 .6-.1.8-.3-.1-.4-.5-.5-.7-.7zm-2.2 4.2c-.7.2-1-.3-1.4-.7-.9-.9-1.6-2.1-2.3-3.2-.2-.4-.9-1.1-.6-1.7h.2c.2.3.5.5.8.8.6.8 1.3 1.5 1.9 2.3.4.5.8.9 1.1 1.4.2.2.3.6.6.8-.2.1-.3.2-.3.3zm.6-2.8c.3.4.8.7.8 1.5-.1.1-.2.2-.4.3h-.1c-.6-.9-1.4-1.7-2-2.6-.2-.3-.5-.5-.8-.8-.4-.5-.8-.9-1.2-1.3-.1-.1-.2-.3-.3-.4 0-.1 0-.1.1-.1.7 0 1 .5 1.4.8.9.8 1.7 1.7 2.5 2.6z\" opacity=\".88\" fill=\"#231F20\" /><radialGradient id=\"wikipedia_M\" cx=\"-2.191\" cy=\"1550.361\" r=\"72.751\" gradientTransform=\"translate(-213.764 -1178.502)\" gradientUnits=\"userSpaceOnUse\"><stop offset=\"0\" stop-opacity=\"0\" /><stop offset=\".802\" stop-opacity=\".08\" /><stop offset=\"1\" stop-opacity=\".388\" /></radialGradient><path d=\"M-204.1 367c0-.6-.4-1.3-.4-1.3v-.1s-.5-.9-1.3-1.2c-.8-.3-1.5.3-1.5.3s-.1.1-.4.5c-.3.4-.5.7-1.2.9-.7.3-1.4.2-1.7 0-.4-.2-.5-.5-.5-.5s-.2-.7-.3-1c-.1-.3-.3-1.7-.3-1.7s-.5-2.7-.5-3.3c0 0 1.5-.1 3.7-.8 2.3-.7 3-1.2 3-1.2s-.4-.2-.5-.7c-.1-.5-.1-1.2-.1-1.2s-.1-.5.5-1.1c.6-.6 1.4-.9 1.8-1 .4-.1 1.3-.2 2.1-.1.8 0 1.3.1 1.6.3.3.2.4.6.4.6v1.1s0 .4.3.5c0 0 .5.3 2.2.1 0 0 .7-.1 1.8-.5 1.1-.3 4.1-1.2 4.6-1.3.4-.1 1-.3 1.6-.5.7-.2 2-.6 2.3-.7.3-.1 1.8-.6 2.9-.8 1.1-.2 2.2-.2 2.8.1 0 0 .4.3.5.7.2.4.5.9.9 1.1.5.2.8.4 1.9.3 0 0 0-.1-.4-.4-.4-.3-1-.7-1-.7s-.3-.2-.4-.4c-.1-.2 0-.3 0-.3l.9-1.4s0-.2.5-.2c.5-.1 1.1-.1 1.7-.3.7-.2.8-.3.8-.3l.6.2s3.5 2.9 4.7 3.6l.2-.2s.4 0 .8.2 1 .6 1 .6 1.6 1.3 2.1 2.2l.2.7-.1.2s.9 1.3 2.1 2.6c0 0 1.2 1.7 1.7 2.1l-.2-.8.3-.2.2-.1.6.3c3.6 4.8 6.4 10.4 8.1 16.3l-.1.5.4.5c1.1 4.2 1.7 8.6 1.7 13.2 0 1.1 0 2.2-.1 3.3l-.3.5.2.6c-2.2 26.1-24.1 46.6-50.8 46.6-18.5 0-34.7-9.9-43.6-24.6l-.1-.4-.2-.2c-3.4-5.7-5.7-12.2-6.6-19.1l.2-.5-.3-.5c-.2-1.9-.3-3.8-.3-5.8 0-3 .3-5.9.7-8.8l.3-.6-.1-.3c1.2-6 3.4-11.7 6.5-16.8l.7-.4h.1s.2-.2.4-.2h.1s1.2-2 1.6-2.6c0 0 .5-.3.7-.4 0 0 .1 0 .2.1 0 0 .5-.4 1.7-2.1 0 0-.1-.1-.1-.2s.1-.6.2-.7c.1-.1.1-.2.1-.2s1.7-2 3.2-3.2c0 0 .3-.2.7-.3 0 0 1.5-.6 3.3-2.2 0 0 .1-.3.5-.9.4-.6 1.5-1.2 2.2-1.3.8-.2.9 0 .9 0l.1.1.5.8s.6-.3 1.4-.6c.8-.3 1-.3 1-.3l.8 1.3-1 2s-.6 1.4-1.7 2.2c0 0-.5.3-1.1.1s-1.1.3-1.1.3l-.2.1s.1 0 .3-.1c0 0 .2.1.3.2.1.2.9 1.2.9 1.2s0 .8-.4 1.9c-.4 1.1-1.5 2.9-1.5 2.9s-.7 1.4-1.1 2.3c-.3.8-.5 1.8-.5 2.3 0 0 .2.1.7-.2.7-.3 1.1 0 1.1 0s.7.5 1 .9c.3.3.8 1.8.2 3.2 0 0-.4 1-1.4 1.7 0 0-.2.3-1.5.2-.4 0-.6-.3-1.4-.2-.8.1-1.2.8-1.2.8-.7 1-1.2 2.5-1.2 2.5l-.1.2s-.2.5-.3 1.8c-.1 1.3.3 3.1.3 3.1s7.9-1.4 9.9-.1l.6.5v.4c-.1.2-.4.7-1 1.1-.6.4-1.2 1.6-.3 2.3 1 .8 1.7.8 3.4.5 1.7-.3 2.9-1.3 2.9-1.3s1-.7.8-1.6c-.2-.9-1-1.2-1-1.2s-.7-.4-.1-1.2c0 0 .1-.7 2.6-1.3 2.4-.6 6.8-1.5 10.6-2 0 0-2.5-8.2-.7-9.3 0 0 .4-.3 1.2-.4h1.5c.5 0 1 .1 1.7-.4.4-.6.4-.9.4-.9\" opacity=\".38\" fill=\"url(#wikipedia_M)\" /></symbol>"
});
var result = __WEBPACK_IMPORTED_MODULE_1_svg_sprite_loader_runtime_browser_sprite_build___default.a.add(symbol);
/* harmony default export */ __webpack_exports__["default"] = (symbol);

/***/ })
/******/ ]);