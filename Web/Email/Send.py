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
"""
<p><img src="cid:dns_config"></p>
"""


@app.task
def SendMail(MailMessage,Attachment,Image,MailTitle,Sender,GoalMailbox,ForgedAddress,Interval,Key):

    # 邮件内容
    TempFilePath = GetTempFilePath().Result()
    MailUploadFilePath = GetMailUploadFilePath().Result()  # 本地文件路径
    for Department in GoalMailbox:#循环获取部门
        for Target in GoalMailbox[Department]:# 向多个目标发送
            time.sleep(float(Interval))#邮件发送间隔
            MD5=hashlib.md5(Target.encode()).hexdigest()#计算文件MD5值
            try:
                EmailBox = MIMEMultipart()  # 创建容器

                EmailBox['From'] = Header(Sender + "<" + ForgedAddress + ">", 'utf-8') # 发送人
                EmailBox['To'] = Header(Target, 'utf-8')# 发给谁
                EmailBox['Subject'] = Header(MailTitle, 'utf-8')  # 标题
                EmailBox["Accept-Language"] = "zh-CN"
                EmailBox["Accept-Charset"] = "ISO-8859-1,utf-8"
                # 消息正文
                TextMessage = MIMEMultipart('alternative')
                EmailBox.attach(TextMessage)
                MailMessage = Template(MailMessage).render(md5=MD5)#对里面的模板进行处理,目前固定为{{ md5 }}占位符
                TextMessage.attach(MIMEText(MailMessage, 'html', 'utf-8'))
                # 发送附件
                for i in Attachment:
                    AttachmentTemp = TempFilePath + i  # 文件名字
                    AttachmentName = MailUploadFilePath + Attachment[i]  # 文件真实名字
                    shutil.copy(AttachmentName, AttachmentTemp)  # 复制到temp目录
                    AttachmentData = MIMEApplication(open(AttachmentTemp, 'rb').read())  # 使用temp文件的重命名文件进行发送
                    AttachmentData.add_header('Content-Disposition', 'attachment', filename=i)
                    TextMessage.attach(AttachmentData)
                # 正文图片
                for x in Image:
                    ImageTemp = TempFilePath + x  # 文件名字
                    ImageName = MailUploadFilePath + Image[x]  # 文件真实名字
                    shutil.copy(ImageName, ImageTemp)  # 复制到temp目录
                    pic = MIMEApplication(open(ImageTemp,'rb').read())
                    pic.add_header("Content-Disposition", "attachment", filename=x)
                    pic.add_header('Content-ID', '<'+x+'>')
                    pic.add_header("X-Attachment-Id", "x")
                    TextMessage.attach(pic)
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
                EmailDetails().Write(email=Target,email_md5=MD5,status="1",project_key=Key,department=Department)
            except Exception as e:
                ErrorLog().Write("Mail delivery failed->" + str(Target), e)
                EmailDetails().Write(email=Target,email_md5=MD5,status="-1",project_key=Key,department=Department)
    EmailProject().ProjectCompletion(redis_id=SendMail.request.id)#修改为完工



