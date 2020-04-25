#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Confluence import ConfluenceMain
from Struts2 import Struts2
from Apache import ApacheMain
from Nginx import NginxMain
from Jenkins import JenkinsMain
from Cms import CmsMain
from FastJson import FastJson
from Harbor import Harbor
from Citrix import CitrixMain
from InformationDetector import sublist3r
from InformationLeakage.InformationLeakDetection import SensitiveFile#这是个类
from Rails import RailsMain
from Kibana import KibanaMain
from PHPStudy import PHPStudy
from Mongo import MongoMain
from OA import OaMian
from Windows import Windows
from Spring import SpringMain
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
parser.add_argument('-i','--Info',type=str,help="Pass in a file, the content of the file should meet the specifications in the document")
parser.add_argument('-t','--ThreadNumber',type=int,help="Set the number of threads, the default number of threads 15.")
parser.add_argument('-f','--InputFileName',type=str,help="Specify bulk scan file batch scan")
parser.add_argument('-sp','--SqlPasswrod',type=str,help="Please enter an password file.")
parser.add_argument('-su','--SqlUser',type=str,help="Please enter an account file.")
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

def BoomDB(Url,SqlUser,SqlPasswrod,InputFileName):
    if SqlUser!=None or SqlPasswrod!=None:
        BlastingDB=ClassCongregation.BlastingDB(SqlUser,SqlPasswrod)#只要其中账号文件或者密码文件不为空的话就开启爆破数据库功能
        if InputFileName == None:#如果不是批量扫描使用就使用单独的UTL
            BlastingDB.BoomDB(Url)
        elif InputFileName != None:#如果是批量扫描就循环传入参数扫描
            with open(InputFileName, encoding='utf-8') as f:
                for UrlLine in f:
                    Urls=UrlLine
                    BlastingDB.BoomDB(Urls)
    else:
        pass

def NmapScan(url):#Nmap扫描这样就可以开多线程了
    ClassCongregation.NmapScan(url).ScanPort()#调用Nmap扫描类

def InitialScan(ThreadPool,InputFileName,Url,Token,Module,agentHeader,proxies):
    try:
        if InputFileName==None:
            try:
                print("\033[1;40;32m[ + ] Scanning target domain:\033[0m" + "\033[1;40;33m {}\033[0m".format(Url))
                San(ThreadPool,Url,agentHeader,Token,Module,proxies)
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
                            San(ThreadPool,UrlLine,agentHeader,Token,Module,proxies)
                            ClassCongregation.NumberOfLoopholes()  # 输出扫描结果个数
                            #ThreadPool.NmapAppend(NmapScan,Urls)#把Nmap放到多线程中
                            #print("\033[1;40;32m[ + ] NmapScan component payload successfully loaded\033[0m")
                        except KeyboardInterrupt as e:
                            exit(0)
            except:
                print("\033[1;40;31m[ ! ] Please check the file path or the file content is correct\033[0m")
    except:
        print("\033[1;40;31m[ ! ] Please enter the correct file path!\033[0m")

def San(ThreadPool,Url,agentHeader,Token,Module,proxies):
    #POC模块存进多线程池，这样如果批量扫描会变快很多
    if Module==None:
        print("\033[1;40;32m[ + ] Scanning across modules:\033[0m" + "\033[1;40;35m AllMod             \033[0m")
        for MedusaModule in MedusaModuleList:
            MedusaModuleList[MedusaModule](ThreadPool, Url, agentHeader, Token,proxies)  # 调用列表里面的值
    else:
        try:
            MedusaModuleList[Module](ThreadPool, Url, agentHeader, Token,proxies)  # 调用列表里面的值
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
    SqlPasswrod=args.SqlPasswrod#传入爆破数据库的密码文件
    SqlUser = args.SqlUser#传入爆破数据库的账号文件
    Module=args.Module#单独模块扫描功能
    SubdomainEnumerate=args.SubdomainEnumerate #开启深度子域名枚举，巨TM耗时间
    Subdomain=args.Subdomain#开启子域名枚举
    ThreadNumber=args.ThreadNumber#要使用的线程数默认15
    proxies= args.ProxiesIP#代理的IP
    InformationProbeFile=args.Info#信息探测文件
    if Values==None:#使用随机头
        agentHeader="None"
    else:
        agentHeader=Values

    #暂时关闭NMAPScan和数据库爆破功能

    ThreadPool = ClassCongregation.ThreadPool()#定义一个线程池
    Token=str(int(time.time()))+"medusa"#获取赋予的token
    if ThreadNumber==None:#如果线程数为空，那么默认为15
        ThreadNumber=15

    if InformationProbeFile!=None:
        try:
            SensitiveFile().File(InformationProbeFile, Token, ThreadNumber, proxies)  # 对文件进行信息探测
            print("\033[1;40;31m[ ! ] After the information leakage detection is over, check the written file or database!\033[0m")
            os._exit(0)
        except:
            print("\033[1;40;31m[ ! ] File input error, please check!\033[0m")
            os._exit(0)  # 直接退出整个函数


    if Url==None and InputFileName==None:#如果找不到URL的话直接退出
        print("\033[1;40;31m[ ! ] Incorrect input, please enter -h to view help\033[0m")
        os._exit(0)#直接退出整个函数
    elif Url!=None and InputFileName!=None:#如果既输入URL又输入URL文件夹一样退出
        print("\033[1;40;31m[ ! ] Incorrect input, please enter -h to view help\033[0m")
        os._exit(0)#直接退出整个函数

    #thread_list.append(threading.Thread(target=BoomDB, args=(Url, SqlUser, SqlPasswrod,InputFileName,)))#数据库爆破功能

    if SubdomainEnumerate==True and Subdomain==True :#对参数判断参数互斥
        print("\033[1;40;31m[ ! ] Incorrect input, please enter -h to view help\033[0m")
    elif SubdomainEnumerate==True:
        SubdomainJudge = "a"
        ThreadPool.SubdomainAppend(SubdomainCrawling, Url,SubdomainJudge) #发送到多线程池中
    elif Subdomain==True:
        SubdomainJudge = "b"
        ThreadPool.SubdomainAppend(SubdomainCrawling, Url,SubdomainJudge)
    InitialScan(ThreadPool,InputFileName, Url,Token,Module,agentHeader,proxies)#最后启动主扫描函数，这样如果多个IP的话优化速度，里面会做url或者url文件的判断
    SensitiveFile().Domain(Url,Token,ThreadNumber,proxies)#单个url信息探测
    print("\033[1;40;31m[ ! ] Scan is complete, please see the ScanResult file\033[0m")


# from IPy import IP
# ip = IP('192.168.0.0/28')#后面批量生成C段扫描会用到
# print(ip.len())#IP个数有多少
# for x in ip:
#     print(x)

