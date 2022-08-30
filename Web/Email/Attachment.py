#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,MailAttachment
from django.http import JsonResponse,HttpResponse
from ClassCongregation import ErrorLog,randoms,GetPath
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import time
import base64
import json
"""email_file_upload
POST /api/upload_mail_attachment/ HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryaFtQbWz7pBzNgCOv
token:XXXXXXXXXXXXXXXX

------WebKitFormBoundaryaFtQbWz7pBzNgCOv
Content-Disposition: form-data; name="file"; filename="test.jpeg"
Content-Type: image/jpeg

XXXXXXXXXXXXXXX
------WebKitFormBoundaryaFtQbWz7pBzNgCOv--
"""
def UploadFiles (request):#上传文件
    RequestLogRecord(request, request_api="email_file_upload")
    if request.method == "POST":
        try:
            token = request.headers["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_file_upload", uid=uid)  # 查询到了在计入

                picture_data = request.FILES.get('file', None)#获取文件数据
                picture_name = picture_data.name # 获取文件名
                result = MailAttachment().Verification(uid=uid, file_name=base64.b64encode(str(picture_name).encode('utf-8')).decode('utf-8'))#验证图片名字是否冲突
                if result:
                    return JsonResponse({'message': '文件名称冲突啦，请修改后上传o(TヘTo)', 'code': 604, })
                else:
                    if 0<picture_data.size:#内容不能为空
                        save_name=randoms().result(50)+str(int(time.time()))#重命名文件
                        save_route=GetPath().EmailUploadFilePath()+save_name#获得保存路径
                        with open(save_route, 'wb') as f:
                            for line in picture_data:
                                f.write(line)
                        MailAttachment().Write(uid=uid,
                                               file_name=base64.b64encode(str(picture_name).encode('utf-8')).decode('utf-8'),
                                               file_size=picture_data.size,
                                               document_real_name=save_name)
                        return JsonResponse({'message': "上传成功~", 'code': 200,})#返回上传图片名称
                    else:
                        return JsonResponse({'message': '它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)',  'code': 603,})
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""email_image_preview
{
	"token": "xxx",
	"document_real_name":"xxxx"
}
"""
def EmailImagePreview (request):#查询加载的文件
    RequestLogRecord(request, request_api="email_image_preview")
    if request.method == "POST":
        try:
            token = request.headers["token"]
            document_real_name = request.headers["document_real_name"]

            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_image_preview", uid=uid)  # 查询到了在计入
                result = MailAttachment().Verify(uid=uid,document_real_name=document_real_name)
                if result:#如果存在
                    picture_bitstream=open(GetPath().EmailUploadFilePath()+document_real_name,'rb').read()
                    return HttpResponse(picture_bitstream)  # 把图片比特流复制给返回包
                else:
                    return JsonResponse({'message': '没有这个文件~',  'code': 603, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""email_attachment_statistical
{
	"token": "xxx"
}
"""
def StatisticalMailAttachment(request):#统计邮件附件个数
    RequestLogRecord(request, request_api="email_attachment_statistical")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_attachment_statistical", uid=uid)  # 查询到了在计入
                result=MailAttachment().Quantity(uid=uid)
                return JsonResponse({'message': result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""email_attachment_details
{
	"token": "xxx",
	"number_of_pages":"1"
}
"""
def EmailAttachmentQuery(request):#查询附件文件
    RequestLogRecord(request, request_api="email_attachment_details")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            number_of_pages=json.loads(request.body)["number_of_pages"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_attachment_details", uid=uid)  # 查询到了在计入
                if int(number_of_pages)>0:
                    result=MailAttachment().Query(uid=uid,number_of_pages=int(number_of_pages))
                    return JsonResponse({'message': result, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
