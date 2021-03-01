### 杀毒软件进程查询接口

`/api/antivirus_software_compared/`用来对比文本中是否存在杀软

```json
{
	"token": "",
	"process_name_list":[]
}
```

>参数解释

- `token`登录后返回的**token**
- `process_name_list`用户传入的进程列表，需要使用dict类型

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 200：返回查询到的杀软
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 666：未查询到杀软

### PE文件解析接口

`/api/windows_portable_execute_analysis/`用来对比文本中是否存在杀软

```json
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
