### 配置数据查询

`/api/medusa_info/`

```json
{
	"token": "XXXX"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回用户当前信息

  ```json
  {
  	"message": {
  		"version": "v1.0.68",
  		"latest_version": "https://github.com/Ascotbe/Medusa/releases",
  		"official_documentation": "https://medusa.ascotbe.com/",
  		"registration_function_status": true,
  		"forgot_password_function_status": false,
  		"cross_site_script_uses_domain_names": {
  			"state": false,
  			"value": "127.0.0.1:1234"
  		},
  		"domain_name_system_address": {
  			"state": false,
  			"value": "dnslog.ascotbe.com"
  		},
  		"local_mail_host": {
  			"state": false,
  			"value": "smtp.ascotbe.com"
  		}
  	},
  	"code": 200
  }
  ```

  > 返回参数解释

  - `version`当前版本
  - `latest_version`最新版本
  - `official_documentation`官方文档
  - `registration_function_status`注册功能状态
  - `forgot_password_function_status`忘记密码状态
  - `cross_site_script_uses_domain_names`XSS域名配置
    - `state`表示是否修改
    - `value`该参数的值
  - `domain_name_system_address`DNSLOG域名配置
    - `state`表示是否修改
    - `value`该参数的值
  - `local_mail_host`自建邮件服务
    - `state`表示是否修改
    - `value`该参数的值

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

