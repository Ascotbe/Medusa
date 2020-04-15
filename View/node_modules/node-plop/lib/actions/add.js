"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _co = _interopRequireDefault(require("co"));

var _commonActionInterfaceCheck = _interopRequireDefault(require("./_common-action-interface-check"));

var _commonActionAddFile = _interopRequireDefault(require("./_common-action-add-file"));

var _commonActionUtils = require("./_common-action-utils");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var _default = _co.default.wrap(function* (data, cfg, plop) {
  const interfaceTestResult = (0, _commonActionInterfaceCheck.default)(cfg);

  if (interfaceTestResult !== true) {
    throw interfaceTestResult;
  }

  cfg.templateFile = (0, _commonActionUtils.getRenderedTemplatePath)(data, cfg, plop);
  return yield (0, _commonActionAddFile.default)(data, cfg, plop);
});

exports.default = _default;