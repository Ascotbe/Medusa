#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord

"""statistics_user_email
{
	"token": "xxx"
}
"""
def StatisticsUserEmail(request):#统计邮件个数
    RequestLogRecord(request, request_api="statistics_user_email")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="statistics_user_email", uid=Uid)  # 查询到了在计入
                StatisticsMaliciousEmailResult=MaliciousEmail().Quantity(uid=Uid)
                return JsonResponse({'message': StatisticsMaliciousEmailResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_MailHistory_StatisticsUserEmail(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""mail_data_query
{
	"token": "xxx",
	"email_id":"1"
}
"""
def MailDataQuery(request):#查询邮件详情
    RequestLogRecord(request, request_api="mail_data_query")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            EmailId=json.loads(request.body)["email_id"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="mail_data_query", uid=Uid)  # 查询到了在计入
                MailQueryResult=MaliciousEmail().Query(uid=Uid,email_id=EmailId)
                return JsonResponse({'message': MailQueryResult, 'code': 200, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_MailHistory_MailDataQuery(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""mail_summary_query
{
	"token": "xxx",
	"number_of_pages":"1"
}
"""
def MailSummaryQuery(request):#查询邮件摘要详情
    RequestLogRecord(request, request_api="mail_summary_query")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            NumberOfPages=json.loads(request.body)["number_of_pages"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="mail_summary_query", uid=Uid)  # 查询到了在计入
                if int(NumberOfPages)>0:
                    MailQueryResult=MaliciousEmail().SummaryQuery(uid=Uid,number_of_pages=int(NumberOfPages))
                    return JsonResponse({'message': MailQueryResult, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_MailHistory_MailDataQuery(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
