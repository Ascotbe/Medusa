"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.getRenderedTemplatePath = getRenderedTemplatePath;
exports.getTemplate = getTemplate;
exports.getRenderedTemplate = getRenderedTemplate;
exports.throwStringifiedError = exports.getRelativeToBasePath = exports.makeDestPath = void 0;

var _path = _interopRequireDefault(require("path"));

var fspp = _interopRequireWildcard(require("../fs-promise-proxy"));

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) { var desc = Object.defineProperty && Object.getOwnPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : {}; if (desc.get || desc.set) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } } newObj.default = obj; return newObj; } }

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

const getFullData = (data, cfg) => Object.assign({}, cfg.data, data);

const makeDestPath = (data, cfg, plop) => _path.default.resolve(plop.getDestBasePath(), plop.renderString(cfg.path || '', getFullData(data, cfg)));

exports.makeDestPath = makeDestPath;

function getRenderedTemplatePath(data, cfg, plop) {
  if (cfg.templateFile) {
    const absTemplatePath = _path.default.resolve(plop.getPlopfilePath(), cfg.templateFile);

    return plop.renderString(absTemplatePath, getFullData(data, cfg));
  }

  return null;
}

function* getTemplate(data, cfg, plop) {
  const makeTmplPath = p => _path.default.resolve(plop.getPlopfilePath(), p);

  let {
    template
  } = cfg;

  if (cfg.templateFile) {
    template = yield fspp.readFile(makeTmplPath(cfg.templateFile));
  }

  if (template == null) {
    template = '';
  }

  return template;
}

function* getRenderedTemplate(data, cfg, plop) {
  const template = yield getTemplate(data, cfg, plop);
  return plop.renderString(template, getFullData(data, cfg));
}

const getRelativeToBasePath = (filePath, plop) => filePath.replace(_path.default.resolve(plop.getDestBasePath()), '');

exports.getRelativeToBasePath = getRelativeToBasePath;

const throwStringifiedError = err => {
  if (typeof err === 'string') {
    throw err;
  } else {
    throw err.message || JSON.stringify(err);
  }
};

exports.throwStringifiedError = throwStringifiedError;