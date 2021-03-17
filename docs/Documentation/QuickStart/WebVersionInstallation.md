> Web版本正在Alpha阶段，谨慎使用

## 手动安装

### 下载项目

```bash
git clone https://github.com/Ascotbe/Medusa.git
```

### Windows

> 必要环境

Redis+npm+jdk 1.8+Python3.7（以上版本）

> 安装前后端依赖

```bash
#进入文件夹
cd Medusa
#一键安装后端依赖
python3 -m pip install -r Medusa.txt
#进入前端文件夹
cd Vue
#安装前端依赖
npm install 
```

> 配置后端

在目录`/Medusa/config.py`中进行配置

- 注意请确保Redis的配置的账号密码端口等信息和当前安装的Redis相同，
- 注册完账号为了安全考虑请关闭注册功能
- 修改注册账号和忘记密码所需要的Key

```python
#redis的配置
redis_host="localhost"#连接redis的地址，默认本地
redis_port="6379"#redis连接端口，默认6379
redis_db="6"#连接的数据库，默认为6
redis_password="I_will_always_like_Rei_Ayanami"#连接redis的密码
#开启功能和修改默认参数
registration_function_status=False#默认关闭注册功能
forgot_password_function_status=False#默认关闭忘记密码功能
secret_key_required_for_account_registration="I_will_always_like_Rei_Ayanami"#注册账号需要的秘钥,最好修改为250个随机字符串
forget_password_key="https://github.com/Ascotbe/Medusa"#修改密码所需要的key
```

> 配置前端

在目录`/Medusa/Vue/faceConfig.js`中进行配置

```vue
const { baseURL } = require("./src/utils/request")

const faceConfig = () =>{
    return{
        // 如果前后端分离，把IP地址修改为你自己的后端地址
        basePath: 'http://127.0.0.1:9999/api/',
        imgPath:'http://127.0.0.1:9999/s/'
    }
}

module.exports = faceConfig()
```

> 启动项目

在更目录中，分别打开3个命令行窗口，运行下面三条命令

- 注意启动的端口要和前端配置文件中的相同
- 注意启动Redis的时候，配置文件的路径请按自己的路径进行替换
- 以下三条命令都在**Medusa/**根目录下面运行

```bash
celery -A Web.Workbench.Tasks worker --loglevel=info --pool=solo
python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
redis-server.exe redis.conf
```

接着再打开一个窗口，在**Medusa/Vue/**目录运行以下命令

```bash
npm run serve
```

最后，如果您在上面的配置中都未修改端口以及IP，那么访问`http://127.0.0.1:8082`即可看到web界面

### Linux&Mac

> 必要环境

Redis+npm+jdk 1.8+Python3.7（以上版本）

> 安装前后端依赖

```bash
#进入文件夹
cd Medusa
#一键安装后端依赖
python3 -m pip install -r Medusa.txt
#进入前端文件夹
cd Vue
#安装前端依赖
npm install 
```

> 配置后端

在目录`/Medusa/config.py`中进行配置

- 注意请确保Redis的配置的账号密码端口等信息和当前安装的Redis相同，
- 注册完账号为了安全考虑请关闭注册功能
- 修改注册账号和忘记密码所需要的Key

```python
#redis的配置
redis_host="localhost"#连接redis的地址，默认本地
redis_port="6379"#redis连接端口，默认6379
redis_db="6"#连接的数据库，默认为6
redis_password="I_will_always_like_Rei_Ayanami"#连接redis的密码
#开启功能和修改默认参数
registration_function_status=False#默认关闭注册功能
forgot_password_function_status=False#默认关闭忘记密码功能
secret_key_required_for_account_registration="I_will_always_like_Rei_Ayanami"#注册账号需要的秘钥,最好修改为250个随机字符串
forget_password_key="https://github.com/Ascotbe/Medusa"#修改密码所需要的key
```

> 配置前端

在目录`/Medusa/Vue/faceConfig.js`中进行配置

```vue
const { baseURL } = require("./src/utils/request")

const faceConfig = () =>{
    return{
        // 如果前后端分离，把IP地址修改为你自己的后端地址
        basePath: 'http://127.0.0.1:9999/api/',
        imgPath:'http://127.0.0.1:9999/s/'
    }
}

module.exports = faceConfig()
```

> 启动项目

在更目录中，分别打开3个命令行窗口，运行下面三条命令

- 注意启动的端口要和前端配置文件中的相同
- 注意启动Redis的时候，配置文件的路径请按自己的路径进行替换
- 以下三条命令都在**Medusa/**根目录下面运行

```bash
celery -A Web.Workbench.Tasks worker --loglevel=info --pool=solo
python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
redis-server /usr/local/etc/redis.conf
```

接着再打开一个窗口，在**Medusa/Vue/**目录运行以下命令

```bash
npm run serve
```

最后，如果您在上面的配置中都未修改端口以及IP，那么访问`http://127.0.0.1:8082`即可看到web界面

## Docker安装

docker容器不一定是最新版本

> docker源请换成官方源，否则下载的容器是几个月前的
>
> 注册中的秘钥在config.py中和手动安装默认秘钥一致

- 首先拉取容器

  ```bash
  docker pull ascotbe/medusa:latest
  ```

- 拉取成功后新建一个`dockerfile`文件

  ```
  vim Dockerfile
  ```

- 接着再文件中写入如下内容

  > 如果是服务器部署需要替换文中的**http://127.0.0.1:9999**为您服务器的ip地址，否则会照成服务器无法访问后端

  ```dockerfile
  FROM ascotbe/medusa:latest
  MAINTAINER ascotbe
  #WORKDIR /Medusa
  #RUN git pull
  WORKDIR /Medusa/Vue 
  RUN echo "const { baseURL } = require(\"./src/utils/request\")\nconst faceConfig = () =>{\n    return{\n        basePath: 'http://127.0.0.1:9999/api/',\n        imgPath:'http://127.0.0.1:9999/s/'\n    }\n}\nmodule.exports = faceConfig()">faceConfig.js
  RUN npm install
  WORKDIR /Medusa
  RUN chmod +x run.sh
  CMD ["./run.sh"]
  ```

- 编译容器后启动

  ```bash
  docker build -t medusa_web .
  docker run -d -i -t --name  medusa -p 8082:8082 -p 9999:9999 medusa_web 
  ```

执行完命令访问`http://127.0.0.1:8082`即可，如果是服务器访问`http://你服务器IP:8082`