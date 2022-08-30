#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,HardwareUsageRateInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import psutil  # 进程运行情况
import platform  # 包含系统信息查询函数
from celery import shared_task

@shared_task
def Monitor():#用于监控系统信息
    try:
        memory_info = psutil.virtual_memory()  # 获取完整内存信息
        # 内存使用率 =  (物理内存大小 - 可用内存大小) / 物理内存大小 * 100
        memory_used = memory_info.total - memory_info.available  # 内存已使用
        memory_free = memory_info.available  # 内存空闲大小
        memory_percent = memory_info.percent  # 内存使用率
        central_processing_unit_usage_rate=psutil.cpu_percent(1)#CUP总使用率
        per_core_central_processing_unit_usage_rate= psutil.cpu_percent(percpu=True)#每个CUP使用率
        HardwareUsageRateInfo().Write(memory_free=memory_free,
                                      memory_percent=memory_percent,
                                      memory_used=memory_used,
                                      central_processing_unit_usage_rate=central_processing_unit_usage_rate,
                                      per_core_central_processing_unit_usage_rate=str(per_core_central_processing_unit_usage_rate))#数据写到数据库中

    except Exception as e:
        ErrorLog().Write(e)



"""system_hardware_initialization
{
	"token": "",
}
"""
def Initialization(request):#用于初始化获取基础信息
    RequestLogRecord(request, request_api="system_hardware_initialization")
    if request.method == "POST":
        try:
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="system_hardware_initialization", uid=uid)  # 查询到了在计入
                memory_info = psutil.virtual_memory()  # 获取完整内存信息
                system_info=platform.platform()
                system_name=platform.system()
                system_type=platform.machine()
                user_name= platform.node()
                central_processing_unit_architecture=platform.processor()
                server_start_time = str(int(psutil.boot_time()))  # 获取服务器启动时间
                memory_total = memory_info.total  # 系统内存总数
                central_processing_unit_count = psutil.cpu_count()  # cpu核数
                return JsonResponse({'message': {"central_processing_unit_architecture":central_processing_unit_architecture,
                                                "system_info":system_info,
                                                 "server_start_time":server_start_time,
                                                 "system_name":system_name,
                                                 "system_type":system_type,
                                                 "user_name":user_name,
                                                 "memory_total":memory_total,
                                                 "central_processing_unit_count":central_processing_unit_count},'code': 200,})
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""system_hardware_usage_query
{
	"token": "",
}
"""

def UsageQuery(request):  # 用于查询CPU和硬件的使用情况
    RequestLogRecord(request, request_api="system_hardware_usage_query")
    if request.method == "POST":
        try:
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="system_hardware_usage_query", uid=uid)  # 查询到了在计入
                result=HardwareUsageRateInfo().Query()#对CPU和内存信息进行查询
                return JsonResponse({'message': result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

