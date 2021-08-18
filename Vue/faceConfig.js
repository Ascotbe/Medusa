const { baseURL } = require("./src/utils/request")

const faceConfig = () =>{
    return{
        // 基础路径,打包发布的时候修改为后端发布服务地址
        basePath: 'https://127.0.0.1:9999/api/',
        imgPath:'https://127.0.0.1:9999/s/'
    }
}

module.exports = faceConfig()
