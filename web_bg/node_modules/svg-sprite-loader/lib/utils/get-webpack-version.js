// eslint-disable-next-line import/no-extraneous-dependencies
const webpackVersion = require('webpack/package.json').version;

/**
 * @param {boolean} [onlyMajor=true]
 * @return {string}
 */
function getWebpackVersion(onlyMajor = true) {
  return onlyMajor ? webpackVersion.split('.')[0] : webpackVersion;
}

getWebpackVersion.IS_1 = getWebpackVersion() === '1';
getWebpackVersion.IS_2 = getWebpackVersion() === '2';
getWebpackVersion.IS_3 = getWebpackVersion() === '3';
getWebpackVersion.IS_4 = getWebpackVersion() === '4';

module.exports = getWebpackVersion;
