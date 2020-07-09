<img src="https://github.com/Ascotbe/Medusa/blob/master/Medusa.png?raw=true" width="1500" alt="Medusa" /> 

 <p align="center">
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-Medusa-green"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/python-3.7+-blueviolet"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.87-red"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
	<a href="https://github.com/ascotbe/Medusa/stargazers"><img alt="Release" src="https://img.shields.io/github/stars/ascotbe/Medusa.svg"></a>
	<a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Plugin-200+-success"></a>
 </p>

<h1 align="center" >Welcome to Medusa</h1>

**请使用者遵守 [中华人民共和国网络安全法](http://www.cac.gov.cn/2016-11/07/c_1119867116.htm)，勿将Medusa项目用于非授权的测试，Medusa项目开发者不负任何连带法律责任。**

### :point_right:About `Medusa`

> The project is licensed under `GPL`.Free for non-commercial use.
>
> The project development manpower is insufficient. If you find a problem or have comments, please contact us.
>
> `bash` Ver. Online
>
> `Bot` Ver. Online
>
> `Web` Ver. Under development

#### **[中文文档](https://github.com/Ascotbe/Medusa/blob/master/README.CN.md) | EnglishDocumentation**

### :bulb:Document

```
http://medusa.ascotbe.com
```

### :mag_right:Bug coverage list

```
http://medusa.ascotbe.com/Documentation/#/PluginDirectory
```

### :space_invader:Demo

![demo](https://github.com/Ascotbe/Random-img/blob/master/Medusa/demo.gif?raw=true)


### :book:`Bash` Ver. instructions for use

```bash
# clone project files(example for ubuntu
git clone https://github.com/Ascotbe/Medusa.git
cd Medusa
# Install python packages
pip3 install -r Medusa.txt
# Use the scanner
python3 MedusaScan.py -u www.ascotbe.com
```

### :rocket:Git proxy

```bash
# If download speed too slow when cloning, then you can use proxy. 
# Global proxy setting
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
```

### :clipboard:Parameters

| Command | Number of parameters | Effect                                                         | Annotation                                                         |
| ---- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| -u   | 1        | Input single url（Use `http://` or `https://` first better than none, do not use any paremeters follow the url | example : `-u https://www.ascotbe.com` or `-u https://192.168.0.1`           |
| -a   | 1        | Specify header files or use random headers                                       | When using this feature, please refer to the documentation for this content |
| -f   | 1        | The filename includes urls that want to scan.                              | `-u` or `-f` must exists one and only one                         |
| -p | 1 | You need to fill in the IP of your proxy, if you have a port you need to bring the port | to use BURP as a proxy then you should pass in 127.0.0.1:8080 |
| -m   | 1        | Scan for single module,such as: Struts2 or Apache, etc.                  | The specific content can be entered by the corresponding name in the project Modules folder. |
| -t   | 1        | Processes usage setting, default(-t 15)                                    |                                                           None   |
|-s    |1       | Enable subdomain detection| |
|-l    |0       | List interactive command execution plugins| This function has not been written yet|
|-e    |1       | You need to use the vulnerability, please use -l to query| |

### :green_book:`Bot` Ver. document

```html
# How to use BOT, please look at the connection
http://medusa.ascotbe.com/EnglishDocumentation/#/Bot
```

### :four_leaf_clover:Updating logs

```
http://medusa.ascotbe.com/Documentation/#/UpDataLog
```

### :open_file_folder:Bug replicate document

```
https://www.ascotbe.com/Loophole
```


### :green_heart:Discussion

- If you find that the corresponding vulnerability cannot be scanned by the plug-in, please submit the [Bug] issue
- If you have any problems that cannot be solved by the documentation, please submit an issue of [help]
- If you have any good comments or ideas, please submit [idea] issue
- QQ group：**690021184**（Secret code：**6CF2D42B629E5AA4E6C293B290798878**）

### :palm_tree:Contributors

![commit](https://opencollective.com/Medusa/contributors.svg?width=890&button=false)


### :checkered_flag:Timeline

![star](https://starchart.cc/Ascotbe/Medusa.svg)

