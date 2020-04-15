const path = require('path');
const merge = require('deepmerge');
const webpack = require('webpack');
const baseConfig = require('../base-webpack.config');
const SpritePlugin = require('../../plugin');

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
          // 'svg-sprite-loader',

          {
              loader: 'svg-sprite-loader',
              options: { extract: true, spriteFilename: 'dll.svg' }
          },
          'svgo-loader'
        ]
      }
    ]
  },

  plugins: [
    new webpack.DllPlugin({
      path: path.join(__dirname, 'build', '[name]-manifest.json'),
      name: 'dll'
    }),
    new SpritePlugin()
  ]
});
