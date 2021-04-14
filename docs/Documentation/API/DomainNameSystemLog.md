### DNSLOG数据查询

`/api/domain_name_system_log/`DNSLOG数据查询接口

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
  		"domain_name": "test8.dnslog.ascotbe.com",
  		"ip": "27.115.80.227",
  		"creation_time": "1618133942"
  	}, {
  		"domain_name": "test10.dnslog.ascotbe.com",
  		"ip": "112.65.184.227",
  		"creation_time": "1618136087"
  	}, {
  		"domain_name": "test10.dnslog.ascotbe.com",
  		"ip": "112.65.184.227",
  		"creation_time": "1618136087"
  	}, {
  		"domain_name": "test11.dnslog.ascotbe.com",
  		"ip": "112.65.184.227",
  		"creation_time": "1618136105"
  	}, {
  		"domain_name": "123.dnslog.ascotbe.com",
  		"ip": "112.65.184.229",
  		"creation_time": "1618136107"
  	}, {
  		"domain_name": "123.dnslog.ascotbe.com",
  		"ip": "112.65.184.229",
  		"creation_time": "1618136107"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  - `domain_name`域名信息
  - `ip`请求IP
  - `creation_time`接收时间

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求



### DNSLOG个数统计

`/api/domain_name_system_log_statistics/`个数统计

```json
{
	"token": ""
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回数据大小

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求