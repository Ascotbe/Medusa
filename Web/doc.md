# Backend（临时文档）
## Packages
- REST Framework 接口形态
- djoser 登陆用
## 栗子
- 创建超级用户  `python3 manage.py createsuperuser` 然后按步骤走即可
- 登陆测试命令 `curl -X POST -d '{"username": "用户名","password": "密码"}' -H 'Content-Type: application/json'  http://127.0.0.1:8000/api/auth/token/login/`
  - 返回令牌（字符串）
- 需要权限的命令（举个例子） `curl -X GET http://127.0.0.1:8000/users/ -H 'Authorization: Token d7194299b329158175940aa2e43c8ce2aa773226' `
  - 无效令牌则错误 `{"detail":"认证令牌无效。"}`
  - 正确则返回普通JSON数据包（不含密码）

## 还没做的内容（还有很多）
- 用户模块（登陆可用，鉴权部分可用（根据令牌判断是否登陆，只能修改自己的内容，其他不可用），其他不可用）
- 扫描模块（目前花瓶）
- 其他模块
