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
import time
import dateutil.parser
import pytz

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
            token=json.loads(request.body)["token"]
            number_of_pages = json.loads(request.body)["number_of_pages"]  # 页数
            name = json.loads(request.body)["name"]  # 页数
            github_id = json.loads(request.body)["github_id"]  # 页数
            html_url = json.loads(request.body)["html_url"]  # 页数
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="github_monitor_search", uid=uid)  # 查询到了在计入
                QueryData={}
                QueryData["number_of_pages"] = int(number_of_pages)
                if name!="":
                    QueryData["name"]=name
                if github_id != "":
                    QueryData["github_id"] = github_id
                if html_url!="":
                    QueryData["html_url"]=html_url
                data = {}  # 最终包含个数和当前页数数据
                data["amount"] =GithubCve().StatisticalData(**QueryData)  # 获取统计个数
                data["data"] = GithubCve().Query(**QueryData)  # 获取github数据
                return JsonResponse({'message': data, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

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
        github_api=requests.get("https://api.github.com/search/repositories?q="+github_cve_monitor_key+"&sort=updated&order=desc",headers=headers, timeout=10)
        github_api_json=json.loads(github_api.text)
        data_extraction=github_api_json["items"]
        for i in data_extraction:
            github_id=i["id"]
            name=i["name"]
            html_url=i["html_url"]
            created_at=dateutil.parser.parse(i["created_at"]).astimezone(pytz.timezone('Asia/Shanghai'))  # 解析string 并转换为北京时区
            created = str(int(time.mktime(created_at.timetuple())))  # 转换为时间戳
            updated_at=dateutil.parser.parse(i["updated_at"]).astimezone(pytz.timezone('Asia/Shanghai'))  # 解析string 并转换为北京时区
            updated = str(int(time.mktime(updated_at.timetuple())))  # 转换为时间戳
            pushed_at=dateutil.parser.parse(i["pushed_at"]).astimezone(pytz.timezone('Asia/Shanghai'))  # 解析string 并转换为北京时区
            pushed = str(int(time.mktime(pushed_at.timetuple())))  # 转换为时间戳
            forks_count=i["forks_count"]
            watchers_count=i["watchers_count"]
            sekect=GithubCve(id=github_id,name=name,html_url=html_url,created_at=created,updated_at=updated,pushed_at=pushed,forks_count=forks_count,watchers_count=watchers_count).Judgment()#先查询数据库
            if sekect:
                GithubCve(id=github_id,name=name,html_url=html_url,created_at=created,updated_at=updated,pushed_at=pushed,forks_count=forks_count,watchers_count=watchers_count).Update()#如果存在就更新
            else:
                GithubCve(id=github_id,name=name,html_url=html_url,created_at=created,updated_at=updated,pushed_at=pushed,forks_count=forks_count,watchers_count=watchers_count).Write()#如果不存在就写入


    except Exception as e:
        ClassCongregation.ErrorLog().Write(e)
