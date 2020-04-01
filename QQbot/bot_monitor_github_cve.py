import requests
import json
import ClassCongregation
import time

def GithubCveApiSend():
    while True:
        time.sleep(300)#5分钟请求一次
        try:
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
            }
            GitCveApi=requests.get("https://api.github.com/search/repositories?q=CVE-20&sort=updated&order=desc",headers=headers)
            con=GitCveApi.text
            GitCveApiJson=json.loads(con)
            DataExtraction=GitCveApiJson["items"]
            cve_list=[]#存放CVE的容器
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
                    localtime=time.localtime()
                    #获取本地的年月日
                    LocaltimeYear=time.strftime("%Y", localtime)
                    LocaltimeMonth=time.strftime("%m", localtime)
                    LocaltimeDay=time.strftime("%d", localtime)
                    #判断是不是当天创建的项目
                    if GithubProjectCreatedYear==LocaltimeYear and LocaltimeMonth==GithubProjectCreatedMonth and GithubProjectCreatedDay==LocaltimeDay:
                        LocaltimeHour = time.localtime(time.time()).tm_hour#获取当前小时
                        cve_list.append(i)#发送到列表中
                        if LocaltimeHour<9:#判断是不是凌晨-上午9点，如果是就pass
                            pass
                        else:
                            for i in cve_list:#如果不是就对容器封装然后发送给群
                                print(i)#封装还没写
                            cve_list.clear()#接着清空容器


                            print(LocaltimeHour)
        except:
            pass


