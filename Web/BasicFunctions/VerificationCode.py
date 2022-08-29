#!/usr/bin/env python
# -*- coding: utf-8 -*-
from captcha.image import ImageCaptcha
from Web.DatabaseHub import VerificationCode
from django.http import JsonResponse,HttpResponse
from ClassCongregation import ErrorLog,randoms
from Web.Workbench.LogRelated import RequestLogRecord


def GenerateVerificationCode(request):#生成验证码函数
    RequestLogRecord(request, request_api="get_verification_code")
    if request.method == "GET":
        try:
            random_verification_code = randoms().LowercaseAndNumbers(6)#获取小写的字符串
            random_verification_code_key=randoms().result(250)#生成验证码相关联的key
            picture_bitstream = ImageCaptcha().generate(random_verification_code).read()#获取图片比特流
            VerificationCode().Write(code=random_verification_code,verification_code_key=random_verification_code_key)#把值写入到数据库中
            result=HttpResponse(picture_bitstream)#把图片比特流复制给返回包
            result['VerificationCodeKey'] = random_verification_code_key#把值传到返回包的头中
            result['Access-Control-Expose-Headers']="VerificationCodeKey"#添加头内容保证前端能够获取到值
            return result
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用GET请求', 'code': 500, })

