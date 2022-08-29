#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,VerificationCode
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,Md5Encryption,GetPath
import json
import time
from config import forget_password_key,forgot_password_function_status
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""login
{
	"username": "ascotbe",
	"passwd": "1",
	"verification_code_key": "1",
	"verification_code":"1"
}
"""
def Login(request):#用户登录，每次登录成功都会刷新一次Token
    RequestLogRecord(request, request_api="login")
    if request.method == "POST":
        try:
            username=json.loads(request.body)["username"]
            passwd=json.loads(request.body)["passwd"]
            verification_code_key = json.loads(request.body)["verification_code_key"]#获取验证码关联的KEY
            verification_code = json.loads(request.body)["verification_code"].lower()#获取验证码,把验证码全部转换成小写
            md5_passwd=Md5Encryption().Md5Result(passwd)#对密码加密
            if verification_code_key!=None and verification_code!=None:#判断传入数据不为空
                verification_code_result=VerificationCode().Query(code=verification_code,verification_code_key=verification_code_key)#获取判断
                if verification_code_result:#如果为真,进行登录验证
                    user_login=UserInfo().UserLogin(username,md5_passwd)
                    if user_login is None:
                        return JsonResponse({'message': '账号或密码错误', 'code': 604, })

                    else:
                        while True:#如果查询确实冲突了
                            token = randoms().result(250)
                            query_token_validity = UserInfo().QueryTokenValidity(token)#用来查询Token是否冲突了
                            if not query_token_validity:#如果不冲突的话跳出循环
                                break
                        update_token=UserInfo().UpdateToken(name=username, token=token)#接着更新Token
                        if update_token:#如果更新成功了
                            uid = UserInfo().QueryUidWithToken(token)  # 查询UID
                            UserOperationLogRecord(request, request_api="login", uid=uid)
                            return JsonResponse({'message': token, 'code': 200, })
                else:
                    return JsonResponse({'message': "验证码错误或者过期！", 'code': 503, })
            else:
                return JsonResponse({'message': "验证码或者验证码秘钥不能为空！", 'code': 504, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""update_password
{
	"username": "ascotbe",
	"old_passwd": "1",
	"new_passwd": "1111",
	"verification_code_key": "1",
	"verification_code":"1"
}
"""
def UpdatePassword(request):#更新密码
    RequestLogRecord(request, request_api="update_password")
    if request.method == "POST":
        try:
            username=json.loads(request.body)["username"]
            old_passwd=json.loads(request.body)["old_passwd"]
            new_passwd = json.loads(request.body)["new_passwd"]
            verification_code_key = json.loads(request.body)["verification_code_key"]#获取验证码关联的KEY
            verification_code = json.loads(request.body)["verification_code"].lower()#获取验证码

            if verification_code_key!=None and verification_code!=None:#判断传入数据不为空
                verification_code_result=VerificationCode().Query(code=verification_code,verification_code_key=verification_code_key)#获取判断
                if verification_code_result:#如果为真,进行登录验证
                    md5_new_passwd = Md5Encryption().Md5Result(new_passwd)  # 对新密码加密
                    md5_old_passwd = Md5Encryption().Md5Result(old_passwd)  # 对旧密码加密
                    update_password=UserInfo().UpdatePasswd(name=username,old_passwd=md5_old_passwd,new_passwd=md5_new_passwd)
                    if update_password:
                        UserOperationLogRecord(request, request_api="update_password", uid=username)#如果修改成功写入数据库中
                        return JsonResponse({'message': '好耶！修改成功~', 'code': 200, })
                    else:
                        return JsonResponse({'message': "输入信息有误重新输入", 'code': 404, })
                else:
                    return JsonResponse({'message': "验证码错误或者过期！", 'code': 503, })
            else:
                return JsonResponse({'message': "验证码或者验证码秘钥不能为空！", 'code': 504, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""update_show_name
{
	"token": "xxxxx",
	"new_show_name": "1"
}
"""
def UpdateShowName(request):#更新显示名字
    RequestLogRecord(request, request_api="update_show_name")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            new_show_name= json.loads(request.body)["new_show_name"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="update_show_name", uid=uid)  # 查询到了在计入
                result=UserInfo().UpdateShowName(uid=uid,show_name=new_show_name)#获取值查看是否成功
                if result:
                    return JsonResponse({'message': '好诶！修改成功~', 'code': 200, })
                else:
                    return JsonResponse({'message': "输入信息有误重新输入", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""update_key
{
	"token": "xxxxx"
}
"""
def UpdateKey(request):#更新Key
    RequestLogRecord(request, request_api="update_key")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            new_key= randoms().result(40)#生成随机的key,有可能会重复，这边先暂时不管了，这概论太j8低了
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="update_key", uid=uid)  # 查询到了在计入
                result=UserInfo().UpdateKey(uid=uid,key=new_key)#获取值查看是否成功
                if result:
                    return JsonResponse({'message': '呐呐呐呐！修改成功了呢~', 'code': 200, })
                else:
                    return JsonResponse({'message': "输入信息有误重新输入", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""user_info
{
	"token": ""
}
"""
def PersonalInformation(request):#用户个人信息
    RequestLogRecord(request, request_api="user_info")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            info=UserInfo().QueryUserInfo(token)
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if info is None:
                return JsonResponse({'message': '搁着闹呢？', 'code': 404, })
            elif info != None and uid!=None:
                UserOperationLogRecord(request, request_api="user_info", uid=uid)
                json_values = {}#对数据进行二次处理
                json_values["id"] = info["id"]
                json_values["key"] = info["key"]
                json_values["name"] = info["name"]
                json_values["token"] = info["token"]
                json_values["show_name"] = info["show_name"]
                json_values["email"] = info["email"]
                json_values["avatar"] = info["avatar"]
                return JsonResponse({'message': json_values, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })


        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""upload_avatar
POST /api/upload_avatar/ HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryaFtQbWz7pBzNgCOv
token:XXXXXXXXXXXXXXXX

------WebKitFormBoundaryaFtQbWz7pBzNgCOv
Content-Disposition: form-data; name="file"; filename="test.jpeg"
Content-Type: image/jpeg

XXXXXXXXXXXXXXX
------WebKitFormBoundaryaFtQbWz7pBzNgCOv--
"""
def UploadAvatar(request):#文件上传功能
    RequestLogRecord(request, request_api="upload_avatar")
    token =request.headers["token"]
    if request.method == "POST":
        try:
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="upload_avatar", uid=uid)  # 查询到了在计入
                picture_data = request.FILES.get('file', None)#获取文件数据
                if 10240<picture_data.size:#最大值10MB，最小值10KB
                    save_file_name=randoms().result(10)+str(int(time.time()))+".jpg"#重命名文件
                    save_route=GetPath().ImageFilePath()+save_file_name#获得保存路径
                    with open(save_route, 'wb') as f:
                        for line in picture_data:
                            f.write(line)
                    UserInfo().UpdateAvatar(avatar=save_file_name,uid=uid)#图片写到本地后更新用户头像
                    return JsonResponse({'message': save_file_name, 'code': 200,})#返回上传图片名称
                else:
                    return JsonResponse({'message': '它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)',  'code': 603,})
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""forget_password
{
	"key": "",
	"name": "",
	"new_passwd": "",
	"email": "",
	"verification_code_key": "1",
	"verification_code":"1"
}
"""
def ForgetPassword(request):#忘记密码接口
    RequestLogRecord(request, request_api="forget_password")
    if request.method == "POST":
        try:
            key = json.loads(request.body)["key"]
            name = json.loads(request.body).get("name")
            new_passwd = json.loads(request.body).get("new_passwd")
            email = json.loads(request.body).get("email")
            verification_code_key = json.loads(request.body)["verification_code_key"]#获取验证码关联的KEY
            verification_code = json.loads(request.body)["verification_code"].lower()#获取验证码

            if verification_code_key!=None and verification_code!=None:#判断传入数据不为空
                verification_code_result=VerificationCode().Query(code=verification_code,verification_code_key=verification_code_key)#获取判断
                if verification_code_result:#如果为真,进行登录验证
                    if forgot_password_function_status:  # 查看状态是否关闭
                        if key==forget_password_key:#如果传入的key相等
                            md5_passwd = Md5Encryption().Md5Result(new_passwd)  # 进行加密
                            result=UserInfo().ForgetPassword(name=name,new_passwd=md5_passwd,email=email)#进行修改密码
                            if result:#如果修改成功
                                return JsonResponse({'message': "修改成功啦~建议去配置文件中关闭忘记密码功能哦~", 'code': 200, })
                            else:
                                return JsonResponse({'message': "这个数据你是认真的嘛(。﹏。)", 'code': 501, })
                        else:
                            return JsonResponse({'message': "大黑阔别乱搞，莎莎好怕怕(*/ω＼*)", 'code': 404, })
                    else:
                        return JsonResponse({'message': "小宝贝你没有开启忘记密码功能哦(๑•̀ㅂ•́)و✧", 'code': 403, })
                else:
                    return JsonResponse({'message': "验证码错误或者过期！", 'code': 503, })
            else:
                return JsonResponse({'message': "验证码或者验证码秘钥不能为空！", 'code': 504, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

