#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse,JsonResponse
from ClassCongregation import ErrorLog
import json
import time
import base64
from Web.DatabaseHub import EmailReceiveData,UserInfo,EmailProject
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import re
"""
http://127.0.0.1:9999/b/eNVqsIHXAV/key=9146ae77f2dcf1ba
"""
def Monitor(request,data):#用于接收信息的监控
    RequestLogRecord(request, request_api="email")
    GetRequestFragment=""#项目ID
    try:
        GetRequestFragment = re.search(r'/[a-zA-Z0-9]{10}', str(request.get_full_path), re.I).group(0)[1:11]
        #print(GetRequestFragment[1:11])
    except Exception as e:
        ErrorLog().Write("Web_Mail_FishingData_Monitor(def)-GetRequestFragment", e)
    EndTime=EmailProject().MonitorQuery(project_key=GetRequestFragment)#查询项目接受数据时间
    if EndTime!=None and int(EndTime)>int(time.time()):#判断项目是否结束
        if request.method == "POST":
            try:
                Key=""
                if request.headers["Content-Type"]=="application/json":
                    DataPackInfo = request.body#获取post数据包信息
                    Key = json.loads(DataPackInfo).get("key")  # 获取md5_middle值
                else:
                    DataPackInfo = str(request.POST.dict()).encode('utf-8')#转换成字典后再换装byte类型穿给加密函数
                    Key = request.POST.dict().get("key")  # 获取md5值
                #HeadersInfo = str(request.headers).encode('utf-8')#获取头信息
                if len(Key) == 32:
                    EmailReceiveData().Write(full_url=str(request.build_absolute_uri()),
                                    request_method="POST",project_key=GetRequestFragment,target=Key,data_pack_info=base64.b64encode(DataPackInfo).decode('utf-8'))
            except Exception as e:
                ErrorLog().Write("Web_Mail_FishingData_Monitor(def)-POST", e)
        elif request.method == "GET":
            try:

                ParameterInfo=str(request.GET.dict()).encode('utf-8')#获取参数信息
               # HeadersInfo=str(request.headers).encode('utf-8')#获取头信息
                Key =request.GET.dict().get("key")#获取md5值
                if len(Key)==32:
                    EmailReceiveData().Write(full_url=str(request.build_absolute_uri()),
                                    request_method="GET",project_key=GetRequestFragment,target=Key,data_pack_info=base64.b64encode(ParameterInfo).decode('utf-8'))

            except Exception as e:
                ErrorLog().Write("Web_Mail_FishingData_Monitor(def)-GET", e)

    return HttpResponse("")


"""mail_receive_data_statistics
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa"
}
"""
def DataStatistics(request):#统计邮件获取到的数据
    RequestLogRecord(request, request_api="mail_receive_data_statistics")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            ProjectKey = json.loads(request.body)["project_key"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="mail_receive_data_statistics", uid=Uid)  # 查询到了在计入
                Result=EmailReceiveData().Quantity(project_key=ProjectKey)
                return JsonResponse({'message': Result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_MailReceiveData_DataStatistics(def)", e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""mail_receive_data_details
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa",
	"number_of_pages":"1"
}
"""
def DataDetails(request):#邮件获取的数据详情
    RequestLogRecord(request, request_api="mail_receive_data_details")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            ProjectKey = json.loads(request.body)["project_key"]
            NumberOfPages=json.loads(request.body)["number_of_pages"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="mail_receive_data_details", uid=Uid)  # 查询到了在计入
                if int(NumberOfPages)>0:
                    Result=EmailReceiveData().Query(project_key=ProjectKey,number_of_pages=int(NumberOfPages))
                    return JsonResponse({'message': Result, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_MailReceiveData_DataDetails(def)", e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
