> 写在开头

- 前端页面在重构，请下载打包版本手动安装，望周知（
- 别用阿里云服务器，他们25端口开不了(腾讯云没测
- 所有的配置只需要拥有一个域名
- docker启动服务器最低需要1核2G配置

## 全局默认值

搭建演示所用到的几个域名

搭建medusa的域名：medusa.test.ascotbe.com

dnslog的域名：dnslog.test.ascotbe.com

邮件服务器域名：smtp.ascotbe.com

你搭建服务器的IP：1.1.1.1

## 手动安装

> 下载项目

```bash
git clone https://github.com/Ascotbe/Medusa.git
```

> 必要环境

```bash
sudo dpkg --add-architecture i386
sudo apt install nodejs -y
sudo apt install npm -y
sudo apt install nginx -y
sudo apt install redis -y
#需要3.7以上的Python版本
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install mingw-w64 -y
sudo apt install golang-go -y
sudo apt install nim -y
sudo apt install wine -y
sudo apt install wine32 -y
sudo apt install libwine -y
```

> 安装前后端依赖

```bash
#进入文件夹
cd Medusa
#一键安装后端依赖
python3 -m pip install --ignore-installed -r Medusa.txt
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

>搭建邮件服务器

首先卸载Postfix，如果没有Postfix就跳过

```bash
sudo systemctl stop postfix
sudo apt remove postfix && apt purge postfix
```

安装Sendmail

```bash
sudo apt install sendmail
```

配置Sendmail服务器

```bash
sudo sendmailconfig
```

编辑`/etc/mail/sendmail.mc`

```bash
DAEMON_OPTIONS(`Family=inet,  Name=MTA-v4, Port=smtp, Addr=127.0.0.1')dnl
DAEMON_OPTIONS(`Family=inet,  Name=MSP-v4, Port=submission, M=Ea, Addr=127.0.0.1')dnl

#找到上面这两行修改为
DAEMON_OPTIONS(`Family=inet,  Name=MTA-v4, Port=smtp, Addr=0.0.0.0')dnl
dnl   DAEMON_OPTIONS(`Family=inet,  Name=MSP-v4, Port=submission, M=Ea, Addr=127.0.0.1')dnl
```

然后将域名添加到`/etc/mail/local-host-names`文件中

```bash
ascotbe.com
mail.ascotbe.com
localhost
localhost.localdomain
```

现在使用 m4宏处理器来编译Sendmail配置文件。m4是基于流的。

```bash
sudo m4 /etc/mail/sendmail.mc > /etc/mail/sendmail.cf
```

重新启动Sendmail服务

```bash
sudo systemctl restart sendmail
```

> 配置后端

在目录`/Medusa/config.py`中看注释修改进行修改，标记` <---------------（必须修改`这段内容是必须修改的，其他的可以使用默认配置

> 配置前端

在目录`/Medusa/Vue/faceConfig.js`中进行配置

```vue
const { baseURL } = require("./src/utils/request")

const faceConfig = () =>{
    return{
        // 这个xxxxxxxx地方修改为你的域名，比如medusa.test.ascotbe.com
        basePath: 'https://medusa.test.ascotbe.com/api/',
        imgPath:'https://medusa.test.ascotbe.com/s/'
    }
}

module.exports = faceConfig()
```

然后对Vue进行编译`npm run build`，编译成功后会有一个**dist**文件夹，接着使用命令进行移动

```bash
mv dist/ /var/www/html/
```

> 配置Nginx

```nginx
server {
    # 服务器端口使用443，开启ssl, 这里ssl就是上面安装的ssl模块
    listen       443 ssl;
    #填写绑定证书的域名
    server_name  medusa.test.ascotbe.com; #你的域名
    client_max_body_size 100m;
    # ssl证书地址，从阿里云或者腾讯云免费申请
    ssl_certificate     /etc/nginx/cert/ssl.pem;  #证书文件名称
    ssl_certificate_key  /etc/nginx/cert/ssl.key; # 私钥文件名称
    
    # ssl验证相关配置
    ssl_session_timeout  5m;    #缓存有效期
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;    #加密算法
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;    #安全链接可选的加密协议
    ssl_prefer_server_ciphers on;   #使用服务器端的首选算法
    #启用压缩
  	gzip on;
    # 启用gzip压缩的最小文件，小于设置值的文件将不会压缩
    gzip_min_length 1k;
    # gzip 压缩级别，1-9，数字越大压缩的越好，也越占用CPU时间，后面会有详细说明
    gzip_comp_level 5;
    # 进行压缩的文件类型。javascript有多种形式。其中的值可以在 mime.types 文件中找到。
    gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript image/jpeg image/gif image/png application/vnd.ms-fontobject font/ttf font/opentype font/x-woff image/svg+xml;
    # 是否在http header中添加Vary: Accept-Encoding，建议开启
    gzip_vary on;
    # 禁用IE 6 gzip
    gzip_disable "MSIE [1-6]\.";
    # 设置压缩所需要的缓冲区大小     
    gzip_buffers 32 4k;
    location / {
    		#网站主页路径。此路径仅供参考，具体请您按照实际目录操作
        root   /var/www/html/dist;
        index  index.html;
    }
    location /api {
    		#后端API接口
    		proxy_pass http://127.0.0.1:9999/api;
    		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    location /s {
    		#图片资源
    		proxy_pass http://127.0.0.1:9999/s;
    		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    location /a {
    		#数据接收
    		proxy_pass http://127.0.0.1:9999/a;
    		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    location /b {
    		#邮件数据接收
    		proxy_pass http://127.0.0.1:9999/b;
    		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
server {
    listen       80;
    server_name  medusa.test.ascotbe.com;
    gzip on;
    # 启用gzip压缩的最小文件，小于设置值的文件将不会压缩
    gzip_min_length 1k;
    # gzip 压缩级别，1-9，数字越大压缩的越好，也越占用CPU时间，后面会有详细说明
    gzip_comp_level 5;
    # 进行压缩的文件类型。javascript有多种形式。其中的值可以在 mime.types 文件中找到。
    gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript image/jpeg image/gif image/png application/vnd.ms-fontobject font/ttf font/opentype font/x-woff image/svg+xml;
    # 是否在http header中添加Vary: Accept-Encoding，建议开启
    gzip_vary on;
    # 禁用IE 6 gzip
    gzip_disable "MSIE [1-6]\.";
    # 设置压缩所需要的缓冲区大小     
    gzip_buffers 32 4k;
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
    location /b {
    		proxy_pass http://127.0.0.1:9999/b;
    		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
#不使用HTTP
#server {
#    listen       80;
#    server_name  medusa.test.ascotbe.com; #你的域名
#    return 301 https://$server_name$request_uri;
#}
server {#这个只是单纯接管一个dnslogtest.ascotbe.com
    listen       80;
  	client_max_body_size 100m;
    server_name  dnslog.test.ascotbe.com;#你的DNSLOG的域名
    location / {
        proxy_pass  http://127.0.0.1:8888; # 转发
        proxy_set_header Host $host;
	      proxy_set_header X-Real-IP $remote_addr; #一般的web服务器用这个 X-Real-IP 来获取源IP
        proxy_set_header x-forwarded-for $proxy_add_x_forwarded_for; 	   #如果nginx 服务器是作为反向代理服务器的，则这个配置项是必须的；否则看不到源IP
    }
}
server {#这个是接管所有的关于dnslogtest.ascotbe.com的子域名
    listen       80;
  	client_max_body_size 100m;
    server_name  *.dnslog.test.ascotbe.com;
    location / {
        proxy_pass  http://127.0.0.1:8888;
        proxy_set_header Host $host;
	      proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header x-forwarded-for $proxy_add_x_forwarded_for; 	  
    }
}
```

接着重新启动Nginx

```
sudo systemctl restart nginx
```

> 启动项目

在**Medusa/**根目录下面运行

```bash
sudo echo -e "#!/bin/bash\npython3 -c 'from Web.CVE.NistMonitoring.NistInitialization import NistInitialization;from Web.ActiveScan import InitializationPlugin;InitializationPlugin.Run();NistInitialization()'\nredis-server /etc/redis/redis.conf &\nservice sendmail start &\npython3 DNSServer.py &\npython3 HTTPServer.py &\ncelery -A Web worker -B --loglevel=info --pool=solo &\nnginx &\ngunicorn Web.wsgi:application --bind 0.0.0.0:9999 --workers 6" > run.sh
#启动运行脚本
sudo chmod +x run.sh
nohup ./run.sh &
```

最后访问`http://medusa.test.ascotbe.com`即可看到web界面（注意这是你自己的域名

## Docker安装

> docker源请换成官方源，否则下载的容器是几个月前的

接着把你申请的域名证书覆盖项目中的ssl.key和ssl.pem这两个文件，不然会默认使用测试证书，然后执行脚本即可，需要传入对应参数即可，每个参数解释如下：

1. Web端域名（必填
2. 接收DNSLOG所需要的域名（必填
6. 自建SMTP服务器（只能传入域名，邮箱@后面的值

```bash
#演示命令如下，参数必须与之对应
git clone https://github.com/Ascotbe/Medusa.git
cd Medusa
sudo chmod +x install.sh
./install.sh -u medusa.test.ascotbe.com -d dnslog.test.ascotbe.com -s ascotbe.com
```

## 配置DNSLOG域名

接收的IP(1.1.1.1)为medusa搭建的那台机器

**切记如果是云服务器一定要把安全策略组的TCP和UDP的53端口开放!!!!!**

```
主机记录            记录类型            线路类型           记录值              
ns1                A                  默认              1.1.1.1
dnslog.test　　　　 MX                 默认              ns1.ascotbe.com
```

## 配置主站域名

接收的IP(1.1.1.1)为medusa搭建的那台机器

```
主机记录            记录类型            线路类型           记录值              
medusa.test        A                  默认              1.1.1.1
```

## 配置自建邮服域名

> docker搭建的只需要配置域名即可

接收的IP(1.1.1.1)为medusa搭建的那台机器

```
主机记录            记录类型            线路类型           记录值              
@                  TXT                默认              v=spf1 ip4:1.1.1.1 -all
@                  A                  默认              1.1.1.1
@                  MX                 默认              mail.ascotbe.com | 10
mail               A                  默认              1.1.1.1
pop3               CNAME              默认              mail.ascotbe.com
pop                CNAME              默认              mail.ascotbe.com
imap               CNAME              默认              mail.ascotbe.com
smtp               CNAME              默认              mail.ascotbe.com
```

