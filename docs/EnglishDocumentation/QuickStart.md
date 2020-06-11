##  Environment configuration

### System environment configuration

> Ubuntu

The `JAVA` environment needs to be installed and the `java` command can be executed in the global variables

> CentOS

1.The `JAVA` environment needs to be installed and the `java` command can be executed in the global variables

2.You need to execute the `yum install sqlite*` command to install the **sqlite3.so** library

> Mac OS

The `JAVA` environment needs to be installed and the `java` command can be executed in the global variables

### Install Python env

The current plug-in is developed under the `Python3.7.x` environment. Below` 3.7`, some functions cannot be used. If you need to use a scanner or write a plug-in, you must first install the `Python` development environment. It is recommended to use` PyCharm` + `Anaconda` as development environment.

### Module install

`Medusa` dependent packages：

```python
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
nonebot==1.5.0
nonebot[scheduler]==1.5.0
typing==3.7.4.1
docxtpl==0.9.2
```


## Configuration file

The configuration file referred to in this section is the same file

#### 0x01 DNSLOG

Since the `DNSLOG` I built does not support certain protocols, there are currently two methods for detecting third-party platforms

> The first method (by default)

The first is the default method, no need to modify, convenient and fast

> The second method

Use `DNSLOG` in http://ceye.io/, this method needs to modify the configuration file

```
#Open this file in the root directory (Medusa directory)
vim config.py
```

Change `ceye_dnslog_url` and`ceye_dnslog_key` to the values of your `Identifier` and` API Token` at http://ceye.io/ , Then change `dnslog_name` to `ceye`

**Note: **When using the script, ensure that the network is unblocked. If the vulnerability is not scanned, you may wish to see if the `DNSLOG` data exists

#### 0x02 Debug mode 

This mode is closed by default. If you need to open it, please modify the parameters in the `config.py` file

```
#Default
debug_mode = False
#Turn on Debug mode
debug_mode = True
```

The output content of this mode is not the progress bar and module loading content, but has become the error message of each plugin

![debug](https://github.com/Ascotbe/Random-img/blob/master/Medusa/0.76Debug.gif?raw=true)

## Quick start

The tool is still in the testing stage. If you have any questions, please submit `issues`. Remember, this scanner is only use for authorized testing

#### 0x01 Use the scanner to scan a single website
```bash
python3 MedusaScan.py -u https://www.ascotbe.com
```

#### 0x02 Use the scanner to scan a batch of websites

`Ascotbe.txt` is the file you store. It is best to put it in the same directory as the` MedusaScan.py` file. The file format you store `URL` is one` url` per line

Documents need to pay attention to several specifications

- Need to fill in `url` and one` url` per line

- `url` needs to bring` http:// `or` https:// `, if both protocols need to be scanned it can be written in two lines

- If different ports in a single `url` correspond to different services, you need to write them. For example, **8080** and **1024** correspond to different services, and if you want to scan all, you need to press the following Written in the form

  ```
  http://ascotbe.com:1024/test
  http://ascotbe.com:8080/test
  ```

- Different subdirectories, such as `test` and` medusa`, also need to be written on separate branches

  ```
  http://ascotbe.com:1024/test
  http://ascotbe.com:1024/medusa
  ```

Next run the following command to start scanning

```bash
python3 MedusaScan.py -f Ascotbe.txt #Your files are best placed in the same level as MedusaScan
```

#### ~~0x03 Link crawling in JavaScript on the target website~~

This function is commented because not very useful now

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -j
```

#### 0x04 Collect subdomains for the target website

The scan result is in the `ScanResult` directory, only the domain name is supported and the **IP** form is not supported

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -s
```

#### 0x05 Proxy function

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -p 127.0.0.1:8080
```

#### 0x06 Using target Header

Supported parameters：`firefox`，`ie`，`msie`，`opera`，`chrome`，`AppleWebKit`，`Gecko`，`safari `

Currently supports common browsers, 3 of which are listed below (case sensitive)

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -a firefox
python3 MedusaScan.py -u https://www.ascotbe.com -a ie
python3 MedusaScan.py -u https://www.ascotbe.com -a Gecko
```

You can also customize the `header` parameter, remember to add double quotes to the custom` header` containing `" "`, if your `header` is not compliant, it will not prompt an error

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -a "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36"
```

#### 0x07 Scanning for single modules

Please use the name supported by the module for the root folder. A folder name corresponds to a module, and please pay attention to capitalization. It is really incomprehensible. Please refer to [in this file](https://www.ascotbe.com/Medusa/Documentation/#/PluginDirectory) name

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -m Struts2
```

#### 0x08 Threads setting

Any function can turn on multi-threading !

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -t 100 #100 threads
```

#### 0x09 sensitive information leakage

Integrated into the module, the full scan is automatically started, if you need to scan separately, you only need to enter the module name



## Result

1. The output `The number of vulnerabilities scanned was: 0` means that the vulnerability was not scanned

2. There are no other files in the `ScanResult` directory except `Medusa.txt`

3. There is no new content in the `Medusa.db` file, or the file is not created

4. If none of the above three points exist, it means that no loopholes really have been found

