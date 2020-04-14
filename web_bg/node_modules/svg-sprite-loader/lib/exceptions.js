const { PACKAGE_NAME } = require('./config');

class LoaderException extends Error {
  constructor(message = '') {
    super(`${PACKAGE_NAME} exception. ${message}`);

    this.name = this.constructor.name;

    /* istanbul ignore else  */
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, this.constructor);
    } else {
      this.stack = (new Error(message)).stack;
    }
  }
}

class InvalidSvg extends LoaderException {
  constructor(content) {
    super(`\n\n${content}`);
  }
}

class ExtractPluginMissingException extends LoaderException {
  constructor() {
    super(`${PACKAGE_NAME} in extract mode requires the corresponding plugin`);
  }
}

class InvalidRuntimeException extends LoaderException {}

class RemainingLoadersInExtractModeException extends LoaderException {
  constructor() {
    super(`Some loaders will be applied after ${PACKAGE_NAME} in extract mode`);
  }
}

exports.LoaderException = LoaderException;
exports.InvalidSvg = InvalidSvg;
exports.ExtractPluginMissingException = ExtractPluginMissingException;
exports.InvalidRuntimeException = InvalidRuntimeException;
exports.RemainingLoadersInExtractModeException = RemainingLoadersInExtractModeException;
