const loaderDefaults = require('../config').loader;

/**
 * @param {string} content
 * @param {boolean} [esModule=false]
 * @return {string}
 */
function generateExport(content, esModule = loaderDefaults.esModule) {
  return esModule ?
    `export default ${content}` :
    `module.exports = ${content}`;
}

module.exports = generateExport;
