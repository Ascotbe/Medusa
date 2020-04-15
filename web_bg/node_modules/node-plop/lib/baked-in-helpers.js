"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _changeCase = _interopRequireDefault(require("change-case"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var _default = {
  camelCase: _changeCase.default.camel,
  snakeCase: _changeCase.default.snake,
  dotCase: _changeCase.default.dot,
  pathCase: _changeCase.default.path,
  lowerCase: _changeCase.default.lower,
  upperCase: _changeCase.default.upper,
  sentenceCase: _changeCase.default.sentence,
  constantCase: _changeCase.default.constant,
  titleCase: _changeCase.default.title,
  dashCase: _changeCase.default.param,
  kabobCase: _changeCase.default.param,
  kebabCase: _changeCase.default.param,
  properCase: _changeCase.default.pascal,
  pascalCase: _changeCase.default.pascal
};
exports.default = _default;