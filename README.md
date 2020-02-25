<img src="https://github.com/Ascotbe/Medusa/blob/master/Medusa.png?raw=true" width="1500" alt="MedusaScan" /> 

 <p align="center">
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-Medusa%20Scan-green"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/python-3.6-blueviolet"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.72-red"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
	<a href="https://github.com/ascotbe/Medusa/stargazers"><img alt="Release" src="https://img.shields.io/github/stars/ascotbe/Medusa.svg"></a>
	<a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Plugin-200+-success"></a>
 </p>

<h1 align="center" >美杜莎扫描器</h1>


**请使用者遵守 [中华人民共和国网络安全法](http://www.cac.gov.cn/2016-11/07/c_1119867116.htm)，勿将Medusa项目用于非授权的测试，Medusa项目开发者不负任何连带法律责任。**

### 关于美杜莎扫描器

>本项目使用 `GPL`协议，未经授权，禁止使用商业用途。
>
>正在构思Web版本，敬请期待~
>
>各位师傅不嫌弃的话可以点个Star支持下

### 使用文档（必看）
> `https://www.ascotbe.com/Medusa`

### 复现文档

> `https://www.ascotbe.com/Loophole`

### Demo

![demo](https://github.com/Ascotbe/Random-img/blob/master/Medusa/demo2.gif?raw=true)


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
### 加速下载

```bash
# 如果下载太慢可以使用代理，需要本地开启SSR，让流量走本地端口，端口为你SSR开的端口
# 全局代理
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
# 只对github使用代理，国内厂库无影响
git config --global http.https://github.com.proxy https://127.0.0.1:1080
git config --global https.https://github.com.proxy https://127.0.0.1:1080
# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy
```



### 参数说明

|短形式|长形式     |参数个数|作用                              |备注                           |
|------|-----------|--------|----------------------------------|-------------------------------|
|-u    |--url    |1       |输入单个目标url（最好使用http://或https://作为开头,并且后面别跟参数 |https://www.baidu.com  or https://192.168.0.1         |
|-a    |--agent   |1       |指定头文件或使用随机头|支持类型(需要小写):firefox,ie,msie,opera,chrome,AppleWebKit,Gecko,safari|
|-f    |--InputFileName   |1       |需要批量扫描目标url所在文件名字|-u和-f只能存在一个，并且必须存在一个|
|-t    |--ThreadNumber   |1       |设置线程数，默认线程数15||
|-sp    |--SqlPasswrod   |1       |爆破数据库的密码字典|如果输入-sp和-su并且其中一个值为空，则使用默认密码爆破|
|-su    |--SqlUser   |1       |爆破数据库的用户字典|无|
|-s    |--Subdomain   |0       |通过DNS以及各大搜索引擎查找子域名|从Sublist3r魔改而来,不支持IP枚举|
|-se    |--SubdomainEnumerate   |0       |包含了-s的功能，并且通过字典枚举(非常耗时|和-s不能同时使用，-s和-se只能存在一个|

### 提交意见&BUG
- 吹B群：**690021184**
- GitHub issue:https://github.com/Ascotbe/Medusa/issues

### 感谢贡献

![commit](https://opencollective.com/Medusa/contributors.svg?width=890&button=false)

### :alarm_clock:共同开发:alarm_clock:

```
目前需要前端和后端大佬的支持
```

[更新日志](https://www.ascotbe.com/Medusa/2.0/#/UpDataLog)


