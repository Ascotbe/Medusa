> 写在开头

- 前端页面在重构，请下载打包版本手动安装，望周知（
- 别用阿里云服务器，他们25端口开不了(腾讯云没测
- 所有的配置只需要拥有一个域名
- docker启动服务器最低需要1核2G配置

## 手动安装项目

### 无SSL证书方式安装

#### 下载项目

```bash
git clone https://github.com/Ascotbe/Medusa.git
```

#### Linux&Mac

> 必要环境

```bash
#macOS把apt替换成brew即可
sudo dpkg --add-architecture i386
sudo apt install nodejs -y
sudo apt install npm -y
sudo apt install nginx -y
sudo apt install redis -y
sudo apt install python3 -y#需要3.7以上版本
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
redis_password="I_will_always_like_AyanamiRei"#连接redis的密码
#开启功能和修改默认参数
registration_function_status=True#默认开启注册功能，注册完毕请手段关闭
forgot_password_function_status=False#默认关闭忘记密码功能
secret_key_required_for_account_registration="I_will_always_like_SoryuAsukaLangley"#注册账号需要的秘钥,最好修改为250个随机字符串
forget_password_key="I_will_always_like_KatsuragiMisato"#修改密码所需要的key
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

在**Medusa/**根目录下面运行

```bash
chmod +x run.sh 
./run.sh
```

接着再打开一个窗口，在**Medusa/Vue/**目录运行以下命令

```bash
npm run serve
```

最后，如果您在上面的配置中都未修改端口以及IP，那么访问`http://127.0.0.1:8082`即可看到web界面

### 使用SSL证书方式安装

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
    server_name  medusa.ascotbe.com; #你的域名
    client_max_body_size 100m;
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
    server_name  medusa.ascotbe.com; #你的域名
    return 301 https://$server_name$request_uri;
}
server {#这个只是单纯接管一个dnslogtest.ascotbe.com
    listen       80;
  	client_max_body_size 100m;
    server_name  dnslogtest.ascotbe.com;#你的DNSLOG的域名
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
    server_name  *.dnslogtest.ascotbe.com;
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
chmod +x run.sh 
./run.sh
```

最后访问`http://ascotbe.com`即可看到web界面（注意这是你自己的域名

### 某些服务器DNSLOG配置的坑

> 如果你服务器不会占用该端口，可以忽略修改，直接跳到域名配置

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
python3 HTTPServer.py
```

**切记如果是云服务器一定要把安全策略组的TCP和UDP的53端口开放!!!!!**

## Docker自动安装

> docker源请换成官方源，否则下载的容器是几个月前的

首先拉取项目

```
git clone --depth=1 https://github.com/Ascotbe/Medusa.git
```

然后进入项目，给install.sh脚本赋予权限

```bash
cd Medusa
sudo chmod +x install.sh
```

接着把你申请的域名证书覆盖项目中的ssl.key和ssl.pem这两个文件，不然会默认使用测试证书

> 演示所用到的几个域名
>
> 搭建medusa的域名：medusa.test.ascotbe.com
>
> dnslog的域名：dnslog.test.ascotbe.com
>
> 邮件服务器域名：smtp.ascotbe.com
>
> 你搭建服务器的IP：1.1.1.1

然后执行脚本即可，需要传入11个参数，每个参数解释如下（如果不想修改，只需传入`none`）：

1. 表示docker环境内的Redis密码（不要传入特殊字符，一般字母+数字即可
2. 你注册用户所要使用的秘钥
3. 你忘记密码位置所使用的秘钥
4. 你需要配置的域名
5. 你用来接收DNSLOG所需要的域名
6. 你使用的第三方smtp服务器账号
7. 你第三方邮件服务器账号
8. 你第三方邮件服务器秘钥
9. 自建SMTP服务器（只能传入域名，邮箱@后面的值
10. 自建服务器邮箱（看这个参数值就知道第9点是什么意思了
11. 你服务器的IP值（必填

```bash
#演示命令如下，参数必须与之对应
./install.sh "redis_pass" "secret_key_required_for_account_registration" "forget_password_key" "medusa.test.ascotbe.com" "dnslog.test.ascotbe.com" "smtp.163.com" "ascotbe@163.com" "third_party_mail_pass" "ascotbe.com" "test@ascotbe.com" "1.1.1.1"
```

## 配置DNSLOG域名

接收的IP(1.1.1.1)为medusa搭建的那台机器

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

> 手动搭建的[参考文章](https://www.ascotbe.com/2021/08/17/Office_0x02/)的第一节:搭建邮件服务器

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

