<img src="https://github.com/Ascotbe/Medusa/blob/master/MedusaScan.png?raw=true" width="1500" alt="MedusaScan" /> 

 <p align="center">
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-Medusa%20Scan-green"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/python-3.6-blueviolet"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.54-red"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
	<a href="https://github.com/ascotbe/Medusa/stargazers"><img alt="Release" src="https://img.shields.io/github/stars/ascotbe/Medusa.svg"></a>
	<a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Plugin-200+-success"></a>
 </p>

<h1 align="center" >美杜莎扫描器</h1>


**请使用者遵守 [中华人民共和国网络安全法](http://www.cac.gov.cn/2016-11/07/c_1119867116.htm)，勿将MedusaScan用于非授权的测试，MedusaScan开发者不负任何连带法律责任。**

### 关于美杜莎扫描器

>本项目使用 `GPL`协议，未经授权，禁止使用商业用途。
>
>目前主要是更新Web版本，敬请期待~
>
>各位师傅不嫌弃的话可以点个Star支持下

### 使用文档（必看）
> `https://www.ascotbe.com/Medusa`

### 复现文档

> `https://www.ascotbe.com/Loophole`

## Demo

![demo](https://github.com/Ascotbe/Random-img/blob/master/Medusa/demo.gif?raw=true)


### 使用说明

```bash
# 安装工具(ubuntu
apt-get install nmap
# 下载文件
git clone https://github.com/Ascotbe/Medusa.git
cd Medusa
# 安装依赖
pip3 install -r Medusa.txt
# 使用扫描器
python3 MedusaScan.py -u www.ascotbe.com
```
### 参数说明
|短形式|长形式     |参数个数|作用                              |备注                           |
|------|-----------|--------|----------------------------------|-------------------------------|
|-u    |--url    |1       |输入单个目标url（最好使用http://或https://作为开头,并且后面别跟参数 |https://www.baidu.com  or https://192.168.0.1         |
|-o    |--OutFileName|1       |你想要输入到那个文件里面，如果没有输入该位置，则默认值将写入根目录|无  |
|-a    |--agent   |1       |指定头文件或使用随机头|支持类型(需要小写):firefox,ie,msie,opera,chrome,AppleWebKit,Gecko,safari|
|-f    |--InputFileName   |1       |需要批量扫描目标url所在文件名字|-u和-f只能存在一个，并且必须存在一个|
|-t    |--ThreadNumber   |1       |设置线程数，默认线程数15||
|-sp    |--SqlPasswrod   |1       |爆破数据库的密码字典|如果输入-sp和-su并且其中一个值为空，则使用默认密码爆破|
|-su    |--SqlUser   |1       |爆破数据库的用户字典|无|
|-j    |--JavaScript   |0       |通过URL中的JS文件深度爬取里面的URL链接以及子域名|从Threezh1项目中魔改而来|
|-s    |--Subdomain   |0       |通过DNS以及各大搜索引擎查找子域名|从Sublist3r魔改而来,不支持IP枚举|
|-se    |--SubdomainEnumerate   |0       |包含了-s的功能，并且通过字典枚举(非常耗时|和-s不能同时使用，-s和-se只能存在一个|

### 功能列表
- `CMS`漏洞扫描
- 各种中间件漏洞扫描
- 子域名收集
- `JS`信息探测
- `Nmap`端口扫描
- 数据库爆破
- 随机`Header`
- ~~使用代理进行扫描~~
- 信息泄露探测
- `OA`系统漏洞扫描

### 提交意见&BUG
    欢迎大家提交Issues

### :alarm_clock:寻基友:alarm_clock:

```
找个几个前端大佬和后端大佬，我自己一个有点时间不够
```

[更新日志](https://www.ascotbe.com/Medusa/2.0/#/UpDataLog)


