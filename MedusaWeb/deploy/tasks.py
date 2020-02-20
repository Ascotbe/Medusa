from __future__ import absolute_import
from celery import shared_task
from Confluence import ConfluenceMain
from Struts2 import Struts2Main
from Apache import ApacheMain
from Nginx import NginxMain
from Jenkins import JenkinsMain
from Cms import CmsMain
from Apache.Solr import SolrMain
from InformationDetector import JS
from InformationLeakage import InformationDisclosureMain
from Php import PhpMain
from OA import OaMian
import ClassCongregation
import urllib.parse
import threading

import json


@shared_task
def add():
    print("dddddddddddddddddddddddddd")
    return ("dsadasdasdasdasdasdasdasdasdasd")


def NmapScan(url):#Nmap扫描这样就可以开多线程了
    ClassCongregation.NmapScan(url).ScanPort()#调用Nmap扫描类
def JSCrawling(Url):
    if Url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(Url)
    else:
        res = urllib.parse.urlparse('http://%s' % Url)
    Urls=res.scheme+"://"+res.hostname
    urls = JS.find_by_url_deep(Urls)
    JS.giveresult(urls,Urls)
@shared_task
def mian(Url,OutFileName=None,Values=None,ProxyIp=None):
    thread_list = []
    thread_list.append(threading.Thread(target=NmapScan, args=(Url,)))  # 把Nmap放到多线程中
    thread_list.append(threading.Thread(target=Struts2Main.Main, args=(Url,OutFileName,Values,ProxyIp,)))# 调用Struts2主函数
    thread_list.append(threading.Thread(target=ConfluenceMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用 Confluence主函数
    thread_list.append(threading.Thread(target=NginxMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))#调用Nginx主函数
    thread_list.append(threading.Thread(target=ApacheMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用Apache主函数
    thread_list.append(threading.Thread(target=PhpMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用Php主函数
    thread_list.append(threading.Thread(target=CmsMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用Cms主函数
    thread_list.append(threading.Thread(target=OaMian.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用OA主函数
    thread_list.append(threading.Thread(target=InformationDisclosureMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用信息泄露主函数
    thread_list.append(threading.Thread(target=JenkinsMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))  # 调用Jenkins主函数
    thread_list.append(threading.Thread(target=SolrMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))  # 调用Solr主函数
    thread_list.append(threading.Thread(target=JSCrawling, args=(Url,)))
    ThreadNumber=15
    for t in thread_list:#开启列表中的多线程
        t.setDaemon(True)
        t.start()
        while True:
            # 判断正在运行的线程数量,如果小于5则退出while循环,
            # 进入for循环启动新的进程.否则就一直在while循环进入死循环
            if (len(threading.enumerate()) < ThreadNumber):
                break

@shared_task
def independent(url,value):#单个组件扫描接口
    OutFileName=None
    Values=None
    ProxyIp=None
    if value.find('nmap')!=-1:
        NmapScan(url)
    elif value.find('struts')!=-1:
        Struts2Main.Main(url,OutFileName,Values,ProxyIp)# 调用Struts2主函数
    elif value.find('confluence')!=-1:
        ConfluenceMain.Main(url, OutFileName, Values, ProxyIp)  # 调用 Confluence主函数
    elif value.find('nginx')!=-1:
        NginxMain.Main(url, OutFileName, Values, ProxyIp)#调用Nginx主函数
    elif value.find('apache')!=-1:
        ApacheMain.Main(url, OutFileName, Values, ProxyIp)  # 调用Apache主函数
    elif value.find('php')!=-1:
        PhpMain.Main(url, OutFileName, Values, ProxyIp)# 调用Php主函数
    elif value.find('cms')!=-1:
        CmsMain.Main(url, OutFileName, Values, ProxyIp)# 调用Cms主函数
    elif value.find('OA')!=-1:
        OaMian.Main(url, OutFileName, Values, ProxyIp)# 调用OA主函数
    elif value.find('information')!=-1:
        InformationDisclosureMain.Main(url, OutFileName, Values, ProxyIp)# 调用信息泄露主函数
    elif value.find('jenkins')!=-1:
        JenkinsMain.Main(url, OutFileName, Values, ProxyIp)  # 调用Jenkins主函数
    elif value.find('solr')!=-1:
        SolrMain.Main(url, OutFileName, Values, ProxyIp) # 调用Solr主函数
    elif value.find('js')!=-1:
        JSCrawling(url)

@shared_task
def result(user,pid):
    values=ClassCongregation.VulnerabilityInquire(pid).Inquire()#数据库查询，user是用来判断用户的

    return json.dumps(values)
