"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _co = _interopRequireDefault(require("co"));

var fspp = _interopRequireWildcard(require("../fs-promise-proxy"));

var _commonActionUtils = require("./_common-action-utils");

var _commonActionInterfaceCheck = _interopRequireDefault(require("./_common-action-interface-check"));

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) { var desc = Object.defineProperty && Object.getOwnPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : {}; if (desc.get || desc.set) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } } newObj.default = obj; return newObj; } }

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

const doAppend = function* (data, cfg, plop, fileData) {
  const stringToAppend = yield (0, _commonActionUtils.getRenderedTemplate)(data, cfg, plop); // if the appended string should be unique (default),
  // remove any occurence of it (but only if pattern would match)

  if (cfg.unique !== false && new RegExp(cfg.pattern).test(fileData)) {
    // only remove after "pattern", so that we remove not too much accidentally
    const parts = fileData.split(cfg.pattern);
    const lastPart = parts[parts.length - 1];
    const lastPartWithoutDuplicates = lastPart.replace(new RegExp(stringToAppend, 'g'), '');
    fileData = fileData.replace(lastPart, lastPartWithoutDuplicates);
  }

  const {
    separator = '\n'
  } = cfg; // add the appended string to the end of the "fileData" if "pattern"
  // was not provided, i.e. null or false

  if (!cfg.pattern) {
    // make sure to add a "separator" if "fileData" is not empty
    if (fileData.length > 0) {
      fileData += separator;
    }

    return fileData + stringToAppend;
  }

  return fileData.replace(cfg.pattern, '$&' + separator + stringToAppend);
};

var _default = _co.default.wrap(function* (data, cfg, plop) {
  const interfaceTestResult = (0, _commonActionInterfaceCheck.default)(cfg);

  if (interfaceTestResult !== true) {
    throw interfaceTestResult;
  }

  const fileDestPath = (0, _commonActionUtils.makeDestPath)(data, cfg, plop);

  try {
    // check path
    const pathExists = yield fspp.fileExists(fileDestPath);

    if (!pathExists) {
      throw 'File does not exists';
    } else {
      let fileData = yield fspp.readFile(fileDestPath);
      fileData = yield doAppend(data, cfg, plop, fileData);
      yield fspp.writeFile(fileDestPath, fileData);
    }

    return (0, _commonActionUtils.getRelativeToBasePath)(fileDestPath, plop);
  } catch (err) {
    (0, _commonActionUtils.throwStringifiedError)(err);
  }
});

exports.default = _default;