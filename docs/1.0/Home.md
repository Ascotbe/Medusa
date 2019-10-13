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

## 关于美杜莎扫描器
    最初版本上线，目前扫描器还在开发中，不完善的地方欢迎大家提Issues
    独自开发更新会比较缓慢，各位师傅不嫌弃的话可以点个Star支持下
## ​Demo



## 使用说明

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
## 参数说明
| 命令   | 参数个数 | 作用                                                         | 备注                                                         |
| ------ |--------  | ------------------------------------------------------------ | ------------------------------------------------------------ |
| -u     | 1        | 输入单个目标url（最好使用http://或https://作为开头,并且后面别跟参数 | https://www.baidu.com  or https://192.168.0.1 |
| -o     | 1        | 你想要输入到那个文件里面，如果没有输入该位置，则默认值将写入根目录 | 无  |
| -p     | 0        | 是否启用全局代理功能(后面不需要跟参数                        | 无 |
| -a     | 1        | 指定头文件或使用随机头                                       | 支持类型(需要小写):firefox,ie,msie,opera,chrome,AppleWebKit,Gecko,safari |
| -f     | 1        | 需要批量扫描目标url所在文件名字                              | -u和-f只能存在一个，并且必须存在一个                         |
| -n     | 1        | nmap扫描哪些端口                                             | 默认1-65535，并且支持批量扫描                                |
| -sp    | 1        | 爆破数据库的密码字典                                         | 如果输入-sp和-su并且其中一个值为空，则使用默认密码爆破       |
| -su    | 1        | 爆破数据库的用户字典                                         | 无                                                           |
| -j     | 0        | 通过URL中的JS文件深度爬取里面的URL链接以及子域名             | 从Threezh1项目中魔改而来                                     |
| -s     | 0        | 通过DNS以及各大搜索引擎查找子域名                            | 从Sublist3r魔改而来,不支持IP枚举                             |
| -se    | 0        | 包含了-s的功能，并且通过字典枚举(非常耗时                    | 和-s不能同时使用，-s和-se只能存在一个                        |

## 讨论区

- 吹B群：690021184
- GitHub issue:https://github.com/Ascotbe/Medusa/issues

