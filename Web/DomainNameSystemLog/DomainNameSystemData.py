from Web.WebClassCongregation import UserInfo,DomainNameSystemLog
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""domain_name_system_log
{
	"token": "",
	"number_of_pages":""
}
"""

def Query(request):  # 用于查询DNSLOG数据
    RequestLogRecord(request, request_api="domain_name_system_log")
    if request.method == "POST":
        try:
            Token = json.loads(request.body)["token"]
            NumberOfPages = json.loads(request.body)["number_of_pages"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="domain_name_system_log", uid=Uid)  # 查询到了在计入
                DomainNameSystemLogResult=DomainNameSystemLog().Query(number_of_pages=int(NumberOfPages))#对解析记录进行查询
                return JsonResponse({'message': DomainNameSystemLogResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_DomainNameSystemLog_DomainNameSystemData_Query(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""domain_name_system_log_statistics
{
	"token": "xxx"
}
"""
def Statistics(request):#对当前整体数据进行统计
    RequestLogRecord(request, request_api="domain_name_system_log_statistics")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="domain_name_system_log_statistics", uid=Uid)  # 查询到了在计入
                SearchResult=DomainNameSystemLog().StatisticalData()#统计的个数
                return JsonResponse({'message': SearchResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_DomainNameSystemLog_DomainNameSystemData_Statistics(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
