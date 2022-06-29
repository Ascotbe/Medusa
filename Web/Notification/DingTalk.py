import requests
from ClassCongregation import ErrorLog
from config import ding_talk_bot_token
def Send(**kwargs):
    Message=kwargs.get("message")#消息正文

    Url="https://oapi.dingtalk.com/robot/send?access_token="+ding_talk_bot_token
    Json={
    "at": {
            "atMobiles":[
                ""
            ],
            "atUserIds":[
                ""
            ],
            "isAtAll": False
        },
        "text": {
            "content":"消息推送：\n"+Message
        },
        "msgtype":"text"
    }
    Headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        }
    try:
        requests.post(Url,json=Json,headers=Headers, timeout=10)
    except Exception as e:
        ErrorLog().Write("Web_Notification_DingTalk_Send(def)", e)






Send(message="""
　 ·“文本与图标” \n
　　 顾名思义，这项是设置解压时的提醒信息与解压包图标的。“自解压文件窗口标题”将出现在解压时的标题栏中，而“显示的文本”会出现在 RAR 的解压提示处。 \n
　　 ·“许可” 这一项就是每次安装软件都能见到的“软件许可协议”，把你需要的内容填进去就行了，要是你愿意，还可以把软件的功能介绍放在这里。 \n
经过这么几步后，其余再按照默认设置，自动安装包就做完了。\n""")