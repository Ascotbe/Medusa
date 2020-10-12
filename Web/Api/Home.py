from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""homepage_data
{
	"token": "XXXX"
}
"""
def HomepageData(request):#用户登录成功后跳转的首页
    RequestLogRecord(request, request_api="homepage_data")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="home", uid=Uid)
            #暂时没用首页数据，当前只是用作首页跳转
                return JsonResponse({'message': '成功了宝贝🐈', 'code': 200, })
        except Exception as e:
            ErrorLog().Write("Web_Api_Home_HomepageData(def)", e)
            return JsonResponse({'message': '莎酱被玩坏啦(>^ω^<)喵', 'code': 500, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
