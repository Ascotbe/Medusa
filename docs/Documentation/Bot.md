#### 安装docker

不通的系统选择不通的安装方式

```bash
#Ubuntu
sudo apt install docker.io
#树莓派
sudo curl -sSL https://get.docker.com | sh
```

#### 拉取coolq仓库

```bash
docker pull ascotbe/medusabot:latest
```

#### 创建个存放数据的容器

```bash
mkdir /root/medusabot
```

#### 启动docker容器

使用`-d`参数来让容器后台运行，也就是开启了守护进程

```bash
docker run -d --name=bot --rm -p 12345:9000 -v /root/medusabot:/home/user/coolq -e VNC_PASSWD=medusa -e COOLQ_ACCOUNT=123456789 -e CQHTTP_SERVE_DATA_FILES=yes ascotbe/medusabot:latest
```

上面的代码只有三个地方需要修改

- `-p 12345:9000`这边可以把`12345`改成你需要外网能访问的端口号

- `COOLQ_ACCOUNT=123456789`中的`123456789`替换为你要登录的`QQ`号
- `VNC_PASSWD=medusa`中`medusa`为你登录网页的密码，也可以不设置

#### 容器配置

首先在上面命令任何都没有改的情况下，访问`http://you_ip:12345` 并输入密码`medusa`即可进入`coolq`

登录你的`QQ`号，最好是使用小号登录，不然当你在手机登录的时候会被挤下线

如果想自己设置数据和IP等信息可以按下文配置，如果想快速配置文件可以直接跳到**快速配置**章节

然后在路径为`/home/user/coolq/app/io.github.richardchien.coolqhttpapi/config`中添加名为` 你QQ号.json`配置信息，下面是图文讲解

![1](https://github.com/Ascotbe/Random-img/blob/master/Medusa/bot/1.png?raw=true)

![2](https://github.com/Ascotbe/Random-img/blob/master/Medusa/bot/2.png?raw=true)

```json
{
    "host": "[::]",
    "port": 5700,
    "use_http": true,
    "ws_host": "[::]",
    "ws_port": 6700,
    "use_ws": false,
    "ws_reverse_url": "",
    "ws_reverse_api_url": "ws://172.17.0.1:8080/ws/api/",
    "ws_reverse_event_url": "ws://172.17.0.1:8080/ws/event/",
    "ws_reverse_reconnect_interval": 3000,
    "ws_reverse_reconnect_on_code_1000": true,
    "use_ws_reverse": true,
    "post_url": "",
    "access_token": "",
    "secret": "",
    "post_message_format": "string",
    "serve_data_files": false,
    "update_source": "china",
    "update_channel": "stable",
    "auto_check_update": false,
    "auto_perform_update": false,
    "enable_heartbeat": true,
    "heartbeat_interval": 15000, 
    "show_log_console": true,
    "log_level": "info"
}
```

上面配置中有一点要说明，`ws_reverse_api_url`和`ws_reverse_event_url`的值如果是使用`docker`容器的话可以进入容器然后使用`cat /etc/hosts`命令查看地址，如下图所示应该填`172.17.0.1`

![1585548667201](https://github.com/Ascotbe/Random-img/blob/master/Medusa/bot/4.png?raw=true)



#### 快速配置

配置方式和上图的第一个步骤一样，进入先进入网页然后在路径为`/home/user/coolq/app/io.github.richardchien.coolqhttpapi/config`中把`12345.json`改为`你QQ.json`即可登录运行

#### 启动Bot

回到你的服务器打开`Medusa`文件夹，配置和启动你的机器人

```python
#配置机器人
vim config.py
#修改参数
debug_mode=False#终端为False,机器人改为True会加快扫描
whitelist_group_status=False#如果改为True，需要把需要处理的群号填入下面
whitelist_group_list=[]#白名单群ID列表，格式为python列表样式
managed_group=[]#你管理的群列表,必须有管理员权限，用来欢迎新人入群和同意入群使用
#配置api key,如果不填也行，就是天气查询和图灵功能不能使用
vim QQbot/bot_config.py
WeatherKey=""#这边填你聚合API的key
TULING_API_KEY =""#这边填图灵机器人的key
#启动机器人
python bot.py
```

![3](https://github.com/Ascotbe/Random-img/blob/master/Medusa/bot/3.png?raw=true)

如果看到图片内容就表示启动成功了

```bash
#如果你已经启动过一次了，并且运行正常，可以结束掉刚才启动的bot，使用如下命令让机器人后台运行，这样你关闭ssh连接bot也不会停止
nohup python bot.py &
```

#### 使用机器人

在群里@机器人并输入help即可查看帮助文档

#### 查看运行状态

```bash
docker logs coolq
```

#### 启动&关闭

```bash
docker start coolq
docker stop coolq
```

