#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from django.http import HttpResponse
from django.http import JsonResponse
from .tasks import *#导入异步处理中声明过的函数
import threading


def api(request):
    return JsonResponse({"result": 0, "msg": "执行成功"})

def get(request):
    id = request.GET.get("id")
    pid = request.GET.get("pid")
    return HttpResponse("获得数据 %s %s"%(id,pid))


def global_scan(request):
    if request.POST.get("task")=="1":#用户ID保留模块
        if request.POST.get("mod") == "medusa":
            post_url_value=request.POST.get("url")
            mian.delay(post_url_value)
    return JsonResponse({"result": 0, "msg": "%s"})


def independent_scan(request):
    user_token=request.POST.get("task")
    independent_mod_name=request.POST.get("value")
    independent_url=request.POST.get("url")
    independent.delay(independent_url,independent_mod_name)
    return JsonResponse({"result": 0, "msg": "执行成功"})

def result_query(request):
    user_token=request.POST.get("task")
    pid=request.POST.get("id")#SQL中唯一的id值
    info=result.delay(user_token,pid)
    return JsonResponse(info)#用JS返回值具体的等查询语句改好写