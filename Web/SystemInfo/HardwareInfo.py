from Web.WebClassCongregation import UserInfo,HardwareUsageRateInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import psutil  # 进程运行情况
import platform  # 包含系统信息查询函数


def Monitor():#用于监控系统信息
    try:
        MemoryInfo = psutil.virtual_memory()  # 获取完整内存信息
        MemoryUsed = MemoryInfo.used  # 内存已使用
        MemoryFree = MemoryInfo.free  # 内存空闲大小
        MemoryPercent = MemoryInfo.percent  # 内存使用率
        CentralProcessingUnitUsageRate=psutil.cpu_percent(1)#CUP总使用率
        PerCoreCentralProcessingUnitUsageRate= psutil.cpu_percent(percpu=True)#每个CUP使用率
        HardwareUsageRateInfo().Write(memory_free=MemoryFree,
                                      memory_percent=MemoryPercent,
                                      memory_used=MemoryUsed,
                                      central_processing_unit_usage_rate=CentralProcessingUnitUsageRate,
                                      per_core_central_processing_unit_usage_rate=str(PerCoreCentralProcessingUnitUsageRate))#数据写到数据库中

    except Exception as e:
        ErrorLog().Write("Web_SystemInfo_HardwareInfo_Monitor(def)", e)


"""system_hardware_initialization
{
	"token": "",
}
"""
def Initialization(request):#用于初始化获取基础信息
    RequestLogRecord(request, request_api="system_hardware_initialization")
    if request.method == "POST":
        try:
            Token = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="system_hardware_initialization", uid=Uid)  # 查询到了在计入
                MemoryInfo = psutil.virtual_memory()  # 获取完整内存信息
                SystemInfo=platform.platform()
                SystemName=platform.system()
                SystemType=platform.machine()
                UserName= platform.node()
                CentralProcessingUnitArchitecture=platform.processor()
                ServerStartTime = str(int(psutil.boot_time()))  # 获取服务器启动时间
                MemoryTotal = MemoryInfo.total  # 系统内存总数
                CentralProcessingUnitCount = psutil.cpu_count()  # cpu核数
                return JsonResponse({'message': {"central_processing_unit_architecture":CentralProcessingUnitArchitecture,
                                                "system_info":SystemInfo,
                                                 "server_start_time":ServerStartTime,
                                                 "system_name":SystemName,
                                                 "system_type":SystemType,
                                                 "user_name":UserName,
                                                 "memory_total":MemoryTotal,
                                                 "central_processing_unit_count":CentralProcessingUnitCount},'code': 200,})
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_SystemInfo_HardwareInfo_Initialization(def)", e)
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
            Token = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="system_hardware_usage_query", uid=Uid)  # 查询到了在计入
                HardwareUsageRateResult=HardwareUsageRateInfo().Query()#对CPU和内存信息进行查询
                return JsonResponse({'message': HardwareUsageRateResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_SystemInfo_HardwareInfo_Initialization(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

