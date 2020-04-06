<img src="https://github.com/Ascotbe/Medusa/blob/master/Medusa.png?raw=true" width="1500" alt="MedusaScan" /> 

 <p align="center">
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-Medusa%20Scan-green"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/python-3.7+-blueviolet"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.77-red"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
	<a href="https://github.com/ascotbe/Medusa/stargazers"><img alt="Release" src="https://img.shields.io/github/stars/ascotbe/Medusa.svg"></a>
	<a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Plugin-200+-success"></a>
 </p>

<h1 align="center" >Medusa Scan</h1>


**请使用者遵守 [中华人民共和国网络安全法](http://www.cac.gov.cn/2016-11/07/c_1119867116.htm)，勿将Medusa项目用于非授权的测试，Medusa项目开发者不负任何连带法律责任。**

### About `Medusa Scan`

> The project is licensed under `GPL`.Free for non-commercial use.
>
> `bash` Ver. Online
>
> `Bot` Ver. Online
>
> `Web` Ver. Under development

#### **[中文文档](https://github.com/Ascotbe/Medusa/blob/master/README.CN.md) | EnglishDocumentation**

### Instructions for install and use

#### Document

```
http://medusa.ascotbe.com
```

#### Bug coverage list

```
http://medusa.ascotbe.com/Documentation/#/PluginDirectory
```

#### Demo

![demo](https://github.com/Ascotbe/Random-img/blob/master/Medusa/0.76.gif?raw=true)


#### `Bash` Ver. instructions for use

```bash
# Need nmap(example for ubuntu
apt-get install nmap
# clone project files
git clone https://github.com/Ascotbe/Medusa.git
cd Medusa
# Install python packages
pip3 install -r Medusa.txt
# Use the scanner
python3 MedusaScan.py -u www.ascotbe.com
```

#### Git proxy

```bash
# If download speed too slow when cloning, then you can use proxy. 
# Global proxy setting
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
```

### Parameters

| Command | Number of parameters | Effect                                                         | Annotation                                                         |
| ---- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| -u   | 1        | Input single url（Use `http://` or `https://` first better than none, do not use any paremeters follow the url | example : `-u https://www.ascotbe.com` or `-u https://192.168.0.1`           |
| -a   | 1        | Specify header files or use random headers                                       | When using this feature, please refer to the documentation for this content |
| -f   | 1        | The filename includes urls that want to scan.                              | `-u` or `-f` must exists one and only one                         |
| -m   | 1        | Scan for single module,such as: Struts2 or Apache, etc.                  | The module list refers to the list of folders on this project.                           |
| -t   | 1        | Threads usage setting, default(-t 15)                                    |                                                           None   |
| -sp  | 1        | Brute-force cracking by password dictionary                                         | If input -sp and -su, scanner use default dictionary when either one of them that value is null.        |
| -su  | 1        | The dictionary for brute-force database                                         | None                                                           |
| -s   | 0        | Subdomain search by DNS and search engine                           | Mod by `Sublist3r`, IP enumerate not support.                             |
| -se  | 0        | Contains `-s` funcitons, in addtional, enumerate by dictionary(time consuming)                     | can not use this with `-s` at the same time.                         |


### Bug replicate document


### `Bot` Ver. document

```bash
# clone project files
git clone https://github.com/Ascotbe/Medusa.git
cd Medusa
# Install python packages
pip3 install -r Medusa.txt
# Configuring look at BOT document
https://www.ascotbe.com/Medusa
```

### Updating logs

```
http://medusa.ascotbe.com/Documentation/#/UpDataLog
```

### Bug replicate document

```
https://www.ascotbe.com/Loophole
```


### Discussion

- QQ group：**690021184**（Secret code：**6CF2D42B629E5AA4E6C293B290798878**）
- GitHub issue

### Friend links

- [零组资料库](http://www.0-sec.org)

### Contributors

![commit](https://opencollective.com/Medusa/contributors.svg?width=890&button=false)


### Timeline

![star](https://starchart.cc/Ascotbe/Medusa.svg)

