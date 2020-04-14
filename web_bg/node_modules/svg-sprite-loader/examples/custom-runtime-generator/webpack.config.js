const path = require('path');
const merge = require('deepmerge');
const baseConfig = require('../base-webpack.config');

const babelOptions = {
  presets: ['react', 'es2015'],
  plugins: ['transform-object-rest-spread']
};

const config = merge(baseConfig, {
  context: __dirname,

  entry: './main.jsx',

  output: {
    path: path.resolve(__dirname, 'build')
  },

  module: {
    rules: [
      {
        test: /\.jsx$/,
        loader: 'babel-loader',
        options: babelOptions
      },
      {
        test: /\.svg$/,
        use: [
          {
            loader: 'babel-loader',
            options: babelOptions
          },
          {
            loader: 'svg-sprite-loader',
            options: {
              runtimeGenerator: require.resolve('./svg-to-icon-component-runtime-generator'),
              runtimeOptions: {
                iconModule: './icon.jsx' // Relative to current build context folder
              }
            }
          }
        ],
      }
    ]
  }
});

module.exports = config;
