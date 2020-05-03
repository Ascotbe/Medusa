from Web.celery import app
from Modules.Confluence import Confluence
from Modules.Struts2 import Struts2
from Modules.Apache import Apache
from Modules.Nginx import Nginx
from Modules.Jenkins import Jenkins
from Modules.Cms import Cms
from Modules.FastJson import FastJson
from Modules.Harbor import Harbor
from Modules.Citrix import Citrix
from Modules.Rails import Rails
from Modules.Kibana import Kibana
from Modules.PHPStudy import PHPStudy
from Modules.Mongo import Mongo
from Modules.OA import Oa
from Modules.Windows import Windows
from Modules.Spring import Spring
from Modules.InformationLeakage.InformationLeakDetection import SensitiveFile

from ClassCongregation import ThreadPool
MedusaVulnerabilityList={
"Struts2":Struts2.Main,
"Confluence":Confluence.Main,
"Nginx":Nginx.Main,
"Apache":Apache.Main,
"PHPStudy": PHPStudy.Main,
"Cms": Cms.Main,
"OA": Oa.Main,
"Jenkins": Jenkins.Main,
"Harbor": Harbor.Main,
"Rails":Rails.Main,
"Kibana":Kibana.Main,
"Citrix":Citrix.Main,
"Mongo":Mongo.Main,
"Spring":Spring.Main,
"FastJson":FastJson.Main,
"Windows":Windows.Main}

@app.task
def MedusaScan(Url,Token,Module,WebScanThreads,Values):
    WebScanThreadPool =ThreadPool()#定义一个线程池
    if Module=="all":
        for MedusaVulnerability in MedusaVulnerabilityList:
            MedusaVulnerabilityList[MedusaVulnerability](WebScanThreadPool, Url, Values, Token)#调用列表里面的值
        WebScanThreadPool.Start(WebScanThreads)
    else:
        try:
            MedusaVulnerabilityList[Module](WebScanThreadPool, Url, Values, Token)  # 调用列表里面的值
            WebScanThreadPool.Start(WebScanThreads)
        except:#如果传入非法字符串会调用出错
            pass

@app.task
def InformationLeakage(Url,Token,ThreadNumber,proxies):
    SensitiveFile().Domain(Url, Token, ThreadNumber, proxies)  # 单个url信息探测







