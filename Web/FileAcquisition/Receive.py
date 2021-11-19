#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,MailAttachment
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,FileAcquisitionPath
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import time
import base64
import json
def Upload(request):#接收所需数据文件
    RequestLogRecord(request, request_api="file_acquisition_receive")
    Key =request.headers["Key"]
    FileFullPath=request.headers["FileFullPath"]
    UUID = request.headers["UUID"]
    if request.method == "POST":
        try:
            Uid = UserInfo().QueryUidWithKey(Key)  # 通过key来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="file_acquisition_receive", uid=Uid)  # 查询到了在计入
                ReceiveData = request.FILES.get('file', None)#获取文件数据
                ReceiveName = ReceiveData.name # 获取文件名
                if 0<ReceiveData.size:#内容不能为空
                    SaveFileName=randoms().result(10)+str(int(time.time()))#重命名文件
                    SaveRoute=FileAcquisitionPath().Result()+SaveFileName#获得保存路径
                    with open(SaveRoute, 'wb') as f:
                        for line in ReceiveData:
                            f.write(line)
                    #MailAttachment().Write(uid=Uid,file_name=base64.b64encode(str(ReceiveName).encode('utf-8')).decode('utf-8'),file_size=PictureData.size,document_real_name=SaveFileName)
                    return JsonResponse({'message': "上传成功~", 'code': 200,})
                else:
                    return JsonResponse({'message': '它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)',  'code': 603,})
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_FileAcquisition_Receive_Upload(def)", e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
