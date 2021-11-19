#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,CrossSiteScriptTemplate
from django.http import JsonResponse
from ClassCongregation import ErrorLog,GetCrossSiteScriptTemplateFilePath
import json
import base64
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import os
"""read_default_cross_site_script_template
{
	"token": ""
}
"""
def ReadDefaultTemplate(request):#用读取默认的模板文件
    RequestLogRecord(request, request_api="read_default_cross_site_script_template")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="read_default_cross_site_script_template", uid=Uid)
                DefaultTemplateFileData=[]#用来存放默认模板数据
                CrossSiteScriptTemplateFilePath=GetCrossSiteScriptTemplateFilePath().Result()#获取模板文件路径
                DefaultTemplateFileList = os.listdir(CrossSiteScriptTemplateFilePath)  # 获取文件夹中全部文件
                for DefaultTemplateFile in DefaultTemplateFileList:  # 清洗不相关文件
                    if DefaultTemplateFile.endswith(".js"):
                        with open(CrossSiteScriptTemplateFilePath+DefaultTemplateFile, 'r+',encoding='UTF-8') as f:#读取文件
                            FileData = f.read()
                        DefaultTemplateFileData.append({"file_name":DefaultTemplateFile,"file_data":base64.b64encode(str(FileData).encode('utf-8')).decode('utf-8')})#把读取到的数据加密后，转换成str类型后存入模板中
                return JsonResponse({'message': DefaultTemplateFileData, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_TemplateManagement_ReadDefaultTemplate(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""save_cross_site_script_template
{
	"token": "",
	"template_name":"",
	"template_data":""
}
"""
def SaveTemplate(request):#用来保存模板数据
    RequestLogRecord(request, request_api="save_cross_site_script_template")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            TemplateName = json.loads(request.body)["template_name"]#传入需要修改的模板名称
            TemplateData = json.loads(request.body)["template_data"]#传入需要修改的模板数据,原始数据即可无需base64加密
            TemplateDataToBase64=base64.b64encode(str(TemplateData).encode('utf-8')).decode('utf-8')#转换成base64的数据
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="save_cross_site_script_template", uid=Uid)
                DatabaseCheck=CrossSiteScriptTemplate().RepeatInvestigation(template_name=TemplateName,uid=Uid)#查询是否在数据库中
                if DatabaseCheck:#如果存在就返回错误
                    return JsonResponse({'message': "该模板已存在！", 'code': 503, })
                else:
                    CrossSiteScriptTemplate().Write(template_name=TemplateName,template_data=TemplateDataToBase64,uid=Uid)#写入新的数据
                    return JsonResponse({'message': "欧拉欧拉欧拉欧拉欧拉欧拉欧拉欧拉(๑•̀ㅂ•́)و✧", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_TemplateManagement_SaveTemplate(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })



"""modify_cross_site_script_template
{
	"token": "",
	"template_name":"",
	"template_data":""
}
"""
def ModifyTemplate(request):#修改模板数据
    RequestLogRecord(request, request_api="modify_cross_site_script_template")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            TemplateName = json.loads(request.body)["template_name"]#传入需要修改的模板名称
            TemplateData = json.loads(request.body)["template_data"]#传入需要修改的模板数据，原始数据即可无需base64加密
            TemplateDataToBase64=base64.b64encode(str(TemplateData).encode('utf-8')).decode('utf-8')#转换成base64的数据
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="modify_cross_site_script_template", uid=Uid)
                DatabaseCheck=CrossSiteScriptTemplate().RepeatInvestigation(template_name=TemplateName,uid=Uid)#查询是否在数据库中
                if DatabaseCheck:#如果存在就更新数据库
                    ReturnValue=CrossSiteScriptTemplate().Update(uid=Uid,template_name=TemplateName,template_data=TemplateDataToBase64)#进行数据更新
                    if ReturnValue:#判断更新是否成功
                        return JsonResponse({'message': "欧拉欧拉欧拉欧拉欧拉欧拉欧拉欧拉(๑•̀ㅂ•́)و✧", 'code': 200, })
                    else:
                        return JsonResponse({'message': "模板更新失败", 'code': 501, })
                else:#如果不存在就报错
                    return JsonResponse({'message': "不存在该模板哦宝贝~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_TemplateManagement_ModifyTemplate(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""read_cross_site_script_template
{
	"token": ""
}
"""
def ReadTemplate(request):#用读取数据库中模板文件
    RequestLogRecord(request, request_api="read_cross_site_script_template")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="read_cross_site_script_template", uid=Uid)
                TemplateData=CrossSiteScriptTemplate().Query(uid=Uid)#查询用户自定义的模板数据
                return JsonResponse({'message': TemplateData, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_TemplateManagement_ReadTemplate(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""delete_cross_site_script_template
{
	"token": "",
	"template_name":""
}
"""
def DeleteTemplate(request):#删除模板
    RequestLogRecord(request, request_api="delete_cross_site_script_template")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            TemplateName = json.loads(request.body)["template_name"]#传入需要修改的模板名称
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="delete_cross_site_script_template", uid=Uid)
                Result=CrossSiteScriptTemplate().Delete(template_name=TemplateName,uid=Uid)#删除模板数据
                if Result:
                    return JsonResponse({'message': "删除成功", 'code': 200, })
                else:
                    return JsonResponse({'message': "删除失败！", 'code': 170, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_TemplateManagement_ReadTemplate(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

