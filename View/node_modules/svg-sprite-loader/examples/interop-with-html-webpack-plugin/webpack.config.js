/* eslint-disable import/no-extraneous-dependencies */
const path = require('path');
const merge = require('deepmerge');
const baseConfig = require('../base-webpack.config');
const SpritePlugin = require('../../plugin');
const HtmlPlugin = require('html-webpack-plugin');

const config = merge(baseConfig, {
  context: __dirname,

  entry: './main',

  output: {
    path: path.resolve(__dirname, 'build')
  },

  module: {
    rules: [
      {
        test: /\.svg$/,
        loader: 'svg-sprite-loader',
        options: { extract: true }
      }
    ]
  },

  plugins: [
    new HtmlPlugin({
      filename: 'index.html',
      template: path.resolve(__dirname, 'template.ejs')
    }),

    new SpritePlugin({
      plainSprite: true
    })
  ]
});

module.exports = config;
