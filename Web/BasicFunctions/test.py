from captcha.image import ImageCaptcha
from Web.WebClassCongregation import UserInfo,HomeInfo
from django.http import JsonResponse,HttpResponse
from ClassCongregation import ErrorLog
import json


def test(request):#用户登录成功后跳转的首页，默认数据

    if request.method == "POST":
        try:
            chars = 'dasdsd'

            image = ImageCaptcha().generate(chars)
            a=HttpResponse(image.read())
            a['123dd'] = 'sss'
            return a
        except Exception as e:
            ErrorLog().Write("Web_Api_Home_HomepageDefaultData(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

