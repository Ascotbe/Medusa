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
            key = json.loads(request.body)["key"]
            number_of_pages = json.loads(request.body)["number_of_pages"]
            uid = UserInfo().QueryUidWithKey(key)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="domain_name_system_log", uid=uid)  # 查询到了在计入
                #通过UID进行获取key
                log_key=DomainNameSystemLogKeyword().Query(uid=uid)#获取key
                DNSKey=log_key+"."+domain_name_system_address#拼接获取该用户的DNSLOG完整值
                result = DomainNameSystemLog().Query2DNS(key=DNSKey,
                    number_of_pages=int(number_of_pages))  # 对解析记录进行查询
                return JsonResponse({'message': result, 'code': 200, })

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
            token = json.loads(request.body)["token"]
            number_of_pages = json.loads(request.body)["number_of_pages"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="http_domain_name_system_log", uid=uid)  # 查询到了在计入
                result = DomainNameSystemLog().Query2HTTP(
                    number_of_pages=int(number_of_pages))  # 对解析记录进行查询
                return JsonResponse({'message': result, 'code': 200, })


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
            token=json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="domain_name_system_log_statistics", uid=uid)  # 查询到了在计入
                log_key = DomainNameSystemLogKeyword().Query(uid=uid)  # 获取key
                if log_key != None:

                    key=log_key+"."+domain_name_system_address#拼接获取该用户的DNSLOG完整值

                    result = DomainNameSystemLog().Statistical2DNS(key=key)  # 统计的个数
                    return JsonResponse({'message': result, 'code': 200, })
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
            token=json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="http_domain_name_system_log_statistics", uid=uid)  # 查询到了在计入

                result = DomainNameSystemLog().Statistical2HTTP()  # 统计的个数
                return JsonResponse({'message': result, 'code': 200, })


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
            key = json.loads(request.body)["key"]
            uid = UserInfo().QueryUidWithKey(key)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="get_domain_name_system_log", uid=uid)  # 查询到了在计入
                #通过UID进行获取key
                log_key=DomainNameSystemLogKeyword().Query(uid=uid)#获取key
                if log_key is not None:
                    DNSKey=log_key+"."+domain_name_system_address#拼接获取该用户的DNSLOG完整值
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