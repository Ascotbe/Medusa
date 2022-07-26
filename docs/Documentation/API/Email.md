### 创建邮件项目

`/api/create_email_project/`

```json
{
	"token": "xxxx"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回该项目的key值
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 505：创建失败！

### 更新项目数据

`/api/updata_email_project/`

```json
{

	"token": "xxxx",
	"end_time": "1659557858",
	"project_key": "eNVqsIHXAV",
  "project_name": "my_name",
	"mail_message": "<p>警戒警戒！莎莎检测到有人入侵！数据以保存喵~</p>\n<p>首先需要制作PE镜像推荐使用<a target=\"_blank\" rel=\"noopener\" href=\"http://baidu.com/{{ md5 }}\">老毛桃</a></p>",
	"attachment": {
		"Medusa.txt": "AeId9BrGeELFRudpjb7wG22LidVLlJuGgepkJb3pK7CXZCvmM51628131056"
	},
	"image": {
		"Medusa.jpg": "2DvWXQc8ufvWMIrhwV5MxrzZZA2oy2f3b5qj5r6VTzb247nQYP1642744866"
	},
	"mail_title": "测试邮件",
	"sender": "瓜皮大笨蛋",
	"goal_mailbox": {
		"信息安全": ["ascotbe@gmail.com", "ascotbe@163.com"],
		"大数据": ["ascotbe@qq.com"],
		"客服": ["12345@qq.com"]
	},
  "email_list_key": "Sp7odgjo78xTh7zfQhUV",
	"third_party": "0",
	"forged_address": "helpdesk@ascotbe.com",
	"interval": "0.1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `end_time` 项目停止接收数据时间
- `project_key`项目的key值，通过创建项目接口获取的，在create_email_project接口
- `project_name`项目名称
- `mail_message` 支持HTML格式，在引入的页面添加占位符`{{ md5 }}`参考上面数据，如果是还需要统计点开邮件用户可以再最下面添加一个图片标签，只发送请求到接收数据接口，不发送数据的那种，同样需要占位符
- `attachment`使用本地附件，通过email_attachment_query这个api接口获取相关信息，如果为空也必须传入`{}`符号
- `image`邮件中插入的图片，通过email_attachment_query这个api接口获取相关信息，如果为空也必须传入`{}`符号
- `mail_title`邮件标题
- `sender`发件人名称
- `goal_mailbox`发送到哪些邮箱中，必须是字典类型，并且不能为空
- `email_list_key`邮箱列表中获取数据根据接口，query_email_list_key能够查询到相关的key，该值优先级大于`goal_mailbox`参数，所以有数据会进行覆盖
- `interval`邮件发送的间隔
- `forged_address`发送的邮件服务器（可以伪造

> 返回状态码

- 169：未知错误(๑•̀ㅂ•́)و✧
- 200：更新成功！
- 400：你家页数是负数的？？？？
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 406：项目已经开启禁止修改，如需修改请停止运行！
- 409：项目已经运行结束禁止修改其中内容！
- 414：未传入邮件接收人！
- 415：附件或者图片必须传入字典类型，不可置空！
- 500：请使用Post请求
- 505：未传入收件人数据！请检查Key是否有用
- 506：时间间隔太长了！
- 507：更新失败！

### 启动项目

`/api/run_email_project/`

```json
{
	"token": "xxxx",
	"project_key":"eNVqsIHXAV"
}
```

> 参数解释

- `token`登录后返回的**token**
- `project_key`邮件项目的key

> 返回状态码

- 169：未知错误，请查看日志(๑•̀ㅂ•́)و✧
- 200：项目启动成功！
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 406：不存在目标无法启动！
- 410：项目已经启动或者已经完成！
- 500：请使用Post请求
- 505：项目启动失败！

### 停止项目（暂时无用

`/api/stop_email_project/`

```json
{
	"token": "xxxx",
	"project_key":"eNVqsIHXAV"
}
```

> 参数解释

- `token`登录后返回的**token**
- `project_key`邮件项目的key

> 返回状态码

- 169：未知错误，请查看日志(๑•̀ㅂ•́)و✧
- 200：项目停止成功！
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 505：项目停止失败！

### 统计邮件项目个数

`/api/email_project_statistics/`

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

### 邮件内容详情

`/api/email_project_details/`

```json
{
	"token": "xxx",
	"project_key":"wAmDVUCHev"
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`页数

> 返回状态码

- 169：未知错误，请查看日志(๑•̀ㅂ•́)و✧

- 200：返回详情内容，**会有多个数组的集合**

  ```json
  {
  	"message": {
  		"goal_mailbox": {
  			"\u4fe1\u606f\u5b89\u5168": ["ascotbe@gmail.com", "ascotbe@163.com"],
  			"\u5927\u6570\u636e": ["ascotbe@qq.com"],
  			"\u5ba2\u670d": ["1099482542@qq.com"]
  		},
  		"end_time": "1659557858",
  		"project_key": "wAmDVUCHev",
      "project_name": "my_name",
  		"mail_message": "PHA+6K2m5oiS6K2m5oiS77yB6I6O6I6O5qOA5rWL5Yiw5pyJ5Lq65YWl5L6177yB5pWw5o2u5Lul5L+d5a2Y5Za1fjwvcD4KPHA+6aaW5YWI6ZyA6KaB5Yi25L2cUEXplZzlg4/mjqjojZDkvb/nlKg8YSB0YXJnZXQ9Il9ibGFuayIgcmVsPSJub29wZW5lciIgaHJlZj0iaHR0cDovL2JhaWR1LmNvbS97eyBtZDUgfX0iPuiAgeavm+ahgzwvYT48L3A+",
  		"attachment": {},
  		"image": {},
  		"mail_title": "5rWL6K+V6YKu5Lu2",
  		"sender": "55Oc55qu5aSn56yo6JuL",
  		"forged_address": "aGVscGRlc2tAYXNjb3RiZS5jb20=",
  		"redis_id": "da8b3bb8-4907-43ad-b90c-c503a9f4f626",
  		"compilation_status": "1",
  		"interval": "0.1",
  		"project_status": "1",
  		"creation_time ": "1654076229"
  	},
  	"code": 200
  }
  ```

  > 参数解释

  - `goal_mailbox`目标邮箱列表

  - `end_time`项目结束时间，结束后不再接受任何数据

  - `project_key`项目唯一关键字，用于判断接收数据所属

  - `project_name`邮件的名称

  - `mail_message`邮件正文，需要base64解密

  - `attachment`附件文件

  - `image` 图片文件

  - `mail_title`邮件头，需要base64解密

  - `sender`发送人名称，需要base64解密

  - `forged_address`伪造的发件人地址，需要base64解密

  - `redis_id`Redis值

  - `compilation_status`任务状态，0表示未完成，1表示完成，如果值为1那么就不再能够更新项目内容

  - `interval`间隔

  - `project_status`项目状态，0表示未运行，1表示运行完毕

  - `creation_time `项目创建时间

    

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求



### 邮件项目内容摘要查询

`/api/email_project_summary/`

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
  		"end_time": "1659557858",
  		"project_key": "eNVqsIHXAV",
  		"project_status": "1",
  		"interval": "0.1",
  		"compilation_status": "1",
  		"creation_time": "1654075687"
  	}, {
  		"end_time": "1659557858",
  		"project_key": "wAmDVUCHev",
  		"project_status": "1",
  		"interval": "0.1",
  		"compilation_status": "1",
  		"creation_time": "1654076229"
  	}],
  	"code": 200
  }
  ```

  > 参数解释

  - `end_time`项目停止接收数据时间
  - `project_key`项目的key值
  - `project_status`项目状态，0表示未启动，1表示启动，启动中无法修改项目
  - `interval`邮件发送间隔
  - `compilation_status`任务状态，0表示未完成，1表示完成，-1表示运行失败，如果值为1那么就不再能够更新项目内容
  - `creation_time`创建时间

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求



### 文件上传

`/api/email_file_upload/`

```json
POST /api/mail_upload_files/ HTTP/1.1
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

`/api/email_attachment_statistical/`

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

`/api/email_attachment_details/`

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

### 加载预览文件

`/api/email_image_preview/`

```json
{
	"token": "xxx",
	"document_real_name":"xxx"
}
```

> 参数解释

- `token`登录后返回的**token**
- `document_real_name`通过email_attachment_query这个api接口获取相关信息

> 返回状态码

- 169：你不对劲！为什么报错了？
- 200：如果查询到返回的是二进制流和验证码一样
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 603：没有这个文件~



### 接收数据全量数据统计

`/api/email_receive_data_statistics/`

```json
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa"
}
```

> 参数解释

- `token`登录后返回的**token**
- `project_key`项目的key

> 返回状态码

- 169：自己去看报错日志！
- 200：返回当前数量
- 400：你家页数是负数的？？？？
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求



### 接收数据全量数据详情查询

`/api/email_receive_data_details/`

```json
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa",
	"number_of_pages":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `project_key`项目的key
- `number_of_pages`页数

> 返回状态码

- 169：自己去看报错日志！

- 200：返回详情内容，**会有多个数组的集合**

  ```json
  {
  	"message": [{
  		"email": "ascotbe@gmail.com",
  		"department": "\u4fe1\u606f\u5b89\u5168",
  		"full_url": "http://127.0.0.1:9999/b/wAmDVUCHev/",
  		"request_method": "POST",
  		"data_pack_info": "eydrZXknOiAnMzdiMDJmMjhjZDdlODk1OTBhZjM2NjExYjI1NTJmMzQnLCAndXNlJzogJ2FhYWRkZGRkJywgJ3Bhc3NzJzogJ2Rhc2Rhc2QnfQ==",
  		"incidental_data": "eyd1c2UnOiAnYWFhZGRkZGQnLCAncGFzc3MnOiAnZGFzZGFzZCd9",
  		"creation_time": "1654667885"
  	}, {
  		"email": "ascotbe@163.com",
  		"department": "\u5927\u6570\u636e",
  		"full_url": "http://127.0.0.1:9999/b/wAmDVUCHev/?key=7adfffee50ed9cb5a49e6e6bb07cd538&use=aaaddddd&passs=dasdasd",
  		"request_method": "GET",
  		"data_pack_info": "eydrZXknOiAnN2FkZmZmZWU1MGVkOWNiNWE0OWU2ZTZiYjA3Y2Q1MzgnLCAndXNlJzogJ2FhYWRkZGRkJywgJ3Bhc3NzJzogJ2Rhc2Rhc2QnfQ==",
  		"incidental_data": "eyd1c2UnOiAnYWFhZGRkZGQnLCAncGFzc3MnOiAnZGFzZGFzZCd9",
  		"creation_time": "1654567715"
  	}],
  	"code": 200
  }
  ```

  > 参数解释

  - `email`接收邮件
  - `department`部门
  - `full_url`完整请求
  - `request_method`请求方式
  - `data_pack_info`完整的数据内容
  - `incidental_data`除了key值以外的数据内容
  - `creation_time`创建时间

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求



### 接收数据模糊查询

`/api/email_receive_data_search/`

```json
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa",
	"email":"163",
	"department":"",
	"start_time":"1654567716",
	"end_time":"19999999999",
	"number_of_pages":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `project_key`项目key
- `email`邮箱的模糊查询值，可以为空
- `department`部门的模糊查询值，可以为空
- `start_time`起始时间
- `end_time`结束时间
- `number_of_pages`页数不能为0

> 返回状态码

- 200：返回详情内容，**会有多个数组的集合**

  ```json
  {
  	"message": [{
  		"email": "ascotbe@163.com",
  		"department": "\u4fe1\u606f\u5b89\u5168",
  		"full_url": "http://127.0.0.1:9999/b/wAmDVUCHev/",
  		"request_method": "POST",
  		"data_pack_info": "eydrZXknOiAnNGFiYjA0ODY5MTQ2YWU3N2YyZGNmMWJhZDY3ZGFiMzcnLCAndXNlJzogJ2FhYWRkZGRkJywgJ3Bhc3NzJzogJ2Rhc2Rhc2QnfQ==",
  		"incidental_data": "eyd1c2UnOiAnYWFhZGRkZGQnLCAncGFzc3MnOiAnZGFzZGFzZCd9",
  		"creation_time": "1654667892"
  	}, {
  		"email": "ascotbe@163.com",
  		"department": "\u4fe1\u606f\u5b89\u5168",
  		"full_url": "http://127.0.0.1:9999/b/wAmDVUCHev/",
  		"request_method": "POST",
  		"data_pack_info": "eydrZXknOiAnNGFiYjA0ODY5MTQ2YWU3N2YyZGNmMWJhZDY3ZGFiMzcnfQ==",
  		"incidental_data": "",
  		"creation_time": "1654669608"
  	}, {
  		"email": "ascotbe@163.com",
  		"department": "\u4fe1\u606f\u5b89\u5168",
  		"full_url": "http://127.0.0.1:9999/b/wAmDVUCHev/",
  		"request_method": "POST",
  		"data_pack_info": "eydrZXknOiAnNGFiYjA0ODY5MTQ2YWU3N2YyZGNmMWJhZDY3ZGFiMzcnLCAndXNlJzogJ2FhYWRkZGRkJywgJ3Bhc3NzJzogJ2Rhc2Rhc2QnfQ==",
  		"incidental_data": "eyd1c2UnOiAnYWFhZGRkZGQnLCAncGFzc3MnOiAnZGFzZGFzZCd9",
  		"creation_time": "1654669616"
  	}],
  	"code": 200
  }
  ```

  > 参数解释

  - `email`接收邮件
  - `department`部门
  - `full_url`完整请求
  - `request_method`请求方式
  - `data_pack_info`完整的数据内容
  - `incidental_data`除了key值以外的数据内容
  - `creation_time`创建时间

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求



### 接收数据模糊查询统计

`/api/email_receive_data_search_quantity/`

```json
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa",
	"email":"163",
	"department":"",
	"start_time":"",
	"end_time":""
}
```

> 参数解释

- `token`登录后返回的**token**
- `project_key`项目key
- `email`邮箱的模糊查询值，可以为空
- `department`部门的模糊查询值，可以为空
- `start_time`起始时间
- `end_time`结束时间

> 返回状态码

- 200：返回个数
- 400：你家页数是负数的？？？？
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求



### 数据表格统计

`/api/email_data_graph_statistics/`

```json
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa"
}
```

> 参数解释

- `token`登录后返回的**token**
- `project_key`项目key

> 返回状态码

- 200：任务下发成功！

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求



### 数据表格查询

`/api/email_data_graph_query/`

```json
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa"
}
```

> 参数解释

- `token`登录后返回的**token**
- `project_key`项目key

> 返回状态码

- 200：返回详情内容，**会有多个数组的集合**

  ```json
  {
  	"message": {
  		"\u4fe1\u606f\u5b89\u5168": {
  			"total_amount": 2,
  			"open_hits": 1,
  			"fooled_hits": 1
  		},
  		"\u5927\u6570\u636e": {
  			"total_amount": 1,
  			"open_hits": 0,
  			"fooled_hits": 1
  		},
  		"\u5ba2\u670d": {
  			"total_amount": 1,
  			"open_hits": 1,
  			"fooled_hits": 0
  		},
  		"open_email_user_data": ["12345@qq.com", "ascotbe@163.com"],
  		"hooked_email_user_data": ["ascotbe@qq.com", "ascotbe@gmail.com", "ascotbe@163.com"]
  	},
  	"code": 200
  }
  ```

  > 参数解释

  - `open_email_user_data`打开邮件的用户
  - `hooked_email_user_data`填写数据的用户
  - 剩余的都是每个部门作为关键字
    - `total_amount`该部门发送量
    - `open_hits`打开邮件量
    - `fooled_hits`填写数据量

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 查询邮件发送状态

`/api/email_sending_status/`

```json
{
	"token": "xxx",
	"number_of_pages":"1",
	"full_data":true,
	"status":"1",
	"project_key":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`页数
- `full_data`是否是全量数据，如果值为true那么会忽略`status`参数的值，如果是false那么会响应`status`参数的值
- `status`邮件状态
- `project_key`项目key

> 返回状态码

- 169：未知错误，请查看日志(๑•̀ㅂ•́)و✧

- 200：返回详情内容，**会有多个数组的集合**

  ```json
  {
  	"message": [{
  		"email": "ascotbe@163.com",
  		"email_md5": "4abb04869146ae77f2dcf1bad67dab37",
  		"status": "1",
  		"department": "\u4fe1\u606f\u5b89\u5168",
  		"creation_time": "1655202052"
  	}, {
  		"email": "123456@qq.com",
  		"email_md5": "35de170fc7836ea645e1a7d7b307ff6e",
  		"status": "-1",
  		"department": "\u5ba2\u670d",
  		"creation_time": "1658298090"
  	}],
  	"code": 200
  }
  ```

  > 参数解释

  - `email`邮件
  - `email_md5`邮件的md5值
  - `status`邮件状态，1表示发送成功，-1表示发送失败
  - `department`当前邮件所属部门
  - `creation_time `项目创建时间

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 405：该项目不属于你不要瞎请求！

- 500：请使用Post请求

### 邮件发送状态统计数量

`/api/email_sending_status_statistics/`

```json
{
	"token": "xxx",
	"project_key":"1",
  "full_data":true,
	"status":"1",
}
```

> 参数解释

- `token`登录后返回的**token**
- `full_data`是否是全量数据，如果值为true那么会忽略`status`参数的值，如果是false那么会响应`status`参数的值
- `status`邮件状态
- `project_key`项目key

> 返回状态码

- 169：未知错误，请查看日志(๑•̀ㅂ•́)و✧
- 200：返回个数是多少
- 400：你家页数是负数的？？？？
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 405：该项目不属于你不要瞎请求！
- 500：请使用Post请求

### 重发未发送成功的邮件

`/api/resend_failure_email/`

```json
{
	"token": "xxx",
	"project_key":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `project_key`项目key

> 返回状态码

- 169：未知错误，请查看日志(๑•̀ㅂ•́)و✧
- 200：任务下发成功
- 400：你家页数是负数的？？？？
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 405：该项目不属于你不要瞎请求！
- 500：请使用Post请求

### 发送测试邮件

`/api/send_test_email/`

```json
{
	"token": "xxxx",
	"mail_message": "<p>警戒警戒！莎莎检测到有人入侵！数据以保存喵~</p>\n<p><img src=\"cid:Medusa.jpg\"></p><p>快快看看这个<a target=\"_blank\" rel=\"noopener\" href=\"http://baidu.com/{{ md5 }}\">数据</a></p>",
	"attachment": {
		"Medusa.txt": "AeId9BrGeELFRudpjb7wG22LidVLlJuGgepkJb3pK7CXZCvmM51628131056"
	},
	"image": {
		"Medusa.jpg": "5x8SfyxamrejUHa6sBMztSUxH2skl6yBZ81lDDhj96264YLiRb1655199840"
	},
	"mail_title": "测试邮件",
	"sender": "瓜皮大笨蛋",
	"goal_mailbox": {
		"信息安全": ["ascotbe@163.com"],
		"大数据": ["ascotbe@qq.com"]
	},
	"forged_address": "helpdesk@test.com",
	"interval": "0.1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `mail_message` 支持HTML格式，在引入的页面添加占位符`{{ md5 }}`参考上面数据，如果是还需要统计点开邮件用户可以再最下面添加一个图片标签，只发送请求到接收数据接口，不发送数据的那种，同样需要占位符
- `attachment`使用本地附件，通过email_attachment_query这个api接口获取相关信息，如果为空也必须传入`{}`符号
- `image`邮件中插入的图片，通过email_attachment_query这个api接口获取相关信息，如果为空也必须传入`{}`符号
- `mail_title`邮件标题
- `sender`发件人名称
- `goal_mailbox`发送到哪些邮箱中，必须是字典类型，并且不能为空
- `interval`邮件发送的间隔
- `forged_address`发送的邮件服务器（可以伪造

> 返回状态码

- 169：未知错误(๑•̀ㅂ•́)و✧
- 200：测试邮件任务下发成功！
- 400：你家页数是负数的？？？？
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 414：未传入邮件接收人！
- 415：附件或者图片必须传入字典类型，不可置空！
- 500：请使用Post请求

### 上传表格提取相关数据

`/api/upload_email_list/`

```json
POST /api/upload_email_list/ HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryaFtQbWz7pBzNgCOv
token:XXXXXXXXXXXXXXXX
Another-Name:\u5403\u996d

------WebKitFormBoundaryaFtQbWz7pBzNgCOv
Content-Disposition: form-data; name="file"; filename="test.xlsx"
Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

XXXXXXXXXXXXXXX
------WebKitFormBoundaryaFtQbWz7pBzNgCOv--
```

> 参数解释

- `token`登录后返回的**token**
- `Another-Name`项目别名

> 返回状态码

- 169：未知错误，请查看日志(๑•̀ㅂ•́)و✧
- 200：写入成功！
- 400：你家页数是负数的？？？？
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 501：写入失败！

### 统计邮件列表个数数据

`/api/statistics_email_list_key/`

```json
{
	"token": "xxx"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：未知错误，请查看日志(๑•̀ㅂ•́)و✧

- 200：返回个数

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 查询邮件列表Key

`/api/query_email_list_key/`

```json
{
	"token": "xxx",
	"number_of_pages": "1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`页数

> 返回状态码

- 169：未知错误，请查看日志(๑•̀ㅂ•́)و✧

- 200：返回详情内容，**会有多个数组的集合**

  ```json
  {
  	"message": [{
  		"project_key": "mTwWHqi6Hb6sSBTHjojP",
  		"another_name": "\\u5413\\u926d",
  		"creation_time": "1658199411"
  	}, {
  		"project_key": "Sp7odgjo78xTh7zfQhUV",
  		"another_name": "\\u5403\\u996d",
  		"creation_time": "1658199672"
  	}],
  	"code": 200
  }
  ```

  > 参数解释

  - `another_name`邮件列表名称

  - `project_key`邮件列表项目关键字

  - `creation_time `项目创建时间

    

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 查询邮件列表全量的数据

`/api/query_email_list/`

```json
{
	"token": "xxx",
	"project_key":"Sp7odgjo78xTh7zfQhUV"
}
```

> 参数解释

- `token`登录后返回的**token**
- `project_key`邮件列表项目key

> 返回状态码

- 169：未知错误，请查看日志(๑•̀ㅂ•́)و✧

- 200：返回详情内容，**会有多个数组的集合**

  ```json
  {
  	"message": {
  		"\u6570\u636e\u5e93": ["ascotbe@qq.com", "123@qq.com"],
  		"\u6572\u626e\u5e93": ["12345@qq.com"]
  	},
  	"code": 200
  }
  ```

  > 参数解释

  - 每个参数开头是部门，后面跟的是邮箱内容

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

