#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from Web.DatabaseHub import NistData
from ClassCongregation import ErrorLog
from Web.DatabaseHub import UserInfo
from django.http import JsonResponse
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import ast

"""nist_data_bulk_query
{
	"token": "xxx",
	"number_of_pages":"20"
}
"""
def NistDataBulkQuery(request):#查询Nist的基础数据监控数据
    RequestLogRecord(request, request_api="nist_data_bulk_query")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            NumberOfPages = json.loads(request.body)["number_of_pages"]#页数
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="nist_data_bulk_query", uid=Uid)  # 查询到了在计入
                if int(NumberOfPages)<0:
                    return JsonResponse({'message': "你家有小于0的页码？", 'code': 503, })
                else:
                    SearchResult=NistData().BulkQuery(number_of_pages=int(NumberOfPages))#获取数据
                    return JsonResponse({'message': SearchResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CVE_NistMonitoring_Nist_NistDataBulkQuery(def)", e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""nist_data_detailed_query
{
	"token": "xxx",
	"common_vulnerabilities_and_exposures":"CVE-2021-3177"
}
"""
def NistDataDetailedQuery(request):#查询单个CVE细节数据
    RequestLogRecord(request, request_api="nist_data_detailed_query")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            CommonVulnerabilitiesAndExposures = json.loads(request.body)["common_vulnerabilities_and_exposures"]#CVE编号
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="nist_data_detailed_query", uid=Uid)  # 查询到了在计入
                SearchResult=NistData().DetailedQuery(common_vulnerabilities_and_exposures=CommonVulnerabilitiesAndExposures)#获取数据
                return JsonResponse({'message':ast.literal_eval(SearchResult), 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CVE_NistMonitoring_Nist_NistDataDetailedQuery(def)", e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""nist_statistics
{
	"token": "xxx"
}
"""
def NistStatistics(request):#对当前的CVE个数进行统计
    RequestLogRecord(request, request_api="nist_statistics")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="nist_statistics", uid=Uid)  # 查询到了在计入
                SearchResult=NistData().StatisticalData()#统计的个数
                return JsonResponse({'message': SearchResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CVE_NistMonitoring_Nist_NistStatistics(def)", e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""nist_search_statistics
{
	"token": "xxx",
	"severity":"xxxx",
	"key":"xxxx"
}
"""
def NistSearchStatistics(request):#模糊搜索数据统计
    RequestLogRecord(request, request_api="nist_search_statistics")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Severity = json.loads(request.body)["severity"]  # 严重性等级
            Key = json.loads(request.body)["key"]  # 查询关键字
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="nist_search_statistics", uid=Uid)  # 查询到了在计入
                if Key=="":
                    return JsonResponse({'message': "咋了？查询不知道传数据吗？", 'code': 505, })
                else:
                    Total = NistData().SearchStatistics(key=Key,severity=Severity)  # 查询漏洞总数
                    return JsonResponse({'message': Total, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CVE_NistMonitoring_Nist_NistSearchStatistics(def)", e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""nist_search
{
	"token": "xxx",
	"number_of_pages":"0",
	"severity":"xxxx",
	"key":"xxxx"
}
"""
def NistSearch(request):#模糊搜索
    RequestLogRecord(request, request_api="nist_search")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            NumberOfPages = json.loads(request.body)["number_of_pages"]  # 页数
            Severity = json.loads(request.body)["severity"]  # 严重性等级
            Key = json.loads(request.body)["key"]  # 查询关键字
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="nist_search", uid=Uid)  # 查询到了在计入
                if int(NumberOfPages)<1:
                    return JsonResponse({'message': "你家有小于1的页码？", 'code': 503, })
                elif Key=="":
                    return JsonResponse({'message': "咋了？查询不知道传数据吗？", 'code': 505, })
                else:
                    Data= NistData().Search(number_of_pages=int(NumberOfPages),key=Key,severity=Severity)  # 对查询分页数据

                    return JsonResponse({'message': Data, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CVE_NistMonitoring_Nist_NistSearch(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
