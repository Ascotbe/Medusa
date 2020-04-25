from Web.celery import app
from Confluence import ConfluenceMain
from Struts2 import Struts2
from Apache import ApacheMain
from Nginx import NginxMain
from Jenkins import JenkinsMain
from Cms import CmsMain
from FastJson import FastJson
from Harbor import Harbor
from Citrix import CitrixMain
from Rails import RailsMain
from Kibana import KibanaMain
from PHPStudy import PHPStudy
from Mongo import MongoMain
from OA import OaMian
from Windows import Windows
from Spring import SpringMain
from InformationLeakage.InformationLeakDetection import SensitiveFile

from ClassCongregation import ThreadPool
MedusaVulnerabilityList={
"Struts2":Struts2.Main,
"Confluence":ConfluenceMain.Main,
"Nginx":NginxMain.Main,
"Apache":ApacheMain.Main,
"PHPStudy": PHPStudy.Main,
"Cms": CmsMain.Main,
"OA": OaMian.Main,
"Jenkins": JenkinsMain.Main,
"Harbor": Harbor.Main,
"Rails":RailsMain.Main,
"Kibana":KibanaMain.Main,
"Citrix":CitrixMain.Main,
"Mongo":MongoMain.Main,
"Spring":SpringMain.Main,
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







