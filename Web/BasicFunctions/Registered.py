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
            ShowName = json.loads(request.body).get("show_name")
            Username=json.loads(request.body).get("username")
            Passwd=json.loads(request.body).get("passwd")
            Email=json.loads(request.body).get("email")
            Key = json.loads(request.body).get("key")
            VerificationCodeKey = json.loads(request.body)["verification_code_key"]#获取验证码关联的KEY
            Code = json.loads(request.body)["verification_code"].lower()#获取验证码

            if VerificationCodeKey!=None and Code!=None:#判断传入数据不为空
                VerificationCodeResult=VerificationCode().Query(code=Code,verification_code_key=VerificationCodeKey)#获取判断
                if VerificationCodeResult:#如果为真,进行登录验证
                    if registration_function_status:#判断是否开启注册功能
                        if len(ShowName.strip("\r\n"))==0 or len(Username.strip("\r\n"))==0 or len(Passwd.strip("\r\n"))==0 or len(Email.strip("\r\n"))==0 or len(Key.strip("\r\n"))==0:#验证数据不为空
                            return JsonResponse({'message': '宝贝数据呢？💚', 'code': 666, })
                        else:
                            if Key==secret_key_required_for_account_registration:#判断是否符合注册值
                                VerifyUsername=UserInfo().VerifyUsername(Username)
                                VerifyEmail=UserInfo().VerifyEmail(Email)
                                if VerifyUsername or VerifyEmail:
                                    return JsonResponse({'message': '用户名或邮箱已存在', 'code': 604, })

                                elif (VerifyUsername is None)or(VerifyEmail is None):

                                    return JsonResponse({'message': '报错了🙄', 'code': 404, })
                                elif not VerifyUsername or not VerifyEmail:
                                    Token=randoms().result(250)
                                    Uid = randoms().result(100)#生成随机数,用户UID
                                    Key = randoms().result(40) #生成key值
                                    DomainNameSystemLogKey = randoms().LowercaseAndNumbers(5)  # 生成DNSLOGkey值
                                    Md5Passwd=Md5Encryption().Md5Result(Passwd)#进行加密
                                    UserWrite=UserInfo().Write(name=Username, show_name=ShowName, token=Token, passwd=Md5Passwd,
                                                     email=Email, uid=Uid,key=Key,avatar="admin.jpg")
                                    DomainNameSystemLogKeyword().Write(uid=Uid,key=DomainNameSystemLogKey)
                                    if UserWrite:
                                        return JsonResponse({'message': '注册成功', 'code': 200, })
                                    elif UserWrite is None:
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
            ErrorLog().Write("Web_BasicFunctions_Registered_Registered(def)", e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
