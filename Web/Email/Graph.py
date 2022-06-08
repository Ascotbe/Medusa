#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse,JsonResponse
from ClassCongregation import ErrorLog
import json
import time
import base64
from Web.DatabaseHub import EmailReceiveData,UserInfo,EmailProject,EmailDetails
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import re
"""email_data_graph
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa"
}
"""
def Statistics(request):#数据表格制作
    RequestLogRecord(request, request_api="email_data_graph")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            ProjectKey = json.loads(request.body)["project_key"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_data_graph", uid=Uid)  # 查询到了在计入
                Result=EmailReceiveData().Statistics(project_key=ProjectKey)
                return JsonResponse({'message': Result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Email_ReceiveData_Statistics(def)", e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
