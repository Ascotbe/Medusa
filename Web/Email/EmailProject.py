#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,MaliciousEmail,EmailProject
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms
import json
import time
import base64
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
	"end_time":"1659557858",
	"project_key":"eNVqsIHXAV",
	"mail_message":"<p>警戒警戒！莎莎检测到有人入侵！数据以保存喵~</p>",
    "attachment": {"Medusa.txt":"AeId9BrGeELFRudpjb7wG22LidVLlJuGgepkJb3pK7CXZCvmM51628131056"},
    "image":{"Medusa.jpg":"2DvWXQc8ufvWMIrhwV5MxrzZZA2oy2f3b5qj5r6VTzb247nQYP1642744866"},
    "mail_title":"测试邮件",
    "sender":"瓜皮大笨蛋",
    "goal_mailbox":["ascotbe@gmail.com","ascotbe@163.com"],
    "third_party":"0",
    "forged_address":"helpdesk@ascotbe.com",
    "interval":"0.1"
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
                if int(EndTime)-int(time.time())<10000000:
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
                                        goal_mailbox=list(set(GoalMailbox)),#去重数据
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


