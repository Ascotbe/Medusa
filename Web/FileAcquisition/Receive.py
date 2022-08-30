#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,FileAcquisitionData,FileAcquisitionPack
from django.http import JsonResponse,FileResponse
from ClassCongregation import ErrorLog,randoms,GetPath
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import time
import json
from Web.celery import app
import zipfile
from config import file_acquisition_size_max


@app.task
def Pack(Uid,FileList):
    Path = GetPath().FileAcquisitionPath()  # 获取路径
    ProcessedData=[]#处理后的数据
    for x in FileList:
        ProcessedData.append((Uid,x))
    DataList = FileAcquisitionData().DocumentAuthentication(ProcessedData)  # 获取结果
    if DataList is False:
        FileAcquisitionPack().UpdateStatus(file_name="", state="-1",redis_id=Pack.request.id)
        print("文件中有不属于该用户数据")
    else:
        ZipFileName=randoms().result(10)+".zip"
        ZipPath= GetPath().FileAcquisitionZipPath() + ZipFileName # 压缩文件路径
        f = zipfile.ZipFile(ZipPath, 'w', zipfile.ZIP_DEFLATED)
        for i in DataList:
            f.write(Path+i[1], i[1] + "_" + i[0])  # 第一个参数是文件路径，第二参数是文件在压缩包的名字
        f.close()
        FileAcquisitionPack().UpdateStatus(file_name=ZipFileName,state="1", redis_id=Pack.request.id) #任务成功





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
                if 0<ReceiveData.size<=int(file_acquisition_size_max):#内容不能为空,且不能操过最大值

                    SaveFileName=randoms().result(10)+str(int(time.time()))#重命名文件
                    SaveRoute= GetPath().FileAcquisitionPath() +SaveFileName#获得保存路径
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
            ErrorLog().Write(e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""file_acquisition_file_pack
{
	"token": "xxx",
	"file_list":["rpTjEE7ecA1637302616","LEI33MECW61637302616"] 
}
"""
def FilePack(request): # 下载所需文件打包
    RequestLogRecord(request, request_api="file_acquisition_file_pack")
    if request.method == "POST":
        try:

            FileList = json.loads(request.body)["file_list"]  # 文件列表
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                PackRedis = Pack.delay(Uid,FileList)
                FileAcquisitionPack().Write(uid=Uid, file_name="",redis_id=PackRedis.task_id, state="0") #下发任务
                return JsonResponse({'message': "任务下发成功(๑•̀ㅂ•́)و✧", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""file_acquisition_pack_download
{
	"token": "xxx",
	"file_name":"XXXX.zip" 
}
"""
def Download(request): # 下载打包文件
    RequestLogRecord(request, request_api="file_acquisition_pack_download")
    if request.method == "POST":
        try:
            file_name = json.loads(request.body)["file_name"]  # 文件名
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                result=FileAcquisitionPack().DownloadAuthentication(uid=uid, file_name=file_name)
                if result:#如果为真
                    file = open(GetPath().FileAcquisitionZipPath()+file_name, 'rb')
                    response = FileResponse(file)
                    return response
                else:
                    return JsonResponse({'message': "宝,这文件不是你的哦(๑•̀ㅂ•́)و✧", 'code': 405, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

