### 获取验证码接口接口

`/api/get_verification_code/`用来对比文本中是否存在杀软

>获取方式

- 直接使用GET请求获取

> 返回状态码

- 200：返回二进制图片数据，并且头部**VerificationCodeKey**为验证码相关的key
- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 500：请使用GET请求



