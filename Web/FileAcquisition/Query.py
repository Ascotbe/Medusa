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
            NumberOfPages=json.loads(request.body)["number_of_pages"]
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="file_acquisition_pack_query", uid=Uid)  # 查询到了在计入
                if int(NumberOfPages)>0:
                    Result=FileAcquisitionPack().Query(uid=Uid,number_of_pages=int(NumberOfPages))
                    return JsonResponse({'message': Result, 'code': 200, })
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
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="file_acquisition_pack_attachment", uid=Uid)  # 查询到了在计入
                Result=FileAcquisitionPack().Quantity(uid=Uid)
                return JsonResponse({'message': Result, 'code': 200, })
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
            NumberOfPages=json.loads(request.body)["number_of_pages"]
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="file_acquisition_query", uid=Uid)  # 查询到了在计入
                if int(NumberOfPages)>0:
                    Result=FileAcquisitionData().Query(uid=Uid,number_of_pages=int(NumberOfPages))
                    return JsonResponse({'message': Result, 'code': 200, })
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
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="file_acquisition_attachment", uid=Uid)  # 查询到了在计入
                Result=FileAcquisitionData().Quantity(uid=Uid)
                return JsonResponse({'message': Result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })