#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,EmailProject,EmailInfo,EmailDetails,EmailData
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
            token=json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="create_email_project", uid=uid)  # 查询到了在计入
                key=randoms().result(10)#生成Key
                result=EmailProject().Write(uid=uid,project_key=key)
                if result:
                    return JsonResponse({'message': key, 'code': 200, })
                else:
                    return JsonResponse({'message': "创建失败！", 'code': 505, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""updata_email_project
{

	"token": "xxxx",
	"end_time": "1659557858",
	"project_key": "eNVqsIHXAV",
	"project_name": "my_name",
	"mail_message": "<p>警戒警戒！莎莎检测到有人入侵！数据以保存喵~</p>\n<p><img src=\"cid:Medusa.jpg\"></p><p>快快看看这个<a target=\"_blank\" rel=\"noopener\" href=\"http://baidu.com/{{ md5 }}\">数据</a></p>",
	"attachment": {
		"Medusa.txt": "AeId9BrGeELFRudpjb7wG22LidVLlJuGgepkJb3pK7CXZCvmM51628131056"
	},
	"image": {
		"Medusa.jpg": "5x8SfyxamrejUHa6sBMztSUxH2skl6yBZ81lDDhj96264YLiRb1655199840"
	},
	"mail_title": "测试邮件",
	"sender": "瓜皮大笨蛋",
	"goal_mailbox": {
		"信息安全": ["ascotbe@gmail.com", "ascotbe@163.com"],
		"大数据": ["ascotbe@qq.com"],
		"客服": ["1099482542@qq.com"]
	},
	"email_list_key": "Sp7odgjo78xTh7zfQhUV",
	"forged_address": "helpdesk@ascotbe.com",
	"interval": "0.1"
}
"""
def Updata(request):#更新项目数据
    RequestLogRecord(request, request_api="updata_email_project")
    if request.method == "POST":
        try:
            end_time = json.loads(request.body)["end_time"]
            token = json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]  # 项目Key
            project_name = json.loads(request.body)["project_name"]  # 项目名称
            mail_message = json.loads(request.body)["mail_message"]  # 文本内容
            attachment = json.loads(request.body)["attachment"]  # 附件列表
            image = json.loads(request.body)["image"]  # 获取内容图片
            mail_title = json.loads(request.body)["mail_title"]  # 邮件标题
            sender = json.loads(request.body)["sender"]  # 发送人姓名
            goal_mailbox = json.loads(request.body)["goal_mailbox"]  # 目标邮箱
            email_list_key = json.loads(request.body)["email_list_key"]  # 邮箱列表数据库Key，和goal_mailbox只能选一个
            forged_address = json.loads(request.body)["forged_address"]  # 伪造发件人
            interval = json.loads(request.body)["interval"]  # 邮件发送间隔
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="updata_email_project", uid=uid)  # 查询到了在计入
                if email_list_key != "":
                    tmp = EmailInfo().Verification(uid=uid,project_key=email_list_key)#查询获取EmailList数据
                    if int(tmp) > 0:
                        email_list=EmailData().SendData(project_key=email_list_key)
                        if len(email_list)<=0 :#如果EmailList为空，且GoalMailbox为空
                            return JsonResponse({'message': "未传入收件人数据！请检查Key是否有用", 'code': 505, })
                        else:
                            goal_mailbox = email_list
                if len(goal_mailbox)<=0 and type(goal_mailbox)==dict:
                    return JsonResponse({'message': "未传入邮件接收人！", 'code': 414, })
                if type(attachment)!=dict or type(image)!=dict:
                    return JsonResponse({'message': "附件或者图片必须传入字典类型，不可置空！", 'code': 415, })
                if len(project_name)==0:
                    return JsonResponse({'message': "项目名称必须填入参数！", 'code': 416, })
                if int(end_time)-int(time.time())<10000000:
                    project_status= EmailProject().ProjectStatus(uid=uid,project_key=project_key)#查看项目是否启动
                    compilation_status = EmailProject().CompilationStatus(uid=uid, project_key=project_key)#查看项目是否完成
                    if compilation_status:
                        return JsonResponse({'message': "项目已经运行结束禁止修改其中内容！", 'code': 409, })
                    if project_status:
                        return JsonResponse({'message': "项目已经开启禁止修改，如需修改请停止运行！", 'code': 406, })
                    else:
                        result=EmailProject().Update(uid=uid,
                                                    mail_message=base64.b64encode(str(mail_message).encode('utf-8')).decode('utf-8'),
                                                    attachment=attachment,
                                                    project_name=project_name,
                                                    image=image,
                                                    mail_title=base64.b64encode(str(mail_title).encode('utf-8')).decode('utf-8'),
                                                    sender=base64.b64encode(str(sender).encode('utf-8')).decode('utf-8'),
                                                    forged_address=base64.b64encode(str(forged_address).encode('utf-8')).decode('utf-8'),
                                                    redis_id="",
                                                    project_key=project_key,
                                                    end_time=end_time,
                                                    goal_mailbox=goal_mailbox,#list(set(GoalMailbox)),#去重数据
                                                    interval=interval)
                        if result:
                            return JsonResponse({'message': "更新成功！", 'code': 200, })
                        else:
                            return JsonResponse({'message': "更新失败！", 'code': 507, })
                else:
                    return JsonResponse({'message': "时间间隔太长了！", 'code': 506, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
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
            token=json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="run_email_project", uid=uid)  # 查询到了在计入
                #下发任务后修改项目状态（下发任务留空），任务完成后项目就不可修改
                result=EmailProject().Query(uid=uid,project_key=project_key)#获取目标
                if result[13]=="0" and result[15]=="0":

                    target_list=ast.literal_eval(result[2])#目标
                    mail_message = base64.b64decode(str(result[6]).encode('utf-8')).decode('utf-8')  # 正文内容，需要用base64加密
                    attachment = ast.literal_eval(result[7])  # 附件文件，需要传入json格式，使用的是本地名称
                    image = ast.literal_eval(result[8])  # 图片文件，使用列表形式窜入
                    mail_title = base64.b64decode(str(result[9]).encode('utf-8')).decode('utf-8')  # 邮件头
                    sender = base64.b64decode(str(result[10]).encode('utf-8')).decode('utf-8')  # 发送人名称
                    forged_address = base64.b64decode(str(result[11]).encode('utf-8')).decode('utf-8')   # 伪造的发件人地址
                    interval = result[14]  # 邮件发送间隔
                    if target_list != 0:

                        redis_task = SendMail.delay(mail_message=mail_message, attachment=attachment,
                                                          image=image, mail_title=mail_title,
                                                          sender=sender, goal_mailbox=target_list,
                                                          forged_address=forged_address,
                                                          interval=interval,
                                                          key=project_key,
                                                          task_status=True)  # 调用下发任务
                        EmailProject().UpdateRedis(uid=uid, project_key=project_key, redis_id = redis_task.task_id)
                        tmp = EmailProject().ModifyProjectStatus(uid=uid, project_key=project_key, project_status="1")

                        if tmp:
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
            ErrorLog().Write(e)
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
            token=json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="stop_email_project", uid=uid)  # 查询到了在计入
                #结束任务后修改项目状态（结束任务留空）
                result=EmailProject().ModifyProjectStatus(uid=uid,project_key=project_key,project_status="0")
                if result:
                    return JsonResponse({'message': "项目停止成功！", 'code': 200, })
                else:
                    return JsonResponse({'message': "项目停止失败！", 'code': 505, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "未知错误，请查看日志(๑•̀ㅂ•́)و✧", 'code': 169, })
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
            token=json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_project_details", uid=uid)  # 查询到了在计入
                result=EmailProject().Query(uid=uid,project_key=project_key)
                json_values={}
                #JsonValues["goal_mailbox"] = ast.literal_eval(Result[2]) #先注释了，几万封邮件会导致很卡
                json_values["end_time"] = result[3]
                json_values["project_key"] = result[4]
                json_values["project_name"] = result[5]
                json_values["mail_message"] = result[6]
                json_values["attachment"] = ast.literal_eval(result[7])
                json_values["image"] = ast.literal_eval(result[8])
                json_values["mail_title"] = result[9]
                json_values["sender"] = result[10]
                json_values["forged_address"] = result[11]
                json_values["redis_id"] = result[12]
                json_values["compilation_status"] = result[13]
                json_values["interval"] = result[14]
                json_values["project_status"] = result[15]
                json_values["creation_time "] = result[16]

                return JsonResponse({'message': json_values, 'code': 200, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "未知错误，请查看日志(๑•̀ㅂ•́)و✧", 'code': 169, })
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
            token=json.loads(request.body)["token"]
            number_of_pages=json.loads(request.body)["number_of_pages"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_project_summary", uid=uid)  # 查询到了在计入
                if int(number_of_pages)>0:
                    result=EmailProject().Summary(uid=uid,number_of_pages=int(number_of_pages))
                    number = EmailProject().Statistics(uid=uid)
                    return JsonResponse({'message': result,'number': number, 'code': 200, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "未知错误，请查看日志(๑•̀ㅂ•́)و✧", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""email_sending_status
{
	"token": "xxx",
	"number_of_pages":"1",
	"full_data":true,
	"status":"1",
	"project_key":"1"
}
"""
def Status(request):#查询单封邮件状态
    RequestLogRecord(request, request_api="email_sending_status")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            number_of_pages=json.loads(request.body)["number_of_pages"]
            project_key = json.loads(request.body)["project_key"]
            full_data = json.loads(request.body)["full_data"]
            status = json.loads(request.body)["status"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_sending_status", uid=uid)  # 查询到了在计入
                if int(number_of_pages)>0:
                    result=EmailProject().Query(uid=uid,project_key=project_key)#验证project_key是否归该用户所属
                    if result!=None:
                        email_data=EmailDetails().Query(project_key=project_key,
                                                       full_data=full_data,
                                                       status=int(status),
                                                       number_of_pages=int(number_of_pages))
                        return JsonResponse({'message': email_data, 'code': 200, })
                    else:
                        return JsonResponse({'message': "该项目不属于你不要瞎请求！", 'code': 405, })
                else:
                    return JsonResponse({'message': "你家页数是负数的？？？？", 'code': 400, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "未知错误，请查看日志(๑•̀ㅂ•́)و✧", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""email_sending_status_statistics
{
	"token": "xxx",
	"project_key":"1",
    "full_data":true,
	"status":"1",
}
"""
def StatusStatistics(request):#查询单封邮件状态统计
    RequestLogRecord(request, request_api="email_sending_status_statistics")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            full_data = json.loads(request.body)["full_data"]
            status = json.loads(request.body)["status"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="email_sending_status_statistics", uid=uid)  # 查询到了在计入
                result=EmailProject().Query(uid=uid,project_key=project_key)#验证project_key是否归该用户所属
                if result!=None:
                    email_data=EmailDetails().Statistics(project_key=project_key,
                                                        full_data=full_data,
                                                        status=int(status))
                    return JsonResponse({'message': email_data, 'code': 200, })
                else:
                    return JsonResponse({'message': "该项目不属于你不要瞎请求！", 'code': 405, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "未知错误，请查看日志(๑•̀ㅂ•́)و✧", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""resend_failure_email
{
	"token": "xxx",
	"project_key":"1"
}
"""


def Resend(request):  # 重发未发送成功的邮件
    RequestLogRecord(request, request_api="resend_failure_email")
    if request.method == "POST":
        try:
            token = json.loads(request.body)["token"]
            project_key = json.loads(request.body)["project_key"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="resend_failure_email", uid=uid)  # 查询到了在计入
                project_result = EmailProject().Query(uid=uid, project_key=project_key)  # 验证project_key是否归该用户所属，并获取目标内容
                if project_result != None:
                    target_list = EmailDetails().ResendQuery(project_key=project_key, status=-1)  # 目标
                    mail_message = base64.b64decode(str(project_result[6]).encode('utf-8')).decode(
                        'utf-8')  # 正文内容，需要用base64加密
                    attachment = ast.literal_eval(project_result[7])  # 附件文件，需要传入json格式，使用的是本地名称
                    image = ast.literal_eval(project_result[8])  # 图片文件，使用列表形式窜入
                    mail_title = base64.b64decode(str(project_result[9]).encode('utf-8')).decode('utf-8')  # 邮件头
                    sender = base64.b64decode(str(project_result[10]).encode('utf-8')).decode('utf-8')  # 发送人名称
                    forged_address = base64.b64decode(str(project_result[11]).encode('utf-8')).decode(
                        'utf-8')  # 伪造的发件人地址
                    interval = project_result[14]  # 邮件发送间隔
                    if target_list != 0:
                        #后续要对是否多次点击做校检
                        Redis = SendMail.delay(mail_message=mail_message, attachment=attachment,
                                              image=image, mail_title=mail_title, sender=sender,
                                              goal_mailbox=target_list,
                                              forged_address=forged_address, interval=interval, key=project_key,
                                              task_status=False)  # 调用下发任务
                        return JsonResponse({'message': "任务下发成功！", 'code': 200, })
                    else:
                        return JsonResponse({'message': "没有需要重发的邮件！", 'code': 400, })
                else:
                    return JsonResponse({'message': "该项目不属于你不要瞎请求！", 'code': 405, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "未知错误，请查看日志(๑•̀ㅂ•́)و✧", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""send_test_email
{

	"token": "xxxx",
	"mail_message": "<p>警戒警戒！莎莎检测到有人入侵！数据以保存喵~</p>\n<p><img src=\"cid:Medusa.jpg\"></p><p>快快看看这个<a target=\"_blank\" rel=\"noopener\" href=\"http://baidu.com/{{ md5 }}\">数据</a></p>",
	"attachment": {
		"Medusa.txt": "AeId9BrGeELFRudpjb7wG22LidVLlJuGgepkJb3pK7CXZCvmM51628131056"
	},
	"image": {
		"Medusa.jpg": "5x8SfyxamrejUHa6sBMztSUxH2skl6yBZ81lDDhj96264YLiRb1655199840"
	},
	"mail_title": "测试邮件",
	"sender": "瓜皮大笨蛋",
	"goal_mailbox": {
		"信息安全": ["ascotbe@gmail.com", "ascotbe@163.com"],
		"大数据": ["ascotbe@qq.com"],
		"客服": ["1099482542@qq.com"]
	},
	"forged_address": "helpdesk@ascotbe.com",
	"interval": "0.1"
}
"""
def Test(request):#发送测试邮件
    RequestLogRecord(request, request_api="send_test_email")
    if request.method == "POST":
        try:
            token = json.loads(request.body)["token"]
            mail_message = json.loads(request.body)["mail_message"]  # 文本内容
            attachment = json.loads(request.body)["attachment"]  # 附件列表
            image = json.loads(request.body)["image"]  # 获取内容图片
            mail_title = json.loads(request.body)["mail_title"]  # 邮件标题
            sender = json.loads(request.body)["sender"]  # 发送人姓名
            goal_mailbox = json.loads(request.body)["goal_mailbox"]  # 目标邮箱
            forged_address = json.loads(request.body)["forged_address"]  # 伪造发件人
            interval = json.loads(request.body)["interval"]  # 邮件发送间隔
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="send_test_email", uid=uid)  # 查询到了在计入
                if len(goal_mailbox)<=0 and type(goal_mailbox)==dict:
                    return JsonResponse({'message': "未传入邮件接收人！", 'code': 414, })
                if type(attachment)!=dict or type(image)!=dict:
                    return JsonResponse({'message': "附件或者图片必须传入字典类型，不可置空！", 'code': 415, })
                else:

                        # 后续要对是否多次点击做校检
                    SendMail.delay(mail_message=mail_message, attachment=attachment,
                                           image=image, mail_title=mail_title, sender=sender,
                                           goal_mailbox=goal_mailbox,
                                           forged_address=forged_address, interval=interval, key="this_is_a_test_mail",
                                           task_status=False)  # 调用下发任务

                    return JsonResponse({'message': "测试邮件任务下发成功！", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "未知错误(๑•̀ㅂ•́)و✧", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
