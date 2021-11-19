#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,FileAcquisitionData
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,FileAcquisitionPath
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import time
from config import file_acquisition_size_max

"""数据包
POST /api/file_acquisition_receive/ HTTP/1.1
Host: 127.0.0.1
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 193956
Content-Type: multipart/form-data; boundary=--cpp-httplib-multipart-data-bvbQiacp9S6eNBla
Filefullpath: C:\ascotbe\1.png
Key: 35pqvPIaZfU3NB6QT5mhd8vLYZa1bXHjRKpWW8sk
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Uuid: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

----cpp-httplib-multipart-data-bvbQiacp9S6eNBla
Content-Disposition: form-data; name="file"; filename="1.png"
Content-Type: application/octet-stream

xxx

----cpp-httplib-multipart-data-bvbQiacp9S6eNBla--
"""
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
                if 0<ReceiveData.size<=file_acquisition_size_max:#内容不能为空,且不能操过最大值

                    SaveFileName=randoms().result(10)+str(int(time.time()))#重命名文件
                    SaveRoute=FileAcquisitionPath().Result()+SaveFileName#获得保存路径
                    with open(SaveRoute, 'wb') as f:
                        for line in ReceiveData:
                            f.write(line)
                    FileAcquisitionData().Write(uid=Uid,file_full_path=FileFullPath,old_file_name=ReceiveName,file_size=ReceiveData.size,new_file_name=SaveFileName,target_machine=UUID)
                    return JsonResponse({'message': "ok", 'code': 200,})
                else:
                    return JsonResponse({'message': '它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)',  'code': 603,})
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_FileAcquisition_Receive_Upload(def)", e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
