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

## 关于美杜莎

> 本项目使用 `GPL`协议，未经授权，禁止使用商业用途。
>
> `bash`版已上线
>
> `Bot`版本已上线
>
> `Web`版开发中，敬请期待~

## Demo

<img alt="Release" src="https://github.com/Ascotbe/Random-img/blob/master/Medusa/demo.gif?raw=true"  >

## 复现文档

> `https://www.ascotbe.com/Loophole`

## 使用说明

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
## 参数说明

| 命令 | 参数个数 | 作用                                                         | 备注                                                         |
| ---- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| -u   | 1        | 输入单个目标url（最好使用http:// 或 https:// 作为开头,并且后面别跟参数 | https://www.ascotbe.com  or https://192.168.0.1                |
| -a   | 1        | 指定头文件或使用随机头                                       | 具体使用参考使用文档 |
| -f   | 1        | 需要批量扫描目标url所在文件名字                              | -u和-f只能存在一个，并且必须存在一个                         |
| -p   | 1        | 需要填入你代理的IP，如果有端口的话也需要带上端口             | 以使用BURP作为代理那么就该传入 127.0.0.1:8080                |
| -m   | 1        | 针对单独的模块进行扫描比如Struts2、Apache等                  | 具体内容可以通过项目文件夹来输入                             |
| -t   | 1        | 设置进程数                                  |    默认进程数15                                                           |
|-s    |1       |开启子域名探测| |
|-l    |0       |列出可以交互的插件| 该功能暂时没写 |
|-e    |1       |您需要使用那个漏洞，具体请使用-l查询| |

## 讨论区

- 吹B群：690021184（加群请输入暗号：6CF2D42B629E5AA4E6C293B290798878）
- [GitHub issue](https://github.com/Ascotbe/Medusa/issues)

