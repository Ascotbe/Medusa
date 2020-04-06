## 启动莎酱

#### Install docker

Different ways for different systems

```bash
#Ubuntu
sudo apt install docker.io
#Raspberry Pi
sudo curl -sSL https://get.docker.com | sh
```

#### Pull the repository of coolq

```bash
docker pull ascotbe/medusabot:latest
```

#### Create a container to save data

```bash
mkdir /root/medusabot
```

#### Boot docker container

Create a background process(daemon) using by parameter `-d`.

```bash
docker run -d --name=bot --rm -p 12345:9000 -v /root/medusabot:/home/user/coolq -e VNC_PASSWD=medusa -e COOLQ_ACCOUNT=123456789 -e CQHTTP_SERVE_DATA_FILES=yes ascotbe/medusabot:latest
```

You should change these three items.

- `-p 12345:9000`: `12345` Change to a port number that you need to be able to access from the Internet
- `COOLQ_ACCOUNT=123456789`: `123456789` Replace with the QQ number you want to login
- `VNC_PASSWD=medusa`: `medusa` The password you use to log in to the web page can also be set

#### Container configuring

First, without changing any of the above commands, visit `http: // you_ip: 12345` and enter the password` medusa` to enter `coolq`

Login to your QQ, it is best to use a smurf to log in, otherwise you will be squeezed offline when you log in on your mobile phone

If you want to set the data and IP information yourself, you can configure it as follows, if you want to quickly configure the file, you can jump directly to the ** Quick Configuration ** chapter

At `/home/user/coolq/app/io.github.richardchien.coolqhttpapi/config` add ` 123456789.json`(name = your qq number) configuration, the following is a graphic explanation

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

Among, `ws_reverse_api_url` and `ws_reverse_event_url`, if using `docker` container, value in `cat /etc/hosts`.For example, it should be filled in as shown below`172.17.0.1`

![1585548667201](https://github.com/Ascotbe/Random-img/blob/master/Medusa/bot/4.png?raw=true)



#### Quickly setting

The configuration is the same as the first step in the above picture, open the web page and at `/home/user/coolq/app/io.github.richardchien.coolqhttpapi/config` change`12345.json`to`your_qq_number.json`.

#### Booting the BOT

Go back at your server, folder `Medusa`, config your BOT and boot it.

```python
# bot configuring example
vim config.py
# parameter modding
debug_mode=False # Terminal = False, change to True when need increasing your BOT scanning speed 
whitelist_group_status=False # If it is changed to True, you need to fill in the group number to be processed below
whitelist_group_list=[] # Whitelist group ID list, format like python list
managed_group=[] # The group list you manage must have administrator rights to welcome newcomers into the group and agree to use it
# Configure the api key. If it is not filled in, the weather query and Turing function cannot be used
vim QQbot/bot_config.py
WeatherKey="" # Polymerization API key
TULING_API_KEY ="" # turing key
bot_email_send=False # Whether enable mailbox push notifications
bot_email_receiver=["XXX@163.com","XXX@qq.com"] # mail receiver
bot_mail_pass="XXXXXXXX" # your password
bot_mail_user="XXX@163.com" # your mailbox

# Boot your BOT
python bot.py
```

![3](https://github.com/Ascotbe/Random-img/blob/master/Medusa/bot/3.png?raw=true)

If you see the picture content, it means the startup is successful

```bash
#If you have already started it once, and it is running normally, you can end the bot you just started. Use the following command to let the robot run in the background, so that if you close the ssh connection, the bot will not stop.
nohup python bot.py &
```

#### Using BOT

In the group @BOT_NAME and enter `help` to view the help document

#### View running status

```bash
docker logs coolq
```

#### Boot and shutdown

```bash
docker start coolq
docker stop coolq
```

## Functions of 莎酱

> CVE group push

It can run that if at your `config.py` set `monitor_group_list=["YOUR_GROUP_ID"]`, need format like list when you have many group.

多个群号示例：`monitor_group_list=["1234565","78979888","12313213"]`

![5](https://github.com/Ascotbe/Random-img/blob/master/Medusa/bot/5.png?raw=true)



> CVE mail push

If you want to use this function, you need to fill in the following data

- `bot_email_send` ：Default `False`.If you need email push, change it to `True`.
- `bot_email_receiver`：The parameters is in the form of a list, multiple mailboxes can be modified to `bot_email_receiver = [" 123@163.com "," 123@qq.com "]`
- `bot_mail_pass`：The `Key` of `SMTP` in your mailbox
- `bot_mail_user`：Your mail box

**Note:** Only when you send an email to your own mailbox will you bring a picture, otherwise it will only be in text form

![6](https://github.com/Ascotbe/Random-img/blob/master/Medusa/bot/6.png?raw=true)

> Bug scan

To use this function, you only need to send the scan + domain name in the group.

This function does not support the form of `ip`, do n’t ask why

**Note:** Add a space character before the domain name

![7] (https://github.com/Ascotbe/Random-img/blob/master/Medusa/bot/7.png?raw=true)

> Bug query

To use this function, just send a query + `Token` +` Key`

Each scanned data can only be viewed by the scanned user, other users cannot query

**Note:** Add a space character before the domain name

![8] (https://github.com/Ascotbe/Random-img/blob/master/Medusa/bot/8.png?raw=true)