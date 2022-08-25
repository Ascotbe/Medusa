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
    ProjectKey=kwargs.get("project_key")
    Uid = kwargs.get("uid")
    Dataset={}
    ProjectResult=EmailProject().Query(uid=Uid,project_key=ProjectKey)#获取目标
    TargetList = ast.literal_eval(ProjectResult[2])  # 目标
    Fooled=[dict(t) for t in set([tuple(d.items()) for d in EmailReceiveData().NotNull(project_key=ProjectKey)])]#上钩数据，查询出来后进行去重
    Open=[dict(t) for t in set([tuple(d.items()) for d in EmailReceiveData().IsNull(project_key=ProjectKey)])]#打开邮件数据，查询出来后进行去重
    Open2Email=[t for t in [d["email"] for d in Open]]#提取出邮件值
    Fooled2Email = [t for t in [d["email"] for d in Fooled]]  # 提取出邮件值
    for i in TargetList:#数据处理
        TotalAmount=len(TargetList[i])#总数
        OpenHits=0#点开邮件命中了数量
        FooledHits=0#上钩了的命中数量

        for x in TargetList[i]:
            if x in Open2Email:
                OpenHits+=1
            elif x in Fooled2Email:
                FooledHits+=1
        Dataset[i]={"total_amount":TotalAmount,"open_hits":OpenHits,"fooled_hits":FooledHits}#统计BU的数据
    Dataset["open_email_user_data"]=Open2Email
    Dataset["hooked_email_user_data"] = Fooled2Email
    EmailGraph().Updata(project_key=ProjectKey,uid=Uid,graph_data=str(Dataset))


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
            Token=json.loads(request.body)["token"]
            ProjectKey = json.loads(request.body)["project_key"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_data_graph_statistics", uid=Uid)  # 查询到了在计入
                GraphResult=EmailGraph().Verification(project_key=ProjectKey, uid=Uid)#查询是否有数据
                if GraphResult:#如果有数据,不管
                    pass
                else:#如果没数据就写入
                    EmailGraph().Write(project_key=ProjectKey, uid=Uid, graph_data="")  # 写入表格数据，判断是否有数据在写入
                Manufacture.delay(project_key=ProjectKey, uid=Uid)  # 下发任务，然后更新表格
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
            Token=json.loads(request.body)["token"]
            ProjectKey = json.loads(request.body)["project_key"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_data_graph_query", uid=Uid)  # 查询到了在计入
                Result=EmailGraph().Query(project_key=ProjectKey, uid=Uid)
                return JsonResponse({'message': ast.literal_eval(Result), 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })

    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })