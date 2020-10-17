from Web.WebClassCongregation import UserInfo,HomeInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""homepage_data
{
	"token": "XXXX",
	"start_time": "1594087497",
	"end_time": "1604087497"
}
"""
def HomepageData(request):#用户登录成功后跳转的首页
    RequestLogRecord(request, request_api="homepage_data")
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
                    UserOperationLogRecord(request, request_api="home", uid=Uid)
                    Home=HomeInfo().Result(uid=Uid, start_time=StartTime,end_time=EndTime)
                    print(Home)
                    if Home==None:
                        return JsonResponse({'message': "想啥呢？不知道查询出问题了吗？", 'code': 404, })
                    else:
                        return JsonResponse({'message': Home, 'code': 200, })
        except Exception as e:
            ErrorLog().Write("Web_Api_Home_HomepageData(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
