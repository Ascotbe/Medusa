> 写在开头

- Web版本正在Alpha阶段，谨慎使用

- 大部分功能正在开发前端页面，望周知


- DNSLOG、邮件发送使用需要配置域名，如何配置后续正式版本添加

- 不太推荐使用docker进行安装

## 无SSL证书方式安装

### 下载项目

```bash
git clone https://github.com/Ascotbe/Medusa.git
```

### Linux&Mac

> 必要环境

```bash
#macOS把apt替换成brew即可
sudo apt install nodejs
sudo apt install npm
sudo apt install nginx
sudo apt install redis
sudo apt install python3 #需要3.7以上版本
sudo apt install python3-pip
sudo apt install mingw-w64
sudo apt install golang-go
sudo apt install nim
```

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
#替换环境编码
export PYTHONIOENCODING=utf-8
```

> 关于免杀插件依赖

当您使用**项目提供的测试插件**时会需要安装依赖包（自己编写的插件自己安装相应包文件

- Go：在编译时会自动安装依赖包

- C/C++：无需依赖包

- Nim：需要在编写插件后本地安装包，以下是测试插件需要用到的包

  ```bash
  nimble install winim
  ```

> 配置后端

在目录`/Medusa/config.py`中进行配置

- 注意请确保Redis的配置的账号密码端口等信息和当前安装的Redis相同
- 注册完账号为了安全考虑请关闭注册功能
- 修改注册账号和忘记密码所需要的Key

```python
#redis的配置
redis_host="localhost"#连接redis的地址，默认本地
redis_port="6379"#redis连接端口，默认6379
redis_db="6"#连接的数据库，默认为6
redis_password="I_will_always_like_Rei_Ayanami"#连接redis的密码
#开启功能和修改默认参数
registration_function_status=True#默认开启注册功能，注册完毕请手段关闭
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
celery -A Web worker --loglevel=info --pool=solo
python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
redis-server /etc/redis/redis.conf
```

接着再打开一个窗口，在**Medusa/Vue/**目录运行以下命令

```bash
npm run serve
```

最后，如果您在上面的配置中都未修改端口以及IP，那么访问`http://127.0.0.1:8082`即可看到web界面

## 使用SSL证书方式安装

后端和环境依赖都和无证书的配置一样，从前端开始有区别

> 配置前端

在目录`/Medusa/Vue/faceConfig.js`中进行配置

```vue
const { baseURL } = require("./src/utils/request")

const faceConfig = () =>{
    return{
        // 这个xxxxxxxx地方修改为你的域名，比如ascotbe.com
        basePath: 'https://ascotbe.com/api/',
        imgPath:'https://ascotbe.com/s/'
    }
}

module.exports = faceConfig()
```

然后对Vue进行编译`npm run build`，编译成功后会有一个**dist**文件夹，接着使用命令进行移动

```
mv dist/ /var/www/html/
```

> 配置Nginx

```nginx
server {
    # 服务器端口使用443，开启ssl, 这里ssl就是上面安装的ssl模块
    listen       443 ssl;
    #填写绑定证书的域名
    server_name  ascotbe.com; ##你的域名
    
    # ssl证书地址，从阿里云或者腾讯云免费申请
    ssl_certificate     /etc/nginx/cert/ssl.pem;  #证书文件名称
    ssl_certificate_key  /etc/nginx/cert/ssl.key; # 私钥文件名称
    
    # ssl验证相关配置
    ssl_session_timeout  5m;    #缓存有效期
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;    #加密算法
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;    #安全链接可选的加密协议
    ssl_prefer_server_ciphers on;   #使用服务器端的首选算法

    location / {
    		#网站主页路径。此路径仅供参考，具体请您按照实际目录操作
        root   /var/www/html/dist;
        index  index.html;
    }
    location /api {
    		proxy_pass http://127.0.0.1:9999/api;
    		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    location /s {
    		proxy_pass http://127.0.0.1:9999/s;
    		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    location /a {
    		proxy_pass http://127.0.0.1:9999/a;
    		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
server {
    listen       80;
    server_name  ascotbe.com; #你的域名
    return 301 https://$server_name$request_uri;
}
```

接着重新启动Nginx

```
sudo systemctl restart nginx
```

> 启动项目

运行下面三条命令

- 注意启动的端口要和前端配置文件中的相同
- 注意启动Redis的时候，配置文件的路径请按自己的路径进行替换
- 以下三条命令都在**Medusa/**根目录下面运行

```bash
nohup celery -A Web worker --loglevel=info --pool=solo &
nohup python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload &
redis-server /etc/redis/redis.conf
```

最后访问`http://ascotbe.com`即可看到web界面（注意这是你自己的域名

## 关于DNSLOG配置

由于Ubuntu默认会占用53端口，使用命令查看`sudo lsof -i:53`

```bash
COMMAND   PID            USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
systemd-r 610 systemd-resolve   12u  IPv4  19377      0t0  UDP localhost:domain 
systemd-r 610 systemd-resolve   13u  IPv4  19378      0t0  TCP localhost:domain (LISTEN)
```

需要在配置中关闭

```bash
sudo vim /etc/systemd/resolved.conf
```

然后把文件`DNSStubListener`修改为no，`DNS`改为谷歌的DNS，具体配置如下图

```bash
[Resolve]
DNS=8.8.8.8
#FallbackDNS=
#Domains=
#LLMNR=no
#MulticastDNS=no
#DNSSEC=no
#DNSOverTLS=no
#Cache=no
DNSStubListener=no
#ReadEtcHosts=yes
```

重启配置

```bash
sudo systemctl restart systemd-resolved.service
```

然后启动数据接收脚本

```bash
python3 DomainNameSystemServer.py
```

**切记如果是云服务器一定要把安全策略组的TCP和UDP的53端口开放!!!!!**



## Docker安装

> docker源请换成官方源，否则下载的容器是几个月前的
>
> docker容器不一定是最新版本(目前停留在v0.92)
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

> 所有的注册KEY都是默认的，可以在config.py文件中找到

执行完命令访问`http://127.0.0.1:8082`即可，如果是服务器访问`http://你服务器IP:8082`