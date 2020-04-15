const stringifiedRegexp = /^'|".*'|"$/;

/**
 * If already stringified - return original content
 * @param {Object|Array} content
 * @return {string}
 */
function stringify(content) {
  if (typeof content === 'string' && stringifiedRegexp.test(content)) {
    return content;
  }
  return JSON.stringify(content, null, 2);
}

module.exports = stringify;
