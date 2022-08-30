#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse,JsonResponse
from ClassCongregation import ErrorLog
import json
import time
import base64
from Web.DatabaseHub import EmailReceiveData,UserInfo,EmailProject,EmailDetails
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import re
"""
http://127.0.0.1:9999/b/eNVqsIHXAV/?key=7adfffee50ed9cb5a49e6e6bb07cd538
http://127.0.0.1:9999/b/eNVqsIHXAV/?key=7adfffee50ed9cb5a49e6e6bb07cd538&use=aaaddddd&passs=dasdasd
{
    "key":"7adfffee50ed9cb5a49e6e6bb07cd538",
    "use":"aaaaaa",
    "passs":"asdsd"
}
key=7adfffee50ed9cb5a49e6e6bb07cd538&use=aaaddddd&passs=dasdasd
"""
def Monitor(request,data):#用于接收信息的监控
    RequestLogRecord(request, request_api="email")
    get_request_fragment=""#项目ID
    try:

        get_request_fragment = re.search(r'/[a-zA-Z0-9]{10}', str(request.get_full_path), re.I).group(0)[1:11]
        #print(GetRequestFragment[1:11])
    except Exception as e:
        ErrorLog().Write(e)
    end_time=EmailProject().MonitorQuery(project_key=get_request_fragment)#查询项目接受数据时间
    if end_time!=None and int(end_time)>int(time.time()):#判断项目是否结束
        if request.method == "POST":
            try:
                key=""
                if request.headers["Content-Type"]=="application/json":
                    data_pack_info = request.body#获取post数据包信息
                    incidental_data = json.loads(request.body)  # 除了key以外的数据
                    key = incidental_data.pop('key')  # 获取md5值,顺便删除了该值
                    if len(incidental_data) <= 0:  # 判断是否为空数据
                        incidental_data = ""
                else:
                    data_pack_info = str(request.POST.dict()).encode('utf-8')#转换成字典后再换装byte类型穿给加密函数
                    incidental_data = request.POST.dict()  # 除了key以外的数据
                    key = incidental_data.pop('key')  # 获取md5值,顺便删除了该值
                    if len(incidental_data) <= 0:  # 判断是否为空数据
                        incidental_data = ""
                #HeadersInfo = str(request.headers).encode('utf-8')#获取头信息
                result = EmailDetails().EmailAndDepartment(email_md5=key, project_key=get_request_fragment)
                if len(key) == 32 and result is not None:
                    EmailReceiveData().Write(full_url=str(request.build_absolute_uri()),
                                             request_method="POST",
                                             project_key=get_request_fragment,
                                             target=key,
                                             email=result[0],
                                             department=result[1],
                                             data_pack_info=base64.b64encode(data_pack_info).decode('utf-8'),
                                             incidental_data=base64.b64encode(str(incidental_data).encode('utf-8')).decode('utf-8'))
            except Exception as e:
                ErrorLog().Write(e)
        elif request.method == "GET":
            try:

                parameter_info=str(request.GET.dict()).encode('utf-8')#获取参数信息
                # HeadersInfo=str(request.headers).encode('utf-8')#获取头信息
                incidental_data=request.GET.dict() #除了key以外的数据
                key =incidental_data.pop('key')#获取md5值,顺便删除了该值
                if len(incidental_data)<=0:#判断是否为空数据
                    incidental_data=""
                result = EmailDetails().EmailAndDepartment(email_md5=key, project_key=get_request_fragment)
                if len(key) == 32 and result is not None:
                    EmailReceiveData().Write(full_url=str(request.build_absolute_uri()),
                                             request_method="GET",
                                             project_key=get_request_fragment,
                                             target=key,
                                             email=result[0],
                                             department=result[1],
                                             data_pack_info=base64.b64encode(parameter_info).decode('utf-8'),
                                             incidental_data=base64.b64encode(str(incidental_data).encode('utf-8')).decode('utf-8'))

            except Exception as e:
                ErrorLog().Write(e)

    return HttpResponse("")


"""email_receive_data_statistics
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa"
}
"""
def Statistics(request):#统计邮件获取到的数据
    RequestLogRecord(request, request_api="email_receive_data_statistics")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_receive_data_statistics", uid=uid)  # 查询到了在计入
                result=EmailReceiveData().Statistics(project_key=project_key)
                return JsonResponse({'message': result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""email_receive_data_details
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa",
	"number_of_pages":"1"
}
"""
def Details(request):#邮件获取的数据详情
    RequestLogRecord(request, request_api="email_receive_data_details")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            number_of_pages=json.loads(request.body)["number_of_pages"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_receive_data_details", uid=uid)  # 查询到了在计入
                if int(number_of_pages)>0:
                    result=EmailReceiveData().Query(project_key=project_key,number_of_pages=int(number_of_pages))
                    return JsonResponse({'message': result, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""email_receive_data_search
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa",
	"email":"163",
	"department":"",
	"start_time":"",
	"end_time":"",
	"number_of_pages":"1"
}
"""
def Search(request):#条件查询
    RequestLogRecord(request, request_api="email_receive_data_search")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            email = json.loads(request.body)["email"]#模糊查询条件，如果没有可以传入空字符串
            department = json.loads(request.body)["department"]#模糊查询条件，如果没有可以传入空字符串
            start_time = json.loads(request.body)["start_time"] # 开始时间
            end_time = json.loads(request.body)["end_time"]# 结束时间
            number_of_pages=json.loads(request.body)["number_of_pages"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_receive_data_search", uid=uid)  # 查询到了在计入
                if int(number_of_pages)>0:
                    result=EmailReceiveData().Search(project_key=project_key,
                                                     number_of_pages=int(number_of_pages),
                                                     email=email,
                                                     department=department,
                                                     start_time=start_time,
                                                     end_time=end_time)
                    return JsonResponse({'message': result, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""email_receive_data_search_quantity
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa",
	"email":"163",
	"department":"",
	"start_time":"",
	"end_time":""
}
"""
def SearchQuantity(request):#搜索数量
    RequestLogRecord(request, request_api="email_receive_data_search_quantity")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            email = json.loads(request.body)["email"]  # 模糊查询条件，如果没有可以传入空字符串
            department = json.loads(request.body)["department"]  # 模糊查询条件，如果没有可以传入空字符串
            start_time = json.loads(request.body)["start_time"]  # 开始时间
            end_time = json.loads(request.body)["end_time"]  # 结束时间
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_receive_data_search_quantity", uid=uid)  # 查询到了在计入
                result = EmailReceiveData().SearchQuantity(project_key=project_key,
                                                           email=email,
                                                           department=department,
                                                           start_time=start_time,
                                                           end_time=end_time)
                return JsonResponse({'message': result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })