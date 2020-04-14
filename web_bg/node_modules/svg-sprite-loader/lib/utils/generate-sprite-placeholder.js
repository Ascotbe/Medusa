/**
 * Because of extract-text-webpack-plugin interop returns just absolute path to filepath
 * @param {string} filepath
 * @return {string}
 */
function generateSpritePlaceholder(filepath) {
  return filepath;
}

module.exports = generateSpritePlaceholder;
