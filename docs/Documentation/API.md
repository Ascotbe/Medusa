当前测试版本只有19个API接口，路径分别如下，只接受POST请求中的JSON格式数据

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
```

#### 注册接口

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

#### 登录接口

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

> 参数解释

- `url` 你扫描的目标
- `token` 登录后返回给你的**token**
- `threads`当前任务使用的进程树
- `module`指定扫描模块，具体名称参考**Modules**目录下的文件名
- `header`自定义头，如果没有的话传入**None**参数，用法和**bash**版一样
- `proxy`该任务指定代理，如果没有代理该值直接传入`0` ，注意代理是否可用

> 返回状态码

- 200：任务下发成功👌
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 666：类型错误！
- 169：莎酱被玩坏掉嘞QAQ
- 500：请使用Post请求

#### 主动扫描目标列表查询接口

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

####  主动扫描目标漏洞列表查询接口

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

#### 主动扫描目标单个漏洞详细内容查询接口

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

#### 扫描报告生成接口

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

#### 扫描报告下载接口

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

#### 获取用户个人信息

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

#### 更新用户密码

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

#### 更新用户显示名称

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

#### 更新用户秘钥

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

#### 创建代理扫描项目

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

#### 首页默认信息

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

#### 首页漏洞分布信息

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

#### 首页GitHub监控信息

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

#### 更新头像

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

#### GitHub监控详细

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

#### 忘记密码接口

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
- 404：大黑阔别乱搞，莎莎好怕怕(*/ω＼*)
- 403：小宝贝你没有开启忘记密码功能哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求