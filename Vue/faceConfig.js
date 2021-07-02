const { baseURL } = require("./src/utils/request")

const faceConfig = () =>{
    return{
        // 基础路径,打包发布的时候修改为后端发布服务地址
        basePath: 'http://101.37.14.144:8888/api/',
        imgPath:'http://101.37.14.144:8888/s/'
    }
}

module.exports = faceConfig()
