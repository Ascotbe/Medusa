#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,CrossSiteScriptTemplate
from django.http import JsonResponse
from ClassCongregation import ErrorLog,GetPath
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
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="read_default_cross_site_script_template", uid=uid)
                default_template_file_data=[]#用来存放默认模板数据
                cross_site_script_template_path=GetPath().XSSTemplatePath()#获取模板文件路径
                default_template_file_list = os.listdir(cross_site_script_template_path)  # 获取文件夹中全部文件
                for default_template_file in default_template_file_list:  # 清洗不相关文件
                    if default_template_file.endswith(".js"):
                        with open(cross_site_script_template_path+default_template_file, 'r+',encoding='UTF-8') as f:#读取文件
                            file_data = f.read()
                        default_template_file_data.append({"file_name":default_template_file,"file_data":base64.b64encode(str(file_data).encode('utf-8')).decode('utf-8')})#把读取到的数据加密后，转换成str类型后存入模板中
                return JsonResponse({'message': default_template_file_data, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
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
            token = json.loads(request.body)["token"]
            template_name = json.loads(request.body)["template_name"]#传入需要修改的模板名称
            template_data = json.loads(request.body)["template_data"]#传入需要修改的模板数据,原始数据即可无需base64加密
            base64_data=base64.b64encode(str(template_data).encode('utf-8')).decode('utf-8')#转换成base64的数据
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="save_cross_site_script_template", uid=uid)
                check=CrossSiteScriptTemplate().RepeatInvestigation(template_name=template_name,uid=uid)#查询是否在数据库中
                if check:#如果存在就返回错误
                    return JsonResponse({'message': "该模板已存在！", 'code': 503, })
                else:
                    CrossSiteScriptTemplate().Write(template_name=template_name,template_data=base64_data,uid=uid)#写入新的数据
                    return JsonResponse({'message': "欧拉欧拉欧拉欧拉欧拉欧拉欧拉欧拉(๑•̀ㅂ•́)و✧", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
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
            token = json.loads(request.body)["token"]
            template_name = json.loads(request.body)["template_name"]#传入需要修改的模板名称
            template_data = json.loads(request.body)["template_data"]#传入需要修改的模板数据，原始数据即可无需base64加密
            base64_data=base64.b64encode(str(template_data).encode('utf-8')).decode('utf-8')#转换成base64的数据
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="modify_cross_site_script_template", uid=uid)
                check=CrossSiteScriptTemplate().RepeatInvestigation(template_name=template_name,uid=uid)#查询是否在数据库中
                if check:#如果存在就更新数据库
                    return_value=CrossSiteScriptTemplate().Update(uid=uid,template_name=template_name,template_data=base64_data)#进行数据更新
                    if return_value:#判断更新是否成功
                        return JsonResponse({'message': "欧拉欧拉欧拉欧拉欧拉欧拉欧拉欧拉(๑•̀ㅂ•́)و✧", 'code': 200, })
                    else:
                        return JsonResponse({'message': "模板更新失败", 'code': 501, })
                else:#如果不存在就报错
                    return JsonResponse({'message': "不存在该模板哦宝贝~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
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
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="read_cross_site_script_template", uid=Uid)
                template_data=CrossSiteScriptTemplate().Query(uid=uid)#查询用户自定义的模板数据
                return JsonResponse({'message': template_data, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
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
            token = json.loads(request.body)["token"]
            template_name = json.loads(request.body)["template_name"]#传入需要修改的模板名称
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="delete_cross_site_script_template", uid=uid)
                result=CrossSiteScriptTemplate().Delete(template_name=template_name,uid=uid)#删除模板数据
                if result:
                    return JsonResponse({'message': "删除成功", 'code': 200, })
                else:
                    return JsonResponse({'message': "删除失败！", 'code': 170, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

