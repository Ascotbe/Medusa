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

![debug](https://github.com/Ascotbe/Random-img/blob/master/Medusa/0.76Debug.gif?raw=true)

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

#### 0x04 对目标网站进行子域名收集

扫描结果在`ScanResult`目录中，只支持域名不支持**IP**形式

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -s
```

#### 0x05 开启代理功能

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -p 127.0.0.1:8080
```

#### 0x06 使用指定Header头

支持的参数有：`firefox`，`ie`，`msie`，`opera`，`chrome`，`AppleWebKit`，`Gecko`，`safari `

目前支持常见的浏览器，下面列举其中3个(需要区分大小写)

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -a firefox
python3 MedusaScan.py -u https://www.ascotbe.com -a ie
python3 MedusaScan.py -u https://www.ascotbe.com -a Gecko
```

还可以自定义`haeder`参数，切记需要对自定义的`header`加上双引号包含着`""`，如果你的`header`不合规是不会提示错误的

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -a "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36"
```

#### 0x07 针对单独模块扫描

该模块所支持的名称请针对根目录文件夹使用，一个文件夹名对应一个模块，并且请注意大小写，实在无法理解请参考[该文件中](https://www.ascotbe.com/Medusa/Documentation/#/PluginDirectory)名称进行使用

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -m Struts2
```

#### 0x08 设置进程数

开启多进程功能，默认是15个进程，进程越多越快，当某个插件有利用for循环的话会在进程中启动多线程！

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -t 100
```

#### 0x09 敏感信息泄露

以集成到模块中，全量扫描自动开启，如果需要单独扫描只需要输入模块名字即可

#### 0x10 交互式命令执行

调用可以进行命令执行交互的插件，可以利用`-l`（目前还没写）参数查看

```bash
python3 MedusaScan.py -u http://127.0.0.1:7001 -e CVE-2019-2729
```

调用成功后会需要首先输入目标操作系统，然后再输入执行的命令，如果改执行是无回显的话会输出`Return packet：The vulnerability is command execution without echo`这句话，如果没有的话就是有回显执行。

如果需要退出的话请输入`QuitMedusa` ，即可退出命令执行。

```bash
ascotbe@orange$ python3 MedusaScan.py -u http://127.0.0.1:7001 -e CVE-2019-2729



  ___ __ __   ______   ______   __  __   ______   ________      
 /__//_//_/\ /_____/\ /_____/\ /_/\/_/\ /_____/\ /_______/\     
 \::\| \| \ \\::::_\/_\:::_ \ \\:\ \:\ \\::::_\/_\::: _  \ \    
  \:.      \ \\:\/___/\\:\ \ \ \\:\ \:\ \\:\/___/\\::(_)  \ \   
   \:.\-/\  \ \\::___\/_\:\ \ \ \\:\ \:\ \\_::._\:\\:: __  \ \  
    \. \  \  \ \\:\____/\\:\/.:| |\:\_\:\ \ /____\:\\:.\ \  \ \ 
     \__\/ \__\/ \_____\/ \____/_/ \_____\/ \_____\/ \__\/\__\/ 
                                                                
 
                                                                                   
          Blog  https://www.ascotbe.com  |  v0.86    

[ + ] Please enter the target operating system [windows / linux]: Windows
[ + ] Please enter the command to be executed: echo Ayanami Rei
[ + ] Command sent successfully, please refer to the returned data packet
[ + ] Return packet：Ayanami Rei
[ + ] Please enter the command to be executed: QuitMedusa
[ ! ] Command execution call has ended~ 
```



## 扫描结果

1.输出`The number of vulnerabilities scanned was:0`就表示未扫描到漏洞

2.`ScanResult`目录中除`Medusa.txt`外无别的文件

3.`Medusa.db`文件中也无新增内容，或者未创建该文件

4.如果以上三点都不存在的话就表示真的没有找到漏洞

