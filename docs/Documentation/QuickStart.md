## 环境配置

正所谓磨刀不误砍柴工

### 安装Python环境

当前插件是在`Python3.6.x `环境下开发，如果需要使用扫描器或者编写插件首先需要安装`Python`开发环境，建议使用`PyCharm`+`Anaconda`作为开发环境。

<a href="https://www.python.org/downloads/release/python-367/" style="font-size:16px;color:gilt">Python 3.6.7</a>

<a href="https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86_64.exe" style="font-size:16px;color:gilt">Anaconda for Windows</a>

<a href="https://repo.anaconda.com/archive/Anaconda3-2019.07-MacOSX-x86_64.pkg" style="font-size:16px;color:gilt">Anaconda for Mac</a>

<a href="http://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC" style="font-size:16px;color:gilt">PyCharm for Windows</a>

<a href="http://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac&code=PCC" style="font-size:16px;color:gilt">PyCharm for Mac</a>

### 安装Module

运行`Medusa`所需要导入的包：

```
bs4 ==0.0.1
fake-useragent ==0.1.11
requests ==2.22.0
urllib3 ==1.25.3
python-nmap ==0.6.1
PyMySQL ==0.9.3
IPy ==1.0
scrapy ==1.7.3
tqdm ==4.38.0
dnspython ==1.16.0
tldextract ==2.2.2
Django==2.2.7
Celery==4.3.0
django_redis==4.10.0
eventlet==0.25.1
pyDES==2.0.1
nonebot==1.3.1
```


## DNSLOG

由于我搭建的`DNSLOG`不支持某些协议所以，接下来请使用http://ceye.io/ 中的`DNSLOG`(等后续会调回来

```
#打开根目录下的这个文件（Medusa目录
vim config.py
```

把`dns_log_url`和`dns_log_key`分别改成你的http://ceye.io/ 里面的`Identifier`和`API Token`值


## 快速使用

该工具还在测试阶段，如有问题请提交`issues`，切记本扫描器只用于授权测试

#### 0x01 使用扫描器对单个网站进行扫描

```bash
python3 MedusaScan.py -u https://www.ascotbe.com
```

#### 0x02 使用扫描器对批量网站扫描

`Ascotbe.txt`为你存放的文件，最好放在和`MedusaScan.py`文件同目录下，你存放`URL`的文件格式为每一行一个`url`

```bash
python3 MedusaScan.py -f Ascotbe.txt  (你的文件，最好放在和MedusaScan同级文件中)
```

#### ~~0x03 对目标网站进行数据库弱口令探测~~

该功能用处不大暂时注释了,如果要使用`/Medusa/Password.txt`这个是你文件的路径

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -sp /Medusa/Password.txt -su /Medusa/Username.txt 
```

#### 0x04 对目标网站进行JavaScript中的链接爬取

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -j
```

#### 0x04 对目标网站进行子域名收集

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -s
```

#### ~~0x05 开启代理功能~~

```
python3 MedusaScan.py -u https://www.ascotbe.com -p （该功能暂时弃用后续在更新
```

#### 0x06 使用指定`Header`头

目前支持常见的浏览器，下面列举其中3个，详情请看项目`README`文档

注意：需要区分大小写

```
python3 MedusaScan.py -u https://www.ascotbe.com -a firefox
python3 MedusaScan.py -u https://www.ascotbe.com -a ie
python3 MedusaScan.py -u https://www.ascotbe.com -a opera
```

#### 0x07 针对单独模块扫描

该模块所支持的名称请针对根目录文件夹使用，一个文件夹名对应一个模块，并且请注意大小写，实在无法理解请参考[该文件中](https://www.ascotbe.com/Medusa/Documentation/#/PluginDirectory)名称进行使用

```
python3 MedusaScan.py -u https://www.ascotbe.com -m Struts2
```

#### 0x08 设置线程数

```
python3 MedusaScan.py -u https://www.ascotbe.com -t 100
```

## 扫描结果

- 扫描结果存在`ScanResult`文件夹中
- 在`Medusa.db`文件中也存在扫描结果
- 如果以上文件都不存在说明目标并无扫描出漏洞

