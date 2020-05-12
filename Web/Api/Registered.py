from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from django.http import HttpResponse
import json
UserInfo().Write(name="name",show_name="show_name",token="2222222222222222222222",passwd="passwd",email="img_path",img_path="img_path")
UserInfo().UpdateEmail(name="name",email="imsafasfasfasfth")
UserInfo().UpdateKey(name="name",key="1111111111")
UserInfo().UpdateImgPath(name="name",img_path="222222222222")
UserInfo().UpdateShowName(name="name",show_name="333333333333")
UserInfo().UpdatePasswd(name="name",passwd="4444444444444444444")
UserInfo().UpdateToken(name="name",token="token")
UserInfo().QueryTokenCreationTime(name="name",token="token")
def Registered(request):
    if request.method == "POST":
        try:
            UserToken=json.loads(request.body)["token"]
            result=VulnerabilityInquire().Inquire(UserToken)
            if len(result)>0:
                return HttpResponse(result)
            else:
                return JsonResponse({'message': '没找到数据', 'code': 200, })
    else:
        return JsonResponse({'message': '请使用Get请求', 'code': 500, })
