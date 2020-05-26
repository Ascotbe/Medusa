from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""login
{
	"username": "ascotbe",
	"passwd": "1"
}
"""
def Login(request):#用户登录，每次登录成功都会刷新一次Token
    RequestLogRecord(request, request_api="login")
    if request.method == "POST":
        try:
            Username=json.loads(request.body)["username"]
            Passwd=json.loads(request.body)["passwd"]
            UserLogin=UserInfo().UserLogin(Username,Passwd)
            if UserLogin is None:
                return JsonResponse({'message': '账号或密码错误', 'code': 604, })

            else:
                while True:#如果查询确实冲突了
                    Token = randoms().result(250)
                    QueryTokenValidity = UserInfo().QueryTokenValidity(Token)#用来查询Token是否冲突了
                    if not QueryTokenValidity:#如果不冲突的话跳出循环
                        break
                UpdateToken=UserInfo().UpdateToken(name=Username, token=Token)#接着更新Token
                if UpdateToken:#如果更新成功了
                    UserName = UserInfo().QueryUserNameWithToken(Token)  # 查询UID
                    UserOperationLogRecord(request, request_api="login", uid=UserName)
                    return JsonResponse({'message': Token, 'code': 200, })
        except Exception as e:
            ErrorLog().Write("Web_Api_User_LogIn(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

##更新密码，邮箱等功能后面再加，先能用就行