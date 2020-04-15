const path = require('path');
const webpack = require('webpack');
const merge = require('deepmerge');
const baseConfig = require('../base-webpack.config');

module.exports = merge(baseConfig, {
  context: __dirname,

  entry: {
    dll: ['./dll']
  },

  output: {
    path: path.resolve(__dirname, 'build'),
    library: 'dll'
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
  },

  plugins: [
    new webpack.DllPlugin({
      path: path.join(__dirname, 'build', '[name]-manifest.json'),
      name: 'dll'
    })
  ]
});
