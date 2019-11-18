<img src="https://github.com/Ascotbe/Medusa/blob/master/MedusaScan.png?raw=true" width="1500" alt="MedusaScan" /> 
 <p align="center">
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-Medusa%20Scan-green"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/python-3.6-blueviolet"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.39-red"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
	<a href="https://github.com/ascotbe/Medusa/stargazers"><img alt="Release" src="https://img.shields.io/github/stars/ascotbe/Medusa.svg"></a>
 </p>

<h1 align="center" >美杜莎扫描器</h1>


**请使用者遵守 [中华人民共和国网络安全法](http://www.cac.gov.cn/2016-11/07/c_1119867116.htm)，勿将MedusaScan用于非授权的测试，MedusaScan开发者不负任何连带法律责任。**

### 关于美杜莎扫描器
    目前对功能进行停止更新，有新的POC会照常更新。
    主要是对版本进行重构，POC插件进行优化，并更新Web版本，敬请期待~
    由于重构导致CMS模块扫描不准确后面会删了重写
    各位师傅不嫌弃的话可以点个Star支持下

### 使用文档
    使用前必看！！！
    https://www.ascotbe.com/Medusa

### 使用说明

```bash
# 安装工具(ubuntu
apt-get install nmap
# 下载文件
git clone https://github.com/Ascotbe/Medusa.git
cd Medusa
# 安装依赖
pip install -r Medusa.txt
# 使用扫描器
python3 MedusaScan.py -u www.ascotbe.com
```
### 参数说明
|短形式|长形式     |参数个数|作用                              |备注                           |
|------|-----------|--------|----------------------------------|-------------------------------|
|-u    |--url    |1       |输入单个目标url（最好使用http://或https://作为开头,并且后面别跟参数 |https://www.baidu.com  or https://192.168.0.1         |
|-o    |--OutFileName|1       |你想要输入到那个文件里面，如果没有输入该位置，则默认值将写入根目录|无  |
|-p    |--Proxy   |0       |是否启用全局代理功能(后面不需要跟参数      |无 |
|-a    |--agent   |1       |指定头文件或使用随机头|支持类型(需要小写):firefox,ie,msie,opera,chrome,AppleWebKit,Gecko,safari|
|-f    |--InputFileName   |1       |需要批量扫描目标url所在文件名字|-u和-f只能存在一个，并且必须存在一个|
|-t    |--ThreadNumber   |1       |设置线程数，默认线程数15|
|-sp    |--SqlPasswrod   |1       |爆破数据库的密码字典|如果输入-sp和-su并且其中一个值为空，则使用默认密码爆破|
|-su    |--SqlUser   |1       |爆破数据库的用户字典|无|
|-j    |--JavaScript   |0       |通过URL中的JS文件深度爬取里面的URL链接以及子域名|从Threezh1项目中魔改而来|
|-s    |--Subdomain   |0       |通过DNS以及各大搜索引擎查找子域名|从Sublist3r魔改而来,不支持IP枚举|
|-se    |--SubdomainEnumerate   |0       |包含了-s的功能，并且通过字典枚举(非常耗时|和-s不能同时使用，-s和-se只能存在一个|

### 功能列表
    1.CMS漏洞扫描
    2.各种中间件漏洞扫描
    3.子域名收集
    4.JS信息探测
    5.Nmap端口扫描
    6.数据库爆破
    7.随机Header
    8.使用代理进行扫描
    9.信息泄露探测
    10.OA系统漏洞扫描

### 提交意见&BUG
    欢迎大家提交Issues


[肥宅博客](https://www.ascotbe.com)


[更新日志](/UpDataLog/README.md)


