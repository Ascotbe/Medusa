import requests
from ClassCongregation import ErrorLog
from config import ding_talk_bot_token
def Send(**kwargs):
    message=kwargs.get("message")#消息正文

    url="https://oapi.dingtalk.com/robot/send?access_token="+ding_talk_bot_token
    data={
            "msgtype": "markdown",
            "markdown": {
                "title": "消息推送",
                "text": message
            },
            "at": {
                "atMobiles": [
                    ""
                ],
                "atUserIds": [
                    ""
                ],
                "isAtAll": False
            }
    }
    headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        }
    try:
        requests.post(url,json=data,headers=headers, timeout=10)
    except Exception as e:
        ErrorLog().Write(e)





