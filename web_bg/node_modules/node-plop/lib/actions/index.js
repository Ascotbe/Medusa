"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
Object.defineProperty(exports, "add", {
  enumerable: true,
  get: function () {
    return _add.default;
  }
});
Object.defineProperty(exports, "addMany", {
  enumerable: true,
  get: function () {
    return _addMany.default;
  }
});
Object.defineProperty(exports, "modify", {
  enumerable: true,
  get: function () {
    return _modify.default;
  }
});
Object.defineProperty(exports, "append", {
  enumerable: true,
  get: function () {
    return _append.default;
  }
});

var _add = _interopRequireDefault(require("./add"));

var _addMany = _interopRequireDefault(require("./addMany"));

var _modify = _interopRequireDefault(require("./modify"));

var _append = _interopRequireDefault(require("./append"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }