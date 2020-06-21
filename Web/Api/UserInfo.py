from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""user_info
{
	"token": ""
}
"""
def PersonalInformation(request):#用户个人信息
    RequestLogRecord(request, request_api="personal_information")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Info=UserInfo().QueryUserInfo(Token)
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询用户名
            if Uid!=None: # 查到了UID
                UserOperationLogRecord(request, request_api="personal_information", uid=Uid)
            if Info is None:
                return JsonResponse({'message': '搁着闹呢？', 'code': 404, })
            elif Info != None:
                JsonValues = {}#对数据进行二次处理
                JsonValues["id"] = Info["id"]
                JsonValues["key"] = Info["key"]
                JsonValues["name"] = Info["name"]
                JsonValues["token"] = Info["token"]
                JsonValues["show_name"] = Info["show_name"]
                JsonValues["email"] = Info["email"]
                JsonValues["img_path"] = Info["img_path"]
                return JsonResponse({'message': JsonValues, 'code': 200, })


        except Exception as e:
            ErrorLog().Write("Web_Api_UserInfo_PersonalInformation(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
