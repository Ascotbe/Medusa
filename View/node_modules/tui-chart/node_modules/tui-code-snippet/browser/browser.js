/**
 * @fileoverview This module detects the kind of well-known browser and version.
 * @author NHN FE Development Lab <dl_javascript@nhn.com>
 */

'use strict';

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
