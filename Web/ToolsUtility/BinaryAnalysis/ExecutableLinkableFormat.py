from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,GetAnalysisFileStoragePath
import time
from config import portable_execute_file_size
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import pefile
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import re
import magic
import os
import hashlib
from asn1crypto import cms

def Linux(request):  # 用于提取保存文件后调用相应的处理函数
    RequestLogRecord(request, request_api="linux_executable_linkable_format_analysis")
    if request.method == "POST":
        try:
            Token =request.headers["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="linux_executable_linkable_format_analysis", uid=Uid)  # 查询到了在计入
                PictureData = request.FILES.get('file', None)  # 获取文件数据
                if 0>=PictureData.size:#判断是不是空文件
                    return JsonResponse({'message': "宝贝数据这么小的嘛？", 'code': 400, })
                elif portable_execute_file_size < PictureData.size:  #和配置文件中做对比
                    SaveFileName = str(int(time.time()))   # 重命名文件
                    SaveRoute = GetAnalysisFileStoragePath().Result() + SaveFileName  # 获得保存路径
                    with open(SaveRoute, 'wb') as f:
                        for line in PictureData:
                            f.write(line)
                    #接下来调用处理函数，接着再调用删除函数
                    return JsonResponse({'message': "成功了", 'code': 200, })
                else:
                    return JsonResponse({'message': "文件太大啦~(๑•̀ㅂ•́)و✧", 'code': 501, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_ToolsUtility_ExecutableLinkableFormat_Linux(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })