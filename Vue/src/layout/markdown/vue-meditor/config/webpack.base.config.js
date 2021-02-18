const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const resolve = dir => path.resolve(__dirname, dir)

const config = {
    entry: resolve('../main.js'),
    output: {
        path: resolve('../dist/'),
        filename: 'simple.js'
    },
    module: {
        rules: [{
            test: /\.(js|vue)$/,
            loader: 'eslint-loader',
            enforce: 'pre',
            include: [resolve('src'), resolve('test')]
        }, {
            test: /\.vue$/,
            loader: 'vue-loader'
        },
            {
                test: /\.js$/,
                use: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.(css|less)$/,
                use: [
                    'vue-style-loader',
                    'css-loader',
                    'less-loader'
                ]
            },
            {
                test: /\.(jpg|png|jpeg)$/,
                use: {
                    loader: 'url-loader',
                    options: {
                        // placeholder
                        name: '[name]_[hash].[ext]',
                        outputPath: 'img/',
                        limit: 4096
                    }
                }
            },
            {
                test: /\.(woff2?|eot|ttf|otf|dtd|svg)(\?.*)?$/,
                loader: 'url-loader',
                options: {
                    limit: 10240,
                    name: 'fonts/[name].[hash:7].[ext]'
                }
            }
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        },
        extensions: ['*', '.js', '.vue', '.json']
    },
    plugins: [
        new VueLoaderPlugin()
    ]
};

module.exports = config;
