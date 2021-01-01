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

### 