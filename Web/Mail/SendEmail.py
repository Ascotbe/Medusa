import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.header import Header
import base64
import shutil
from email.mime.image import MIMEImage
from config import mail_host,mail_pass,mail_user
from Web.WebClassCongregation import UserInfo,MaliciousEmail
from django.http import JsonResponse
from ClassCongregation import ErrorLog,GetMailAttachmentFilePath,GetTempFilePath
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""
<p><img src="cid:dns_config"></p>
"""

"""send_fishing_mail
{
	"token": "xxxx",
	"mail_message":"<p>警戒警戒！莎莎检测到有人入侵！数据以保存喵~</p>",
    "attachment": {"Medusa.txt":"AeId9BrGeELFRudpjb7wG22LidVLlJuGgepkJb3pK7CXZCvmM51628131056"},
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
            MailStatus={}
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="send_fishing_mail", uid=Uid)  # 查询到了在计入
                # 邮件内容
                TempFilePath=GetTempFilePath().Result()
                MailAttachmentFilePath = GetMailAttachmentFilePath().Result()#本地文件路径
                for Target in list(set(GoalMailbox)):#先去重，然后像多个目标发送
                    try:
                        EmailBox = MIMEMultipart()  # 创建容器
                        EmailBox['From'] = Sender+"<" + mail_user + ">"  # 发送人
                        EmailBox['To'] = Target  # 发给谁
                        EmailBox['Subject'] = Header(MailTitle, 'utf-8')  # 标题
                        # 发送附件
                        for i in Attachment:
                            Temp=TempFilePath+i#文件名字
                            AttachmentName=MailAttachmentFilePath+Attachment[i]#文件真实名字
                            shutil.copy(AttachmentName, Temp)#复制到temp目录
                            AttachmentData = MIMEApplication(open(Temp, 'rb').read())#使用temp文件的重命名文件进行发送
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
                        MailStatus[Target]="1"#写到状态表中
                        SMTP.quit()
                        SMTP.close()
                    except Exception as e:
                        MailStatus[Target] = "0"
                        ErrorLog().Write("Mail delivery failed->"+str(Target), e)
                MaliciousEmail().Write(uid=Uid, mail_message=base64.b64encode(str(MailMessage).encode('utf-8')).decode('utf-8'), attachment=Attachment, mail_title=base64.b64encode(str(MailTitle).encode('utf-8')).decode('utf-8'),
                                       sender=base64.b64encode(str(Sender).encode('utf-8')).decode('utf-8'), mail_status=json.dumps(MailStatus))
                return JsonResponse({'message': "发送成功~", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Mail_SendEamil_SendEamil(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

