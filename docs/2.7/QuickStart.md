## 环境配置

正所谓磨刀不误砍柴工

### 安装Python环境

当前插件是在```Python3.6.x ```环境下开发，如果需要使用扫描器或者编写插件首先需要安装```Python```开发环境，建议使用```PyCharm```+```Anaconda```作为开发环境。

<a href="https://www.python.org/downloads/release/python-367/" style="font-size:16px;color:gilt">Python 3.6.7</a>

<a href="https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86_64.exe" style="font-size:16px;color:gilt">Anaconda for Windows</a>

<a href="https://repo.anaconda.com/archive/Anaconda3-2019.07-MacOSX-x86_64.pkg" style="font-size:16px;color:gilt">Anaconda for Mac</a>

<a href="http://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC" style="font-size:16px;color:gilt">PyCharm for Windows</a>

<a href="http://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac&code=PCC" style="font-size:16px;color:gilt">PyCharm for Mac</a>

### 安装Module

运行```Medusa```所需要导入的包：

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
```

## 快速使用

#### 0x01 使用扫描器对单个网站进行扫描

```bash
python3 MedusaScan.py -u https://www.ascotbe.com
```

#### 0x02 使用扫描器对批量网站扫描

```bash
python3 MedusaScan.py -f c：//Ascotbe.txt  (url所在文件路径)
```

#### 0x03 对目标网站进行数据库弱口令探测

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -sp c：//Password.txt -su c：//Username.txt
```

#### 0x04 对目标网站进行```JavaScript```中的链接爬取

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -j
```

#### 0x04 对目标网站进行子域名收集

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -s
```

#### 0x05 开启代理功能

```
python3 MedusaScan.py -u https://www.ascotbe.com -p
```

#### 0x06 使用指定```Header```头

目前支持常见的浏览器，下面列举其中3个，详情请看项目README文档

注意：需要区分大小写

```
python3 MedusaScan.py -u https://www.ascotbe.com -a firefox
python3 MedusaScan.py -u https://www.ascotbe.com -a ie
python3 MedusaScan.py -u https://www.ascotbe.com -a opera
```

## 扫描结果

- 扫描的结果存在根目录中的```ScanResult```文件夹中

