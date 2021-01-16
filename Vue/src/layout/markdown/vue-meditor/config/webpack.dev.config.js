const webpack = require('webpack');
var HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');
const merge = require('webpack-merge');
const baseConfig = require('./webpack.base.config');
const resolve = dir => path.resolve(__dirname, dir)

const devConfig = {
    mode: 'development',
    devtool: 'cheap-module-eval-source-map',
    devServer: {
        // open: true,
        hot: true,
        hotOnly: true
    },
    resolve: {
        extensions: ['.js', '.vue', '.json'],
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        }
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: resolve('../index.dev.html')
        }),
        new webpack.HotModuleReplacementPlugin()
    ]
};
module.exports = merge(baseConfig, devConfig);
