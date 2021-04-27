

> ## Bash版本放弃更新，望周知

## Demo



![Bashdemo](https://github.com/Ascotbe/Random-img/blob/master/Medusa/demo.gif?raw=true)


## 参数说明	

| 命令 | 参数个数 | 作用                                                         | 备注                                                         |
| ---- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| -u   | 1        | 输入单个目标url（最好使用[http://或https://作为开头,并且后面别跟参数](http://xn--https-wm6j//作为开头,并且后面别跟参数) | [https://www.ascotbe.com](https://www.ascotbe.com/) or [https://192.168.0.1](https://192.168.0.1/) |
| -a   | 1        | 指定头文件或使用随机头                                       | 具体使用参考使用文档                                         |
| -f   | 1        | 需要批量扫描目标url所在文件名字                              | -u和-f只能存在一个，并且必须存在一个                         |
| -p   | 1        | 需要填入你代理的IP，如果有端口的话也需要带上端口             | 以使用BURP作为代理那么就该传入 127.0.0.1:8080                |
| -m   | 1        | 针对单独的模块进行扫描比如Struts2、Apache等                  | 具体内容可以通过项目Modules文件夹中对应名字来输入            |
| -t   | 1        | 设置进程数                                                   | 默认进程数5                                                  |
| -s   | 1        | 开启子域名探测                                               |                                                              |
| -PL  | 1        | 列表形式的端口                                               | 只要是使用非数字隔开即可，超过65535的端口都会剔除，如果不输出 -p 或者 -P 会对默认端口进行扫描。eg:22,139,445,3389 |
| -PR  | 1        | 范围形式的端口                                               | 只要是使用非数字隔开即可，超过65535的端口都会剔除，如果不输出 -p 或者 -P 会对默认端口进行扫描。eg:1-65535 |

## 环境配置

### 系统环境配置

> Ubuntu

需要安装`JAVA`环境，且全局变量中可执行`java`命令

> CentOS

1.需要安装`JAVA`环境，且全局变量中可执行`java`命令

2.需要执行`yum install sqlite*`命令来安装**sqlite3.so**库

> Mac OS

需要安装`JAVA`环境，且全局变量中可执行`java`命令

### 安装Python环境

当前插件是在`Python3.7.x `环境下开发，低于`3.7`会导致某些功能无法使用，如果需要使用扫描器或者编写插件首先需要安装`Python`开发环境，建议使用`PyCharm`+`Anaconda`作为开发环境。

### 安装依赖包

运行`Medusa`所需要的包，在根目录下执行

```bash
pip install -r Medusa.txt
```

## 配置文件

该小节所指的配置文件是同一个文件

#### 0x01 DNSLOG

由于我搭建的`DNSLOG`不支持某些协议所以目前有两种第三方平台检测方法

> 第一种方法（默认开启）

第一种是默认开启的方法，无需修改，方便快捷

> 第二种方法

使用http://ceye.io/ 中的`DNSLOG`，该方法需要修改配置文件

```
#打开根目录下的这个文件（Medusa目录
vim config.py
```

把`ceye_dnslog_url`和`ceye_dnslog_key`分别改成你的http://ceye.io/ 里面的`Identifier`和`API Token`值，接着把`dnslog_name`改成`ceye`即可

**注意：**使用脚本的时候确保网络畅通，如果没扫描出来漏洞不妨看看`DNSLOG`数据是否存在

#### 0x02 Debug模式

该模式默认是关闭的，如果需要打开请在`config.py`文件中修改参数

```
#默认情况
debug_mode=False
#开启Debug模式
debug_mode=True
```

这个模式输出内容不在是进度条和模块加载内容，而变成了每个插件的报错信息


#### 0x03 多线程数

由于重构把之前的多线程替换为多进程，单个插件中的for循环替换成多线程，所以默认线程数为**15**，如果需要修改，把配置文件中的`thread_number`值修改为你需要的线程数

```
thread_number=15 #默认线程数
```

## 快速使用

该工具还在测试阶段，如有问题请提交`issues`，切记本扫描器只用于授权测试

#### 0x01 使用扫描器对单个网站进行扫描

注意：推荐把完整的路径放进去，有些插件需要用到全路径名，比如：`Struts2`

```bash
python3 MedusaScan.py -u https://www.ascotbe.com
```

#### 0x02 使用扫描器对批量网站扫描

`Ascotbe.txt`为你存放的文件，最好放在和`MedusaScan.py`文件同目录下，你存放`URL`的文件格式为每一行一个`url`

文件需要注意几点规范

- 需要填入`url`并且每一行一个`url`

- `url`需要带上`http://`或者`https://`，如果两个协议都需要扫描可以写成两行

  ```
  http://ascotbe.com
  https://ascotbe.com
  ```

- 如果单个`url`中不同的端口对应不同的服务话，需要都写上，例如**8080**和**1024**分别对应不同的服务，而你想要都扫描到的话需要按下面的形式写

  ```
  http://ascotbe.com:1024
  http://ascotbe.com:8080
  ```


接下来运行下面命令即可开始扫描

```bash
python3 MedusaScan.py -f Ascotbe.txt  (你的文件，最好放在和MedusaScan同级文件中)
```

#### ~~0x03 对目标网站进行JavaScript中的链接爬取~~

用处不大暂时注释了

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -j
```

#### ~~0x04 对目标网站进行子域名收集~~

暂时关闭等待重构

~~扫描结果在`ScanResult`目录中，只支持域名不支持**IP**形式~~

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -s
```

#### 0x05 HTTP请求相关配置

需要在**config.py**配置文件中进行配置

```python
#########################################################################
#requests请求配置
#########################################################################
user_agent_randomization=False#是否开启headers头中的随机化，默认关闭
user_agent_browser_type="chrome"#目前只支持如下浏览器，修改为其他的可能会导致无法使用。
                                #firefox、ie、msie、opera、chrome、AppleWebKit、Gecko、safari
#默认请求头，里面保存必须数据，User-Agent头数据如果开启随机化会改变
#WEB版加个判断，如果用户传入header会对该header进行覆盖
headers={
    "Connection": "close",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "dnt": "1"
}
#如果过不想使用代理把下面参数替换为：proxies=None
proxies = {
  "http": "http://127.0.0.1:8080",
  "https": "https://127.0.0.1:8080",
}
```

#### 0x06 针对单独模块扫描

该模块所支持的名称请针对根目录文件夹使用，一个文件夹名对应一个模块，并且请注意大小写，实在无法理解请参考[该文件中](https://www.ascotbe.com/Medusa/Documentation/#/PluginDirectory)名称进行使用

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -m Struts2
```

#### 0x07 设置进程数

开启多进程功能，默认是15个进程，进程越多越快，当某个插件有利用for循环的话会在进程中启动多线程！

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -t 100
```

#### 0x08 敏感信息泄露

以集成到模块中，全量扫描自动开启，如果需要单独扫描只需要输入模块名字即可

## 扫描结果

1.输出`The number of vulnerabilities scanned was:0`就表示未扫描到漏洞

2.`ScanResult`目录中除`Medusa.txt`外无别的文件

3.`Medusa.db`文件中也无新增内容，或者未创建该文件

4.如果以上三点都不存在的话就表示真的没有找到漏洞

