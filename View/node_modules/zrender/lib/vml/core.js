var env = require("../core/env");

var urn = 'urn:schemas-microsoft-com:vml';
var win = typeof window === 'undefined' ? null : window;
var vmlInited = false;
var doc = win && win.document;

function createNode(tagName) {
  return doCreateNode(tagName);
} // Avoid assign to an exported variable, for transforming to cjs.


var doCreateNode;

if (doc && !env.canvasSupported) {
  try {
    !doc.namespaces.zrvml && doc.namespaces.add('zrvml', urn);

    doCreateNode = function (tagName) {
      return doc.createElement('<zrvml:' + tagName + ' class="zrvml">');
    };
  } catch (e) {
    doCreateNode = function (tagName) {
      return doc.createElement('<' + tagName + ' xmlns="' + urn + '" class="zrvml">');
    };
  }
} // From raphael


function initVML() {
  if (vmlInited || !doc) {
    return;
  }

  vmlInited = true;
  var styleSheets = doc.styleSheets;

  if (styleSheets.length < 31) {
    doc.createStyleSheet().addRule('.zrvml', 'behavior:url(#default#VML)');
  } else {
    // http://msdn.microsoft.com/en-us/library/ms531194%28VS.85%29.aspx
    styleSheets[0].addRule('.zrvml', 'behavior:url(#default#VML)');
  }
}

exports.doc = doc;
exports.createNode = createNode;
exports.initVML = initVML;