const { interpolateName } = require('loader-utils');

/**
 * @param {string} pattern
 * @param {Object} options
 * @param {string} options.resourcePath
 * @param {string} [options.context]
 * @param {string} [options.content]
 */
function interpolate(pattern, options) {
  const { resourcePath, context, content } = options;
  return interpolateName({ resourcePath }, pattern, { context, content });
}

module.exports = interpolate;
