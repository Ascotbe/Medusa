var _config = require("../config");

var debugMode = _config.debugMode;

var log = function () {};

if (debugMode === 1) {
  log = function () {
    for (var k in arguments) {
      throw new Error(arguments[k]);
    }
  };
} else if (debugMode > 1) {
  log = function () {
    for (var k in arguments) {
      console.log(arguments[k]);
    }
  };
}

var _default = log;
module.exports = _default;