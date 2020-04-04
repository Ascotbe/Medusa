import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from config import bot_email_receiver,bot_mail_pass,bot_mail_user
import sys,os
# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
def SendEamil(cve_message):
    # 邮件内容
    for receiver in bot_email_receiver:

        email_box = MIMEMultipart()#创建容器
        # message = MIMEText("警戒警戒！莎莎检测到有人入侵！数据以保存喵~", 'plain', 'utf-8')#邮箱文字
        # email_box.attach(message)#存入
        email_box['From'] =  "Salsa<"+bot_mail_user+ ">"#发送人
        email_box ['To'] =  receiver#发给谁
        email_box ['Subject'] = Header("推送CVE啦~", 'utf-8')#标题

            # #发送压缩文件
            # zip_apart = MIMEApplication(open(zip_file, 'rb').read())
            # zip_apart.add_header('Content-Disposition', 'attachment', filename=zip_file)
            # email_box.attach(zip_apart)
            #添加表情包图片
        if bot_mail_user==receiver:
            msgAlternative = MIMEMultipart('alternative')
            email_box.attach(msgAlternative)
            mail_msg = """
            <p>莎莎检测到有最新CVE！请注意查收喵~</p>
            <p>{}<p>
            <p><img src="cid:bot_image"></p>
            """.format(cve_message)
            msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
            # 指定图片为当前目录
            global email_image
            if sys.platform == "win32" or sys.platform == "cygwin":
                email_image = os.path.split(os.path.realpath(__file__))[0] + "\\bot_image.gif"
            elif sys.platform == "linux" or sys.platform == "darwin":
                email_image = os.path.split(os.path.realpath(__file__))[0] + "/bot_image.gif"
            print(email_image)
            file = open(email_image, "rb")
            img_data = file.read()
            file.close()
            img = MIMEImage(img_data)
            img.add_header('Content-ID', 'bot_image')
            email_box.attach(img)
        else:
            msgAlternative = MIMEMultipart('alternative')
            email_box.attach(msgAlternative)
            mail_msg = """
            <p>莎莎检测到有最新CVE！请注意查收喵~</p>
            <p>{}<p>
            """.format(cve_message)
            msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(bot_mail_user, bot_mail_pass)
            smtpObj.sendmail(bot_mail_user, receiver, email_box.as_string())
            #print("发送成功")
            smtpObj.quit()
            smtpObj.close()
        except smtplib.SMTPException as e:
            pass
            #print(e)


