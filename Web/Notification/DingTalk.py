import requests
from ClassCongregation import ErrorLog
from config import ding_talk_bot_token
from Web.DatabaseHub import NistData
import time
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





def Bot():
    try:
        nist_data = NistData().Bot(time_difference=7200)
        for i in nist_data:
            m = "### 编号:" + str(i["vulnerability_number"]) + "\r\n"
            if i["v3_base_score"] != "" and i["v3_base_severity"] != "":
                if i["v3_base_severity"] == "HIGH":
                    m += "CVSS3:" + str(i["v3_base_score"]) + "🔴" + str(i["v3_base_severity"]) + "\r\n  "
                elif i["v3_base_severity"] == "MEDIUM":
                    m += "CVSS3:" + str(i["v3_base_score"]) + "🟡" + str(i["v3_base_severity"]) + "\r\n  "
                elif i["v3_base_severity"] == "LOW":
                    m += "CVSS3:" + str(i["v3_base_score"]) + "🟢" + str(i["v3_base_severity"]) + "\r\n  "
            if i["v2_base_score"] != "" and i["v2_base_everity"] != "":
                if i["v2_base_severity"] == "HIGH":
                    m += "CVSS2:" + str(i["v2_base_score"]) + "🔴" + str(i["v2_base_severity"]) + "\r\n  "
                elif i["v2_base_severity"] == "MEDIUM":
                    m += "CVSS2:" + str(i["v2_base_score"]) + "🟠" + str(i["v2_base_severity"]) + "\r\n  "
                elif i["v2_base_severity"] == "LOW":
                    m += "CVSS2:" + str(i["v2_base_score"]) + "🟢" + str(i["v2_base_severity"]) + "\r\n  "

            m += "\n描述:\n > " + str(i["vulnerability_description"]) + "\r\n  "
            if len(i["vendors"]) > 0:
                m += "\n厂商:"
                for x in i["vendors"]:
                    m += x + " "
                m += "\r\n  "
            if len(i["products"]) > 0:
                m += "\n产品:"
                for x in i["products"]:
                    m += x + " "
                m += "\r\n  "
            Send(message=m)
            time.sleep(5)  # 暂停5秒，一分钟超过20条会被钉钉屏蔽
    except Exception as e:
        ErrorLog().Write(e)