#!/usr/bin/env python
# _*_ coding: utf-8 _*_


#import Weblogic.WeblogicMain
import Confluence.ConfluenceMain
import Struts2.Struts2Main
import Nginx.NginxMain
import ClassCongregation
import Banner
import argparse
import requests
import os
parser = argparse.ArgumentParser()#description="xxxxxx")
##########################################################################################################################################################################
#舍弃的 OptionParser模块
#from optparse import OptionParser
#parser = OptionParser()
# parser.add_option('-o','--out',type=str,help='The file where the url is located,If you do not enter the location, the default is written to the root directory.',dest='OutFileName')
# parser.add_option('-u','--url',type=str,help="Target url",dest='url')
# parser.add_option('-a','--agent',type=str,help="Specify a header file or use a random header",dest='agent')
# parser.add_option('-f','--file',type=str,help="Specify bulk scan file batch scan",dest='InputFileName')
# parser.add_option('-n','--nmap',type=str,help="Incoming scan port range (1-65535), use this command to enable nmap scan function by default.",dest='NmapScanRange')
# parser.add_option('-sp','--sqlpass',type=str,help="Please enter an password file.",dest='SqlPasswrod')
# parser.add_option('-su','--sqluser',type=str,help="Please enter an account file.",dest='SqlUser')
##########################################################################################################################################################################
UrlGroup = parser.add_mutually_exclusive_group()#定义一个互斥参数组
#UrlGroup .add_argument("-q", "--quiet", action="store_true")#增加到互斥参数组里面去
parser.add_argument('-o','--OutFileName',type=str,help='The file where the url is located,If you do not enter the location, the default is written to the root directory.')
parser.add_argument('-u','--url',type=str,help="Target url")
parser.add_argument('-p','--Proxy',help="Whether to enable the global proxy function",action="store_true")
parser.add_argument('-a','--agent',type=str,help="Specify a header file or use a random header")
parser.add_argument('-f','--InputFileName',type=str,help="Specify bulk scan file batch scan")
parser.add_argument('-n','--NmapScanRange',type=str,help="Incoming scan port range (1-65535), use this command to enable nmap scan function by default.")
parser.add_argument('-sp','--SqlPasswrod',type=str,help="Please enter an password file.")
parser.add_argument('-su','--SqlUser',type=str,help="Please enter an account file.")




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

def San(OutFileName,Url,Values,ProxyIp):
    # try:
    #     Weblogic.WeblogicMain.Main(Url)#调用weblogic主函数
    # except:
    #     print("WeblogicSanExcept")
    try:
        Struts2.Struts2Main.Main(Url,OutFileName,Values,ProxyIp)  # 调用Struts2主函数
    except:
        print("Struts2SanExcept")
    try:
        Confluence.ConfluenceMain.Main(Url,OutFileName,Values,ProxyIp)# 调用 Confluence主函数
    except:
        print("ConfluenceExcept")
    try:
        Nginx.NginxMain.Main(Url,OutFileName,Values,ProxyIp)# 调用 Confluence主函数
    except:
        print("NginxExcept")

def OpenProxy():
    ProxyFlag=True#设置函数内的标志
    ProxyIpComparison=""
    try:#尝试打开文件查看是否有代理池
        with open("ProxyPool.txt", encoding='utf-8') as f:
            while ProxyFlag:#判断是否进行运行
                for ProxyPool in f:#读取代理IP进行测试是否可以使用

                    ProxyIps=ProxyPool[:-1]#删除换行符号\n
                    if ProxyIps==ProxyIpComparison:#对当前IP和上个IP进行对比如果相同代表爬取的IP全部不能用就直接跳出不在使用代理
                        return
                    ProxyIpComparison = ProxyPool[:-1]
                    proxies = {
                        #"http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                        "http":"http://" + str(ProxyIps)
                    }
                    try:
                        if requests.get('https://www.baidu.com/', proxies=proxies, timeout=2).status_code == 200:
                            ProxyFlag=False#如果代理能用就重置标志
                            return ProxyIps#二次清洗完成的代理IP能用就返回
                    except:
                        pass
    except:
        HttpProxy=ClassCongregation.Proxy()
        HttpProxy.HttpIpProxy()#如果不存在该文件就调用爬取类
        OpenProxy()#接着调用自身

    # HttpsProxy=Proxy.HttpsIpProxy()



if __name__ == '__main__':
    print(Banner.RandomBanner())#输出随机横幅
    args = parser.parse_args()
    InputFileName = args.InputFileName#批量扫描文件所在位置
    OutFileName= args.OutFileName#输出最终结果文件名字
    Url = args.url
    Values=args.agent#判断是否使用随机头，判断写在Class里面
    NmapScanRange=args.NmapScanRange#传入扫描参数
    SqlPasswrod=args.SqlPasswrod#传入爆破数据库的密码文件
    SqlUser = args.SqlUser#传入爆破数据库的账号文件
    Proxy=args.Proxy#不需要传入参数如果开启只需要-p
    WriteFile = ClassCongregation.WriteFile(OutFileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)

    if Url==None and InputFileName==None:#如果找不到URL的话直接退出
        print("Incorrect input, please enter -h to view help")
        os._exit(0)#直接退出整个函数
    elif Url!=None and InputFileName!=None:#如果既输入URL又输入URL文件夹一样退出
        print("Incorrect input, please enter -h to view help")
        os._exit(0)#直接退出整个函数

    ProxyIp=None#声明全局变量的ProxyIp值
    if Proxy:#如果输入了参数表示开启了代理进而调用函数
        ProxyIp=OpenProxy()
        while ProxyIp==None:
            OpenProxy()#如果传入空值


    try:
        if InputFileName==None:
            Urls=Url
            if NmapScanRange != None:
                NmapScan = ClassCongregation.NmapScan(Url, NmapScanRange)  # 声明调用类集合中的NmapScan类，并传入Url和扫描范围
                NmapScan.ScanPort()
            try:
                San(OutFileName, Urls, Values,ProxyIp)
                # 最后该类扫描结束输出结果语句
                SanOver = Urls + "  Scan completed"
                WriteFile.Write(SanOver)
                print("Scan is complete, please see the result file")
            except KeyboardInterrupt as e:
                exit(0)
        elif InputFileName!=None:
            try:
                with open(InputFileName, encoding='utf-8') as f:
                    for UrlLine in f:
                        Urls=UrlLine
                        if NmapScanRange != None:
                            NmapScan = ClassCongregation.NmapScan(Url, NmapScanRange)  # 声明调用类集合中的NmapScan类，并传入Url和扫描范围
                            NmapScan.ScanPort()
                        try:
                            San(OutFileName, Urls, Values,ProxyIp)
                            # 最后该类扫描结束输出结果语句
                            SanOver = Urls + "  Scan completed"
                            WriteFile.Write(SanOver)
                            print("Scan is complete, please see the result file")
                        except KeyboardInterrupt as e:
                            exit(0)
            except:
                print("Please check the file path or the file content is correct")
    except:
        print("Please enter the correct file path!")


    BoomDB(Url, SqlUser, SqlPasswrod,InputFileName)#调用爆破数据库函数




# from IPy import IP
# ip = IP('192.168.0.0/28')#后面批量生成C段扫描会用到
# print(ip.len())#IP个数有多少
# for x in ip:
#     print(x)

