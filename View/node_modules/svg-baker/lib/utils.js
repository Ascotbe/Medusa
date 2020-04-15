const { interpolateName, getHashDigest } = require('loader-utils');

/**
 * @param {PostHTMLTree} tree
 * @return {Object} Node
 */
exports.getRoot = function getRoot(tree) {
  return tree.find(node => typeof node === 'object' && 'tag' in node);
};

/**
 * @param {string|Function} pattern
 * @param {string} resourcePath
 * @param {Object} [options]
 * @param {string} options.context
 * @param {string} options.content
 * @param {string} options.regExp
 */
exports.interpolate = function interpolate(pattern, resourcePath, options = null) {
  const opts = Object.assign({ context: process.cwd() }, options);

  return interpolateName({ resourcePath }, pattern, opts);
};

exports.getHash = function getHash(content) {
  return getHashDigest(content, 'md5', 'hex', 6);
};
