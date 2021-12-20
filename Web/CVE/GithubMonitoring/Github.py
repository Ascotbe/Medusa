# !/usr/bin/python env
# -*- coding:utf-8 -*-
import ClassCongregation
import requests
from Web.DatabaseHub import UserInfo,GithubCve
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from celery import shared_task
from config import github_cve_monitor_key
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""github_monitor_search
{
	"token": "xxx",
	"name":"xx",
	"github_id":"",
	"html_url":"",
	"number_of_pages": "xxx"
}
"""
def GithubQuery(request):#查询github监控数据
    RequestLogRecord(request, request_api="github_monitor_search")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            NumberOfPages = json.loads(request.body)["number_of_pages"]  # 页数
            Name = json.loads(request.body)["name"]  # 页数
            GithubId = json.loads(request.body)["github_id"]  # 页数
            HtmlUrl = json.loads(request.body)["html_url"]  # 页数
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="github_monitor_search", uid=Uid)  # 查询到了在计入
                QueryData={}
                QueryData["number_of_pages"] = int(NumberOfPages)
                if Name!="":
                    QueryData["name"]=Name
                if GithubId != "":
                    QueryData["github_id"] = GithubId
                if HtmlUrl!="":
                    QueryData["html_url"]=HtmlUrl
                Data = {}  # 最终包含个数和当前页数数据
                Data["amount"] =GithubCve().StatisticalData(**QueryData)  # 获取统计个数
                Data["data"] = GithubCve().Query(**QueryData)  # 获取github数据
                return JsonResponse({'message': Data, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CVE_VulnerabilityUtilizationMonitoring_Github_GithubQuery(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

@shared_task
def Monitor():
    try:
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        }
        GitCveApi=requests.get("https://api.github.com/search/repositories?q="+github_cve_monitor_key+"&sort=updated&order=desc",headers=headers, timeout=10)
        GitCveApiJson=json.loads(GitCveApi.text)
        DataExtraction=GitCveApiJson["items"]
        for i in DataExtraction:
            GithubId=i["id"]
            Name=i["name"]
            HtmlUrl=i["html_url"]
            Created=i["created_at"]
            Updated=i["updated_at"]
            Pushed=i["pushed_at"]
            ForksCount=i["forks_count"]
            WatchersCount=i["watchers_count"]
            GithubCveSekect=GithubCve(id=GithubId,name=Name,html_url=HtmlUrl,created_at=Created,updated_at=Updated,pushed_at=Pushed,forks_count=ForksCount,watchers_count=WatchersCount).Judgment()#先查询数据库
            if GithubCveSekect:
                GithubCve(id=GithubId,name=Name,html_url=HtmlUrl,created_at=Created,updated_at=Updated,pushed_at=Pushed,forks_count=ForksCount,watchers_count=WatchersCount).Update()#如果存在就更新
            else:
                GithubCve(id=GithubId,name=Name,html_url=HtmlUrl,created_at=Created,updated_at=Updated,pushed_at=Pushed,forks_count=ForksCount,watchers_count=WatchersCount).Write()#如果不存在就写入


    except Exception as e:
        ClassCongregation.ErrorLog().Write("Web_CVE_GithubMonitoring_Github_Monitor(def)", e)

