#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from django.http import HttpResponse
from django.http import JsonResponse
from .tasks import add,mian#导入异步处理中声明过的函数
import threading


def api(request):
    return JsonResponse({"result": 0, "msg": "执行成功"})

def get(request):
    id = request.GET.get("id")
    pid = request.GET.get("pid")
    return HttpResponse("获得数据 %s %s"%(id,pid))


def global_scan(request):
    if request.POST.get("task")=="1":
        if request.POST.get("mod") == "medusa":
            post_url_value=request.POST.get("url")
            mian.delay(post_url_value)
            # concat = request.POST.get("id")
            # json_post_data=request.body
            # print(concat)
            # print(json_post_data)
    return JsonResponse({"result": 0, "msg": "%s"})#这边会有很长时间的停顿明天再解决

#每个单读的模块写个接口，或者写个处理函数调用单独的模块
def yibu(request):
    add.delay()
    print("111111111111111")
    print("22222222222")
    return HttpResponse('nenew Django Celery worker run !')

