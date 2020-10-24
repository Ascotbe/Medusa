from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,GithubCveApi
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""github_monitor
{
	"token": "xxx"
}
"""
def GithubMonitor(request):#查询github监控数据
    RequestLogRecord(request, request_api="github_monitor")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="github_monitor", uid=Uid)  # 查询到了在计入
                GithubMonitorResult=GithubCveApi().Query()#获取github数据
                return JsonResponse({'message': GithubMonitorResult, 'code': 200, })
            else:
                return JsonResponse({'message': "非法查询哦宝贝！", 'code': 404, })
        except Exception as e:
            ErrorLog().Write("Web_Api_User_UpdateShowName(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
