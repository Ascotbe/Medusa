const {CleanWebpackPlugin} = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const ProgressBarPlugin = require('progress-bar-webpack-plugin');
const {BundleAnalyzerPlugin} = require('webpack-bundle-analyzer');
const CopyPlugin = require('copy-webpack-plugin');
const path = require('path');
const merge = require('webpack-merge');
const baseConfig = require('./webpack.base.config');

const resolve = dir => path.resolve(__dirname, dir);
const analyzerPlugins = process.env.analyzer==='1'?[new BundleAnalyzerPlugin({analyzerPort:5555})]:[];

const devConfig = {
    mode: 'production',
    entry: {
        simple: resolve('../src/simple.js'),
        pro: resolve('../src/pro.js'),
        preview: resolve('../src/preview.js')
    },
    output: {
        path: resolve('../dist/'),
        filename: '[name].js',
        libraryTarget: 'umd',
        libraryExport: 'default',
        library: 'makdown',
        umdNamedDefine: true,
        globalObject: 'typeof self !== \'undefined\' ? self : this'
    },
    plugins: [
        ...analyzerPlugins,
        new CleanWebpackPlugin(),
        new ProgressBarPlugin({
            width: 100,
            clear: false
        }),
        new CopyPlugin([
            {from: resolve('../index.js'), to: resolve('../dist/')}
        ]),
    ],
    performance: {
        hints: false
    }
};

module.exports = merge(baseConfig, devConfig);
