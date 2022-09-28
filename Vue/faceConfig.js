// const { baseURL } = require("@/api/request")

const faceConfig = () => {
  return {
    // 基础路径,打包发布的时候修改为后端发布服务地址

    basePath: 'https://medusa.ascotbe.asia/api/',
    imgPath: 'https://medusa.ascotbe.asia/s/',
    scriptUrl: '//at.alicdn.com/t/font_1734998_iv1ouwpdggf.js'//icon 图标库
  }
}

module.exports = faceConfig()
