### 下发获取文件打包任务

`/api/file_acquisition_file_pack/`

```json
{
	"token": "xxx",
	"file_list":["rpTjEE7ecA1637302616","LEI33MECW61637302616"] 
}
```

> 参数解释

- `token`登录后返回的**token**
- `file_list`文件列表

> 返回状态码

- 169：你不对劲！为什么报错了？	

- 200：任务下发成功(๑•̀ㅂ•́)و✧

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 下载打包的文件

`/api/file_acquisition_file_pack/`

```json
{
	"token": "xxx",
	"file_name":"XXXX.zip" 
}
```

> 参数解释

- `token`登录后返回的**token**
- `file_name` 需要下载的文件名，通过`/api/file_acquisition_pack_query/`接口获取

> 返回状态码

- 169：你不对劲！为什么报错了？	
- 200：直接返回下载文件流
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 405：宝,这文件不是你的哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求

### 打包文件数据查询

`/api/file_acquisition_pack_query/`

```json
{
	"token": "xxx",
	"number_of_pages":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`查询的页数，单页默认100个数据

> 返回状态码

- 169：你不对劲！为什么报错了？

- 200：返回用户当前信息

  ```json
  {
  	"message": [{
  		"file_name": "5GaYUjlPD5.zip",
  		"state": "1",
  		"creation_time": "1637563840"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  - `file_name`文件名
  - `state`任务状态，1表示任务成功，0表示任务进行中，-1表示存在非法文件
  - `creation_time`任务创建时间

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 打包文件个数统计

`/api/file_acquisition_pack_attachment/`

```json
{
	"token": "xxx"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回用户当前信息

  ```json
  {
  	"message": 1,
  	"code": 200
  }
  ```

  > 返回参数解释

  - `message`为个数

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 获取文件数据查询

`/api/file_acquisition_query/`

```json
{
	"token": "xxx",
	"number_of_pages":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`查询的页数，单页默认100个数据

> 返回状态码

- 169：你不对劲！为什么报错了？

- 200：返回用户当前信息

  ```json
  {
  	"message": [{
  		"file_full_path": "C:\\\\Python27\\Lib\\site-packages\\drozer\\modules\\exploit\\fileformat\\ca89ef3ffa6f48ca4147387638559d94.docx",
  		"old_file_name": "ca89ef3ffa6f48ca4147387638559d94.docx",
  		"file_size": "38138",
  		"new_file_name": "tbsUWxcsuU1637302398",
  		"target_machine": "63904D56-830F-B4DB-3A87-73947E15A6E1",
  		"creation_time": "1637302398"
  	}, {
  		"file_full_path": "C:\\\\Users\\ascotbe\\anaconda3\\Lib\\site-packages\\docx\\templates\\default.docx",
  		"old_file_name": "default.docx",
  		"file_size": "38116",
  		"new_file_name": "mXvXRWX5u21637302398",
  		"target_machine": "63904D56-830F-B4DB-3A87-73947E15A6E1",
  		"creation_time": "1637302398"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  - `file_full_path`目标机器文件完整路径
  - `old_file_name`目标机器中文件名
  - `file_size`文件大小
  - `new_file_name` 重命名后文件
  - `target_machine`目标机器唯一UUID值
  - `creation_time`任务创建时间

- 400：你家页数是负数的？？？？

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 获取文件个数统计

`/api/file_acquisition_attachment/`

```json
{
	"token": "xxx"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回用户当前信息

  ```json
  {
  	"message": 19,
  	"code": 200
  }
  ```

  > 返回参数解释

  - `message`为个数

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求