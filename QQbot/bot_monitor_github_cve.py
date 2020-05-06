# !/usr/bin/python env
# -*- coding:utf-8 -*-
import json
import ClassCongregation
from nonebot import get_bot,scheduler
import requests
import config
import re
from datetime import datetime
import time
from pytz import timezone
from QQbot.bot_emil import SendEamil

cve_list = []  # 存放CVE的容器
bot=get_bot()

@scheduler.scheduled_job(
    'interval',
    # weeks=0,
    # days=0,
    # hours=0,
    minutes=3,
    # seconds=0,
    # start_date=time.now(),
    # end_date=None,
)
async def GithubCveApiSend():
    CveGroupMessage=""
    CveEmailMessage = ""
    try:
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        }
        GitCveApi=requests.get("https://api.github.com/search/repositories?q=CVE-20&sort=updated&order=desc",headers=headers, timeout=10)
        con=GitCveApi.text
        GitCveApiJson=json.loads(con)
        DataExtraction=GitCveApiJson["items"]
        for i in DataExtraction:
            GithubCveSekect=ClassCongregation.GithubCveApi(i).Sekect()#先查询数据库
            if GithubCveSekect:
                ClassCongregation.GithubCveApi(i).Update(int(time.time()))#如果存在就更新
            else:
                ClassCongregation.GithubCveApi(i).Write()#如果不存在就写入
                #写完后对数据进行分析
                GithubProjectCreatedTime=i["created_at"]#github项目创建时间
                GithubProjectCreatedDate,cccccc=GithubProjectCreatedTime.strip("Z").split("T")#对数据分割
                GithubProjectCreatedYear,GithubProjectCreatedMonth,GithubProjectCreatedDay=GithubProjectCreatedDate.split("-")#对日期分割
                #获取美国时间，因为github项目创建是基于美国时间的
                data = int(time.time())
                data = datetime.utcfromtimestamp(data)
                utc_tz = timezone('UTC')
                data = data.replace(tzinfo=utc_tz)
                USDate, aaaa = str(data.astimezone(timezone('US/Eastern'))).split(" ")
                AmericanTimeYear, AmericanTimeMonth, AmericanTimeDay = USDate.split("-")

                #判断是不是当天创建的项目
                if GithubProjectCreatedYear==AmericanTimeYear and AmericanTimeMonth==GithubProjectCreatedMonth:
                    #LocaltimeHour = time.localtime(time.time()).tm_hour#获取当前小时
                    cve_list.append(i)#发送到列表中
        for cve in cve_list:#如果不是就对容器封装然后发送给群
            regular_match_results = re.search(r'CVE-\d{4,4}-\d{4,10}',str(cve["name"]), re.I)
            if regular_match_results != None:
                CveGroupMessage=CveGroupMessage+"项目名称："+str(cve["name"])+"\r\n"+"项目地址："+str(cve["html_url"])+"\r"
        if config.bot_email_send:  # 判断是否开启该功能
            for cve_email in cve_list:#用于发送给邮箱的数据
                CveEmailMessage=CveEmailMessage+"项目名称："+str(cve_email["name"])+"<br>"+"项目地址："+str(cve_email["html_url"])+"<br>"+"使用项目前请验证准确性，谨防钓鱼[CQ:emoji,id=128153]"+"<br>"

        cve_list.clear()#接着清空容器
        if len(CveGroupMessage)>10:
            for group_monitor_id in config.monitor_group_list:
                await bot.send_group_msg(group_id=group_monitor_id,
                                     message='[CQ:emoji,id=127918]来自莎酱最新CVE推送，请查收瞄~\r\n' +CveGroupMessage+"\r\n"+"使用项目前请验证准确性，谨防钓鱼[CQ:emoji,id=128153]\r\n")  # 对管理的群发送
        if len(CveEmailMessage)>10:
            SendEamil(CveEmailMessage)
    except:
        pass


