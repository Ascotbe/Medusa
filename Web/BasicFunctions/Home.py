from Web.WebClassCongregation import UserInfo,HomeInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""homepage_default_data
{
	"token": "XXXX"
}
"""
def HomepageDefaultData(request):#用户登录成功后跳转的首页，默认数据
    RequestLogRecord(request, request_api="homepage_default_data")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="homepage_default_data", uid=Uid)
                DefaultData=HomeInfo().DefaultData(uid=Uid)
                if DefaultData==None:
                    return JsonResponse({'message': "想啥呢？不知道查询出问题了吗？", 'code': 404, })
                else:
                    return JsonResponse({'message': DefaultData, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Api_Home_HomepageDefaultData(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""homepage_vulnerability_distributiont_data
{
	"token": "XXXX",
	"start_time": "1594087497",
	"end_time": "1604087497"
}
"""
def HomepageVulnerabilityDistributiontData(request):#用户登录成功后跳转的首页，漏洞分布数据
    RequestLogRecord(request, request_api="homepage_vulnerability_distributiont_data")
    if request.method == "POST":
        try:
            StartTime = json.loads(request.body)["start_time"]
            EndTime=json.loads(request.body)["end_time"]
            UserToken = json.loads(request.body)["token"]
            if StartTime==None or EndTime==None:
                return JsonResponse({'message': '小宝贝时间呢？', 'code': 503, })
            else:
                Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
                if Uid != None:  # 查到了UID
                    UserOperationLogRecord(request, request_api="homepage_vulnerability_distributiont_data", uid=Uid)
                    VulnerabilityDistribution=HomeInfo().VulnerabilityDistribution(uid=Uid, start_time=StartTime,end_time=EndTime)
                    if VulnerabilityDistribution==None:
                        return JsonResponse({'message': "想啥呢？不知道查询出问题了吗？", 'code': 404, })
                    else:
                        return JsonResponse({'message': VulnerabilityDistribution, 'code': 200, })
                else:
                    return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Api_Home_HomepageData(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""homepage_github_monitor_data
{
	"token": "XXXX",
	"start_time": "1594087497",
	"end_time": "1604087497"
}
"""
def HomepageGithubMonitorData(request):#用户登录成功后跳转的首页，Github监控数据
    RequestLogRecord(request, request_api="homepage_github_monitor_data")
    if request.method == "POST":
        try:
            StartTime = json.loads(request.body)["start_time"]
            EndTime=json.loads(request.body)["end_time"]
            UserToken = json.loads(request.body)["token"]
            if StartTime==None or EndTime==None:
                return JsonResponse({'message': '小宝贝时间呢？', 'code': 503, })
            else:
                Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
                if Uid != None:  # 查到了UID
                    UserOperationLogRecord(request, request_api="homepage_github_monitor_data", uid=Uid)
                    GithubMonitor=HomeInfo().GithubMonitor(uid=Uid, start_time=StartTime,end_time=EndTime)
                    if GithubMonitor==None:
                        return JsonResponse({'message': "想啥呢？不知道查询出问题了吗？", 'code': 404, })
                    else:
                        return JsonResponse({'message': GithubMonitor, 'code': 200, })
                else:
                    return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Api_Home_HomepageData(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })