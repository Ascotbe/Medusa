当前测试版本只有个API接口，路径分别如下，只接受POST请求中的JSON格式数据

```
/api/vulnerability_scanning/
/api/active_scan_list_query/
/api/registered/
/api/login/
/api/scan_information_query/
/api/medusa_query/
/api/generate_word/
/api/download_word/
/api/user_info/
/api/update_password/
/api/update_show_name/
/api/update_key/
```

#### 注册接口

`/api/registered`该接口只能注册用户权限账户，接收数据格式如下

```
{
	"show_name": "7777777",
	"username": "ascotbe",
	"passwd": "1",
	"email": "1@qq.com"
}
```

- `show_name`表示用户显示名字，可以重复
- `username`表示登录名，具有唯一性
- `passwd`用户密码（~~目前明文存储，正式版后在更改~~
- `email`用户邮箱具有唯一性。（~~无校检，任意字符串都可以~~

#### 登录接口

`/api/login`接收数据如下，登录成功返回**token**，并且具有时效性（目前暂无验证码后续更新

```
{
	"username": "ascotbe",
	"passwd": "1"
}
```

- `username` 登录名
- `passwd`登录密码

#### 扫描任务下发接口

`/api/vulnerability_scanning` 用来下发任务，如果下发成功返回**200**

```
{
	"url": "www.ascotbe.com",
	"token": "XXXXXXXXXXXXXXXX",
	"threads": 200,
	"module": "all",
	"header": "None",
	"proxy": "127.0.0.1:8080"
}
```

- `url` 你扫描的目标
- `token` 登录后返回给你的**token**
- `threads`当前任务使用的进程树
- `module`指定扫描模块，具体名称参考**Modules**目录下的文件名
- `header`自定义头，如果没有的话传入**None**参数，用法和**bash**版一样
- `proxy`该任务指定代理，如果没有代理该值直接传入`0` ，注意代理是否可用

#### 主动扫描目标列表查询接口

`/api/active_scan_list_query` 用来查询用户下发了哪些任务列表，返回结果是**JSON**格式

```
{
	"token": "XXXXX"
}
```

- `token`登录后返回的**token**

####  主动扫描目标漏洞列表查询接口

`/api/scan_information_query` 用来查询用户某个任务漏洞列表，返回结果是`JSON`格式

```
{
	"token": "XXXXX",
	"sid":"1"
}
```

- `token`登录后返回的**token**
- `sid`目标的**sid**值，上个接口查询返回中存在

#### 主动扫描目标单个漏洞详细内容查询接口

`/api/medusa_query`用来查询某个任务中某个漏洞详细信息，返回结果是`JSON`格式

```
{
	"token": "XXXXX",
	"ssid":"1"
}
```

- `token`登录后返回的**token**
- `ssid`目标的**ssid**值，上个接口查询返回中存在

#### 扫描报告生成接口

`/api/generate_word`用来生成报告使用，返回结果存在生成文件名

```
{
	"token": "XXX",
	"sid": "X"
}
```

- `token`登录后返回的**token**
- `sid`目标的**sid**值，可以通过`/api/active_scan_list_query`接口来获取

#### 扫描报告下载接口

`/api/download_word/`下载报告使用

```
{
   "token": "XXX",
   "file_name": "X"
}
```

- `token`登录后返回的**token**
- `file_name`文件名通过上个接口获得

#### 获取用户个人信息

`/api/user_info/`获取个人详细信息使用

```
{
   "token": "XXX"
}
```

- `token`登录后返回的**token**

#### 更新用户密码

`/api/update_password/`更新用户密码

```
{
	"username": "ascotbe",
	"old_passwd": "1",
	"new_passwd": "1111"
}
```

- `username`为用户名称，唯一值
- `old_passwd`该用户以前密码
- `new_passwd`该用户需要修改的新密码

#### 更新用户显示名称

`/api/update_show_name/`更新用户显示名称

```
{
   "token": "xxxxx",
   "new_show_name": "1"
}
```

- `token`登录后返回的**token**
- `new_show_name`用户需要更新的新显示名

#### 更新用户秘钥

`/api/update_key/`更新用户key

```
{
   "token": "xxxxx"
}
```

- `token`登录后返回的**token**