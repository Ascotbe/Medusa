from Web.WebClassCongregation import UserInfo
from ClassCongregation import ErrorLog,randoms
from django.http import JsonResponse
import json
# UserInfo().Write(name="name",show_name="show_name",token="2222222222222222222222",passwd="passwd",email="img_path",img_path="img_path")
# UserInfo().UpdateEmail(name="name",email="imsafasfasfasfth")
# UserInfo().UpdateKey(name="name",key="1111111111")
# UserInfo().UpdateImgPath(name="name",img_path="222222222222")
# UserInfo().UpdateShowName(name="name",show_name="333333333333")
# UserInfo().UpdatePasswd(name="name",passwd="4444444444444444444")
# UserInfo().UpdateToken(name="name",token="token")
# UserInfo().QueryTokenCreationTime(name="name",token="token")

"""
{
	"show_name": "7777777",
	"username": "ascotbe",
	"passwd": "1",
	"email": "1@qq.com"
}
"""
def Registered(request):
    if request.method == "POST":
        try:
            ShowName = json.loads(request.body).get("show_name")
            Username=json.loads(request.body).get("username")
            Passwd=json.loads(request.body).get("passwd")
            Email=json.loads(request.body).get("email")
            if len(ShowName.strip(" \r\n"))==0 or len(Username.strip(" \r\n"))==0 or len(Passwd.strip(" \r\n"))==0 or len(Email.strip(" \r\n"))==0:#验证数据不为空
                return JsonResponse({'message': '宝贝数据呢？', 'code': 666, })
            else:
                VerifyUsername=UserInfo().VerifyUsername(Username)
                VerifyEmail=UserInfo().VerifyEmail(Email)
                if VerifyUsername or VerifyEmail:
                    return JsonResponse({'message': '用户名或邮箱已存在', 'code': 604, })

                elif (VerifyUsername is None)or(VerifyEmail is None):

                    return JsonResponse({'message': '报错了', 'code': 404, })
                elif not VerifyUsername or not VerifyEmail:
                    Token=randoms().result(250)
                    UserWrite=UserInfo().Write(name=Username, show_name=ShowName, token=Token, passwd=Passwd,
                                     email=Email, img_path="img_path")
                    if UserWrite:
                        return JsonResponse({'message': '注册成功', 'code': 200, })
                    elif UserWrite is None:
                        return JsonResponse({'message': '未知错误', 'code': 400, })
                    else:
                        return JsonResponse({'message': '注册失败', 'code': 603, })
        except Exception as e:
            ErrorLog().Write("Web_Api_Registered_Registered(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
