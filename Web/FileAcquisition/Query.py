#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,FileAcquisitionData,FileAcquisitionPack
from django.http import JsonResponse
from ClassCongregation import ErrorLog
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import json


"""file_acquisition_pack_query
{
	"token": "xxx",
	"number_of_pages":"1"
}
"""
def PockQuery(request):
    RequestLogRecord(request, request_api="file_acquisition_pack_query")
    if request.method == "POST":
        try:
            number_of_pages=json.loads(request.body)["number_of_pages"]
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="file_acquisition_pack_query", uid=uid)  # 查询到了在计入
                if int(number_of_pages)>0:
                    result=FileAcquisitionPack().Query(uid=uid,number_of_pages=int(number_of_pages))
                    return JsonResponse({'message': result, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""file_acquisition_pack_attachment
{
	"token": "xxx"
}
"""
def PackAttachment(request):#统计打包文件个数
    RequestLogRecord(request, request_api="file_acquisition_pack_attachment")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="file_acquisition_pack_attachment", uid=uid)  # 查询到了在计入
                result=FileAcquisitionPack().Quantity(uid=uid)
                return JsonResponse({'message': result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""file_acquisition_query
{
	"token": "xxx",
	"number_of_pages":"1"
}
"""
def Query(request):  #文件接收查询
    RequestLogRecord(request, request_api="file_acquisition_query")
    if request.method == "POST":
        try:
            number_of_pages=json.loads(request.body)["number_of_pages"]
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="file_acquisition_query", uid=uid)  # 查询到了在计入
                if int(number_of_pages)>0:
                    result=FileAcquisitionData().Query(uid=uid,number_of_pages=int(number_of_pages))
                    return JsonResponse({'message': result, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""file_acquisition_attachment
{
	"token": "xxx"
}
"""
def Attachment(request):#接收文件个数
    RequestLogRecord(request, request_api="file_acquisition_attachment")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="file_acquisition_attachment", uid=uid)  # 查询到了在计入
                result=FileAcquisitionData().Quantity(uid=uid)
                return JsonResponse({'message': result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })