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

### 查询协同作战项目

`/api/query_markdown_project/`用来查询协同作战，返回所有属于该用户的项目

```json
{
	"token": "xxxx"
}
```

>参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回查询到的数据内容

  ```json
  {
  	"message": [{
  		"markdown_project_name": "xxddddx",
  		"markdown_name": "uGvAGWO1N9IQOd7JywecwwF0iXpkfAumL4s7Sr5DLaqx3UDdA5BaBvK6DtQ8RqDboMLYtw1sEr2zHkBvmqW8MASFAYhvcazSpyUQ5tGx8gaBMQT2zrnjZKDCCQDEAg7AycTylGHnqojhJh4393wpO6EKDytdcaocY8cCz4W70vmY31JkQzwkrIyk5E1IvSDbphlROpeDyaLZr0XzSud1uAUfbPC0lOPAOGFs5CQtbvSrn8I5OHemMfhMvm",
  		"creation_time": "1609480740"
  	}, {
  		"markdown_project_name": "xxddddx",
  		"markdown_name": "NFDYXeTeniuN0JhMWMEQqvJwYr3Nrwq7DP0AO8WCb3YwANGBBafetFgeSTr3xA4dqa48WJpgRiNEplu9VqWy9Q2dRokzT9p9QrqG6VU4IYTkjr5r0jTNLtn7Nm795U1HoxlwgMAXTBF1SAyZpIgsoVSRKadCQpW4aOl4DB2ohtRUlU703aRETVbmyQKLbPRhQnKIsp1PXS7Sz4KojQa0kIaCvtpQfwHT4Vpuv2c0q2gqE4klJf9JvnpUkc",
  		"creation_time": "1609480951"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  **message有中存在多个数据**

  - `markdown_project_name`项目名称
  - `markdown_name`文档名称
  - `creation_time`项目创建时间

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

- 200：保存成功啦~阿巴阿巴~
- 403：小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧
- 404：小朋友不是你的东西别乱动哦~~
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
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