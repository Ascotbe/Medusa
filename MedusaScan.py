#!/usr/bin/env python
# _*_ coding: utf-8 _*_


#import Weblogic.WeblogicMain
from Confluence import ConfluenceMain
#如果在自己创建的文件夹里面加入__init__.py文件的话就可以是用from 文件夹名 import 文件夹总的文件名来导入文件
#Struts2Main.Main()这样就导入了文件夹中Struts2Main.py文件中的Main函数
from Struts2 import Struts2Main
from Apache import ApacheMian
from Nginx import NginxMain
from InformationDetector import JS
import ClassCongregation
import Banner
import argparse
import requests
import os
import  threading
import sys, time
from tqdm import tqdm

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
parser.add_argument('-j','--JavaScript',type=str,help="Used URL to deeply crawl the information in the JS file and the subdomain",action="store_true")

'''
在pycharm中设置固定要获取的参数，进行获取
在XXX.py 中 按住 “alt+shift+f9”  ----选择编辑配置（edit configurations）---script parameters(脚本程序)
在里面输入参数就可以使用debug调试了
'''


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
def InitialScan(InputFileName,Url,NmapScanRange,ProxyIp):
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
                    for UrlLine in tqdm(f,ascii=True,desc="IP scanning progress:"):#设置头文件使用的字符类型和开头的名字
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

def San(OutFileName,Url,Values,ProxyIp):
    # try:
    #     Weblogic.WeblogicMain.Main(Url)#调用weblogic主函数
    # except:
    #     print("WeblogicSanExcept")
    try:
        Struts2Main.Main(Url,OutFileName,Values,ProxyIp)  # 调用Struts2主函数
    except:
        pass
    try:
        ConfluenceMain.Main(Url,OutFileName,Values,ProxyIp)# 调用 Confluence主函数
    except:
        pass
    try:
        NginxMain.Main(Url,OutFileName,Values,ProxyIp)# 调用 Confluence主函数
    except:
        pass
    try:
        ApacheMian.Main(Url,OutFileName,Values,ProxyIp)  # 调用Apache主函数
    except:
        pass

def OpenProxy():
    global RepeatCleaningAgent
    RepeatCleaningAgent = 1#检查是否是刚爬取的并清洗的IP
    ProxyIpComparison=""
    try:#尝试打开文件查看是否有代理池
        with open("/ScanResult/ProxyPool.txt", encoding='utf-8') as f:
            try:
                FileCreationYime = time.localtime(os.path.getctime("/ScanResult/ProxyPool.txt"))  # 获取文件创建时间
                CurrentTime = time.localtime(time.time())  # 获取当前时间
                if FileCreationYime.tm_year == CurrentTime.tm_year:  # 判断年份是否相同
                    if CurrentTime.tm_mon == FileCreationYime.tm_mon:  # 判断月份是否相同
                        a = FileCreationYime.tm_mday
                        b = CurrentTime.tm_mday
                        c = abs(a - b)  # 计算绝对值
                        if c >= 3:  # 如果大于3天删除
                            f.close()#关闭打开的文件后删除文件
                            os.remove("/ScanResult/ProxyPool.txt")
                    else:
                        f.close()
                        os.remove("/ScanResult/ProxyPool.txt")
                else:
                    f.close()
                    os.remove("/ScanResult/ProxyPool.txt")
            except:
                pass
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
                        return ProxyIps#二次清洗完成的代理IP能用就返回
                except:
                    pass
    except:
        if RepeatCleaningAgent==1:
            HttpProxy=ClassCongregation.Proxy()
            HttpProxy.HttpIpProxy()#如果不存在该文件就调用爬取类
            OpenProxy()#接着调用自身
        else:
            pass
        RepeatCleaningAgent = 0 #定义全局变量防止出问题
        # 如果不是第一次爬取，就会进到这个函数里面，然后爬取清洗后再调用自身后把标签重置为真，这样就不会进入死循环


    # HttpsProxy=Proxy.HttpsIpProxy()
def JSCrawling(Url):
    urls = JS.find_by_url_deep(args.url)
    JS.giveresult(urls, args.url)


if __name__ == '__main__':
    Banner.RandomBanner()#输出随机横幅
    args = parser.parse_args()
    InputFileName = args.InputFileName#批量扫描文件所在位置
    OutFileName= args.OutFileName#输出最终结果文件名字
    Url = args.url
    Values=args.agent#判断是否使用随机头，判断写在Class里面
    NmapScanRange=args.NmapScanRange#传入扫描参数
    SqlPasswrod=args.SqlPasswrod#传入爆破数据库的密码文件
    SqlUser = args.SqlUser#传入爆破数据库的账号文件
    Proxy=args.Proxy#不需要传入参数如果开启只需要-p
    JavaScript=args.JavaScript#开启深度爬取JS文件中的子域名以及链接
    WriteFile = ClassCongregation.WriteFile(OutFileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)

    if Url==None and InputFileName==None:#如果找不到URL的话直接退出
        print("Incorrect input, please enter -h to view help")
        os._exit(0)#直接退出整个函数
    elif Url!=None and InputFileName!=None:#如果既输入URL又输入URL文件夹一样退出
        print("Incorrect input, please enter -h to view help")
        os._exit(0)#直接退出整个函数

    ProxyIp=""
    if Proxy:#如果输入了参数表示开启了代理进而调用函数
        ProxyIp=OpenProxy()

    if JavaScript:
        BootJS=threading.Thread(target=JSCrawling,args=(Url,))
        BootScanner = threading.Thread(target=InitialScan, args=(InputFileName, Url, NmapScanRange, ProxyIp,))
        BootBoomDB = threading.Thread(target=BoomDB, args=(Url, SqlUser, SqlPasswrod, InputFileName,))
        BootJS.start()
        BootScanner.start()
        BootBoomDB.start()
        BootScanner.join()
        BootBoomDB.join()
        BootJS.join()
    else:
        # InitialScan(InputFileName, Url, NmapScanRange)#初始化san主函数
        # BoomDB(Url, SqlUser, SqlPasswrod,InputFileName)#调用爆破数据库函数
        BootScanner=threading.Thread(target=InitialScan,args=(InputFileName, Url, NmapScanRange,ProxyIp,))
        BootBoomDB=threading.Thread(target=BoomDB, args=(Url, SqlUser, SqlPasswrod,InputFileName,))
        BootScanner.start()
        BootBoomDB.start()
        BootScanner.join()
        BootBoomDB.join()


# from IPy import IP
# ip = IP('192.168.0.0/28')#后面批量生成C段扫描会用到
# print(ip.len())#IP个数有多少
# for x in ip:
#     print(x)

