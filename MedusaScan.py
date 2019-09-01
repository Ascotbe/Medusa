#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from optparse import OptionParser
#import Weblogic.WeblogicMain
import Confluence.ConfluenceMain
import Struts2.Struts2Main
import Nginx.NginxMain
import time
import ClassCongregation
import nmap
import Banner

parser = OptionParser()
'''
第一个参数表示option的缩写，以单个中划线引导，例如-f、-d，只能用单个字母，可以使用大写;
第二个参数表示option的全拼，以两个中划线引导，例如--file、--Opencv_version;
第一第二个参数可以单独使用，也可以同时使用，但必须保证有其中一个;
从第三个参数开始是命名参数，是可选参数，常用的几个：
type=: 表示输入命令行参数的值的类型，默认为string，可以指定为string, int, choice, float，complex其中一种;
default=: 表示命令参数的默认值；
metavar=: 显示到帮助文档中用来提示用户输入期望的命令参数；
dest=：指定参数在options对象中成员的名称，如果没有指定dest参数，将用命令行参数名来对options对象的值进行存取。
help=:  显示在帮助文档中的信息;
'''
parser.add_option('-o','--out',type=str,help='The file where the url is located,If you do not enter the location, the default is written to the root directory.',dest='OutFileName')
parser.add_option('-u','--url',type=str,help="Target url",dest='url')
parser.add_option('-a','--agent',type=str,help="Specify a header file or use a random header",dest='agent')
parser.add_option('-f','--file',type=str,help="Specify bulk scan file batch scan",dest='InputFileName')
parser.add_option('-n','--nmap',type=str,help="Incoming scan port range (1-65535), use this command to enable nmap scan function by default.",dest='NmapScanRange')



#Port=options.port

def San(OutFileName,Url,Values):
    # try:
    #     Weblogic.WeblogicMain.Main(Url)#调用weblogic主函数
    # except:
    #     print("WeblogicSanExcept")
    try:
        Struts2.Struts2Main.Main(Url,OutFileName,Values)  # 调用Struts2主函数
    except:
        print("Struts2SanExcept")
    try:
        Confluence.ConfluenceMain.Main(Url,OutFileName,Values)# 调用 Confluence主函数
    except:
        print("ConfluenceExcept")
    try:
        Nginx.NginxMain.Main(Url,OutFileName,Values)# 调用 Confluence主函数
    except:
        print("NginxExcept")

if __name__ == '__main__':
    print(Banner.RandomBanner())#输出随机横幅
    (options, args) = parser.parse_args()  # options里面存了所有的dest中的值
    InputFileName = options.InputFileName#批量扫描文件所在位置
    OutFileName= options.OutFileName#输出最终结果文件名字
    Url = options.url
    Values=options.agent#判断是否使用随机头，判断写在Class里面
    NmapScanRange=options.NmapScanRange#传入扫描参数

    WriteFile = ClassCongregation.WriteFile(OutFileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)

    try:
        if InputFileName==None:
            Urls=Url
            if NmapScanRange != None:
                NmapScan = ClassCongregation.NmapScan(Url, NmapScanRange)  # 声明调用类集合中的NmapScan类，并传入Url和扫描范围
                NmapScan.ScanPort()
            try:
                San(OutFileName, Urls, Values)
                # 最后该类扫描结束输出结果语句
                SanOver = Urls + "  Scan completed"
                WriteFile.Write(SanOver)
                print("Scan is complete, please see the result file")
            except KeyboardInterrupt as e:
                exit(0)
        elif InputFileName!=None:
            with open(InputFileName, encoding='utf-8') as f:
                for UrlLine in f:
                    Urls=UrlLine
                    if NmapScanRange != None:
                        NmapScan = ClassCongregation.NmapScan(Url, NmapScanRange)  # 声明调用类集合中的NmapScan类，并传入Url和扫描范围
                        NmapScan.ScanPort()
                    try:
                        San(OutFileName, Urls, Values)
                        # 最后该类扫描结束输出结果语句
                        SanOver = Urls + "  Scan completed"
                        WriteFile.Write(SanOver)
                        print("Scan is complete, please see the result file")
                    except KeyboardInterrupt as e:
                        exit(0)
    except:
        print("Please enter the correct file path!")

# from IPy import IP
# ip = IP('192.168.0.0/28')#后面批量生成C段扫描会用到
# print(ip.len())#IP个数有多少
# for x in ip:
#     print(x)

