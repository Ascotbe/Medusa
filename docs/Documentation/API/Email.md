### 邮件批量发送功能

`/api/send_fishing_mail/`

```json
{
	"token": "xxxx",
	"mail_message":"<p>警戒警戒！莎莎检测到有人入侵！数据以保存喵~</p>",
    "attachment": {"Medusa.txt":"AeId9BrGeELFRudpjb7wG22LidVLlJuGgepkJb3pK7CXZCvmM51628131056"},
    "mail_title":"测试邮件",
    "sender":"喵狗子",
    "goal_mailbox":["ascotbe@gmail.com","ascotbe@163.com"],
    "third_party":"0",
    "forged_address":"helpdesk@ascotbe.com"
}
```

> 参数解释

- `token`登录后返回的**token**
- `mail_message`发送数据内容
- `attachment`使用本地附件，通过email_attachment_query这个api接口获取相关信息
- `mail_title`邮件标题
- `sender`发件人名称
- `goal_mailbox`发送到哪些邮箱中，传入一个列表的形式
- `third_party`判断是否是用第三方邮件服务器，0表示本地自己搭建（需要在配置文件中填上你的自建邮服务），1表示使用qq或者163等第三方邮件服务器（需要配置文件中修改你的key）
- `forged_address`发送的邮件服务器（可以伪造

> 返回状态码

- 200：任务下发成功~
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 503：未知错误(๑•̀ㅂ•́)و✧

### 邮件发送数据详情

`/api/malicious_mail_query/`

```json
{
	"token": "xxx",
	"number_of_pages":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`页数

> 返回状态码

- 200：返回查询到的数据，**会有多个数组的集合**

  ```json
  {
  	"message": [{
  		"mail_message": "PHA+6K2m5oiS6K2m5oiS77yB6I6O6I6O5qOA5rWL5Yiw5pyJ5Lq65YWl5L6177yB5pWw5o2u5Lul5L+d5a2Y5Za1fjwvcD4=",
  		"attachment": "{}",
  		"mail_title": "5rWL6K+V6YKu5Lu2",
  		"sender": "dGVzdA==",
  		"forged_address": "YUdWc2NHUmxjMnRBZEhKcGNDNWpiMjA9",
  		"mail_status": "{\"test@ascotbe.com\": \"1\"}",
  		"compilation_status": "1",
  		"creation_time": "1628652828"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  - `mail_message`发送的数据内容，使用base64加密
  - `attachment`使用那个本地附件
  - `mail_title`邮件标题，使用base64加密
  - `sender`发件人名称，使用base64加密
  - `forged_address`发送的邮件服务器
  - `mail_status`各个邮件发送的状态，1表示成功，0表示失败
  - `compilation_status`任务状态，1表示已经完成，0表示未完成

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 邮件发送个数统计

`/api/statistics_malicious_email/`

```json
{
	"token": "xxx"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：所有发送的邮件任务个数
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求

### 邮件附件上传接口

`/api/upload_mail_attachment/`

```json
POST /api/upload_mail_attachment/ HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryaFtQbWz7pBzNgCOv
token:XXXXXXXXXXXXXXXX

------WebKitFormBoundaryaFtQbWz7pBzNgCOv
Content-Disposition: form-data; name="file"; filename="test.jpeg"
Content-Type: image/jpeg

XXXXXXXXXXXXXXX
------WebKitFormBoundaryaFtQbWz7pBzNgCOv--
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：你不对劲！为什么报错了？
- 200：上传成功~
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 603：它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)

### 邮件附件个数统计

`/api/statistical_mail_attachment/`

```json
{
	"token": "xxx"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回统计个数
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求

### 邮件附件详情查询

`/api/email_attachment_query/`

```json
{
	"token": "xxx",
	"number_of_pages":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`页数

> 返回状态码

- 200：返回详情内容，**会有多个数组的集合**

  ```json
  {
  	"message": [{
  		"file_name": "dGVzdC5qcGVn",
  		"file_size": "15",
  		"document_real_name": "AeId9BrGeELFRudpjb7wG22LidVLlJuGgepkJb3pK7CXZCvmM51628131056",
  		"creation_time": "1628131056"
  	}],
  	"code": 200
  }
  ```

  > 参数解释

  - `file_name`文件上传的时候的名字，使用base64加密
  - `file_size`文件大小
  - `document_real_name`文件本地保存的名字
  - `creation_time`创建时间

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 统计通过邮箱获取到的请求数据

`/api/fishing_data_statistics/`

```json
{
	"token": "xxx",
	"request_key":"aaaaaaaaaa"
}
```

> 参数解释

- `token`登录后返回的**token**
- `request_key`该值为10位，通过`http://127.0.0.1:9999/b/aaaaaaaaaa/?dasd=dasd`请求获取

> 返回状态码

- 200：返回统计个数
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求

### 邮件附件详情查询

`/api/fishing_data_details/`

```json
{
	"token": "xxx",
	"request_key":"aaaaaaaaaa",
	"number_of_pages":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `request_key`该值为10位，通过`http://127.0.0.1:9999/b/aaaaaaaaaa/?dasd=dasd`请求获取
- `number_of_pages`页数

> 返回状态码

- 200：返回详情内容，**会有多个数组的集合**

  ```json
  {
  	"message": [{
  		"full_url": "http://127.0.0.1:9999/b/aaaaaaaaaa/?dasd=fsalsdkalsjflahgkahguiwfkjaldfnlsjjgblakjdg",
  		"request_method": "GET",
  		"headers_info": "eydDb250ZW50LUxlbmd0aCc6ICcnLCAnQ29udGVudC1UeXBlJzogJ3RleHQvcGxhaW4nLCAnSG9zdCc6ICcxMjcuMC4wLjE6OTk5OScsICdDb25uZWN0aW9uJzogJ2tlZXAtYWxpdmUnLCAnU2VjLUNoLVVhJzogJyJDaHJvbWl1bSI7dj0iOTIiLCAiIE5vdCBBO0JyYW5kIjt2PSI5OSIsICJHb29nbGUgQ2hyb21lIjt2PSI5MiInLCAnU2VjLUNoLVVhLU1vYmlsZSc6ICc/MCcsICdVcGdyYWRlLUluc2VjdXJlLVJlcXVlc3RzJzogJzEnLCAnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xMF8zKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvODMuMC40MTAzLjg3IFNhZmFyaS81MzcuMzYnLCAnQWNjZXB0JzogJ3RleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL2F2aWYsaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCxhcHBsaWNhdGlvbi9zaWduZWQtZXhjaGFuZ2U7dj1iMztxPTAuOScsICdTZWMtRmV0Y2gtU2l0ZSc6ICdub25lJywgJ1NlYy1GZXRjaC1Nb2RlJzogJ25hdmlnYXRlJywgJ1NlYy1GZXRjaC1Vc2VyJzogJz8xJywgJ1NlYy1GZXRjaC1EZXN0JzogJ2RvY3VtZW50JywgJ0FjY2VwdC1FbmNvZGluZyc6ICdnemlwLCBkZWZsYXRlLCBicicsICdBY2NlcHQtTGFuZ3VhZ2UnOiAnemgtQ04semg7cT0wLjksZW47cT0wLjgnLCAnRG50JzogJzEnLCAnU2VjLUdwYyc6ICcxJ30=",
  		"data_pack_info": "eydkYXNkJzogJ2ZzYWxzZGthbHNqZmxhaGdrYWhndWl3ZmtqYWxkZm5sc2pqZ2JsYWtqZGcnfQ==",
  		"creation_time": "1628673894"
  	}],
  	"code": 200
  }
  ```

  > 参数解释

  - `full_url`请求的完整地址
  - `request_method`请求的方式，有GET和POST
  - `headers_info`请求头内容，base64加密
  - `data_pack_info`请求数据包内容，base64加密
  - `creation_time`创建时间

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求