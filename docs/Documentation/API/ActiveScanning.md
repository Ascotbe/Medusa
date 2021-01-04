### 扫描任务下发接口

`/api/vulnerability_scanning` 用来下发任务，如果下发成功返回**200**

```json
{
	"url": "www.ascotbe.com",
	"token": "XXXXXXXXXXXXXXXX",
	"process": 200,
	"module": "all",
	"header": "",
	"proxy": "127.0.0.1:8080"
}
```

> 参数解释

- `url` 你扫描的目标
- `token` 登录后返回给你的**token**
- `process`当前任务使用的进程树
- `module`指定扫描模块，具体名称参考**Modules**目录下的文件名
- `header`自定义头，如果没有的话传入`""`即可，如果想要自定义请传入完整的header以字典的形式传入，当传入`""`的值的时候会默认使用**config.py**文件中的配置
- `proxy`该任务指定代理，如果没有代理该值直接传入`""` 即可，注意代理是否可用，当传入`""`的值的时候会默认使用**config.py**文件中的配置

> 返回状态码

- 169：莎酱被玩坏掉嘞QAQ
- 200：任务下发成功👌
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 666：类型错误！

### 主动扫描目标列表查询接口

`/api/active_scan_list_query` 用来查询用户下发了哪些任务列表，返回结果是**JSON**格式

```json
{
	"token": "XXXXX"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：莎酱被玩坏啦(>^ω^<)喵

- 200：返回扫描列表信息

  ```json
  {
  	"message": [{
  		"active_scan_id": 1,
  		"url": "http://127.0.0.1:8000",
  		"creation_time": "1609054280",
  		"proxy": "None",
  		"status": "0",
  		"process": "2",
  		"module": "BIG-IP"
  	}, {
  		"active_scan_id": 2,
  		"url": "http://127.0.0.1:8000",
  		"creation_time": "1609054345",
  		"proxy": "None",
  		"status": "1",
  		"process": "2",
  		"module": "BIG-IP"
  	}, {
  		"active_scan_id": 3,
  		"url": "http://127.0.0.1:8000",
  		"creation_time": "1609054565",
  		"proxy": "None",
  		"status": "1",
  		"process": "2",
  		"module": "BIG-IP"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  **会有多个数组的集合**

  - `active_scan_id`任务ID
  - `url`目标连接
  - `creation_time`任务创建时间
  - `proxy`是否使用代理
  - `status`任务状态，1表示已解释，0表示正在扫描
  - `process`使用进程数
  - `module`使用的模块名称

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 404：数据库出问题了🐈

- 500：请使用Post请求

###  主动扫描目标漏洞列表查询接口

`/api/scan_information_query` 用来查询用户某个任务漏洞列表，返回结果是`JSON`格式

```json
{
	"token": "XXXXX",
	"active_scan_id":"1"
}
```

>参数解释

- `token`登录后返回的**token**
- `active_scan_id`目标的**active_scan_id**值，上个接口查询返回中存在

> 返回状态码

- 169：莎酱被玩坏啦ヽ(･ω･´ﾒ)

- 200：返回关系查询列表结果

  ```json
  {
  	"message": [{
  		"url": "http://127.0.0.1:8000",
  		"scan_info_id": "1",
  		"rank": "\u9ad8\u5371",
  		"name": "BIG_IP\u8fdc\u7a0b\u4ee3\u7801\u6267\u884c\u6f0f\u6d1e"
  	}, {
  		"url": "http://127.0.0.1:8000",
  		"scan_info_id": "2",
  		"rank": "\u9ad8\u5371",
  		"name": "BIG_IP\u8fdc\u7a0b\u4ee3\u7801\u6267\u884c\u6f0f\u6d1e"
  	}, {
  		"url": "http://127.0.0.1:8000",
  		"scan_info_id": "3",
  		"rank": "\u9ad8\u5371",
  		"name": "BIG_IP\u8fdc\u7a0b\u4ee3\u7801\u6267\u884c\u6f0f\u6d1e"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  **会有多个数组的集合**

  - `url`目标连接
  - `scan_info_id`扫描详情ID值，用来查询具体漏洞信息
  - `rank`漏洞等级
  - `name`漏洞名称

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 404：数据库炸了BOOM~🐈

- 500：请使用Post请求

### 主动扫描目标单个漏洞详细内容查询接口

`/api/medusa_query`用来查询某个任务中某个漏洞详细信息，返回结果是`JSON`格式

```json
{
	"token": "XXXXX",
	"scan_info_id":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `scan_info_id`目标的**scan_info_id**值，上个接口查询返回中存在

> 返回状态码

- 169：莎酱被玩坏啦ヾ(=･ω･=)o

- 200：返回数据库单个漏洞查询结果

  ```json
  {
  	"message": [{
  		"scan_info_id": 3,
  		"url": "http://127.0.0.1:8000",
  		"name": "BIG_IP\u8fdc\u7a0b\u4ee3\u7801\u6267\u884c\u6f0f\u6d1e",
  		"affects": "BIG-IP",
  		"rank": "\u9ad8\u5371",
  		"suggest": "\u5347\u7ea7\u6700\u65b0BIG-IP\u7248\u672c",
  		"desc_content": "\u672a\u6388\u6743\u7684\u8fdc\u7a0b\u653b\u51fb\u8005\u901a\u8fc7\u5411\u6f0f\u6d1e\u9875\u9762\u53d1\u9001\u7279\u5236\u7684\u8bf7\u6c42\u5305\uff0c\u53ef\u4ee5\u9020\u6210\u4efb\u610f Java \u4ee3\u7801\u6267\u884c\u3002\u8fdb\u800c\u63a7\u5236 F5 BIG-IP \u7684\u5168\u90e8\u529f\u80fd\uff0c\u5305\u62ec\u4f46\u4e0d\u9650\u4e8e: \u6267\u884c\u4efb\u610f\u7cfb\u7edf\u547d\u4ee4\u3001\u5f00\u542f/\u7981\u7528\u670d\u52a1\u3001\u521b\u5efa/\u5220\u9664\u670d\u52a1\u5668\u7aef\u6587\u4ef6\u7b49\u3002\u8be5\u6f0f\u6d1e\u5f71\u54cd\u63a7\u5236\u9762\u677f\u53d7\u5f71\u54cd\uff0c\u4e0d\u5f71\u54cd\u6570\u636e\u9762\u677f\u3002",
  		"details": "aHR0cDovLzEyNy4wLjAuMTo4MDAwIOWtmOWcqEJJR19JUOi/nOeoi+S7o+eggeaJp+ihjOa8j+a0nihDVkUtMjAyMC01OTAyKQ0K6aqM6K+B5pWw5o2uOg0K5L2/55SoUE9DOmh0dHA6Ly8xMjcuMC4wLjE6ODAwMC90bXVpL2xvZ2luLmpzcC8uLjsvdG11aS9sb2NhbGxiL3dvcmtzcGFjZS9maWxlUmVhZC5qc3A/ZmlsZU5hbWU9L2V0Yy9wYXNzd2QNCui/lOWbnuaVsOaNruWMhTo8IURPQ1RZUEUgSFRNTCBQVUJMSUMgIi0vL1czQy8vRFREIEhUTUwgNC4wMS8vRU4iCiAgICAgICAgImh0dHA6Ly93d3cudzMub3JnL1RSL2h0bWw0L3N0cmljdC5kdGQiPgo8aHRtbD4KICAgIDxoZWFkPgogICAgICAgIDxtZXRhIGh0dHAtZXF1aXY9IkNvbnRlbnQtVHlwZSIgY29udGVudD0idGV4dC9odG1sO2NoYXJzZXQ9dXRmLTgiPgogICAgICAgIDx0aXRsZT5FcnJvciByZXNwb25zZTwvdGl0bGU+CiAgICA8L2hlYWQ+CiAgICA8Ym9keT4KICAgICAgICA8aDE+RXJyb3IgcmVzcG9uc2U8L2gxPgogICAgICAgIDxwPkVycm9yIGNvZGU6IDQwNDwvcD4KICAgICAgICA8cD5NZXNzYWdlOiBGaWxlIG5vdCBmb3VuZC48L3A+CiAgICAgICAgPHA+RXJyb3IgY29kZSBleHBsYW5hdGlvbjogSFRUUFN0YXR1cy5OT1RfRk9VTkQgLSBOb3RoaW5nIG1hdGNoZXMgdGhlIGdpdmVuIFVSSS48L3A+CiAgICA8L2JvZHk+CjwvaHRtbD4KDQo=",
  		"number": "CVE-2020-5902",
  		"author": "Ascotbe",
  		"create_date": "2020-7-6",
  		"disclosure": "2020-07-3",
  		"algroup": "BIG_IPRemoteCodeExecutionVulnerability",
  		"version": "BIG-IP 15.x: 15.1.0/15.0.0\r\nBIG-IP 14.x: 14.1.0 ~ 14.1.2\r\nBIG-IP 13.x: 13.1.0 ~ 13.1.3\r\n\r\nBIG-IP 12.x: 12.1.0 ~ 12.1.5\r\n\r\nBIG-IP 11.x: 11.6.1 ~ 11.6.5",
  		"timestamp": "1609054345",
  		"active_scan_id": "2",
  		"response_headers": "eydTZXJ2ZXInOiAnU2ltcGxlSFRUUC8wLjYgUHl0aG9uLzMuNy42JywgJ0RhdGUnOiAnU3VuLCAyNyBEZWMgMjAyMCAwNzozMjoyNSBHTVQnLCAnQ29ubmVjdGlvbic6ICdjbG9zZScsICdDb250ZW50LVR5cGUnOiAndGV4dC9odG1sO2NoYXJzZXQ9dXRmLTgnLCAnQ29udGVudC1MZW5ndGgnOiAnNDY5J30=",
  		"response_text": "PCFET0NUWVBFIEhUTUwgUFVCTElDICItLy9XM0MvL0RURCBIVE1MIDQuMDEvL0VOIgogICAgICAgICJodHRwOi8vd3d3LnczLm9yZy9UUi9odG1sNC9zdHJpY3QuZHRkIj4KPGh0bWw+CiAgICA8aGVhZD4KICAgICAgICA8bWV0YSBodHRwLWVxdWl2PSJDb250ZW50LVR5cGUiIGNvbnRlbnQ9InRleHQvaHRtbDtjaGFyc2V0PXV0Zi04Ij4KICAgICAgICA8dGl0bGU+RXJyb3IgcmVzcG9uc2U8L3RpdGxlPgogICAgPC9oZWFkPgogICAgPGJvZHk+CiAgICAgICAgPGgxPkVycm9yIHJlc3BvbnNlPC9oMT4KICAgICAgICA8cD5FcnJvciBjb2RlOiA0MDQ8L3A+CiAgICAgICAgPHA+TWVzc2FnZTogRmlsZSBub3QgZm91bmQuPC9wPgogICAgICAgIDxwPkVycm9yIGNvZGUgZXhwbGFuYXRpb246IEhUVFBTdGF0dXMuTk9UX0ZPVU5EIC0gTm90aGluZyBtYXRjaGVzIHRoZSBnaXZlbiBVUkkuPC9wPgogICAgPC9ib2R5Pgo8L2h0bWw+Cg==",
  		"response_byte": "PCFET0NUWVBFIEhUTUwgUFVCTElDICItLy9XM0MvL0RURCBIVE1MIDQuMDEvL0VOIgogICAgICAgICJodHRwOi8vd3d3LnczLm9yZy9UUi9odG1sNC9zdHJpY3QuZHRkIj4KPGh0bWw+CiAgICA8aGVhZD4KICAgICAgICA8bWV0YSBodHRwLWVxdWl2PSJDb250ZW50LVR5cGUiIGNvbnRlbnQ9InRleHQvaHRtbDtjaGFyc2V0PXV0Zi04Ij4KICAgICAgICA8dGl0bGU+RXJyb3IgcmVzcG9uc2U8L3RpdGxlPgogICAgPC9oZWFkPgogICAgPGJvZHk+CiAgICAgICAgPGgxPkVycm9yIHJlc3BvbnNlPC9oMT4KICAgICAgICA8cD5FcnJvciBjb2RlOiA0MDQ8L3A+CiAgICAgICAgPHA+TWVzc2FnZTogRmlsZSBub3QgZm91bmQuPC9wPgogICAgICAgIDxwPkVycm9yIGNvZGUgZXhwbGFuYXRpb246IEhUVFBTdGF0dXMuTk9UX0ZPVU5EIC0gTm90aGluZyBtYXRjaGVzIHRoZSBnaXZlbiBVUkkuPC9wPgogICAgPC9ib2R5Pgo8L2h0bWw+Cg==",
  		"response_status_code": "404",
  		"request_path_url": "/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd",
  		"request_body": "Tm9uZQ==",
  		"request_method": "GET",
  		"request_headers": "eydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDExXzBfMSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg3LjAuNDI4MC44OCBTYWZhcmkvNTM3LjM2JywgJ0FjY2VwdC1FbmNvZGluZyc6ICdnemlwLCBkZWZsYXRlJywgJ0FjY2VwdCc6ICd0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC45JywgJ0Nvbm5lY3Rpb24nOiAnY2xvc2UnLCAnQWNjZXB0LUxhbmd1YWdlJzogJ3poLUNOLHpoO3E9MC45LGVuO3E9MC44JywgJ2RudCc6ICcxJ30="
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  - `scan_info_id`当前漏洞ID编号
  - `url`目标连接
  - `name`漏洞名称
  - `affects`漏洞组件
  - `rank`漏洞等级
  - `suggest`漏洞组件
  - `desc_content`漏洞描述
  - `details`漏洞结果
  - `number` CVE编号
  - `author`插件作者
  - `create_date`插件创建时间
  - `disclosure`漏洞披露时间
  - `algroup`插件名称
  - `version`漏洞影响的版本
  - `timestamp`写入漏洞的时间戳
  - `response_headers`响应头，base64加密后数据
  - `response_text`响应返回数据包，base64加密后数据
  - `response_byte`响应返回byte类型数据包，base64加密后数据
  - `response_status_code`响应状态码
  - `request_path_url`请求路径
  - `request_body`请求的POST请求数据，base64加密后数据
  - `request_method` 请求方式
  - `request_headers`请求头，base64加密后数据

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 404：数据库GG了🐈

- 500：请使用Post请求

### 扫描报告生成接口

`/api/generate_word`用来生成报告使用，返回结果存在生成文件名

```json
{
	"token": "XXX",
	"active_scan_id": "X"
}
```

> 参数解释

- `token`登录后返回的**token**
- `active_scan_id`目标的**sid**值，可以通过`/api/active_scan_list_query`接口来获取

> 返回状态码

- 169：莎酱被玩坏啦(>^ω^<)喵
- 200：返回报告下载文件名
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：莎酱生不出小莎酱惹QAQ
- 500：请使用Post请求

### 扫描报告下载接口

`/api/download_word/`下载报告使用

```json
{
   "token": "XXX",
   "file_name": "X"
}
```

> 参数解释

- `token`登录后返回的**token**
- `file_name`文件名通过上个接口获得

> 返回状态码

- 169：莎酱被玩坏啦(>^ω^<)喵
- 403：小宝贝这是非法下载哦(๑•̀ㅂ•́)و✧
- 404：啊啊啊它不是你的小莎酱，别乱抱呀！
- 500：请使用Post请求
- 成功不返回任何结果直接跳转下载

### 主动扫描端口查询

`/api/actively_scan_port_information/`用来查询主动扫描中的端口扫描信息

```json
{
	"token": "XXXXX",
	"active_scan_id":"1"
}
```

>参数解释

- `token`登录后返回的**token**
- `active_scan_id`目标的**active_scan_id**值，主动扫描生成的值

> 返回状态码

- 169：莎酱被玩坏啦ヽ(･ω･´ﾒ)
- 200：返回关系查询列表结果
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：宝贝没有数据哦🐈'
- 500：请使用Post请求

