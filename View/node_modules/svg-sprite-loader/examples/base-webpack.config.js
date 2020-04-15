const path = require('path');
const packageName = require('../package.json').name;
const { getWebpackVersion } = require('../lib/utils');

const webpackVersion = getWebpackVersion();

const config = {
  output: {
    filename: '[name].js'
  },

  devtool: false,

  resolve: {
    alias: {
      [packageName]: path.resolve(__dirname, '..')
    }
  },

  resolveLoader: {
    alias: {
      [packageName]: path.resolve(__dirname, '..')
    }
  }
};

if (webpackVersion >= 4) {
  config.mode = 'development';
}

module.exports = config;
