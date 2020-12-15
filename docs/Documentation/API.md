当前测试版本API接口，路径分别如下，只接受POST请求中的JSON格式数据

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
/api/create_proxy_scan_project/
/api/homepage_default_data/
/api/homepage_vulnerability_distributiont_data/
/api/homepage_github_monitor_data/
/api/upload_avatar/
/api/github_monitor/
/api/forget_password/
/api/actively_scan_port_information/
/api/create_cross_site_script_project/
/api/query_cross_site_script_project/
/api/query_cross_site_script_project_data/
/api/read_cross_site_script_template/
/api/read_default_cross_site_script_template/
/api/save_cross_site_script_template/
/api/system_hardware_initialization/
/api/system_hardware_usage_query/
/api/antivirus_software_compared/
/api/modify_cross_site_script_template/
/api/modify_cross_site_script_project/
/api/windows_portable_execute_analysis/
/api/query_cross_site_script_project_info/
```

### 注册接口

`/api/registered`该接口只能注册用户权限账户，接收数据格式如下

```
{
	"show_name": "Rei Ayanami",
	"username": "ascotbe",
	"passwd": "Soryu Asuka Langley",
	"email": "medusa@ascotbe.com",
	"key": "XXXXXXXXm"
}
```

> 参数解释

- `show_name`表示用户显示名字，可以重复
- `username`表示登录名，具有唯一性
- `passwd`用户密码（使用MD5存储
- `email`用户邮箱具有唯一性。（~~无校检，任意字符串都可以~~
- `key`用户本地**config.py**文件中设置的**secret_key_required_for_account_registration**字段值

> 返回状态码

- 604：用户名或邮箱已存在
- 404：报错
- 403：小宝贝这是非法注册哦(๑•̀ㅂ•́)و✧
- 200：注册成功
- 400：位置错误
- 603：注册失败
- 503：小宝贝你没有开启注册功能哦！！
- 666：宝贝数据呢？
- 500：请使用Post请求

### 登录接口

`/api/login`接收数据如下，登录成功返回**token**，并且具有时效性（目前暂无验证码后续更新

```
{
	"username": "ascotbe",
	"passwd": "Soryu Asuka Langley"
}
```

> 参数解释

- `username` 登录名
- `passwd`登录密码

>返回状态码

- 604：账号或密码错误
- 200：返回用户token
- 500：请使用Post请求

### 扫描任务下发接口

`/api/vulnerability_scanning` 用来下发任务，如果下发成功返回**200**

```
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
- `header`自定义头，如果没有的话传入`""`即可，如果想要自定义请传入完整的header以字典的形式传入
- `proxy`该任务指定代理，如果没有代理该值直接传入`""` 即可，注意代理是否可用

> 返回状态码

- 200：任务下发成功👌
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 666：类型错误！
- 169：莎酱被玩坏掉嘞QAQ
- 500：请使用Post请求

### 主动扫描目标列表查询接口

`/api/active_scan_list_query` 用来查询用户下发了哪些任务列表，返回结果是**JSON**格式

```
{
	"token": "XXXXX"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回扫描列表信息
- 404：数据库出问题了🐈
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：莎酱被玩坏啦(>^ω^<)喵
- 500：请使用Post请求

###  主动扫描目标漏洞列表查询接口

`/api/scan_information_query` 用来查询用户某个任务漏洞列表，返回结果是`JSON`格式

```
{
	"token": "XXXXX",
	"active_scan_id":"1"
}
```

>参数解释

- `token`登录后返回的**token**
- `active_scan_id`目标的**sid**值，上个接口查询返回中存在

> 返回状态码

- 200：返回关系查询列表结果
- 404：数据库炸了BOOM~🐈
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：莎酱被玩坏啦ヽ(･ω･´ﾒ)
- 500：请使用Post请求

### 主动扫描目标单个漏洞详细内容查询接口

`/api/medusa_query`用来查询某个任务中某个漏洞详细信息，返回结果是`JSON`格式

```
{
	"token": "XXXXX",
	"scan_info_id":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `scan_info_id`目标的**ssid**值，上个接口查询返回中存在

> 返回状态码

- 200：返回数据库单个漏洞查询结果
- 404：数据库GG了🐈
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：莎酱被玩坏啦ヾ(=･ω･=)o
- 500：请使用Post请求

### 扫描报告生成接口

`/api/generate_word`用来生成报告使用，返回结果存在生成文件名

```
{
	"token": "XXX",
	"active_scan_id": "X"
}
```

> 参数解释

- `token`登录后返回的**token**
- `active_scan_id`目标的**sid**值，可以通过`/api/active_scan_list_query`接口来获取

> 返回状态码

- 200：返回报告下载文件名
- 404：莎酱生不出小莎酱惹QAQ
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：莎酱被玩坏啦(>^ω^<)喵
- 500：请使用Post请求

### 扫描报告下载接口

`/api/download_word/`下载报告使用

```
{
   "token": "XXX",
   "file_name": "X"
}
```

> 参数解释

- `token`登录后返回的**token**
- `file_name`文件名通过上个接口获得

> 返回状态码

- 404：啊啊啊它不是你的小莎酱，别乱抱呀！
- 169：莎酱被玩坏啦(>^ω^<)喵
- 403：小宝贝这是非法下载哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 成功不返回任何结果直接跳转下载

### 获取用户个人信息

`/api/user_info/`获取个人详细信息使用

```
{
   "token": "XXX"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 404：搁着闹呢？
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 200：返回个人用户详细信息
- 500：请使用Post请求

### 更新用户密码

`/api/update_password/`更新用户密码

```
{
	"username": "ascotbe",
	"old_passwd": "Soryu Asuka Langley",
	"new_passwd": "XXXXXXXXXXXXXXXXXXX"
}
```

> 参数解释

- `username`为用户名称，唯一值
- `old_passwd`该用户以前密码
- `new_passwd`该用户需要修改的新密码

> 返回状态码

- 200：好耶！修改成功~
- 404：输入信息有误重新输入
- 500：请使用Post请求

### 更新用户显示名称

`/api/update_show_name/`更新用户显示名称

```
{
   "token": "xxxxx",
   "new_show_name": "阿巴阿巴阿巴"
}
```

> 参数解释

- `token`登录后返回的**token**
- `new_show_name`用户需要更新的新显示名

> 返回状态码

- 200：好诶！修改成功~
- 404：输入信息有误重新输入
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求

### 更新用户秘钥

`/api/update_key/`更新用户key

```
{
   "token": "xxxxx"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：呐呐呐呐！修改成功了呢~
- 404：输入信息有误重新输入
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求

### 创建代理扫描项目

`/api/create_proxy_scan_project/`创建代理扫描项目

```
{
    "token": "XXXXXX",
    "proxy_project_name":"Soryu Asuka Langley",
    "proxy_username":"ascotbe",
    "proxy_password":"ascotbe",
    "end_time":"1610751014"
}
```

> 参数解释

- `token`登录后返回的**token**
- `proxy_project_name`代理扫描项目的名字
- `proxy_username`代理扫描用户名
- `proxy_password`代理扫描用户密码
- `end_time`代理扫描结束时间

> 返回状态码

- 200：小宝贝!创建成功了呢~
- 503：代理扫描项目创建失败!
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求

### 首页默认信息

`/api/homepage_default_data/`首页信息查询接口

```
{
	"token": "XXXX"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 404：想啥呢？不知道查询出问题了吗？
- 200：返回用户当前信息
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用Post请求

### 首页漏洞分布信息

`/api/homepage_vulnerability_distributiont_data/`首页信息查询接口

```
{
	"token": "XXXX",
	"start_time": "1594087497",
	"end_time": "1604087497"
}
```

> 参数解释

- `token`登录后返回的**token**
- `start_time`首次登陆默认传入当前时间30天以前的**Unix**
- `end_time`默认传入当前时间的**Unix**

> 返回状态码

- 503：小宝贝时间呢？
- 404：想啥呢？不知道查询出问题了吗？
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 200：返回用户当前信息
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用Post请求

### 首页GitHub监控信息

`/api/homepage_github_monitor_data/`首页信息查询接口

```
{
	"token": "XXXX",
	"start_time": "1594087497",
	"end_time": "1604087497"
}
```

> 参数解释

- `token`登录后返回的**token**
- `start_time`首次登陆默认传入当前时间30天以前的**Unix**
- `end_time`默认传入当前时间的**Unix**

> 返回状态码

- 503：小宝贝时间呢？
- 404：想啥呢？不知道查询出问题了吗？
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 200：返回用户当前信息
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用Post请求

### 更新头像

`/api/upload_avatar/`更新头像接口

```
POST /api/upload_avatar/ HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryaFtQbWz7pBzNgCOv
token:UserToken

------WebKitFormBoundaryaFtQbWz7pBzNgCOv
Content-Disposition: form-data; name="file"; filename="test.jpeg"
Content-Type: image/jpeg

FileDate
------WebKitFormBoundaryaFtQbWz7pBzNgCOv--
```

> 参数解释

- `token`这个参数放在数据包中的header中
- `FileDate`这个参数是图片文件内容

> 返回状态码

- 200：返回用户头像名字
- 603：它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：宝贝没有用户你要插到哪里去呢？
- 169：你不对劲！为什么报错了？
- 500：请使用Post请求

### GitHub监控详细

`/api/github_monitor/`GitHubCVE数查询接口

```
{
	"token": "xxx"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回查询到的数据
- 404：非法查询哦宝贝！
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求

### 忘记密码接口

`/api/forget_password/`用来忘记密码修改使用

```
{
	"key": "XXXXX",
	"name": "ascotbe",
	"new_passwd": "test",
	"email": "medusa@ascotbe.com",
}
```

> 参数解释

- `key`用户本地**config.py**文件中设置的**forget_password_key**值
- `name`用户的用户名
- `new_passwd`用户新密码
- `email`用户的邮箱

> 返回状态码

- 200：修改成功啦~建议去配置文件中关闭忘记密码功能哦~
- 503：这个数据你是认真的嘛(。﹏。)
- 404：大黑阔别乱搞，莎莎好怕怕(\*/ω＼*)
- 403：小宝贝你没有开启忘记密码功能哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求



### 主动扫描端口查询

`/api/actively_scan_port_information/`用来查询主动扫描中的端口扫描信息

```
{
	"token": "XXXXX",
	"active_scan_id":"1"
}
```

>参数解释

- `token`登录后返回的**token**
- `active_scan_id`目标的**active_scan_id**值，主动扫描生成的值

> 返回状态码

- 200：返回关系查询列表结果
- 404：宝贝没有数据哦🐈'
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：莎酱被玩坏啦ヽ(･ω･´ﾒ)
- 500：请使用Post请求

### 创建跨站脚本钓鱼项目

`/api/create_cross_site_script_project/`用来创建跨站脚本项目

```
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

```
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

```
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

### 查询跨站脚本钓鱼项目详细信息

`/api/query_cross_site_script_project_info/`用来查询用户的跨站脚本项目的详细信息

```
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

### 

### 查询跨站脚本钓鱼项目中数据

`/api/query_cross_site_script_project_data/`用来查询用户的跨站脚本项目中的数据信息

```
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

### 读取默认跨站脚本模板数据

`/api/read_default_cross_site_script_template/`用来跨站脚本中的默认数据有哪些

```
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

```
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

```
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

```
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



### 获取当前机器基础信息

`/api/system_hardware_initialization/`用来当前机器的基础信息

```
{
	"token": ""
}
```

>参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回计算机信息
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用Post请求

### 获取当前机器CPU和内存使用率

`/api/system_hardware_usage_query/`用来当前机器的CPU和内存使用率，区间为当前时间之前1小时

```
{
	"token": ""
}
```

>参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回查询到的详细信息
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用Post请求

### 杀毒软件进程查询接口

`/api/antivirus_software_compared/`用来对比文本中是否存在杀软

```
{
	"token": "",
	"process_name_list":[]
}
```

>参数解释

- `token`登录后返回的**token**
- `process_name_list`用户传入的进程列表，需要使用dict类型

> 返回状态码

- 200：返回查询到的杀软
- 666：未查询到杀软
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用Post请求

### PE文件解析接口

`/api/windows_portable_execute_analysis/`用来对比文本中是否存在杀软

```
POST /api/windows_portable_execute_analysis/ HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryaFtQbWz7pBzNgCOv
token:UserToken

------WebKitFormBoundaryaFtQbWz7pBzNgCOv
Content-Disposition: form-data; name="file"; filename="test.exe"
Content-Type: text/exe

FileDate
------WebKitFormBoundaryaFtQbWz7pBzNgCOv--
```

>参数解释

- `token`登录后返回的**token**
- `FileDate`上传文件的内容

> 返回状态码

- 200：成功了
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 501：文件太大啦~(๑•̀ㅂ•́)و✧