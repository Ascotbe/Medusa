#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,ThreadPool
import json
from Web.celery import app
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord

"""subdomain_search
{
	"token": "",
	"app_name":""
}
"""
def SubdomainSearch(request):  # 子域名搜索函数
    RequestLogRecord(request, request_api="subdomain_search")
    if request.method == "POST":
        try:
            Token = json.loads(request.body)["token"]
            Url=json.loads(request.body)["url"]
            #后续还有其他配置等后面再说
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="subdomain_search", uid=Uid)  # 查询到了在计入

                return JsonResponse({'message': "任务下发成功(๑•̀ㅂ•́)و✧", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法请求哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Subdomain_UnifiedSchedulingOfSubdomains_SubdomainSearch(def)", e)
            return JsonResponse({'message': "出现未知错误，详情看日志文件", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
@app.task
def SubdomainWorkbench(Url):#子域名搜索调用函数
    SubdomainList = []#全局子域名列表
    SubdomainThreadPool =ThreadPool()#定义一个子域名搜索线程池
    SubdomainThreadPool.Append(xxxx,Url=Url,SubdomainList=SubdomainList)#传入全局的子域名列表，这样就能获取到结果了

    SubdomainThreadPool.Start(5)#默认5个，后面使用配置文件
    #redis_id=SubdomainWorkbench.request.id#获取任务值