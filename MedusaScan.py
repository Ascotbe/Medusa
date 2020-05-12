#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Confluence import Confluence
from Modules.Struts2 import Struts2
from Modules.Apache import Apache
from Modules.Nginx import Nginx
from Modules.Jenkins import Jenkins
from Modules.Cms import Cms
from Modules.FastJson import FastJson
from Modules.Harbor import Harbor
from Modules.Citrix import Citrix
from Modules.InformationDetector import sublist3r
from Modules.InformationLeakage import InformationLeakage
from Modules.Rails import Rails
from Modules.Kibana import Kibana
from Modules.PHPStudy import PHPStudy
from Modules.Mongo import Mongo
from Modules.Liferay import Liferay
from Modules.OA import Oa
from Modules.Windows import Windows
from Modules.Spring import Spring
import ClassCongregation
import tldextract#域名处理函数可以识别主域名和后缀
import Banner
import argparse
import os
import sys
import time

parser = argparse.ArgumentParser()#description="xxxxxx")
#UrlGroup = parser.add_mutually_exclusive_group()#定义一个互斥参数组
#UrlGroup .add_argument("-q", "--quiet", action="store_true")#增加到互斥参数组里面去
parser.add_argument('-u','--url',type=str,help="Target url")
parser.add_argument('-m','--Module',type=str,help="Scan an application individually")
parser.add_argument('-p','--ProxiesIP',type=str,help="Need to enter a proxy IP")
parser.add_argument('-a','--agent',type=str,help="Specify a header file or use a random header")
parser.add_argument('-t','--ThreadNumber',type=int,help="Set the number of threads, the default number of threads 15.")
parser.add_argument('-f','--InputFileName',type=str,help="Specify bulk scan file batch scan")
parser.add_argument('-s','--Subdomain',help="Collect subdomains",action="store_true")
parser.add_argument('-se','--SubdomainEnumerate',help="Collect subdomains and turn on enumerations",action="store_true")
'''
在pycharm中设置固定要获取的参数，进行获取
在XXX.py 中 按住 “alt+shift+f9”  ----选择编辑配置（edit configurations）---script parameters(脚本程序)
在里面输入参数就可以使用debug调试了
'''
#漏洞哥哥插件的主函数
MedusaModuleList={
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
"Windows":Windows.Main,
"Liferay":Liferay.Main,
"InformationLeakage":InformationLeakage.Main
}


def NmapScan(url):#Nmap扫描这样就可以开多线程了
    ClassCongregation.NmapScan(url).ScanPort()#调用Nmap扫描类

def InitialScan(ThreadPool,InputFileName,Url,Module,agentHeader,proxies,**kwargs):
    try:
        if InputFileName==None:
            try:
                print("\033[1;40;32m[ + ] Scanning target domain:\033[0m" + "\033[1;40;33m {}\033[0m".format(Url))
                San(ThreadPool,Url,agentHeader,Module,proxies,**kwargs)
                ClassCongregation.NumberOfLoopholes()  # 输出扫描结果个数
                        #ThreadPool.NmapAppend(NmapScan,Urls)#把Nmap放到多线程中
                        #print("\033[1;40;32m[ + ] NmapScan component payload successfully loaded\033[0m")

            except KeyboardInterrupt as e:
                exit(0)
        elif InputFileName!=None:
            try:
                with open(InputFileName, encoding='utf-8') as f:
                    for UrlLine in f:#设置头文件使用的字符类型和开头的名字
                        try:
                            print("\033[1;40;32m[ + ] In batch scan, the current target is:\033[0m"+"\033[1;40;33m {}\033[0m".format(UrlLine.replace('\n', '')))
                            San(ThreadPool,UrlLine.strip("\r\n"),agentHeader,Module,proxies,**kwargs)
                            ClassCongregation.NumberOfLoopholes()  # 输出扫描结果个数
                            #ThreadPool.NmapAppend(NmapScan,Urls)#把Nmap放到多线程中
                            #print("\033[1;40;32m[ + ] NmapScan component payload successfully loaded\033[0m")
                        except KeyboardInterrupt as e:
                            exit(0)
            except:
                print("\033[1;40;31m[ ! ] Please check the file path or the file content is correct\033[0m")
    except:
        print("\033[1;40;31m[ ! ] Please enter the correct file path!\033[0m")

def San(ThreadPool,Url,agentHeader,Module,proxies,**kwargs):
    #POC模块存进多线程池，这样如果批量扫描会变快很多
    if Module==None:
        print("\033[1;40;32m[ + ] Scanning across modules:\033[0m" + "\033[1;40;35m AllMod             \033[0m")
        for MedusaModule in MedusaModuleList:
            MedusaModuleList[MedusaModule](ThreadPool, Url, agentHeader, proxies,**kwargs)  # 调用列表里面的值
    else:
        try:
            MedusaModuleList[Module](ThreadPool, Url, agentHeader,proxies,**kwargs)  # 调用列表里面的值
        except:  # 如果传入非法字符串会调用出错
            print("\033[1;40;31m[ ! ] Please enter the correct scan module name\033[0m")
            os._exit(0)  # 直接退出整个函数
    ThreadPool.Start(ThreadNumber)#启动多线程


def SubdomainCrawling(Url,SubdomainJudge):#开启子域名函数
    SubdomainCrawlingUrls= tldextract.extract(Url)
    SubdomainCrawlingUrl=SubdomainCrawlingUrls.domain+"."+SubdomainCrawlingUrls.suffix
    savefile=""
    if sys.platform == "win32" or sys.platform == "cygwin":
        savefile = os.path.split(os.path.realpath(__file__))[
                            0] + "\\ScanResult\\" + "Subdomain.txt"
    elif sys.platform == "linux" or sys.platform == "darwin":
        savefile = os.path.split(os.path.realpath(__file__))[
                            0] + "/ScanResult/" + "Subdomain.txt"
    if SubdomainJudge=="a":
        sublist3r.main(SubdomainCrawlingUrl, savefile, silent=False,subbrutes=True)
    else:
        sublist3r.main(SubdomainCrawlingUrl, savefile, silent=False, subbrutes=False)

if __name__ == '__main__':
    Banner.RandomBanner()#输出随机横幅
    args = parser.parse_args()
    InputFileName = args.InputFileName#批量扫描文件所在位置
    Url = args.url
    Values=args.agent#判断是否使用随机头，判断写在Class里面
    Module=args.Module#单独模块扫描功能
    SubdomainEnumerate=args.SubdomainEnumerate #开启深度子域名枚举，巨TM耗时间
    Subdomain=args.Subdomain#开启子域名枚举
    ThreadNumber=args.ThreadNumber#要使用的线程数默认15
    proxies= args.ProxiesIP#代理的IP
    if Values==None:#使用随机头
        agentHeader="None"
    else:
        agentHeader=Values

    #暂时关闭NMAPScan和数据库爆破功能

    ThreadPool = ClassCongregation.ThreadPool()#定义一个线程池
    Token=str(int(time.time()))+"medusa"#获取赋予的token
    if ThreadNumber==None:#如果线程数为空，那么默认为15
        ThreadNumber=15

    if Url==None and InputFileName==None:#如果找不到URL的话直接退出
        print("\033[1;40;31m[ ! ] Incorrect input, please enter -h to view help\033[0m")
        os._exit(0)#直接退出整个函数
    elif Url!=None and InputFileName!=None:#如果既输入URL又输入URL文件夹一样退出
        print("\033[1;40;31m[ ! ] Incorrect input, please enter -h to view help\033[0m")
        os._exit(0)#直接退出整个函数

    if SubdomainEnumerate==True and Subdomain==True :#对参数判断参数互斥
        print("\033[1;40;31m[ ! ] Incorrect input, please enter -h to view help\033[0m")
    elif SubdomainEnumerate==True:
        SubdomainJudge = "a"
        ThreadPool.SubdomainAppend(SubdomainCrawling, Url,SubdomainJudge) #发送到多线程池中
    elif Subdomain==True:
        SubdomainJudge = "b"
        ThreadPool.SubdomainAppend(SubdomainCrawling, Url,SubdomainJudge)
    InitialScan(ThreadPool,InputFileName, Url,Module,agentHeader,proxies,Sid="123",Uid="MMMMMMMMMMM")#最后启动主扫描函数，这样如果多个IP的话优化速度，里面会做url或者url文件的判断
    print("\033[1;40;31m[ ! ] Scan is complete, please see the ScanResult file\033[0m")


# from IPy import IP
# ip = IP('192.168.0.0/28')#后面批量生成C段扫描会用到
# print(ip.len())#IP个数有多少
# for x in ip:
#     print(x)

