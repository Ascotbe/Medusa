#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Confluence import Confluence
from Modules.Struts2 import Struts2
from Modules.Nginx import Nginx
from Modules.Jenkins import Jenkins
from Modules.Cms import Cms
from Modules.FastJson import FastJson
from Modules.Harbor import Harbor
from Modules.Citrix import Citrix
from Modules.InformationLeakage import InformationLeakage
from Modules.Rails import Rails
from Modules.Kibana import Kibana
from Modules.PHPStudy import PHPStudy
from Modules.Mongo import Mongo
from Modules.Dubbo import Dubbo
from Modules.Liferay import Liferay
from Modules.Weblogic import Weblogic
from Modules.OA.Seeyou import Seeyou
from Modules.OA.Tongda import Tongda
from Modules.OA.Weaver import Weaver
from Modules.OA.Ruvar import Ruvar
from Modules.Windows import Windows
from Modules.Spring import Spring
from Modules.Apache.Shiro import Shiro
from Modules.Apache.Flink import Flink
from Modules.Apache.Log4j import Log4j
from Modules.Apache.ActiveMQ import ActiveMQ
from Modules.Apache.Solr import Solr
from Modules.BIG_IP import BIG_IP
from Modules.Apache.Tomcat import Tomcat
import tldextract
from Modules.Subdomain.SubdomainSearch import SubdomainSearch
from Exploit.Exploit import main#命令执行函数
import ClassCongregation
import Banner
import argparse
import os

parser = argparse.ArgumentParser()#description="xxxxxx")
#UrlGroup = parser.add_mutually_exclusive_group()#定义一个互斥参数组
#UrlGroup .add_argument("-q", "--quiet", action="store_true")#增加到互斥参数组里面去
parser.add_argument('-u','--Url',type=str,help="Target url")
parser.add_argument('-m','--Module',type=str,help="Scan an application individually")
parser.add_argument('-p','--ProxiesIP',type=str,help="Need to enter a proxy IP")
parser.add_argument('-a','--Agent',type=str,help="Specify a header file or use a random header")
parser.add_argument('-t','--ProcessNumber',type=int,help="Set the number of process, the default number of process 5.")
parser.add_argument('-f','--InputFileName',type=str,help="Specify bulk scan file batch scan")
parser.add_argument('-s','--Subdomain',help="Collect subdomains",action="store_true")
parser.add_argument('-l','--List',help="List interactive command execution plugins",action="store_true")
parser.add_argument('-e','--Exploit',help="You need to use the vulnerability, please use -l to query",type=str)
parser.add_argument('-d','--Deserialization',help="Use deserialization to execute commands",type=str)

'''
在pycharm中设置固定要获取的参数，进行获取
在XXX.py 中 按住 “alt+shift+f9”  ----选择编辑配置（edit configurations）---script parameters(脚本程序)
在里面输入参数就可以使用debug调试了
'''
#漏洞各个插件的主函数
MedusaModuleList={
"Struts2":Struts2.Main,
"Confluence":Confluence.Main,
"Nginx":Nginx.Main,
"PHPStudy": PHPStudy.Main,
"Cms": Cms.Main,
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
"Shiro":Shiro.Main,
"Flink":Flink.Main,
"Log4j":Log4j.Main,
"ActiveMQ":ActiveMQ.Main,
"Solr":Solr.Main,
"Tomcat":Tomcat.Main,
"Ruvar":Ruvar.Main,
"Seeyou":Seeyou.Main,
"Tongda":Tongda.Main,
"Weaver":Weaver.Main,
"Weblogic":Weblogic.Main,
"Dubbo":Dubbo.Main,
"BIG-IP":BIG_IP.Main,
"InformationLeakage":InformationLeakage.Main
}


def NmapScan(url):#Nmap扫描这样就可以开多线程了
    ClassCongregation.NmapScan(url).ScanPort()#调用Nmap扫描类

def InitialScan(Pool,InputFileName,Url,Module,AgentHeader,Proxies,**kwargs):
    try:
        if InputFileName==None:
            try:
                print("\033[32m[ + ] Scanning target domain:\033[0m" + "\033[33m {}\033[0m".format(Url))
                GOV = tldextract.extract(Url)
                if GOV.suffix.lower() == "gov.cn":  # 禁止扫描
                    print("\033[31m[ ! ] 扫描你🐎的国家网站呢？\033[0m")
                    os._exit(0)  # 直接退出整个函数
                San(Pool,Url,AgentHeader,Module,Proxies,**kwargs)
            except Exception as e:
                ClassCongregation.ErrorLog().Write("InitialScan(def)SingleTarget", e)
        elif InputFileName!=None:
            try:
                with open(InputFileName, encoding='utf-8') as f:
                    for UrlLine in f:#设置头文件使用的字符类型和开头的名字
                        try:
                            Url=UrlLine.strip("\r\n")
                            print("\033[32m[ + ] In batch scan, the current target is:\033[0m"+"\033[33m {}\033[0m".format(UrlLine.replace('\n', '')))
                            GOV = tldextract.extract(Url)
                            if GOV.suffix.lower() == "gov.cn":  # 禁止扫描
                                print("\033[31m[ ! ] 扫描你🐎的国家网站呢？\033[0m")
                                os._exit(0)  # 直接退出整个函数
                            San(Pool,Url,AgentHeader,Module,Proxies,**kwargs)
                        except Exception as e:
                            ClassCongregation.ErrorLog().Write("InitialScan(def)CyclicError", e)
            except Exception as e:
                ClassCongregation.ErrorLog().Write("InitialScan(def)ErrorReadingFile", e)
                print("\033[31m[ ! ] Please check the file path or the file content is correct\033[0m")
    except Exception as e:
        ClassCongregation.ErrorLog().Write("InitialScan(def)functionCallError", e)
        print("\033[31m[ ! ] Please enter the correct file path!\033[0m")


def San(Pool,Url,AgentHeader,Module,Proxies,**kwargs):
    #POC模块存进多进程池，这样如果批量扫描会变快很多
    if Module==None:
        print("\033[32m[ + ] Scanning across modules:\033[0m" + "\033[35m AllMod             \033[0m")
        for MedusaModule in MedusaModuleList:
            MedusaModuleList[MedusaModule](Pool, Url, AgentHeader, Proxies,**kwargs)  # 调用列表里面的值
    else:
        try:
            MedusaModuleList[Module](Pool, Url, AgentHeader,Proxies,**kwargs)  # 调用列表里面的值
        except:  # 如果传入非法字符串会调用出错
            print("\033[31m[ ! ] Please enter the correct scan module name\033[0m")
            os._exit(0)  # 直接退出整个函数
    Pool.Start(ProcessNumber)#启动多进程


if __name__ == '__main__':
    Banner.RandomBanner()#输出随机横幅
    args = parser.parse_args()
    InputFileName = args.InputFileName#批量扫描文件所在位置
    Url = args.Url
    AgentHeader=args.Agent#判断是否使用随机头，判断写在Class里面
    Module=args.Module#单独模块扫描功能
    Subdomain=args.Subdomain#开启子域名枚举
    ProcessNumber=args.ProcessNumber#要使用的进程数默认15
    Proxies= args.ProxiesIP#代理的IP
    ExploitList = args.List  # 列出所有可以交互使用的poc
    Exploit = args.Exploit  # 利用那个可以交互的poc
    Deserialization=args.Deserialization#获取反序列化插件

    if ProcessNumber==None:#如果线程数为空，那么默认为5
        ProcessNumber=5

    if Url==None and InputFileName==None:#如果找不到URL的话直接退出
        print("\033[31m[ ! ] Incorrect input, please enter -h to view help\033[0m")
        os._exit(0)#直接退出整个函数
    elif Url!=None and InputFileName!=None:#如果既输入URL又输入URL文件夹一样退出
        print("\033[31m[ ! ] Incorrect input, please enter -h to view help\033[0m")
        os._exit(0)#直接退出整个函数

    #暂时关闭NMAPScan和数据库爆破功能
    Sid="Soryu Asuka Langley"
    Uid = "Ayanami Rei"
    if ExploitList==True:
        pass#调用列表函数，暂定未写
        os._exit(0)  # 直接退出整个函数
    if Exploit!=None and Deserialization!=None:
        print("\033[31m[ ! ] Please do not use -e and -d parameters at the same time\033[0m")
        os._exit(0)  # 直接退出整个函数
    elif Exploit!=None or Deserialization!=None:
        main(Exploit=Exploit,Deserialization=Deserialization,Url=Url,AgentHeader=AgentHeader,Proxies=Proxies,Sid=Sid,Uid=Uid) #启动子进程永真方式调用exp

    Pool=ClassCongregation.ProcessPool()#定义一个进程池
    #ThreadPool = ClassCongregation.ThreadPool()#定义一个线程池

    if Subdomain:#如果传入-s启动子域名探测
        Pool.Append(SubdomainSearch, Url, AgentHeader, proxies=Proxies,Sid=Sid,Uid=Uid)

    InitialScan(Pool,InputFileName, Url,Module,AgentHeader,Proxies,Sid=Sid,Uid=Uid)#最后启动主扫描函数，这样如果多个IP的话优化速度，里面会做url或者url文件的判断
    print("\033[31m[ ! ] Scan is complete, please see the ScanResult file\033[0m")



# from IPy import IP
# ip = IP('192.168.0.0/28')#后面批量生成C段扫描会用到
# print(ip.len())#IP个数有多少
# for x in ip:
#     print(x)

