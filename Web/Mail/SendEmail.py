import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from config import mail_host,mail_pass,mail_user
from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,GetMailAttachmentFilePath,GetMailImageFilePath
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""
<p><img src="cid:dns_config"></p>
"""

"""send_fishing_mail
{
	"token": "xxxx",
	"mail_message":"<p>警戒警戒！莎莎检测到有人入侵！数据以保存喵~</p>",
    "attachment": ["Medusa.txt"],
    "mail_title":"测试邮件",
    "sender":"喵狗子",
    "goal_mailbox":["ascotbe@gmail.com","ascotbe@163.com"]
}
"""
def SendEamil(request):#查询github监控数据
    RequestLogRecord(request, request_api="send_fishing_mail")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            MailMessage =json.loads(request.body)["mail_message"]#文本内容
            Attachment=json.loads(request.body)["attachment"]#附件列表
            MailTitle = json.loads(request.body)["mail_title"]  # 邮件标题
            Sender= json.loads(request.body)["sender"]  # 发送人姓名
            GoalMailbox = json.loads(request.body)["goal_mailbox"]  # 目标邮箱
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="send_fishing_mail", uid=Uid)  # 查询到了在计入
                # 邮件内容
                for Target in GoalMailbox:#像多个目标发送
                    try:
                        EmailBox = MIMEMultipart()  # 创建容器
                        EmailBox['From'] = Sender+"<" + mail_user + ">"  # 发送人
                        EmailBox['To'] = Target  # 发给谁
                        EmailBox['Subject'] = Header(MailTitle, 'utf-8')  # 标题
                        # 发送附件
                        MailAttachmentFilePath= GetMailAttachmentFilePath().Result()
                        for i in Attachment:
                            AttachmentData = MIMEApplication(open(MailAttachmentFilePath+i, 'rb').read())
                            AttachmentData.add_header('Content-Disposition', 'attachment', filename=i)
                            EmailBox.attach(AttachmentData)
                        # 消息正文
                        TextMessage = MIMEMultipart('alternative')
                        EmailBox.attach(TextMessage)
                        TextMessage.attach(MIMEText(MailMessage, 'html', 'utf-8'))
                        # # 指定图片为当前目录
                        # MailImageFilePath = GetMailImageFilePath().Result()
                        # file = open(image_file, "rb")
                        # img_data = file.read()
                        # file.close()
                        # img = MIMEImage(img_data)
                        # img.add_header('Content-ID', 'dns_config')
                        # EmailBox.attach(img)
                        SMTP = smtplib.SMTP()
                        SMTP.connect(mail_host, 25)  # 25 为 SMTP 端口号
                        SMTP.login(mail_user, mail_pass)
                        SMTP.sendmail(mail_user, Target, EmailBox.as_string())
                        print("成功"+Target)
                        SMTP.quit()
                        SMTP.close()
                    except Exception as e:
                        print("失败"+Target)#到时候写数据库
                        return JsonResponse({'message': "发送失败！！", 'code': 503, })
                return JsonResponse({'message': "发送成功~", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_SendEamil_SendEamil(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

