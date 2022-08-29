#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,VerificationCode,DomainNameSystemLogKeyword
from ClassCongregation import ErrorLog,randoms
from django.http import JsonResponse
import json
from config import secret_key_required_for_account_registration,registration_function_status
from ClassCongregation import Md5Encryption
from Web.Workbench.LogRelated import RequestLogRecord

"""registered
{
	"show_name": "7777777",
	"username": "ascotbe",
	"passwd": "1",
	"email": "1@qq.com",
	"key": "XXXXXXXXm",
	"verification_code_key": "1",
	"verification_code":"1"
}
"""
def Registered(request):
    RequestLogRecord(request, request_api="registered")
    if request.method == "POST":
        try:
            show_name = json.loads(request.body).get("show_name")
            username=json.loads(request.body).get("username")
            passwd=json.loads(request.body).get("passwd")
            email=json.loads(request.body).get("email")
            key = json.loads(request.body).get("key")
            verification_code_key = json.loads(request.body)["verification_code_key"]#获取验证码关联的KEY
            Code = json.loads(request.body)["verification_code"].lower()#获取验证码

            if verification_code_key!=None and Code!=None:#判断传入数据不为空
                verification_code_result=VerificationCode().Query(code=Code,verification_code_key=verification_code_key)#获取判断
                if verification_code_result:#如果为真,进行登录验证
                    if registration_function_status:#判断是否开启注册功能
                        if len(show_name.strip("\r\n"))==0 or len(username.strip("\r\n"))==0 or len(passwd.strip("\r\n"))==0 or len(email.strip("\r\n"))==0 or len(key.strip("\r\n"))==0:#验证数据不为空
                            return JsonResponse({'message': '宝贝数据呢？💚', 'code': 666, })
                        else:
                            if key==secret_key_required_for_account_registration:#判断是否符合注册值
                                verify_username=UserInfo().VerifyUsername(username)
                                verify_email=UserInfo().VerifyEmail(email)
                                if verify_username or verify_email:
                                    return JsonResponse({'message': '用户名或邮箱已存在', 'code': 604, })

                                elif (verify_username is None)or(verify_email is None):

                                    return JsonResponse({'message': '报错了🙄', 'code': 404, })
                                elif not verify_username or not verify_email:
                                    token=randoms().result(250)
                                    uid = randoms().result(100)#生成随机数,用户UID
                                    key = randoms().result(40) #生成key值
                                    domain_name_system_log_key = randoms().LowercaseAndNumbers(5)  # 生成DNSLOGkey值
                                    md5_passwd=Md5Encryption().Md5Result(passwd)#进行加密
                                    user_write=UserInfo().Write(name=username, show_name=show_name, token=token, passwd=md5_passwd,
                                                     email=email, uid=uid,key=key,avatar="admin.jpg")
                                    DomainNameSystemLogKeyword().Write(uid=uid,key=domain_name_system_log_key)
                                    if user_write:
                                        return JsonResponse({'message': '注册成功', 'code': 200, })
                                    elif user_write is None:
                                        return JsonResponse({'message': '未知错误', 'code': 400, })
                                    else:
                                        return JsonResponse({'message': '注册失败', 'code': 603, })
                            else:
                                return JsonResponse({'message': '小宝贝这是非法注册哦(๑•̀ㅂ•́)و✧', 'code': 403, })
                    else:
                        return JsonResponse({'message': '小宝贝你没有开启注册功能哦！！', 'code': 503, })
                else:
                    return JsonResponse({'message': "验证码错误或者过期！", 'code': 504, })
            else:
                return JsonResponse({'message': "验证码或者验证码秘钥不能为空！", 'code': 505, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
