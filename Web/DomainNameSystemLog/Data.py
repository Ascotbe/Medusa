#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,DomainNameSystemLog,DomainNameSystemLogKeyword
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
from config import domain_name_system_address
"""domain_name_system_log
{
	"key": "",
	"number_of_pages":""
}
"""
def DNSQuery(request):  # 用于DNS类型的DNSLOG数据查询
    RequestLogRecord(request, request_api="domain_name_system_log")
    if request.method == "POST":
        try:
            Key = json.loads(request.body)["key"]
            NumberOfPages = json.loads(request.body)["number_of_pages"]
            Uid = UserInfo().QueryUidWithKey(Key)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="domain_name_system_log", uid=Uid)  # 查询到了在计入
                #通过UID进行获取key
                DomainNameSystemLogKey=DomainNameSystemLogKeyword().Query(uid=Uid)#获取key
                DNSKey=DomainNameSystemLogKey+"."+domain_name_system_address#拼接获取该用户的DNSLOG完整值
                DomainNameSystemLogResult = DomainNameSystemLog().Query2DNS(key=DNSKey,
                    number_of_pages=int(NumberOfPages))  # 对解析记录进行查询
                return JsonResponse({'message': DomainNameSystemLogResult, 'code': 200, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""http_domain_name_system_log
{
	"token": "",
	"number_of_pages":""
}
"""
def HTTPQuery(request):  # 用于HTTP类型的DNSLOG数据查询
    RequestLogRecord(request, request_api="http_domain_name_system_log")
    if request.method == "POST":
        try:
            Token = json.loads(request.body)["token"]
            NumberOfPages = json.loads(request.body)["number_of_pages"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="http_domain_name_system_log", uid=Uid)  # 查询到了在计入
                DomainNameSystemLogResult = DomainNameSystemLog().Query2HTTP(
                    number_of_pages=int(NumberOfPages))  # 对解析记录进行查询
                return JsonResponse({'message': DomainNameSystemLogResult, 'code': 200, })


            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""domain_name_system_log_statistics
{
	"token": "xxx"
}
"""
def DNSStatistics(request):#对DNS类型数据进行统计
    RequestLogRecord(request, request_api="domain_name_system_log_statistics")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="domain_name_system_log_statistics", uid=Uid)  # 查询到了在计入
                DomainNameSystemLogKey = DomainNameSystemLogKeyword().Query(uid=Uid)  # 获取key
                if DomainNameSystemLogKey is not None:

                    Key=DomainNameSystemLogKey+"."+domain_name_system_address#拼接获取该用户的DNSLOG完整值

                    Result = DomainNameSystemLog().Statistical2DNS(key=Key)  # 统计的个数
                    return JsonResponse({'message': Result, 'code': 200, })
                else:
                    return JsonResponse({'message': "小宝贝找不到你的key呢(๑•̀ㅂ•́)و✧", 'code': 501, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""http_domain_name_system_log_statistics
{
	"token": "xxx"
}
"""
def HTTPStatistics(request):#对DNS类型数据进行统计
    RequestLogRecord(request, request_api="http_domain_name_system_log_statistics")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="http_domain_name_system_log_statistics", uid=Uid)  # 查询到了在计入

                Result = DomainNameSystemLog().Statistical2HTTP()  # 统计的个数
                return JsonResponse({'message': Result, 'code': 200, })


            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""get_domain_name_system_log
{
	"key": "xxx"
}
"""
def GetDNSLog(request):#获取用户的DNSLOG
    RequestLogRecord(request, request_api="get_domain_name_system_log")
    if request.method == "POST":
        try:
            Key = json.loads(request.body)["key"]
            Uid = UserInfo().QueryUidWithKey(Key)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="get_domain_name_system_log", uid=Uid)  # 查询到了在计入
                #通过UID进行获取key
                DomainNameSystemLogKey=DomainNameSystemLogKeyword().Query(uid=Uid)#获取key
                if DomainNameSystemLogKey is not None:
                    DNSKey=DomainNameSystemLogKey+"."+domain_name_system_address#拼接获取该用户的DNSLOG完整值
                    return JsonResponse({'message': DNSKey, 'code': 200, })
                else:
                    return JsonResponse({'message': "小宝贝获取失败啦(๑•̀ㅂ•́)و✧", 'code': 503, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })