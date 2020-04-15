const path = require('path');
const merge = require('deepmerge');
const baseConfig = require('../base-webpack.config');

module.exports = merge(baseConfig, {
  context: __dirname,

  entry: './main',

  output: {
    path: path.resolve(__dirname, 'build')
  },

  module: {
    rules: [
      {
        test: /\.svg$/,
        use: [
          'svg-sprite-loader',
          'svgo-loader'
        ]
      }
    ]
  }
});
