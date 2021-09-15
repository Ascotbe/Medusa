### 创建协同作战项目

`/api/create_markdown_project/`用来创建协同作战

```json
{
	"token": "xxxx",
  "markdown_project_name": "xxx"
}
```

>参数解释

- `token`登录后返回的**token**
- `markdown_project_name`项目名

> 返回状态码

- 200：创建成功啦~玛卡玛卡~
- 403：小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用POST请求



### 加入协同作战项目

`api/join_markdown_project/`用来加入协同作战

```json
{
	"token": "xxxx",
    "markdown_project_invitation_code": "xxx"
}
```

>参数解释

- `token`登录后返回的**token**
- `markdown_project_invitation_code`项目生成的随机秘钥

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 200：加入项目成功啦~咕噜咕噜~
- 403：小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧
- 404：小宝贝不要调皮哦(⊙x⊙;)
- 500：请使用POST请求
- 501：小宝贝邀请码的长度不合规哦Σ(っ °Д °;)っ
- 502：你已经加入过项目啦~拉卡拉卡~
- 503：这就是你的项目，瞎鸡儿加个啥



### 查询协同作战项目

`/api/query_markdown_project/`用来查询协同作战，返回所有属于该用户的项目

```json
{
	"token": "xxxx",
  "number_of_pages":"1"
}
```

>参数解释

- `token`登录后返回的**token**
- `number_of_pages`页数

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回查询到的数据内容

  ```json
  {
  	"message": [{
      "markdown_project_owner": "xxddddx",
      "markdown_project_invitation_code": "xxddddx",
  		"markdown_project_name": "xxddddx",
  		"markdown_name": "uGvAGWO1N9IQOd7JywecwwF0iXpkfAumL4s7Sr5DLaqx3UDdA5BaBvK6DtQ8RqDboMLYtw1sEr2zHkBvmqW8MASFAYhvcazSpyUQ5tGx8gaBMQT2zrnjZKDCCQDEAg7AycTylGHnqojhJh4393wpO6EKDytdcaocY8cCz4W70vmY31JkQzwkrIyk5E1IvSDbphlROpeDyaLZr0XzSud1uAUfbPC0lOPAOGFs5CQtbvSrn8I5OHemMfhMvm",
  		"creation_time": "1609480740"
  	}, {
      "markdown_project_owner": "xxddddx",
      "markdown_project_invitation_code": "xxddddx",
  		"markdown_project_name": "xxddddx",
  		"markdown_name": "NFDYXeTeniuN0JhMWMEQqvJwYr3Nrwq7DP0AO8WCb3YwANGBBafetFgeSTr3xA4dqa48WJpgRiNEplu9VqWy9Q2dRokzT9p9QrqG6VU4IYTkjr5r0jTNLtn7Nm795U1HoxlwgMAXTBF1SAyZpIgsoVSRKadCQpW4aOl4DB2ohtRUlU703aRETVbmyQKLbPRhQnKIsp1PXS7Sz4KojQa0kIaCvtpQfwHT4Vpuv2c0q2gqE4klJf9JvnpUkc",
  		"creation_time": "1609480951"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  **message有中存在多个数据**

  - `markdown_project_owner`项目是否所属用户，1表示属于，0表示不属于
  - `markdown_project_invitation_code`邀请别人加入项目的邀请码
  - `markdown_project_name`项目名称
  - `markdown_name`文档名称
  - `creation_time`项目创建时间

- 403：小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧

- 500：请使用POST请求



### 统计用户协同作战项目个数

`/api/markdown_project_statistical/`

```json
{
	"token": "xxxx"
}
```

>参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回个数
- 403：小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用POST请求



### 保存Markdown文档数据

`/api/save_markdown_data/`用来保存Markdown文档数据

```json
{
	"token": "xxxx",
	"markdown_data": "xxx",
	"markdown_name": "xxx"
}
```

>参数解释

- `token`登录后返回的**token**
- `markdown_data`文档数据
- `markdown_name`文档名称

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 200：保存成功啦~阿巴阿巴~
- 403：小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧
- 404：小朋友不是你的东西别乱动哦~~
- 500：请使用POST请求
- 503：保存失败~玛卡巴卡~~



### 查询Markdown文档数据

`/api/query_markdown_data/`用来查询Markdown文档数据

```json
{
	"token": "xxxx",
	"markdown_name": "xxx"
}
```

>参数解释

- `token`登录后返回的**token**
- `markdown_name`文档名称

> 返回状态码

- 200：返回查询的数据

  ```json
  {
  	"message": [{
  		"markdown_name": "a1C3rADzVrlmGSCgBSxo8xQyqppMyG7vmy2uNeTA55Onw0hRFEgPScPhdAD3WRt3fYj84wWbi8r8Pmx3Fp3sbJl2t6Kf58AKAxQMQi9pYgYZ6qb0oUpF8y6iTP1EocmUy5w4H7a9ilFev10TPd7wlCRtn1L5gFduncv4aYlcBh02JjxJyVt6Ya4euDn4AyR3B7dLC4HZASkybJntjVeuRULKohgtfyiSSGLypYJeRXSzc1Ltpn7sUWRZiH",
  		"markdown_data": "eDIyMnh4",
  		"creation_time": "1609483284",
  		"update_time": "1609484109"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  - `markdown_name`文档名称
  - `markdown_data`文档数据，前端需要进行base64解密
  - `creation_time`文档创建时间
  - `update_time`文档最后一次修改时间

- 403：小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧

- 404：小朋友不是你的东西别乱动哦~~

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 500：请使用POST请求



### 上传文档中的图片

`/api/markdown_image_upload/`上传文档中的图片接口

```
POST /api/markdown_image_upload/ HTTP/1.1
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

- 169：你不对劲！为什么报错了？
- 200：返回用户头像名字
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：宝贝没有用户你要插到哪里去呢？
- 500：请使用Post请求
- 603：它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)

### Markdown文档数据对比

`/api/markdown_data_comparison/`用来查询Markdown文档数据

```json
{
	"token": "xxxx",
	"new_markdown_data": "xxxx",
	"markdown_name": "xxx"
}
```

>参数解释

- `token`登录后返回的**token**
- `new_markdown_data`用户需要保持的数据
- `markdown_name`文档名称

> 返回状态码

- 200：返回查询的数据

  ```json
  {
  	"message": "",
  	"code": 200
  }
  ```

  > 返回参数解释

  - `message`中保持的是对比后的html格式数据

- 403：小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧

- 404：小朋友不是你的东西别乱动哦~~

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 500：请使用POST请求

