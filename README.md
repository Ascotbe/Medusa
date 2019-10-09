<img src="https://github.com/Ascotbe/Medusa/blob/master/MedusaScan.png?raw=true" width="1500" alt="MedusaScan" /> 
 <p align="center">
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-Medusa%20Scan-green"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/python-3.6-blueviolet"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.22-red"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
	<a href="https://github.com/ascotbe/Medusa/stargazers"><img alt="Release" src="https://img.shields.io/github/stars/ascotbe/Medusa.svg"></a>
 </p>

<h1 align="center" >美杜莎扫描器</h1>



**请使用者遵守 [中华人民共和国网络安全法](http://www.cac.gov.cn/2016-11/07/c_1119867116.htm)，勿将MedusaScan用于非授权的测试，MedusaScan开发者不负任何连带法律责任。**

### 关于美杜莎扫描器
    最初版本上线，目前扫描器还在开发中，不完善的地方欢迎大家提Issues
	独自开发更新会比较缓慢，各位师傅不嫌弃的话可以点个Star支持下
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
### 待更新功能
     基于各大网站进行泄露信息收集
     目录扫描
     CMS指纹识别后优先调用前5的CmsPayload
     自动化XSS测试
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
|-n    |--NmapScanRange   |1       |nmap扫描哪些端口|默认1-65535，并且支持批量扫描| 
|-sp    |--SqlPasswrod   |1       |爆破数据库的密码字典|如果输入-sp和-su并且其中一个值为空，则使用默认密码爆破| 
|-su    |--SqlUser   |1       |爆破数据库的用户字典|无| 
|-j    |--JavaScript   |0       |通过URL中的JS文件深度爬取里面的URL链接以及子域名|从Threezh1项目中魔改而来| 
|-s    |--Subdomain   |0       |通过DNS以及各大搜索引擎查找子域名|从Sublist3r魔改而来,不支持IP枚举| 
|-se    |--SubdomainEnumerate   |0       |包含了-s的功能，并且通过字典枚举(非常耗时|和-s不能同时使用，-s和-se只能存在一个| 

### 提交意见&BUG
    欢迎大家提交Issues
    交流Q群690021184

### 参与开发
    POC编写文档:
    https://github.com/Ascotbe/Medusa/VulnerabilityTemplate/v0.1.md

#### 封面作者
<a href="https://github.com/czkm"><img alt="Release" src="https://avatars2.githubusercontent.com/u/36911813?s=460&v=4"  width="50"></a>
#### 共同开发
<a href="https://github.com/ZiYuMis"><img alt="Release" src="https://avatars2.githubusercontent.com/u/33992514?s=400&v=4"  width="50"></a>
<a href="https://github.com/czkm"><img alt="Release" src="https://avatars2.githubusercontent.com/u/36911813?s=460&v=4"  width="50"></a>
<a href="https://github.com/TrojanAZhen"><img alt="Release" src="https://avatars2.githubusercontent.com/u/15818542?s=460&v=4"  width="50"></a>
<a href="https://github.com/rabbitmask"><img alt="Release" src="https://avatars0.githubusercontent.com/u/37649548?s=460&v=4"  width="50"></a>

[肥宅博客](https://ascotbe.github.io)


[更新日志](/UpDataLog/README.md)


