'use strict'
const path = require('path')

const {defineConfig} = require('@vue/cli-service')

function resolve(dir) {
    return path.join(__dirname, dir)
}

module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave: false,
    outputDir: './dist',
    publicPath: process.env.NODE_ENV === 'production' ? './' : '/',
    devServer: {
        port: process.env.VUE_APP_DEVELOP_PORT
    },
    productionSourceMap: process.env.NODE_ENV !== 'production', // 设置上线后是否加载webpack文件
    configureWebpack: {
        devtool: 'source-map',
        performance: {
            hints: 'warning',
            maxEntrypointSize: 50000000,
            maxAssetSize: 30000000,
            assetFilter: function (assetFilename) {
                return assetFilename.endsWith('.js');
            }
        },
        resolve: {
            alias: {
                "%": resolve('src')
            },
        },
    },
    css: {
        loaderOptions: {
            less: {
                javascriptEnabled: true
            }
        }
    },
})
