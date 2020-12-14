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
from Modules.BaoTa import BaoTa
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
from Subdomain import SubdomainSearch
import ClassCongregation
import Banner
import argparse
import os
from config import headers,user_agent_randomization,proxies

parser = argparse.ArgumentParser()#description="xxxxxx")
#UrlGroup = parser.add_mutually_exclusive_group()#定义一个互斥参数组
#UrlGroup .add_argument("-q", "--quiet", action="store_true")#增加到互斥参数组里面去
parser.add_argument('-u','--Url',type=str,help="Target url")
parser.add_argument('-m','--Module',type=str,help="Scan an application individually")
#parser.add_argument('-p','--ProxiesIP',type=str,help="Need to enter a proxy IP")
#parser.add_argument('-a','--Agent',type=str,help="Specify a header file or use a random header")
parser.add_argument('-t','--ProcessNumber',type=int,help="Set the number of process, the default number of process 5.")
parser.add_argument('-f','--InputFileName',type=str,help="Specify bulk scan file batch scan")
#parser.add_argument('-s','--Subdomain',help="Collect subdomains",action="store_true")
parser.add_argument('-PL', '--PortListInformation', type=str, help="The input port format is 22,445,3389")
parser.add_argument('-PR', '--PortRangeInformation', type=str, help="The input port format is 1-65535")

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
"InformationLeakage":InformationLeakage.Main,
"BaoTa":BaoTa.Main
}



def InitialScan(Pool,InputFileName,Module,ActiveScanId,Uid,Headers,Url):
    try:

        if InputFileName==None:
            try:

                print("\033[32m[ + ] Scanning target domain:\033[0m" + "\033[33m {}\033[0m".format(Url))
                GOV = tldextract.extract(Url)
                if GOV.suffix.lower() == "gov.cn":  # 禁止扫描
                    print("\033[31m[ ! ] 扫描你🐎的国家网站呢？\033[0m")
                    os._exit(0)  # 直接退出整个函数
                San(Pool,Module,ActiveScanId,Uid,Headers,Url)
            except Exception as e:
                ClassCongregation.ErrorLog().Write("InitialScan(def)SingleTarget", e)
        elif InputFileName!=None:
            try:
                with open(InputFileName, encoding='utf-8') as f:
                    for UrlLine in f:#设置头文件使用的字符类型和开头的名字
                        try:
                            Url=UrlLine.strip("\r\n")
                            GOV = tldextract.extract(Url)
                            print("\033[32m[ + ] In batch scan, the current target is:\033[0m"+"\033[33m {}\033[0m".format(UrlLine.replace('\n', '')))
                            if GOV.suffix.lower() == "gov.cn":  # 禁止扫描
                                print("\033[31m[ ! ] 扫描你🐎的国家网站呢？\033[0m")
                                os._exit(0)  # 直接退出整个函数
                            San(Pool,Module,ActiveScanId,Uid,Headers,Url)
                        except Exception as e:
                            ClassCongregation.ErrorLog().Write("InitialScan(def)CyclicError", e)
            except Exception as e:
                ClassCongregation.ErrorLog().Write("InitialScan(def)ErrorReadingFile", e)
                print("\033[31m[ ! ] Please check the file path or the file content is correct\033[0m")
    except Exception as e:
        ClassCongregation.ErrorLog().Write("InitialScan(def)functionCallError", e)
        print("\033[31m[ ! ] Please enter the correct file path!\033[0m")


def San(Pool,Module,ActiveScanId,Uid,Headers,Url):
    #POC模块存进多进程池，这样如果批量扫描会变快很多
    #主动扫描在这个位置对URL进行处理
    #如果插件中有需要固定端口的，后面写一个正则替换端口即可
    scheme, url, port = ClassCongregation.UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    Url=scheme + "://" + url + ":" + str(port)#处理后的URL
    if Module==None:
        print("\033[32m[ + ] Scanning across modules:\033[0m" + "\033[35m AllMod             \033[0m")
        for MedusaModule in MedusaModuleList:
            MedusaModuleList[MedusaModule](Pool,ActiveScanId=ActiveScanId,Uid=Uid,Headers=Headers,Url=Url,Proxies=proxies)  # 调用列表里面的值
    else:
        try:
            MedusaModuleList[Module](Pool, ActiveScanId=ActiveScanId,Uid=Uid,Headers=Headers,Url=Url,Proxies=proxies)  # 调用列表里面的值
        except:  # 如果传入非法字符串会调用出错
            print("\033[31m[ ! ] Please enter the correct scan module name\033[0m")
            os._exit(0)  # 直接退出整个函数
    Pool.Start(ProcessNumber)#启动多进程

def Port(**kwargs):
    ClassCongregation.PortScan().Start(**kwargs)

if __name__ == '__main__':
    Banner.RandomBanner()#输出随机横幅
    args = parser.parse_args()
    InputFileName = args.InputFileName#批量扫描文件所在位置
    Url = args.Url
    Module=args.Module#单独模块扫描功能
    #Subdomain=args.Subdomain#开启子域名枚举
    ProcessNumber=args.ProcessNumber#要使用的进程数默认15

    PortListInformation = args.PortListInformation  # 字典类型端口
    PortRangeInformation = args.PortRangeInformation  # 范围型端口
    if ProcessNumber==None:#如果进程数为空，那么默认为5
        ProcessNumber=5

    if Url==None and InputFileName==None:#如果找不到URL的话直接退出
        print("\033[31m[ ! ] Incorrect input, please enter -h to view help\033[0m")
        os._exit(0)#直接退出整个函数
    elif Url!=None and InputFileName!=None:#如果既输入URL又输入URL文件夹一样退出
        print("\033[31m[ ! ] Incorrect input, please enter -h to view help\033[0m")
        os._exit(0)#直接退出整个函数

    ActiveScanId="Soryu Asuka Langley"
    Uid = "Ayanami Rei"

    Pool=ClassCongregation.ProcessPool()#定义一个进程池
    #子域名探测关闭
    # if Subdomain:#如果传入-s启动子域名探测
    #     Pool.Append(SubdomainSearch, Url, AgentHeader, proxies=Proxies,ActiveScanId=ActiveScanId,Uid=Uid)

    ################
    #对端口传入进行判断
    ################
    if PortListInformation == None and PortRangeInformation == None:  # 默认默认扫描端口信息
        print("\033[32m[ + ] Use default port detection module \033[0m")
        Pool.PortAppend(Port,Url=Url,PortInformation="",PortType=3,ActiveScanId=ActiveScanId,Uid=Uid)
    elif PortListInformation != None and PortRangeInformation != None:  # 都不等于空的情况
        print("\033[31m[ ! ] Only one format port can be entered, please use -h to view the help file!\033[0m")
        os._exit(0)  # 直接退出整个函数
    elif PortListInformation == None and PortRangeInformation != None:  # 输入范围型端口
        PortType = 1
        Pool.PortAppend(Port,Url=Url ,PortInformation=PortRangeInformation, PortType=1, ActiveScanId=ActiveScanId, Uid=Uid)
        print("\033[32m[ + ] The scan range is: "+"\033[0m"+"\033[35m"+PortRangeInformation+"\033[0m")
    elif PortListInformation != None and PortRangeInformation == None:  # 输入字典型端口
        PortType = 2
        Pool.PortAppend(Port, Url=Url,PortInformation=PortListInformation, PortType=2, ActiveScanId=ActiveScanId, Uid=Uid)
        print("\033[32m[ + ] The scanned dictionary is"+"\033[0m"+"\033[35m"+ PortListInformation+ "\033[0m")


    if not user_agent_randomization:  # 如果值为Ture
        headers["User-Agent"] = ClassCongregation.AgentHeader().result()  # 传入随机头
    InitialScan(Pool,InputFileName, Module,ActiveScanId,Uid,headers,Url)#最后启动主扫描函数，这样如果多个IP的话优化速度，里面会做url或者url文件的判断
    print("\033[31m[ ! ] Scan is complete, please see the ScanResult file\033[0m")


#Url和proxies写到kwargs中
#Headers写到配置文件中
# from IPy import IP
# ip = IP('192.168.0.0/28')#后面批量生成C段扫描会用到
# print(ip.len())#IP个数有多少
# for x in ip:
#     print(x)

