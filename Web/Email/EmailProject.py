#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,EmailProject
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms
import json
import time
import base64
import ast
from Web.Email.Send import SendMail
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord

"""create_email_project
{

	"token": "xxxx"
}
"""
def Creation(request):#创建生成项目
    RequestLogRecord(request, request_api="create_email_project")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="create_email_project", uid=Uid)  # 查询到了在计入
                Key=randoms().result(10)#生成Key
                Result=EmailProject().Write(uid=Uid,project_key=Key)
                if Result:
                    return JsonResponse({'message': Key, 'code': 200, })
                else:
                    return JsonResponse({'message': "创建失败！", 'code': 505, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Email_EmailProject_Creation(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""updata_email_project
{

	"token": "xxxx",
	"end_time": "1659557858",
	"project_key": "eNVqsIHXAV",
	"mail_message": "<p>警戒警戒！莎莎检测到有人入侵！数据以保存喵~</p>\n<p>首先需要制作PE镜像推荐使用<a target=\"_blank\" rel=\"noopener\" href=\"http://baidu.com/{{ md5 }}\">老毛桃</a></p>",
	"attachment": {
		"Medusa.txt": "AeId9BrGeELFRudpjb7wG22LidVLlJuGgepkJb3pK7CXZCvmM51628131056"
	},
	"image": {
		"Medusa.jpg": "2DvWXQc8ufvWMIrhwV5MxrzZZA2oy2f3b5qj5r6VTzb247nQYP1642744866"
	},
	"mail_title": "测试邮件",
	"sender": "瓜皮大笨蛋",
	"goal_mailbox": {
		"信息安全": ["ascotbe@gmail.com", "ascotbe@163.com"],
		"大数据": ["ascotbe@qq.com"],
		"客服": ["1099482542@qq.com"]
	},
	"third_party": "0",
	"forged_address": "helpdesk@ascotbe.com",
	"interval": "0.1"
}
"""
def Updata(request):#更新项目数据
    RequestLogRecord(request, request_api="updata_email_project")
    if request.method == "POST":
        try:
            EndTime = json.loads(request.body)["end_time"]
            Token = json.loads(request.body)["token"]
            Key = json.loads(request.body)["project_key"]  # 项目Key
            MailMessage = json.loads(request.body)["mail_message"]  # 文本内容
            Attachment = json.loads(request.body)["attachment"]  # 附件列表
            Image = json.loads(request.body)["image"]  # 获取内容图片
            MailTitle = json.loads(request.body)["mail_title"]  # 邮件标题
            Sender = json.loads(request.body)["sender"]  # 发送人姓名
            GoalMailbox = json.loads(request.body)["goal_mailbox"]  # 目标邮箱
            ForgedAddress = json.loads(request.body)["forged_address"]  # 伪造发件人
            Interval = json.loads(request.body)["interval"]  # 邮件发送间隔
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="updata_email_project", uid=Uid)  # 查询到了在计入
                if len(GoalMailbox)<=0 and type(GoalMailbox)==dict:
                    return JsonResponse({'message': "未传入邮件接收人！", 'code': 414, })
                if type(Attachment)!=dict or type(Image)!=dict:
                    return JsonResponse({'message': "附件或者图片必须传入字典类型，不可置空！", 'code': 415, })
                if int(EndTime)-int(time.time())<10000000:
                    ProjectStatus= EmailProject().ProjectStatus(uid=Uid,project_key=Key)#查看项目是否启动
                    CompilationStatus = EmailProject().CompilationStatus(uid=Uid, project_key=Key)#查看项目是否完成
                    if CompilationStatus:
                        return JsonResponse({'message': "项目已经运行结束禁止修改其中内容！", 'code': 409, })
                    if ProjectStatus:
                        return JsonResponse({'message': "项目已经开启禁止修改，如需修改请停止运行！", 'code': 406, })
                    else:
                        Result=EmailProject().Updata(uid=Uid,
                                            mail_message=base64.b64encode(str(MailMessage).encode('utf-8')).decode('utf-8'),
                                            attachment=Attachment,
                                            image=Image,
                                            mail_title=base64.b64encode(str(MailTitle).encode('utf-8')).decode('utf-8'),
                                            sender=base64.b64encode(str(Sender).encode('utf-8')).decode('utf-8'),
                                            forged_address=base64.b64encode(str(ForgedAddress).encode('utf-8')).decode('utf-8'),
                                            redis_id="",
                                            project_key=Key,
                                            end_time=EndTime,
                                            goal_mailbox=GoalMailbox,#list(set(GoalMailbox)),#去重数据
                                            interval=Interval)
                        if Result:
                            return JsonResponse({'message': "更新成功！", 'code': 200, })
                        else:
                            return JsonResponse({'message': "更新失败！", 'code': 507, })
                else:
                    return JsonResponse({'message': "时间间隔太长了！", 'code': 506, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Email_EmailProject_Updata(def)", e)
            return JsonResponse({'message': "未知错误(๑•̀ㅂ•́)و✧", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""run_email_project
{

	"token": "xxxx",
	"project_key":"eNVqsIHXAV"
}
"""
def Run(request):#运行项目
    RequestLogRecord(request, request_api="run_email_project")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Key = json.loads(request.body)["project_key"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="run_email_project", uid=Uid)  # 查询到了在计入
                #下发任务后修改项目状态（下发任务留空），任务完成后项目就不可修改
                ProjectResult=EmailProject().Query(uid=Uid,project_key=Key)#获取目标
                if ProjectResult[12]=="0" and ProjectResult[14]=="0":

                    TargetList=ast.literal_eval(ProjectResult[2])#目标
                    MailMessage = base64.b64decode(str(ProjectResult[5]).encode('utf-8')).decode('utf-8')  # 正文内容，需要用base64加密
                    Attachment = ast.literal_eval(ProjectResult[6])  # 附件文件，需要传入json格式，使用的是本地名称
                    Image = ast.literal_eval(ProjectResult[7])  # 图片文件，使用列表形式窜入
                    MailTitle =base64.b64decode(str(ProjectResult[8]).encode('utf-8')).decode('utf-8')  # 邮件头
                    Sender = base64.b64decode(str(ProjectResult[9] ).encode('utf-8')).decode('utf-8')  # 发送人名称
                    ForgedAddress = base64.b64decode(str(ProjectResult[10]).encode('utf-8')).decode('utf-8')   # 伪造的发件人地址
                    Interval = ProjectResult[13]  # 邮件发送间隔
                    if TargetList!=0:

                        SendMailForRedis = SendMail.delay(MailMessage, Attachment, Image, MailTitle, Sender, TargetList,
                                                         ForgedAddress,Interval,Key)  # 调用下发任务
                        EmailProject().UpdataRedis(uid=Uid, project_key=Key, redis_id = SendMailForRedis.task_id)
                        Result = EmailProject().ModifyProjectStatus(uid=Uid, project_key=Key, project_status="1")

                        if Result:
                            return JsonResponse({'message': "项目启动成功！", 'code': 200, })
                        else:
                            return JsonResponse({'message': "项目启动失败！", 'code': 505, })
                    else:
                        return JsonResponse({'message': "不存在目标无法启动！", 'code': 406, })
                else:
                    return JsonResponse({'message': "项目已经启动或者已经完成！", 'code': 410, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Email_EmailProject_Run(def)", e)
            return JsonResponse({'message': "未知错误，请查看日志(๑•̀ㅂ•́)و✧", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""stop_email_project
{

	"token": "xxxx",
	"project_key":"eNVqsIHXAV"
}
"""
def Stop(request):#运行项目
    RequestLogRecord(request, request_api="stop_email_project")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Key = json.loads(request.body)["project_key"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="stop_email_project", uid=Uid)  # 查询到了在计入
                #结束任务后修改项目状态（结束任务留空）
                Result=EmailProject().ModifyProjectStatus(uid=Uid,project_key=Key,project_status="0")
                if Result:
                    return JsonResponse({'message': "项目停止成功！", 'code': 200, })
                else:
                    return JsonResponse({'message': "项目停止失败！", 'code': 505, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Email_EmailProject_Stop(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""statistics_email_project
{
	"token": "xxx"
}
"""
def Statistics(request):#统计项目个数
    RequestLogRecord(request, request_api="statistics_email_project")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="statistics_email_project", uid=Uid)  # 查询到了在计入
                Result=EmailProject().Statistics(uid=Uid)
                return JsonResponse({'message': Result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Email_EmailProject_Statistics(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""email_project_details
{
	"token": "xxx",
	"project_key":"1"
}
"""
def Details(request):#查询邮件详情
    RequestLogRecord(request, request_api="email_project_details")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Key = json.loads(request.body)["project_key"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_project_details", uid=Uid)  # 查询到了在计入
                Result=EmailProject().Query(uid=Uid,project_key=Key)
                return JsonResponse({'message': Result[2:], 'code': 200, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Email_EmailProject_Details(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""email_project_summary
{
	"token": "xxx",
	"number_of_pages":"1"
}
"""
def Summary(request):#查询邮件摘要详情
    RequestLogRecord(request, request_api="email_project_summary")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            NumberOfPages=json.loads(request.body)["number_of_pages"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_project_summary", uid=Uid)  # 查询到了在计入
                if int(NumberOfPages)>0:
                    Result=EmailProject().Summary(uid=Uid,number_of_pages=int(NumberOfPages))
                    return JsonResponse({'message': Result, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Email_EmailProject_Summary(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
