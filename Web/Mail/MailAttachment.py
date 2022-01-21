#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,MailAttachment
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,GetMailUploadFilePath
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import time
import base64
import json
"""mail_upload_files
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
    RequestLogRecord(request, request_api="mail_upload_files")
    if request.method == "POST":
        try:
            Token = request.headers["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="mail_upload_files", uid=Uid)  # 查询到了在计入
                PictureData = request.FILES.get('file', None)#获取文件数据
                PictureName = PictureData.name # 获取文件名
                if 0<PictureData.size:#内容不能为空
                    SaveFileName=randoms().result(50)+str(int(time.time()))#重命名文件
                    SaveRoute=GetMailUploadFilePath().Result()+SaveFileName#获得保存路径
                    with open(SaveRoute, 'wb') as f:
                        for line in PictureData:
                            f.write(line)
                    MailAttachment().Write(uid=Uid,file_name=base64.b64encode(str(PictureName).encode('utf-8')).decode('utf-8'),file_size=PictureData.size,document_real_name=SaveFileName)
                    return JsonResponse({'message': "上传成功~", 'code': 200,})#返回上传图片名称
                else:
                    return JsonResponse({'message': '它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)',  'code': 603,})
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_MailAttachment_UploadMailAttachment(def)", e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""statistical_mail_attachment
{
	"token": "xxx"
}
"""
def StatisticalMailAttachment(request):#统计邮件附件个数
    RequestLogRecord(request, request_api="statistical_mail_attachment")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="statistical_mail_attachment", uid=Uid)  # 查询到了在计入
                StatisticalMailAttachmentResult=MailAttachment().Quantity(uid=Uid)
                return JsonResponse({'message': StatisticalMailAttachmentResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_MailAttachment_StatisticalMailAttachment(def)", e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""email_attachment_query
{
	"token": "xxx",
	"number_of_pages":"1"
}
"""
def EmailAttachmentQuery(request):#查询附件文件
    RequestLogRecord(request, request_api="email_attachment_query")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            NumberOfPages=json.loads(request.body)["number_of_pages"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_attachment_query", uid=Uid)  # 查询到了在计入
                if int(NumberOfPages)>0:
                    EmailAttachmentQueryResult=MailAttachment().Query(uid=Uid,number_of_pages=int(NumberOfPages))
                    return JsonResponse({'message': EmailAttachmentQueryResult, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_MailAttachment_EmailAttachmentQuery(def)", e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
