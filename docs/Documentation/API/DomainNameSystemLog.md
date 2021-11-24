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
  		"type": "dns",
  		"request": "",
  		"response": "",
  		"creation_time": "1618133942"
  	}, {
  		"domain_name": "",
  		"ip": "",
  		"type": "http",
  		"request": "R0VUIC8gSFRUUC8xLjEKSG9zdDogMTI3LjAuMC4xOjg4ODgKVXNlci1BZ2VudDogTW96aWxsYS81LjAgemdyYWIvMC54CkFjY2VwdDogKi8qCkFjY2VwdC1FbmNvZGluZzogZ3ppcAoK",
  		"response": "SFRUUC8xLjAgMjAwIE9LDQpTZXJ2ZXI6IEJhc2VIVFRQLzAuNiBQeXRob24vMy44LjEwDQpEYXRlOiBUdWUsIDIzIE5vdiAyMDIxIDA5OjE2OjU2IEdNVA0KQ29udGVudC10eXBlOiB0ZXh0L2h0bWwNCg==",
  		"creation_time": "1618133942"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  每种类型数据独立拥有，其他的值为空

  - `domain_name`DNS类型域名信息
  - `ip`DNS类型请求IP
  - `type`解析类型，有DNS和HTTP
  - `request`HTTP类型请求数据，需要使用base64解密
  - `response`HTTP类型返回数据，需要使用base64解密
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