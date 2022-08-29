#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,HomeInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""homepage_default_data
{
	"token": "XXXX"
}
"""
def HomepageDefaultData(request):#用户登录成功后跳转的首页，默认数据
    RequestLogRecord(request, request_api="homepage_default_data")
    if request.method == "POST":
        try:
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="homepage_default_data", uid=uid)
                default_data=HomeInfo().DefaultData(uid=uid)
                if default_data == None:
                    return JsonResponse({'message': "想啥呢？不知道查询出问题了吗？", 'code': 404, })
                else:
                    return JsonResponse({'message': default_data, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""homepage_vulnerability_distributiont_data
{
	"token": "XXXX",
	"start_time": "1594087497",
	"end_time": "1604087497"
}
"""
def HomepageVulnerabilityDistributiontData(request):#用户登录成功后跳转的首页，漏洞分布数据
    RequestLogRecord(request, request_api="homepage_vulnerability_distributiont_data")
    if request.method == "POST":
        try:
            start_time = json.loads(request.body)["start_time"]
            end_time=json.loads(request.body)["end_time"]
            token = json.loads(request.body)["token"]
            if start_time==None or end_time==None:
                return JsonResponse({'message': '小宝贝时间呢？', 'code': 503, })
            else:
                uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
                if uid != None:  # 查到了UID
                    UserOperationLogRecord(request, request_api="homepage_vulnerability_distributiont_data", uid=uid)
                    vulnerability_distribution=HomeInfo().VulnerabilityDistribution(uid=uid, start_time=start_time,end_time=end_time)
                    if vulnerability_distribution==None:
                        return JsonResponse({'message': "想啥呢？不知道查询出问题了吗？", 'code': 404, })
                    else:
                        return JsonResponse({'message': vulnerability_distribution, 'code': 200, })
                else:
                    return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""homepage_github_monitor_data
{
	"token": "XXXX",
	"start_time": "1594087497",
	"end_time": "1604087497"
}
"""
def HomepageGithubMonitorData(request):#用户登录成功后跳转的首页，Github监控数据
    RequestLogRecord(request, request_api="homepage_github_monitor_data")
    if request.method == "POST":
        try:
            start_time = json.loads(request.body)["start_time"]
            end_time=json.loads(request.body)["end_time"]
            token = json.loads(request.body)["token"]
            if start_time==None or end_time == None:
                return JsonResponse({'message': '小宝贝时间呢？', 'code': 503, })
            else:
                uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
                if uid != None:  # 查到了UID
                    UserOperationLogRecord(request, request_api="homepage_github_monitor_data", uid=uid)
                    github_monitor=HomeInfo().GithubMonitor(uid=uid, start_time=start_time,end_time=end_time)
                    if github_monitor==None:
                        return JsonResponse({'message': "想啥呢？不知道查询出问题了吗？", 'code': 404, })
                    else:
                        return JsonResponse({'message': github_monitor, 'code': 200, })
                else:
                    return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })