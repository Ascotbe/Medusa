#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.DatabaseHub import EmailReceiveData,UserInfo,EmailProject,EmailGraph
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import ast
from Web.celery import app

@app.task
def Manufacture(**kwargs):
    project_key=kwargs.get("project_key")
    uid = kwargs.get("uid")
    data_set={}
    project_result=EmailProject().Query(uid=uid,project_key=project_key)#获取目标
    target_list = ast.literal_eval(project_result[2])  # 目标
    fooled=[dict(t) for t in set([tuple(d.items()) for d in EmailReceiveData().NotNull(project_key=project_key)])]#上钩数据，查询出来后进行去重
    open_data=[dict(t) for t in set([tuple(d.items()) for d in EmailReceiveData().IsNull(project_key=project_key)])]#打开邮件数据，查询出来后进行去重
    open_email=[t for t in [d["email"] for d in open_data]]#提取出邮件值
    fooled_email = [t for t in [d["email"] for d in fooled]]  # 提取出邮件值
    for i in target_list:#数据处理
        total_amount=len(target_list[i])#总数
        open_hits=0#点开邮件命中了数量
        fooled_hits=0#上钩了的命中数量

        for x in target_list[i]:
            if x in open_email:
                open_hits+=1
            elif x in fooled_email:
                fooled_hits+=1
        data_set[i]={"total_amount":total_amount,"open_hits":open_hits,"fooled_hits":fooled_hits}#统计BU的数据
    data_set["open_email_user_data"]=open_email
    data_set["hooked_email_user_data"] = fooled_email
    EmailGraph().Updata(project_key=project_key,uid=uid,graph_data=str(data_set))


"""email_data_graph_statistics
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa"
}
"""
def Statistics(request):#数据表格制作
    RequestLogRecord(request, request_api="email_data_graph_statistics")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_data_graph_statistics", uid=uid)  # 查询到了在计入
                graph_result=EmailGraph().Verification(project_key=project_key, uid=uid)#查询是否有数据
                if graph_result:#如果有数据,不管
                    pass
                else:#如果没数据就写入
                    EmailGraph().Write(project_key=project_key, uid=uid, graph_data="")  # 写入表格数据，判断是否有数据在写入
                Manufacture.delay(project_key=project_key, uid=uid)  # 下发任务，然后更新表格
                return JsonResponse({'message': "任务下发成功！", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""email_data_graph_query
{
	"token": "xxx",
	"project_key":"aaaaaaaaaa"
}
"""
def Query(request):#数据表格查询
    RequestLogRecord(request, request_api="email_data_graph_query")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_data_graph_query", uid=uid)  # 查询到了在计入
                result=EmailGraph().Query(project_key=project_key, uid=uid)
                return JsonResponse({'message': ast.literal_eval(result), 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })