### 注册接口

`/api/registered`该接口只能注册用户权限账户，接收数据格式如下

```json
{
	"show_name": "Rei Ayanami",
	"username": "ascotbe",
	"passwd": "Soryu Asuka Langley",
	"email": "medusa@ascotbe.com",
	"key": "XXXXXXXXm",
	"verification_code_key": "1",
	"verification_code":"1"
}
```

> 参数解释

- `show_name`表示用户显示名字，可以重复
- `username`表示登录名，具有唯一性
- `passwd`用户密码（使用MD5存储
- `email`用户邮箱具有唯一性。（~~无校检，任意字符串都可以~~
- `key`用户本地**config.py**文件中设置的**secret_key_required_for_account_registration**字段值
- `verification_code_key`验证码相关的KEY
- `verification_code`验证码相关的值

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
- 503：验证码错误或者过期！
- 504：验证码或者验证码秘钥不能为空！



### 登录接口

`/api/login`接收数据如下，登录成功返回**token**，并且具有时效性（目前暂无验证码后续更新

```json
{
	"username": "ascotbe",
	"passwd": "Soryu Asuka Langley",
	"verification_code_key": "1",
	"verification_code":"1"
}
```

> 参数解释

- `username` 登录名
- `passwd`登录密码
- `verification_code_key`验证码相关的KEY
- `verification_code`验证码相关的值

>返回状态码

- 604：账号或密码错误
- 200：返回用户token
- 500：请使用Post请求
- 503：验证码错误或者过期！
- 504：验证码或者验证码秘钥不能为空！

### 获取用户个人信息

`/api/user_info/`获取个人详细信息使用

```json
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

```json
{
	"username": "ascotbe",
	"old_passwd": "Soryu Asuka Langley",
	"new_passwd": "XXXXXXXXXXXXXXXXXXX",
	"verification_code_key": "1",
	"verification_code":"1"
}
```

> 参数解释

- `username`为用户名称，唯一值
- `old_passwd`该用户以前密码
- `new_passwd`该用户需要修改的新密码
- `verification_code_key`验证码相关的KEY
- `verification_code`验证码相关的值

> 返回状态码

- 200：好耶！修改成功~
- 404：输入信息有误重新输入
- 500：请使用Post请求
- 503：验证码错误或者过期！
- 504：验证码或者验证码秘钥不能为空！

### 更新用户显示名称

`/api/update_show_name/`更新用户显示名称

```json
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

```json
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

### 忘记密码接口

`/api/forget_password/`用来忘记密码修改使用

```json
{
	"key": "XXXXX",
	"name": "ascotbe",
	"new_passwd": "test",
	"email": "medusa@ascotbe.com",
	"verification_code_key": "1",
	"verification_code":"1"
}
```

> 参数解释

- `key`用户本地**config.py**文件中设置的**forget_password_key**值
- `name`用户的用户名
- `new_passwd`用户新密码
- `email`用户的邮箱
- `verification_code_key`验证码相关的KEY
- `verification_code`验证码相关的值

> 返回状态码

- 200：修改成功啦~建议去配置文件中关闭忘记密码功能哦~
- 501：这个数据你是认真的嘛(。﹏。)
- 404：大黑阔别乱搞，莎莎好怕怕(\*/ω＼*)
- 403：小宝贝你没有开启忘记密码功能哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 503：验证码错误或者过期！
- 504：验证码或者验证码秘钥不能为空！

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

