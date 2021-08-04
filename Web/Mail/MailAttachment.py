from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,GetMailAttachmentFilePath
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import time
"""upload_mail_attachment
POST /api/upload_mail_attachment/ HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryaFtQbWz7pBzNgCOv
token:XXXXXXXXXXXXXXXX

------WebKitFormBoundaryaFtQbWz7pBzNgCOv
Content-Disposition: form-data; name="file"; filename="test.jpeg"
Content-Type: image/jpeg

XXXXXXXXXXXXXXX
------WebKitFormBoundaryaFtQbWz7pBzNgCOv--
"""
def UploadMailAttachment (request):#上传邮件附件
    RequestLogRecord(request, request_api="upload_mail_attachment")
    Token =request.headers["token"]
    if request.method == "POST":
        try:
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="upload_mail_attachment", uid=Uid)  # 查询到了在计入
                PictureData = request.FILES.get('file', None)#获取文件数据
                if 0<PictureData.size:#内容不能为空
                    SaveFileName=randoms().result(50)+str(int(time.time()))#重命名文件
                    SaveRoute=GetMailAttachmentFilePath().Result()+SaveFileName#获得保存路径
                    with open(SaveRoute, 'wb') as f:
                        for line in PictureData:
                            f.write(line)
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
