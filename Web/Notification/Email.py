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
from config import email_test,third_party_mail_host,third_party_mail_user,third_party_mail_pass,local_mail_host,local_mail_user
from Web.DatabaseHub import EmailDetails,EmailProject
from ClassCongregation import ErrorLog,GetMailUploadFilePath,GetTempFilePath
from Web.celery import app
@app.task
def Send(**kwargs):
    EmailList=kwargs.get("email_list")#邮件列表
    EmailTitle=kwargs.get("email_title")#邮件标题
    Sender=kwargs.get("sender")#发送人
    ForgedAddress=kwargs.get("forged_address")#发送人地址
    EmailMessage=kwargs.get("email_message")#邮件内容
    # 邮件内容
    # TempFilePath = GetTempFilePath().Result()
    # MailUploadFilePath = GetMailUploadFilePath().Result()  # 本地文件路径

    for Target in EmailList:# 向多个目标发送
        try:
            EmailBox = MIMEMultipart()  # 创建容器

            EmailBox['From'] = Header(Sender + "<" + ForgedAddress + ">", 'utf-8') # 发送人
            EmailBox['To'] = Header(Target)# 发给谁
            EmailBox['Subject'] = Header(EmailTitle, 'utf-8')  # 标题
            EmailBox["Accept-Language"] = "zh-CN"
            EmailBox["Accept-Charset"] = "ISO-8859-1,utf-8"
            # 消息正文
            TextMessage = MIMEMultipart('alternative')
            EmailBox.attach(TextMessage)
            TextMessage.attach(MIMEText(EmailMessage, 'html', 'utf-8'))
            # 生成好看的图片模块
            # for x in Image:
            #     ImageTemp = TempFilePath + x  # 文件名字
            #     ImageName = MailUploadFilePath + Image[x]  # 文件真实名字
            #     shutil.copy(ImageName, ImageTemp)  # 复制到temp目录
            #     pic = MIMEApplication(open(ImageTemp,'rb').read())
            #     pic.add_header("Content-Disposition", "attachment", filename=x)
            #     pic.add_header('Content-ID', '<'+x+'>')
            #     pic.add_header("X-Attachment-Id", "x")
            #     TextMessage.attach(pic)
            SMTP = smtplib.SMTP()
            if email_test:  #判断是否测试用例
                SMTP.connect(third_party_mail_host, 25)  # 25 为 SMTP 端口号
                SMTP.login(third_party_mail_user, third_party_mail_pass)
                SMTP.sendmail(third_party_mail_user, Target, EmailBox.as_string())
            else:
                SMTP.connect(local_mail_host, 25)  # 25 为 SMTP 端口号
                #SMTP.set_debuglevel(True)
                SMTP.sendmail(local_mail_user, Target, EmailBox.as_string())
            SMTP.quit()
            SMTP.close()
        except Exception as e:
            ErrorLog().Write("Web_Notification_Email_Send(def)" + str(Target), e)


