const path = require('path');
const merge = require('deepmerge');
const baseConfig = require('../base-webpack.config');
const SpritePlugin = require('../../plugin');

module.exports = merge(baseConfig, {
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
        use: [
          {
            loader: 'svg-sprite-loader',
            options: {
              extract: true,
              publicPath: '/static/'
            }
          },
          'svgo-loader'
        ]
      }
    ]
  },

  plugins: [
    new SpritePlugin()
  ]
});
