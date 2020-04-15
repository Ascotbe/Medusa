// eslint-disable-next-line import/no-extraneous-dependencies
const webpackPkg = require('webpack/package.json');

const webpackMajorVersion = parseInt(webpackPkg.version.split('.')[0], 10);

module.exports = webpackMajorVersion === 1;
