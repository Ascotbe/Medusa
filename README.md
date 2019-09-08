<img src="https://github.com/Ascotbe/Medusa/blob/master/MedusaScan.png?raw=true" width="1500" alt="MedusaScan" /> 
 <p align="center">
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-Medusa%20Scan-green"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/python-3.6-blueviolet"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.16-red"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
 </p>

<h1 align="center" >美杜莎扫描器</h1>


    最初版本上线，不完善的地方欢迎大家提Issues

**请使用者遵守 [中华人民共和国网络安全法](http://www.cac.gov.cn/2016-11/07/c_1119867116.htm)，勿将MedusaScan用于非授权的测试，MedusaScan开发者不负任何连带法律责任。**

### 关于美杜莎扫描器
	美杜莎扫描器是集漏洞扫描和端口扫描以及敏感信息收集等功能为一体的扫描器
	
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
python3 MedusaScan.py -u 192.168.0.1
```
### 参数说明
    -u 输入单个目标url（最好使用http://或https://作为开头,并且后面别跟参数
                        例如:https://www.baidu.com  or https://192.168.0.1
    -o 你想要输入到那个文件里面，如果没有输入该位置，则默认值将写入根目录
    -p 是否启用全局代理功能(后面不需要跟参数
    -a 指定头文件或使用随机头（支持类型(需要小写):firefox,ie,msie,opera,chrome,AppleWebKit,Gecko,safari
                               输入错误，乱输入，不输入都会默认使用随机header
    -f 需要批量扫描目标url所在文件名字(-u和-f只能存在一个，并且必须存在一个
    -n nmap扫描哪些端口(默认1-65535，并且支持批量扫描
    -sp 爆破数据库的密码字典
    -su 爆破数据库的用户字典（如果输入-sp和-su并且路径都对，则正常运行
                              如果输入-sp和-su并且其中一个值为空，则使用默认密码爆破

							  
### 提交意见&BUG
    欢迎大家提交Issues

### 参与开发
    等框架完善并且模板写出来后，欢迎大家贡献宝贵的代码

#### 封面作者
<a href="https://github.com/czkm"><img alt="Release" src="https://avatars2.githubusercontent.com/u/36911813?s=460&v=4"  width="50"></a>

[肥宅博客](https://ascotbe.github.io)   


[更新日志](/UpDataLog/README.md)

[插件模板]()