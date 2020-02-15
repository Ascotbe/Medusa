#!/usr/bin/env python
# _*_ coding: utf-8 _*_


#import Weblogic.WeblogicMain
from Confluence import ConfluenceMain
#如果在自己创建的文件夹里面加入__init__.py文件的话就可以是用from 文件夹名 import 文件夹总的文件名来导入文件
#Struts2Main.Main()这样就导入了文件夹中Struts2Main.py文件中的Main函数
from Struts2 import Struts2Main
from Apache import ApacheMain
from Nginx import NginxMain
from Jenkins import JenkinsMain
from Cms import CmsMain
from Solr import SolrMain
from Citrix import CitrixMain
from InformationDetector import sublist3r
#from InformationLeakage import InformationDisclosureMain
from Rails import RailsMain
from Kibana import KibanaMain
from Php import PhpMain
from Mongo import MongoMain
from OA import OaMian
from Spring import SpringMain
import ClassCongregation
import tldextract#域名处理函数可以识别主域名和后缀
import Banner
import argparse
import os
import threading
from tqdm import tqdm

parser = argparse.ArgumentParser()#description="xxxxxx")
UrlGroup = parser.add_mutually_exclusive_group()#定义一个互斥参数组
#UrlGroup .add_argument("-q", "--quiet", action="store_true")#增加到互斥参数组里面去
parser.add_argument('-o','--OutFileName',type=str,help='The file where the url is located,If you do not enter the location, the default is written to the root directory.')
parser.add_argument('-u','--url',type=str,help="Target url")
parser.add_argument('-p','--Proxy',help="Whether to enable the global proxy function",action="store_true")
parser.add_argument('-a','--agent',type=str,help="Specify a header file or use a random header")
parser.add_argument('-f','--InputFileName',type=str,help="Specify bulk scan file batch scan")
parser.add_argument('-t','--ThreadNumber',type=int,help="Set the number of threads, the default number of threads 15.")
parser.add_argument('-sp','--SqlPasswrod',type=str,help="Please enter an password file.")
parser.add_argument('-su','--SqlUser',type=str,help="Please enter an account file.")
parser.add_argument('-s','--Subdomain',help="Collect subdomains",action="store_true")
parser.add_argument('-se','--SubdomainEnumerate',help="Collect subdomains and turn on enumerations",action="store_true")
'''
在pycharm中设置固定要获取的参数，进行获取
在XXX.py 中 按住 “alt+shift+f9”  ----选择编辑配置（edit configurations）---script parameters(脚本程序)
在里面输入参数就可以使用debug调试了
'''
thread_list = []#线程列表，到时候可以一起循环调用

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

def InitialScan(InputFileName,Url,ProxyIp):
    try:
        if InputFileName==None:
            Urls=Url
            try:
                San(OutFileName, Urls, Values,ProxyIp)
                thread_list.append(threading.Thread(target=NmapScan, args=(Urls,)))#把Nmap放到多线程中

            except KeyboardInterrupt as e:
                exit(0)
        elif InputFileName!=None:
            try:
                with open(InputFileName, encoding='utf-8') as f:
                    for UrlLine in tqdm(f,ascii=True,desc="IP scanning progress:"):#设置头文件使用的字符类型和开头的名字
                        Urls=UrlLine
                        try:
                            San(OutFileName, Urls, Values,ProxyIp)
                            thread_list.append(threading.Thread(target=NmapScan, args=(Urls,)))#把Nmap放到多线程中
                        except KeyboardInterrupt as e:
                            exit(0)
            except:
                print("Please check the file path or the file content is correct")
    except:
        print("Please enter the correct file path!")

def San(OutFileName,Url,Values,ProxyIp):
    #POC模块存进多线程池，这样如果批量扫描会变快很多
    thread_list.append(threading.Thread(target=Struts2Main.Main, args=(Url,OutFileName,Values,ProxyIp,)))# 调用Struts2主函数
    thread_list.append(threading.Thread(target=ConfluenceMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用 Confluence主函数
    thread_list.append(threading.Thread(target=NginxMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))#调用Nginx主函数
    thread_list.append(threading.Thread(target=ApacheMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用Apache主函数
    thread_list.append(threading.Thread(target=PhpMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用Php主函数
    thread_list.append(threading.Thread(target=CmsMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用Cms主函数
    thread_list.append(threading.Thread(target=OaMian.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用OA主函数
    #thread_list.append(threading.Thread(target=InformationDisclosureMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))# 调用信息泄露主函数
    thread_list.append(threading.Thread(target=JenkinsMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))  # 调用Jenkins主函数
    thread_list.append(threading.Thread(target=SolrMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))  # 调用Solr主函数
    thread_list.append(threading.Thread(target=RailsMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))  # 调用RailsMain主函数
    thread_list.append(threading.Thread(target=KibanaMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))  # 调用KibanaMain主函数
    thread_list.append(threading.Thread(target=CitrixMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))  # 调用CitrixMain主函数
    thread_list.append(threading.Thread(target=MongoMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))  # 调用MongoMain主函数
    thread_list.append(threading.Thread(target=SpringMain.Main, args=(Url, OutFileName, Values, ProxyIp,)))  # 调用SpringMain主函数

def SubdomainCrawling(Url,SubdomainJudge):#开启子域名函数
    SubdomainCrawlingUrls= tldextract.extract(Url)
    SubdomainCrawlingUrl=SubdomainCrawlingUrls.domain+"."+SubdomainCrawlingUrls.suffix
    savefile= "./ScanResult/Subdomain.txt"
    if SubdomainJudge=="a":
        sublist3r.main(SubdomainCrawlingUrl, savefile, silent=False,subbrutes=True)
    else:
        sublist3r.main(SubdomainCrawlingUrl, savefile, silent=False, subbrutes=False)

if __name__ == '__main__':
    Banner.RandomBanner()#输出随机横幅
    args = parser.parse_args()
    InputFileName = args.InputFileName#批量扫描文件所在位置
    OutFileName= args.OutFileName#输出最终结果文件名字
    Url = args.url
    Values=args.agent#判断是否使用随机头，判断写在Class里面
    SqlPasswrod=args.SqlPasswrod#传入爆破数据库的密码文件
    SqlUser = args.SqlUser#传入爆破数据库的账号文件
    Proxy=args.Proxy#不需要传入参数如果开启只需要-p
    SubdomainEnumerate=args.SubdomainEnumerate #开启深度子域名枚举，巨TM耗时间
    Subdomain=args.Subdomain#开启子域名枚举
    ThreadNumber=args.ThreadNumber#要使用的线程数默认15
    #WriteFile = ClassCongregation.WriteFile(OutFileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)

    if ThreadNumber==None:#如果线程数为空，那么默认为15
        ThreadNumber=15
    if Url==None and InputFileName==None:#如果找不到URL的话直接退出
        print("Incorrect input, please enter -h to view help")
        os._exit(0)#直接退出整个函数
    elif Url!=None and InputFileName!=None:#如果既输入URL又输入URL文件夹一样退出
        print("Incorrect input, please enter -h to view help")
        os._exit(0)#直接退出整个函数


    ProxyIp=None



    thread_list.append(threading.Thread(target=BoomDB, args=(Url, SqlUser, SqlPasswrod,InputFileName,)))

    if SubdomainEnumerate==True and Subdomain==True :#对参数判断参数互斥
        print("Incorrect input, please enter -h to view help")
    elif SubdomainEnumerate==True:
        SubdomainJudge = "a"
        thread_list.append(threading.Thread(target=SubdomainCrawling, args=(Url,SubdomainJudge,)))
        #加入多线程池这样会流畅点
        #SubdomainCrawling(Url,SubdomainJudge )
    elif Subdomain==True:
        SubdomainJudge = "b"
        thread_list.append(threading.Thread(target=SubdomainCrawling, args=(Url, SubdomainJudge,)))
        #SubdomainCrawling(Url, SubdomainJudge)
    InitialScan(InputFileName, Url, ProxyIp)#最后启动主扫描函数，这样如果多个IP的话优化速度，里面会做url或者url文件的判断
    for t in thread_list:#开启列表中的多线程
        t.setDaemon(True)
        t.start()
        while True:
            # 判断正在运行的线程数量,如果小于5则退出while循环,
            # 进入for循环启动新的进程.否则就一直在while循环进入死循环
            if (len(threading.enumerate()) < ThreadNumber):
                break
    for t in thread_list:#除POC外功能总进度条
        t.join()
    print("Scan is complete, please see the result file")


# from IPy import IP
# ip = IP('192.168.0.0/28')#后面批量生成C段扫描会用到
# print(ip.len())#IP个数有多少
# for x in ip:
#     print(x)

