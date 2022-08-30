#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import time
from jinja2 import Template
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.header import Header
import hashlib
import shutil
from config import email_debug,third_party_mail_host,third_party_mail_user,third_party_mail_pass,local_mail_host,local_mail_user
from Web.DatabaseHub import EmailDetails,EmailProject
from ClassCongregation import ErrorLog,GetPath
from Web.celery import app
"""
<p>这是一段文字</p>
<p><img src="cid:dns_config"></p>
<p>这个也是</p>
"""


@app.task
def SendMail(**kwargs):
    mail_message=kwargs.get('mail_message') #邮件内容
    attachment=kwargs.get('attachment')#附件
    image=kwargs.get('image')#图片
    mail_title=kwargs.get('mail_title')#邮件标题
    sender=kwargs.get('sender')#发件人
    goal_mailbox=kwargs.get('goal_mailbox')#收件人
    forged_address=kwargs.get('forged_address')#伪造邮件地址
    interval=kwargs.get('interval')#发送间隔
    key=kwargs.get('key')#邮件key
    task_status=kwargs.get('task_status')#任务状态,如果任务状态是真，表示是统一的发送逻辑，其余的都是再发送或者测试发送
    # 邮件内容
    temp_path = GetPath().TempFilePath()
    mail_upload_path = GetPath().EmailUploadFilePath()  # 本地文件路径
    for department in goal_mailbox:#循环获取部门
        for Target in goal_mailbox[department]:# 向多个目标发送
            time.sleep(float(interval))#邮件发送间隔
            md5=hashlib.md5(Target.encode()).hexdigest()#计算文件MD5值
            try:
                email_box = MIMEMultipart()  # 创建容器

                email_box['From'] = Header(sender + "<" + forged_address + ">", 'utf-8') # 发送人
                email_box['To'] = Header(Target)# 发给谁
                email_box['Subject'] = Header(mail_title, 'utf-8')  # 标题
                email_box["Accept-Language"] = "zh-CN"
                email_box["Accept-Charset"] = "ISO-8859-1,utf-8"
                # 消息正文
                text_message = MIMEMultipart('alternative')
                email_box.attach(text_message)
                mail_message = Template(mail_message).render(md5=md5)#对里面的模板进行处理,目前固定为{{ md5 }}占位符
                text_message.attach(MIMEText(mail_message, 'html', 'utf-8'))
                # 发送附件
                for i in attachment:
                    attachment_temp = temp_path + i  # 文件名字
                    attachment_name = mail_upload_path + attachment[i]  # 文件真实名字
                    shutil.copy(attachment_name, attachment_temp)  # 复制到temp目录
                    attachment_data = MIMEApplication(open(attachment_temp, 'rb').read())  # 使用temp文件的重命名文件进行发送
                    attachment_data.add_header('Content-Disposition', 'attachment', filename=i)
                    text_message.attach(attachment_data)
                # 正文图片
                for x in image:
                    image_temp = temp_path + x  # 文件名字
                    image_name = mail_upload_path + image[x]  # 文件真实名字
                    shutil.copy(image_name, image_temp)  # 复制到temp目录
                    pic = MIMEApplication(open(image_temp,'rb').read())
                    pic.add_header("Content-Disposition", "attachment", filename=x)
                    pic.add_header('Content-ID', '<'+x+'>')
                    pic.add_header("X-Attachment-Id", "x")
                    text_message.attach(pic)
                SMTP = smtplib.SMTP()
                if email_debug:  #判断是否测试用例
                    SMTP.connect(third_party_mail_host, 25)  # 25 为 SMTP 端口号
                    SMTP.login(third_party_mail_user, third_party_mail_pass)
                    SMTP.sendmail(third_party_mail_user, Target, email_box.as_string())
                else:
                    SMTP.connect(local_mail_host, 25)  # 25 为 SMTP 端口号
                    #SMTP.set_debuglevel(True)
                    SMTP.sendmail(local_mail_user, Target, email_box.as_string())
                SMTP.quit()
                SMTP.close()

                result=EmailDetails().Verification(email=Target, project_key=key,department=department)#验证数据是否存在
                if result:#如果有数据
                    EmailDetails().Update(email=Target, project_key=key,department=department,status="1")#更新数据
                else:
                    EmailDetails().Write(email=Target,email_md5=md5,status="1",project_key=key,department=department)
            except Exception as e:
                ErrorLog().Write(e)
                result=EmailDetails().Verification(email=Target, project_key=key,department=department)#验证数据是否存在
                if result:#如果有数据
                    EmailDetails().Update(email=Target, project_key=key,department=department,status="-1")#更新数据
                else:
                    EmailDetails().Write(email=Target,email_md5=md5,status="-1",project_key=key,department=department)
    if task_status:
        EmailProject().ProjectCompletion(redis_id=SendMail.request.id)#修改为完工



