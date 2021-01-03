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

- 200：创建后本地生成的js文件
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
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

- 200：文件内容覆盖成功~
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：你没有查询这个项目的权限哦宝贝~
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用Post请求

### 查询跨站脚本钓鱼项目

`/api/query_cross_site_script_project/`用来查询用户的跨站脚本项目

```json
{
	"token": "",
}
```

>参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回查询到的项目信息
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用Post请求

### 查询跨站脚本钓鱼项目中数据

`/api/query_cross_site_script_project_data/`用来查询用户的跨站脚本项目中的数据信息

```json
{
	"token": "",
	"project_associated_file_name":""
}
```

>参数解释

- `token`登录后返回的**token**
- `project_associated_file_name`项目中生成的特殊文件名，也就是**/api/query_cross_site_scripting_project/**接口传回的**file_name**数据

> 返回状态码

- 200：返回查询到的项目信息
- 404：你没有查询这个项目的权限哦宝贝~
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
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

- 200：返回项目中js文件的详细信息，内容通过base64编码过，以及几个POC的利用语句
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：你没有查询这个项目的权限哦宝贝~
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
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

- 200：返回查询到的项目信息
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
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

- 200：返回查询到的项目信息
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
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

