"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _co = _interopRequireDefault(require("co"));

var _path = _interopRequireDefault(require("path"));

var _fs = _interopRequireDefault(require("fs"));

var _globby = _interopRequireDefault(require("globby"));

var _commonActionInterfaceCheck = _interopRequireDefault(require("./_common-action-interface-check"));

var _commonActionAddFile = _interopRequireDefault(require("./_common-action-add-file"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

const defaultConfig = {
  verbose: true
};

var _default = _co.default.wrap(function* (data, userConfig, plop) {
  // shallow-merge default config and input config
  const cfg = Object.assign({}, defaultConfig, userConfig); // check the common action interface attributes. skip path check because it's NA

  const interfaceTestResult = (0, _commonActionInterfaceCheck.default)(cfg, {
    checkPath: false
  });

  if (interfaceTestResult !== true) {
    throw interfaceTestResult;
  } // check that destination (instead of path) is a string value


  const dest = cfg.destination;

  if (typeof dest !== 'string' || dest.length === 0) {
    throw `Invalid destination "${dest}"`;
  }

  if (cfg.base) {
    cfg.base = plop.renderString(cfg.base, data);
  }

  if (typeof cfg.templateFiles === 'function') {
    cfg.templateFiles = cfg.templateFiles();
  }

  cfg.templateFiles = [].concat(cfg.templateFiles) // Ensure `cfg.templateFiles` is an array, even if a string is passed.
  .map(file => plop.renderString(file, data)); // render the paths as hbs templates

  const templateFiles = resolveTemplateFiles(cfg.templateFiles, cfg.base, cfg.globOptions, plop);
  const filesAdded = [];

  for (let templateFile of templateFiles) {
    const absTemplatePath = _path.default.resolve(plop.getPlopfilePath(), templateFile);

    const fileCfg = Object.assign({}, cfg, {
      path: resolvePath(cfg.destination, templateFile, cfg.base),
      templateFile: absTemplatePath
    });
    const addedPath = yield (0, _commonActionAddFile.default)(data, fileCfg, plop);
    filesAdded.push(addedPath);
  }

  const summary = `${filesAdded.length} files added`;
  if (!cfg.verbose) return summary;else return `${summary}\n -> ${filesAdded.join('\n -> ')}`;
});

exports.default = _default;

function resolveTemplateFiles(templateFilesGlob, basePath, globOptions, plop) {
  globOptions = Object.assign({
    cwd: plop.getPlopfilePath()
  }, globOptions);
  return _globby.default.sync(templateFilesGlob, Object.assign({
    nobrace: true
  }, globOptions)).filter(isUnder(basePath)).filter(isAbsoluteOrRelativeFileTo(plop.getPlopfilePath()));
}

function isAbsoluteOrRelativeFileTo(relativePath) {
  const isFile = file => _fs.default.existsSync(file) && _fs.default.lstatSync(file).isFile();

  return file => isFile(file) || isFile(_path.default.join(relativePath, file));
}

function isUnder(basePath = '') {
  return path => path.startsWith(basePath);
}

function resolvePath(destination, file, rootPath) {
  return toUnix(_path.default.join(destination, dropFileRootPath(file, rootPath)));
}

function toUnix(path) {
  return !path.sep || path.sep === '\\' ? path.replace(/\\/g, '/') : path;
}

function dropFileRootPath(file, rootPath) {
  return rootPath ? file.replace(rootPath, '') : dropFileRootFolder(file);
}

function dropFileRootFolder(file) {
  const fileParts = _path.default.normalize(file).split(_path.default.sep);

  fileParts.shift();
  return fileParts.join(_path.default.sep);
}