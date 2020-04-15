const path = require('path');
const merge = require('deepmerge');
const baseConfig = require('../base-webpack.config');
const SpritePlugin = require('../../plugin');

const config = merge(baseConfig, {
  context: __dirname,

  entry: './main',

  output: {
    path: path.resolve(__dirname, 'build'),
    publicPath: 'build/'
  },

  module: {
    rules: [
      {
        test: /\.svg$/,
        loader: 'svg-sprite-loader',
        options: {
          extract: true,
          runtimeGenerator: require.resolve('./extracting-runtime-generator.js')
        }
      }
    ]
  },
  plugins: [
    new SpritePlugin()
  ]
});

module.exports = config;
