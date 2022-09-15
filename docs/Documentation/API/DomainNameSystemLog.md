### 获取DNSLOG

`/api/get_domain_name_system_log/` 用来获取当前用户分配的DNSLOG值

```json
{
	"key": "",
}
```

> 参数解释

- `key` 该值来自`/api/user_info/`这个接口中的key值

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：为当前用户的dnslog值

  ```json
  {
  	"message": "wlqjd.dnslog.ascotbe.com",
  	"code": 200
  }
  ```

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

- 503：小宝贝获取失败啦(๑•̀ㅂ•́)و✧



### DNS类型的数据查询

`/api/domain_name_system_log/`

```json
{
	"key": "",
	"number_of_pages":""
}
```

> 参数解释

- `key` 该值来自`/api/user_info/`这个接口中的key值
- `number_of_pages`查询的页数，单页默认100个数据

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回用户当前信息

  ```json
  {
  	"message": [{
  		"domain_name": "addd.9128123.JPaFj.dnslog.ascotbe.com",
  		"ip": "211.136.115.194",
  		"creation_time": "1639207193"
  	}, {
  		"domain_name": "addd.JPaFj.dnslog.ascotbe.com",
  		"ip": "211.136.115.198",
  		"creation_time": "1639207086"
  	}],
    "number": 2,
  	"code": 200
  }
  ```
  
  > 返回参数解释
  
  - `message`每种类型数据独立拥有
  
    - `domain_name`DNS类型域名信息
  
    - `ip`DNS类型请求IP
  
    - `creation_time`接收时间
  
  - `number`个数
  
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求



### HTTP类型数据查询

`/api/http_domain_name_system_log/`

```json
{
	"token": "",
	"number_of_pages":""
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`查询的页数，单页默认100个数据

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回用户当前信息

  ```json
  {
  	"message": [{
  		"request": "R0VUIC9mYXZpY29uLmljbyBIVFRQLzEuMApIb3N0OiB3bHFqZC5kbnNsb2cudGVzdC5jb20KWC1SZWFsLUlQOiAxMS4xMTEuNDcuNTAKeC1mb3J3YXJkZWQtZm9yOiAxMS4xMTEuNDcuNTAKQ29ubmVjdGlvbjogY2xvc2UKVXNlci1BZ2VudDogTW96aWxsYS81LjAgKFgxMTsgTGludXggaTY4NikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgVWJ1bnR1IENocm9taXVtLzk1LjAuNDY3NS42MSBDaHJvbWUvOTUuMC40Njc1LjYxIFNhZmFyaS81MzcuMzYKQWNjZXB0OiBpbWFnZS9hdmlmLGltYWdlL3dlYnAsaW1hZ2UvYXBuZyxpbWFnZS9zdmcreG1sLGltYWdlLyosKi8qO3E9MC44ClJlZmVyZXI6IGh0dHA6Ly93bHFqZC5kbnNsb2cudGVzdC5jb20vCkFjY2VwdC1FbmNvZGluZzogZ3ppcCwgZGVmbGF0ZQpBY2NlcHQtTGFuZ3VhZ2U6IHpoLUNOLHpoO3E9MC45LGVuO3E9MC44CmRudDogMQpzZWMtZ3BjOiAxCgo=",
  		"response": "SFRUUC8xLjAgMjAwIE9LDQpTZXJ2ZXI6IEJhc2VIVFRQLzAuNiBQeXRob24vMy44LjEwDQpEYXRlOiBTYXQsIDExIERlYyAyMDIxIDA3OjQ0OjIxIEdNVA0KQ29udGVudC10eXBlOiB0ZXh0L2h0bWwNCg==",
  		"creation_time": "1639208661"
  	}],
    "number": 1,
  	"code": 200
  }
  ```

  > 返回参数解释

  - `message`每种类型数据独立拥有

    - `request`HTTP类型请求数据包

    - `response`HTTP类型请求响应数据包

    - `creation_time`接收时间

  - `number`个数

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求


