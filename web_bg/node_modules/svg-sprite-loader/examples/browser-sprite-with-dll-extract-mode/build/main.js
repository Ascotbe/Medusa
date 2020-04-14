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
/******/ 	__webpack_require__.p = "build/";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__assets_twitter_svg__ = __webpack_require__(1);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__dll__ = __webpack_require__(2);



// => {id string, width: string, height: string, viewBox: string, url: string}

console.log(`main: ${__WEBPACK_IMPORTED_MODULE_0__assets_twitter_svg__["a" /* default */]}`);

window.addEventListener('DOMContentLoaded', () => {
  const image = `<img width="${__WEBPACK_IMPORTED_MODULE_0__assets_twitter_svg__["a" /* default */].width}" height="${__WEBPACK_IMPORTED_MODULE_0__assets_twitter_svg__["a" /* default */].height}" src="${__WEBPACK_IMPORTED_MODULE_0__assets_twitter_svg__["a" /* default */].url}">`;
  const usage = `<svg viewBox="${__WEBPACK_IMPORTED_MODULE_0__assets_twitter_svg__["a" /* default */].viewBox}"><use xlink:href="${__WEBPACK_IMPORTED_MODULE_0__assets_twitter_svg__["a" /* default */].url}"></use></svg>`;

  document.body.insertAdjacentHTML('beforeend', `${image} ${usage}`);

  Object(__WEBPACK_IMPORTED_MODULE_1__dll__["a" /* dll */])();
});


/***/ }),
/* 1 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony default export */ __webpack_exports__["a"] = ({
      id: "twitter-usage",
      viewBox: "0 0 273.4 222.2",
      url: __webpack_require__.p + "sprite.svg#twitter-usage",
      toString: function () {
        return this.url;
      }
    });

/***/ }),
/* 2 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = dll;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__assets_facebook_svg__ = __webpack_require__(3);


// => {id string, width: string, height: string, viewBox: string, url: string}

console.log(`dll: ${__WEBPACK_IMPORTED_MODULE_0__assets_facebook_svg__["a" /* default */]}`);
let image;
let usage;

window.addEventListener('DOMContentLoaded', () => {
  image = `<img width="${__WEBPACK_IMPORTED_MODULE_0__assets_facebook_svg__["a" /* default */].width}" height="${__WEBPACK_IMPORTED_MODULE_0__assets_facebook_svg__["a" /* default */].height}" src="${__WEBPACK_IMPORTED_MODULE_0__assets_facebook_svg__["a" /* default */].url}">`;
  usage = `<svg viewBox="${__WEBPACK_IMPORTED_MODULE_0__assets_facebook_svg__["a" /* default */].viewBox}"><use xlink:href="${__WEBPACK_IMPORTED_MODULE_0__assets_facebook_svg__["a" /* default */].url}"></use></svg>`;
});

function dll() {
  console.log('dll module');

  document.body.insertAdjacentHTML('beforeend', `${image} ${usage}`);
}


/***/ }),
/* 3 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony default export */ __webpack_exports__["a"] = ({
      id: "facebook-usage",
      viewBox: "0 0 1000 1000",
      url: __webpack_require__.p + "sprite.svg#facebook-usage",
      toString: function () {
        return this.url;
      }
    });

/***/ })
/******/ ]);