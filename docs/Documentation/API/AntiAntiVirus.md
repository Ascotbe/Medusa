### 通过shellcode来生成免杀

`/api/shellcode_to_virus/`通过shellcode来生成

```json
{
	"token": "xxx",
	"shellcode":"\xdb\xdb\xdb\xdb\xdb\xdb",
	"shellcode_type":"1"
}
```

> 参数解释

- `token`登录后返回的**token**
- `shellcode` 通过**MSF**或者**CS**来生成的值，格式必须为`\xFF`
- `shellcode_type`来自**MSF**传入1，来自**CS**传入2

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 200：宝贝任务已下发~
- 403：小宝贝这是非法请求哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 600：你的电脑不是Windows或者Linux无法使用该功能ლ(•̀ _ •́ ლ)

### 用户免杀数据查询

`/api/anti_anti_virus_data_query/`用来查询当前用户下发的任务和状态

```json
{
	"token": "xxx",
	"number_of_pages":"20"
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`查询的页数，单页默认100个数据

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回用户当前信息

  ```json
  XX
  ```

  > 返回参数解释

  - `shellcode_type`来自**MSF**为1，来自**CS**为2
  - `virus_original_file_name`生成的未编译的文件名
  - `virus_generate_file_name`生成编译好的文件名
  - `compilation_status`文件编译状态，0为未完成，1完成，-1出错
  - `creation_time`创建时间

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求



### 用户免杀数据个数

`/api/anti_anti_virus_data_statistics/`个数统计

```json
{
	"token": ""
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回数据大小

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求