from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms
import json
# UserInfo().Write(name="name",show_name="show_name",token="2222222222222222222222",passwd="passwd",email="img_path",img_path="img_path")
# UserInfo().UpdateEmail(name="name",email="imsafasfasfasfth")
# UserInfo().UpdateKey(name="name",key="1111111111")
# UserInfo().UpdateImgPath(name="name",img_path="222222222222")
# UserInfo().UpdateShowName(name="name",show_name="333333333333")
# UserInfo().UpdatePasswd(name="name",passwd="4444444444444444444")
# UserInfo().UpdateToken(name="name",token="token")
# UserInfo().QueryTokenCreationTime(name="name",token="token")
"""login
{
	"username": "ascotbe",
	"passwd": "1"
}
"""
def Login(request):#用户登录，每次登录成功都会刷新一次Token
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
                    return JsonResponse({'message': Token, 'code': 200, })
        except Exception as e:
            ErrorLog().Write("Web_Api_User_LogIn(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

##更新密码，邮箱等功能后面再加，先能用就行