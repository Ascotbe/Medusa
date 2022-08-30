#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import RequestLog,UserOperationLog
import base64
from config import request_log_record
def GetIp(request):
    '''获取请求者的IP信息'''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP
    return ip

def UserOperationLogRecord(request,**kwargs):#用户操作写入SDK
    if request_log_record:#如果为真就写入日志，反之不写入
        request_api = kwargs.get("request_api")
        uid = kwargs.get("uid")
        headers=base64.b64encode(str(request.headers).encode(encoding="utf-8"))
        post_date=base64.b64encode(str(request.body).encode(encoding="utf-8"))
        UserOperationLog().Write(uid=uid,request_ip=GetIp(request),request_url=request.get_full_path(),request_api=request_api,header=headers,request_method=request.method,post_date=post_date)
    else:
        pass
def RequestLogRecord(request,**kwargs):#操作写入SDK
    if request_log_record:#如果为真就写入日志，反之不写入
        request_api = kwargs.get("request_api")
        header=base64.b64encode(str(request.headers).encode(encoding="utf-8"))
        post_date=base64.b64encode(str(request.body).encode(encoding="utf-8"))
        RequestLog().Write(request_ip=GetIp(request),request_url=request.get_full_path(),request_api=request_api,header=header,request_method=request.method,post_date=post_date)
    else:
        pass