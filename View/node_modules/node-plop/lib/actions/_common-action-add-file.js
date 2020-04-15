"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = addFile;

var _path = _interopRequireDefault(require("path"));

var _del = _interopRequireDefault(require("del"));

var _commonActionUtils = require("./_common-action-utils");

var _isbinaryfile = _interopRequireDefault(require("isbinaryfile"));

var fspp = _interopRequireWildcard(require("../fs-promise-proxy"));

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) { var desc = Object.defineProperty && Object.getOwnPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : {}; if (desc.get || desc.set) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } } newObj.default = obj; return newObj; } }

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function* addFile(data, cfg, plop) {
  const fileDestPath = (0, _commonActionUtils.makeDestPath)(data, cfg, plop);
  const {
    force,
    skipIfExists = false
  } = cfg;

  try {
    // check path
    let destExists = yield fspp.fileExists(fileDestPath); // if we are forcing and the file already exists, delete the file

    if (force === true && destExists) {
      yield (0, _del.default)([fileDestPath]);
      destExists = false;
    } // we can't create files where one already exists


    if (destExists) {
      if (skipIfExists) {
        return `[SKIPPED] ${fileDestPath} (exists)`;
      }

      throw `File already exists\n -> ${fileDestPath}`;
    } else {
      yield fspp.makeDir(_path.default.dirname(fileDestPath));
      const absTemplatePath = cfg.templateFile && _path.default.resolve(plop.getPlopfilePath(), cfg.templateFile) || null;

      if (absTemplatePath != null && _isbinaryfile.default.sync(absTemplatePath)) {
        const rawTemplate = yield fspp.readFileRaw(cfg.templateFile);
        yield fspp.writeFileRaw(fileDestPath, rawTemplate);
      } else {
        const renderedTemplate = yield (0, _commonActionUtils.getRenderedTemplate)(data, cfg, plop);
        yield fspp.writeFile(fileDestPath, renderedTemplate);
      } // keep the executable flags


      if (absTemplatePath != null) {
        const sourceStats = yield fspp.stat(absTemplatePath);
        const destStats = yield fspp.stat(fileDestPath);
        const executableFlags = sourceStats.mode & (fspp.constants.S_IXUSR | fspp.constants.S_IXGRP | fspp.constants.S_IXOTH);
        yield fspp.chmod(fileDestPath, destStats.mode | executableFlags);
      }
    } // return the added file path (relative to the destination path)


    return (0, _commonActionUtils.getRelativeToBasePath)(fileDestPath, plop);
  } catch (err) {
    (0, _commonActionUtils.throwStringifiedError)(err);
  }
}