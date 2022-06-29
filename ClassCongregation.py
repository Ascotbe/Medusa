#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import urllib.parse
import sqlite3
import logging
import os
import re
import base64
import random
import sys
import time
from typing import List, Tuple
import subprocess
import hashlib
from Crypto.Cipher import AES
import ast
############################################
#这里面的关于数据库的表都是没用的后续会慢慢移除重写#
############################################
def IpProcess(Url: str) -> str:
    if Url.startswith("http"):  # 记个小知识点：必须带上https://这个头不然urlparse就不能正确提取hostname导致后面运行出差错
        res = urllib.parse.urlparse(Url)  # 小知识点2：如果只导入import urllib包使用parse这个类的话会报错，必须在import requests导入这个包才能正常运行
    else:
        res = urllib.parse.urlparse('http://%s' % Url)
    return (res.hostname)




class Proxies:  # 代理处理函数
    def result(self, proxies_ip: str or None):
        try:
            if proxies_ip == None:
                return proxies_ip
            else:
                return {"http": "http://{}".format(proxies_ip), "https": "https://{}".format(proxies_ip)}
        except Exception as e:
            ErrorLog().Write("ClassCongregation_Proxies(class)_result(def)", e)
            return None#报错就返回空




class GetDatabaseFilePath:  # 主数据库文件路径返回值
    def result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            DatabaseFilePath = GetRootFileLocation().Result() + "\\Medusa.db"
            return DatabaseFilePath
        elif sys.platform == "linux" or sys.platform == "darwin":
            DatabaseFilePath = GetRootFileLocation().Result() + "/Medusa.db"
            return DatabaseFilePath

#
# class PortScan:  # 扫描端口类
#     def __init__(self):
#         try:
#
#             self.CustomizePortList =[] # 用户输入处理后的列表
#             self.DefaultPortList = [20, 21, 22, 23, 53,80, 161, 389, 443, 873, 1025, 1099, 2222, 2601, 2604, 3312, 3311, 4440, 5900, 5901,
#                        5902, 7002, 9000, 9200, 10000, 50000, 50060, 50030, 8080, 139, 445, 3389, 13389, 7001, 1521, 3306,
#                        1433, 5000, 5432, 27017, 6379, 11211]  # 常用端口扫描列表
#             self.OpenPorts=[]
#         except Exception as e:
#             ErrorLog().Write("ClassCongregation_PortScan(class)___init__(def)", e)
#
#
#     def PortTest(self,**kwargs):
#         port = int(kwargs.get("port"))
#
#         try:
#             sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             sk.connect((self.Ip, port))
#             sk.settimeout(port_timeout_period)
#             sk.close()
#             self.OpenPorts.append(str(port))  # 传入列表中
#             #成功直接调用写入端口函数
#
#         except Exception as e:
#             pass
#     def Start(self,**kwargs):
#         #传入端口列表，主函数中写入
#         PortInformation = kwargs.get("PortInformation")
#         PortType = kwargs.get("PortType")
#         Uid=kwargs.get("Uid")
#         Url = kwargs.get("Url")
#         self.Host = IpProcess(Url)  # 调用IP处理函数,获取URL或者IP
#         self.Ip = socket.gethostbyname(self.Host)  # 如果是URL会进行二次处理获取到IP
#         ActiveScanId=kwargs.get("ActiveScanId")
#         self.PortHandling(PortInformation,PortType)
#         try:
#             Pool = ThreadPool()
#             for Port in self.CustomizePortList:
#                 Pool.Append(self.PortTest, port=Port)
#
#             Pool.Start(port_threads_number)  # 启动线程池
#             #print(self.OpenPorts)
#             #调用写入数据库函数和调用写入文件函数
#             CreationTime=str(int(time.time()))
#             for i in self.OpenPorts:#循环写入到数据库中
#                 PortDB(uid=Uid,active_scan_id=ActiveScanId,ip=self.Ip,domain=self.Host,creation_time=CreationTime,port=i).Write()#写到数据库中
#         except Exception as e:
#             ErrorLog().Write("ClassCongregation_PortScan(class)_Start(def)", e)
#
#
#     def PortHandling(self,PortInformation,PortType):  # 进行正则匹配处理
#         try:
#             Pattern = re.compile(r'\d*')  # 查找数字
#             RegularResult = Pattern.findall(PortInformation)
#             if PortType == 1:  # 处理为范围类型数据
#                 ExtractContent = []  # 剔除空字节内容和超过最大端口数据
#                 for i in RegularResult:
#                     if i != "" and int(i) <= 65535:
#                         ExtractContent.append(i)
#                 PortStart = int(ExtractContent[0])  # 起始端口
#                 PortEnd = int(ExtractContent[1])  # 起始端口
#                 if PortEnd < PortStart:  # 如果用户输入错误为大的在前面小的在后面的话
#                     tmp = PortEnd
#                     PortEnd = PortStart
#                     PortStart = tmp
#                 for Port in range(PortStart, PortEnd + 1):
#                     self.CustomizePortList.append(Port)
#             if PortType == 2:  # 处理为字典类型数据
#                 for Port in RegularResult:
#                     if Port != "" and int(Port) <= 65535:
#                         self.CustomizePortList.append(Port)
#             if PortType == 3:  # 使用默认字典
#                 self.CustomizePortList=self.DefaultPortList
#         except Exception as e:
#             self.CustomizePortList = self.DefaultPortList#如果报错直接使用默认端口进行扫描
#             ErrorLog().Write("ClassCongregation_PortScan(class)_PortHandling(def)", e)
#
#
#
#
# class PortDB:  # 端口数据表
#     def __init__(self,**kwargs):
#         self.uid = kwargs.get("uid") # 用户UID
#         self.active_scan_id = kwargs.get("active_scan_id")  # 扫描active_scan_id
#         self.port = kwargs.get("port")  # 开放端口
#         self.ip = kwargs.get("ip")  # 目标IP
#         self.domain = kwargs.get("domain") # 目标域名
#         self.creation_time=kwargs.get("creation_time") # 创建时间
#         # 如果数据库不存在的话，将会自动创建一个 数据库
#         self.con = sqlite3.connect(GetDatabaseFilePath().result())
#         # 获取所创建数据的游标
#         self.cur = self.con.cursor()
#         # 创建表
#         try:
#             self.cur.execute("CREATE TABLE PortInfo\
#                             (port_info_id INTEGER PRIMARY KEY,\
#                             uid TEXT NOT NULL,\
#                             active_scan_id TEXT NOT NULL,\
#                             port TEXT NOT NULL,\
#                             ip TEXT NOT NULL,\
#                             domain TEXT NOT NULL,\
#                             creation_time TEXT NOT NULL)")
#         except Exception as e:
#             ErrorLog().Write("ClassCongregation_PortDB(class)_init(def)", e)
#
#     def Write(self):
#         try:
#             self.cur.execute(
#                 """INSERT INTO PortInfo (uid,active_scan_id,port,ip,domain,creation_time) VALUES (?,?,?,?,?,?)""",
#                 (self.uid, self.active_scan_id,self.port, self.ip, self.domain, self.creation_time,))
#             # 提交
#             self.con.commit()
#             self.con.close()
#         except Exception as e:
#             ErrorLog().Write("ClassCongregation_PortDB(class)_Write(def)", e)
#
#     def Query(self, **kwargs):
#             Uid = kwargs.get("uid")
#             ActiveScanId = kwargs.get("active_scan_id")
#             try:
#                 self.cur.execute("select * from PortInfo where active_scan_id =? and uid=?", (ActiveScanId, Uid,))
#                 result_list = []  # 存放json的返回结果列表用
#                 for i in self.cur.fetchall():
#                     JsonValues = {}
#                     # JsonValues["active_scan_id"] = i[2]
#                     JsonValues["port"] = i[3]
#                     JsonValues["ip"] = i[4]
#                     JsonValues["domain"] = i[5]
#                     JsonValues["creation_time"] = i[6]
#                     result_list.append(JsonValues)
#                 self.con.close()
#                 return result_list
#             except Exception as e:
#                 ErrorLog().Write("Web_WebClassCongregation_ReportGenerationList(class)_QueryTokenValidity(def)", e)
#                 return None




class VulnerabilityDetails:  # 所有数据库写入都是用同一个类
    def __init__(self, medusa,request, **kwargs):
        try:
            self.url = str(kwargs.get("Url"))  # 目标域名，如果是代理扫描会有完整的路径
            self.timestamp = str(int(time.time()))  # 获取时间戳
            self.name = medusa['name']  # 漏洞名称
            self.number = medusa['number']  # CVE编号
            self.author = medusa['author']  # 插件作者
            self.create_date = medusa['create_date']  # 插件创建时间
            self.algroup = medusa['algroup']  # 插件名称
            self.rank = medusa['rank']  # 漏洞等级
            self.disclosure = medusa['disclosure']  # 漏洞披露时间，如果不知道就写编写插件的时间
            self.details = base64.b64encode(medusa['details'].encode(encoding="utf-8")).decode('utf-8')  # 对结果进行编码写入数据库，鬼知道数据里面有什么玩意
            self.affects = medusa['affects']  # 漏洞组件
            self.desc_content = medusa['desc_content']  # 漏洞描述
            self.suggest = medusa['suggest']  # 修复建议
            self.version = medusa['version']  # 漏洞影响的版本
            self.uid = kwargs.get("Uid")  # 传入的用户ID
            self.active_scan_id = kwargs.get("ActiveScanId")  # 传入的父表SID
            try:
                self.response_headers=base64.b64encode(str(request.headers).encode(encoding="utf-8")).decode(encoding="utf-8") # 响应头base64加密后数据
                self.response_text=base64.b64encode(str(request.text).encode(encoding="utf-8")).decode(encoding="utf-8")  # 响应返回数据包
                self.response_byte=base64.b64encode(request.content).decode(encoding="utf-8")#响应返回byte类型数据包
                self.response_status_code=str(request.status_code) # 响应状态码
                self.request_path_url=str(request.request.path_url)  # 请求路径
                self.request_body=base64.b64encode(str(request.request.body).encode(encoding="utf-8")).decode(encoding="utf-8")  # 请求的POST请求数据
                self.request_method=str(request.request.method)  # 请求方式
                self.request_headers=base64.b64encode(str(request.request.headers).encode(encoding="utf-8")).decode(encoding="utf-8")  # 请求头
            except:
                #如果报错就爆数据全部置空
                self.response_headers = ""
                self.response_text = ""
                self.response_byte = ""
                self.response_status_code = ""
                self.request_path_url = ""
                self.request_body = ""
                self.request_method = ""
                self.request_headers = ""

            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(GetDatabaseFilePath().result())
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表
            try:
                # 如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
                self.cur.execute("CREATE TABLE Medusa\
                            (scan_info_id INTEGER PRIMARY KEY,\
                            url TEXT NOT NULL,\
                            name TEXT NOT NULL,\
                            affects TEXT NOT NULL,\
                            rank TEXT NOT NULL,\
                            suggest TEXT NOT NULL,\
                            desc_content TEXT NOT NULL,\
                            details TEXT NOT NULL,\
                            number TEXT NOT NULL,\
                            author TEXT NOT NULL,\
                            create_date TEXT NOT NULL,\
                            disclosure TEXT NOT NULL,\
                            algroup TEXT NOT NULL,\
                            version TEXT NOT NULL,\
                            timestamp TEXT NOT NULL,\
                            active_scan_id TEXT NOT NULL,\
                            uid TEXT NOT NULL,\
                            response_headers TEXT NOT NULL,\
                            response_text TEXT NOT NULL,\
                            response_byte TEXT NOT NULL,\
                            response_status_code TEXT NOT NULL,\
                            request_path_url TEXT NOT NULL,\
                            request_body TEXT NOT NULL,\
                            request_method TEXT NOT NULL,\
                            request_headers TEXT NOT NULL)")
            except Exception as e:
                ErrorLog().Write("ClassCongregation_VulnerabilityDetails(class)_init(def)_CREATETABLE", e)
        except Exception as e:
            ErrorLog().Write("ClassCongregation_VulnerabilityDetails(class)_init(def)", e)

    def Write(self):  # 统一写入
        try:
            self.cur.execute("""INSERT INTO Medusa (url,name,affects,rank,suggest,desc_content,details,number,author,create_date,disclosure,algroup,version,timestamp,active_scan_id,uid,response_headers,response_text,response_byte,response_status_code,request_path_url,request_body,request_method,request_headers) \
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
                self.url, self.name, self.affects, self.rank, self.suggest, self.desc_content, self.details,
                self.number,
                self.author, self.create_date, self.disclosure, self.algroup, self.version, self.timestamp,
                self.active_scan_id,self.uid,self.response_headers,self.response_text,self.response_byte,self.response_status_code,self.request_path_url,self.request_body,self.request_method,self.request_headers,))
            # 提交
            GetSsid = self.cur.lastrowid
            self.con.commit()
            self.con.close()
            ScanInformation().Write(scan_info_id=GetSsid,url=self.url,active_scan_id=self.active_scan_id,rank=self.rank,uid=self.uid,name=self.name)#调用web版数据表，写入ScanInformation关系表
        except Exception as e:
            ErrorLog().Write("ClassCongregation_VulnerabilityDetails(class)_Write(def)", e)

class ErrorLog:  # 报错写入日志
    def __init__(self):
        global filename
        LogDate=time.strftime("%Y-%m-%d", time.localtime())
        if sys.platform == "win32" or sys.platform == "cygwin":
            filename = os.path.split(os.path.realpath(__file__))[0] + '\\Log\\'+LogDate+'.log'  # 获取当前文件所在的目录，即父目录
        elif sys.platform == "linux" or sys.platform == "darwin":
            filename = os.path.split(os.path.realpath(__file__))[0] + '/Log/'+LogDate+'.log'  # 获取当前文件所在的目录，即父目录


    def Write(self, Name, ErrorInfo):
        log_format = '%(asctime)s - %(processName)s[%(process)d] - %(levelname)s: %(message)s'
        logging.basicConfig(filename=filename, filemode='a', level=logging.INFO,
                            format=log_format)  # 初始化配置信息
        logging.info(Name)
        logging.warning(ErrorInfo)
        logging.shutdown()#通过刷新和关闭所有处理程序来通知日志记录系统执行有序的关闭。


# class Dnslog:  # Dnslog判断
#     def __init__(self):
#         #该网站是通过PHPSESSID来判断dns归属谁的所有可以随机一个这个
#         h = "abcdefghijklmnopqrstuvwxyz0123456789"
#         salt_cookie = ""
#         for i in range(26):
#             salt_cookie += random.choice(h)
#         self.headers = {
#             "Cookie": "PHPSESSID="+salt_cookie
#         }
#         H = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
#         salt = ""
#         for i in range(15):
#             salt += random.choice(H)
#         try:
#             self.host = str(salt + "." + self.get_dnslog_url())
#         except Exception as e:
#             print("\033[31m[ ! ] Unable to get dnslog, please replace ceye! \033[0m")
#             self.host=""
#             ErrorLog().Write("ClassCongregation_Dnslog(class)_init_(def)", e)
#
#     def dns_host(self) -> str:
#         return str(self.host)
#
#     def get_dnslog_url(self):
#         if dnslog_name=="dnslog.cn":
#             try:
#                 self.dnslog_cn=requests.get("http://www.dnslog.cn/getdomain.php",headers=self.headers,timeout=6).text
#                 return self.dnslog_cn
#             except Exception as e:
#                 ErrorLog().Write("ClassCongregation_Dnslog(class)_get_dns_log_url(def)", e)
#
#     def result(self) -> bool:
#         # DNS判断后续会有更多的DNS判断，保持准确性
#         if dnslog_name=="dnslog.cn":
#             return self.dnslog_cn_dns()
#
#
#
#     def dnslog_cn_dns(self) -> bool:
#         try:
#             status = requests.get("http://www.dnslog.cn/getrecords.php?t="+self.dnslog_cn,headers=self.headers,  timeout=6)
#             self.dnslog_cn_text = status.text
#             if self.dnslog_cn_text.find(self.host) != -1:  # 如果找到Key
#                 return True
#             else:
#                 return False
#         except Exception as e:
#             ErrorLog().Write(self.host + "|| dnslog_cn_dns", e)
#
#     def dns_text(self):
#         if dnslog_name=="dnslog.cn":
#             return self.dnslog_cn_text


class randoms:  # 生成随机数
    def result(self, nub: int) -> str:
        H = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt
    def LowercaseAndNumbers(self, nub: int) -> str:#生成小写和数字的值
        H = "abcdefghijklmnopqrstuvwxyz123456789"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt
    def Numbers(self, nub: int) -> str:#生成小写和数字的值
        H = "123456789"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt
    def EnglishAlphabet(self, nub: int) -> str:#生成英文字母
        H = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt
    def Lowercase(self, nub: int) -> str:#生成小写字母
        H = "abcdefghijklmnopqrstuvwxyz"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt
    def XOR(self) -> int: #生成随机的xor字符，1-255
        return random.randint(1, 255)


class UrlProcessing:  # URL处理函数
    def result(self, url: str) -> Tuple[str, str, int]:
        if url.startswith("http"):  # 判断是否有http头，如果没有就在下面加入
            res = urllib.parse.urlparse(url)
        else:
            res = urllib.parse.urlparse('http://%s' % url)
        return res.scheme, res.hostname, res.port

#
# class ThreadPool:  # 线程池，适用于单个插件
#     def __init__(self):
#         self.ThreaList = []  # 存放线程列表
#         self.text = 0  # 统计线程数
#
#     def Append(self, plugin,**kwargs):
#         self.text += 1
#         self.ThreaList.append(threading.Thread(target=plugin,kwargs=kwargs))
#
#     def Start(self,ThreadNumber):
#         for t in self.ThreaList:  # 开启列表中的多线程
#             t.start()
#             while True:
#                 # 判断正在运行的线程数量,如果小于5则退出while循环,
#                 # 进入for循环启动新的进程.否则就一直在while循环进入死循环
#                 if (len(threading.enumerate()) < ThreadNumber):
#                     break
#         for p in self.ThreaList:
#             p.join(thread_timeout_number)
#         self.ThreaList.clear()  # 清空列表，防止多次调用导致重复使用
#
# class ProcessPool:  # 进程池，解决pythonGIL锁问题，单核跳舞实在难受
#     def __init__(self):
#         self.ProcessList=[]#创建进程列表
#         self.CountList = []  # 用来计数判断进程数
#
#     def Append(self, Plugin,**kwargs):
#
#
#         # Uid=kwargs.get("Uid")
#         # Sid=kwargs.get("Sid")
#         self.ProcessList.append(multiprocessing.Process(target=Plugin,kwargs=kwargs))
#
#     def PortAppend(self, Plugin, **kwargs):
#         self.ProcessList.append(multiprocessing.Process(target=Plugin, kwargs=kwargs))
#
#     def Start(self, ProcessNumber):
#         if debug_mode:  # 如果开了debug模式就不显示进度条
#             for t in self.ProcessList:  # 开启列表中的多进程
#                 t.start()
#                 self.CountList.append(t)#发送到容器中用于判断
#                 while True:
#                     # 判断正在运行的线程数量,如果小于5则退出while循环,
#                     # 进入for循环启动新的进程.否则就一直在while循环进入死循环
#                     if len([p for p in self.CountList if p.exitcode is None])<ProcessNumber:
#                         break
#             for p in self.ProcessList:
#                 p.join()
#         else:  # 如果没开Debug就改成进度条形式
#             for t in tqdm(self.ProcessList, ascii=True,
#                           desc="\033[32m[ + ] Medusa scan progress bar\033[0m"):  # 开启列表中的多线程
#                 t.start()
#                 while True:
#                     # 判断正在运行的线程数量,如果小于5则退出while循环,
#                     # 进入for循环启动新的进程.否则就一直在while循环进入死循环
#                     if len([p for p in self.CountList if p.exitcode is None]) < ProcessNumber:
#                         break
#             for p in tqdm(self.ProcessList, ascii=True, desc="\033[32m[ + ] Medusa cleanup thread progress\033[0m"):
#                 p.join()
#         self.ProcessList.clear()  # 清空列表，防止多次调用导致重复使用
#


#
# class CommandLineWidth:  # 输出横幅，就是每个组件加载后输出的东西
#     def getTerminalSize(self):
#         import platform  # 获取使用这个软件的平台
#         current_os = platform.system()  # 获取操作系统的具体类型
#         tuple_xy = None
#         if current_os == 'Windows':
#             tuple_xy = self._getTerminalSize_windows()
#             if tuple_xy is None:
#                 tuple_xy = self._getTerminalSize_tput()
#                 # needed for window's python in cygwin's xterm!
#         if current_os == 'Linux' or current_os == 'Darwin' or current_os.startswith('CYGWIN'):
#             tuple_xy = self._getTerminalSize_linux()
#         if tuple_xy is None:
#             tuple_xy = (80, 25)  # default value
#         return tuple_xy
#
#     # 函数名前下划线代表这是一个私有方法 这样我们在导入我们的这个模块的时候 python是不会导入方法名前带有下划线的方法的
#     def _getTerminalSize_windows(self):
#         res = None
#         try:
#             from ctypes import windll, create_string_buffer
#             """
#             STD_INPUT_HANDLE = -10  获取输入的句柄
#             STD_OUTPUT_HANDLE = -11 获取输出的句柄
#             STD_ERROR_HANDLE = -12  获取错误的句柄
#             """
#             h = windll.kernel32.GetStdHandle(-12)  # 获得输入、输出/错误的屏幕缓冲区的句柄
#             csbi = create_string_buffer(22)
#             res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
#         except:
#             return None
#         if res:
#             import struct
#             (bufx, bufy, curx, cury, wattr,
#              left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
#             sizex = right - left + 1
#             sizey = bottom - top + 1
#             return sizex, sizey
#         else:
#             return None
#
#     # 函数名前下划线代表这是一个私有方法 这样我们在导入我们的这个模块的时候 python是不会导入方法名前带有下划线的方法的
#
#     def _getTerminalSize_tput(self):
#         try:
#             import subprocess
#             proc = subprocess.Popen(["tput", "cols"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#             output = proc.communicate(input=None)
#             cols = int(output[0])
#             proc = subprocess.Popen(["tput", "lines"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#             output = proc.communicate(input=None)
#             rows = int(output[0])
#             return (cols, rows)
#         except:
#             return None
#
#     def _getTerminalSize_linux(self):
#         def ioctl_GWINSZ(fd):
#             try:
#                 import fcntl, termios, struct, os
#                 cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
#             except:
#                 return None
#             return cr
#
#         cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
#         if not cr:
#             try:
#                 fd = os.open(os.ctermid(), os.O_RDONLY)
#                 cr = ioctl_GWINSZ(fd)
#                 os.close(fd)
#             except:
#                 pass
#         if not cr:
#             try:
#                 env = os.environ
#                 cr = (env['LINES'], env['COLUMNS'])
#             except:
#                 return None
#         return int(cr[1]), int(cr[0])



class GetRootFileLocation:  # 获取当前文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            Path = os.path.split(os.path.realpath(__file__))[0]
            return Path
        elif system_type == "linux" or system_type == "darwin":
            Path = os.path.split(os.path.realpath(__file__))[0]
            return Path

class GetToolFilePath:  # 获取TOOL文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            Path = GetRootFileLocation().Result()+"\\Tool\\"
            return Path
        elif system_type == "linux" or system_type == "darwin":
            Path = GetRootFileLocation().Result()+"/Tool/"
            return Path

class GetTempFilePath:  # 获取Temp文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            Path = GetRootFileLocation().Result()+"\\Temp\\"
            return Path
        elif system_type == "linux" or system_type == "darwin":
            Path = GetRootFileLocation().Result()+"/Temp/"
            return Path

class ExecuteChildprocess:  # 执行子进程类
    def Execute(self, command: List[str]) -> None:
        self.cmd = subprocess.Popen(command, stdout=subprocess.PIPE)

    def Read(self) -> bytes:
        text = self.cmd.stdout.read()
        return text

#这个是web的类先这这边，有点小BUG
class ScanInformation:#ActiveScanList的子表，单个URL相关漏洞表,写入父表中的SID和UID,以及子表中的SSID，使他们相关连，这个就是一个关系表，关联MEDUSA表和ActiveScanList表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE ScanInformation\
                            (id INTEGER PRIMARY KEY,\
                            active_scan_id TEXT NOT NULL,\
                            url TEXT NOT NULL,\
                            rank TEXT NOT NULL,\
                            scan_info_id TEXT NOT NULL,\
                            uid TEXT NOT NULL,\
                            name TEXT NOT NULL,\
                            creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ScanInformation(class)_init(def)", e)
    def Write(self,**kwargs)->bool:#写入相关信息
        CreationTime = str(int(time.time())) # 创建时间
        Url=kwargs.get("url")
        ScanInfoId=kwargs.get("scan_info_id")
        Uid = kwargs.get("uid")
        ActiveScanId = kwargs.get("active_scan_id")
        Rank = kwargs.get("rank")
        Name= kwargs.get("name")
        try:
            self.cur.execute("INSERT INTO ScanInformation(active_scan_id,url,rank,scan_info_id,uid,name,creation_time)\
            VALUES (?,?,?,?,?,?,?)",(ActiveScanId,Url,Rank,ScanInfoId,Uid,Name,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True#获取主键的ID值，也就是sid的值
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ScanInformation(class)_Write(def)", e)
            return False
    def Query(self,**kwargs)->str or None:#查询相关表内容

        Uid=kwargs.get("uid")
        ActiveScanId = kwargs.get("active_scan_id")
        try:
            self.cur.execute("select * from ScanInformation where uid =? and active_scan_id = ?", (Uid,ActiveScanId,))
            result_list = []  # 存放json的返回结果列表用
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["url"] = i[2]
                JsonValues["scan_info_id"] = i[4]
                JsonValues["rank"] = i[3]
                JsonValues["name"] = i[6]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ScanInformation(class)_Query(def)", e)
            return None


class SubdomainTable:  # 这是一个子域名表
    def __init__(self,Subdomain:str,url: str, **kwargs):
        try:
            self.url = str(url)  # 目标域名
            self.timestamp = str(int(time.time()))  # 获取时间戳
            self.subdomain=Subdomain#获取的子域名
            self.uid = kwargs.get("Uid")  # 传入的用户ID
            self.active_scan_id=kwargs.get("ActiveScanId")# 传入的父表SID
            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(GetDatabaseFilePath().result())
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表
            try:
                # 如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
                self.cur.execute("CREATE TABLE Subdomain\
                            (id INTEGER PRIMARY KEY,\
                            url TEXT NOT NULL,\
                            subdomain TEXT NOT NULL,\
                            timestamp TEXT NOT NULL,\
                            active_scan_id TEXT NOT NULL,\
                            uid TEXT NOT NULL)")
            except Exception as e:
                ErrorLog().Write("ClassCongregation_SubdomainTable(class)_init(def)_CREATETABLE", e)
        except Exception as e:
            ErrorLog().Write("ClassCongregation_SubdomainTable(class)_init(def)", e)

    def Write(self):  # 统一写入
        try:
            self.cur.execute("""INSERT INTO Subdomain (url,subdomain,timestamp,active_scan_id,uid) \
            VALUES (?,?,?,?,?)""", (self.url, self.subdomain,self.timestamp,self.active_scan_id,self.uid,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
            ErrorLog().Write("ClassCongregation_SubdomainTable(class)_Write(def)", e)

class Md5Encryption:#加密类
    def __init__(self):
        self.Md5=hashlib.md5()

    def Md5Result(self,str):
        self.Md5.update(str.encode("utf8"))
        return self.Md5.hexdigest()

    def Md5GbkResult(self,str):
        self.Md5.update(str.encode("gb2312"))
        return self.Md5.hexdigest()

class GetImageFilePath:  # 获取Image文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            Path = GetRootFileLocation().Result()+"\\Web\\Image\\"
            return Path
        elif system_type == "linux" or system_type == "darwin":
            Path = GetRootFileLocation().Result()+"/Web/Image/"
            return Path

class GetJavaScriptFilePath:  # 获取JavaScript文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            Path = GetRootFileLocation().Result()+"\\Web\\CrossSiteScriptHub\\CrossSiteScriptProject\\"
            return Path
        elif system_type == "linux" or system_type == "darwin":
            Path = GetRootFileLocation().Result()+"/Web/CrossSiteScriptHub/CrossSiteScriptProject/"
            return Path

class GetCrossSiteScriptTemplateFilePath:  # 获取CrossSiteScriptTemplate文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            Path = GetRootFileLocation().Result()+"\\Web\\CrossSiteScriptHub\\CrossSiteScriptTemplate\\"
            return Path
        elif system_type == "linux" or system_type == "darwin":
            Path = GetRootFileLocation().Result()+"/Web/CrossSiteScriptHub/CrossSiteScriptTemplate/"
            return Path

class GetAnalysisFileStoragePath:  # 获取分析文件存储路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            Path = GetRootFileLocation().Result()+"\\Web\\ToolsUtility\\BinaryAnalysis\\AnalysisFileStorage\\"
            return Path
        elif system_type == "linux" or system_type == "darwin":
            Path = GetRootFileLocation().Result()+"/Web/ToolsUtility/BinaryAnalysis/AnalysisFileStorage/"
            return Path
class GetTrojanPluginsPath:  # 获取木马插件名称
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            Path = GetRootFileLocation().Result()+"\\Web\\TrojanOrVirus\\Modules\\"
            return Path
        elif system_type == "linux" or system_type == "darwin":
            Path = GetRootFileLocation().Result()+"/Web/TrojanOrVirus/Modules/"
            return Path

class GetTrojanFilePath:  # 获取生成好的病毒文件路径
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            Path = GetRootFileLocation().Result()+"\\Web\\TrojanOrVirus\\TrojanFile\\"
            return Path
        elif system_type == "linux" or system_type == "darwin":
            Path = GetRootFileLocation().Result()+"/Web/TrojanOrVirus/TrojanFile/"
            return Path

def PortReplacement(Url,Prot):#替换URL里面的端口
    try:
        Result = re.sub(r':(6[0-5]{2}[0-3][0-5]|[1-5]\d{4}|[1-9]\d{1,3}|[0-9])', ":"+str(Prot), Url)
        return Result
    except Exception as e:
        ErrorLog().Write("ClassCongregation_PortReplacement(def)", e)


class GetNistDatabaseFilePath:  #  Nist数据库文件路径返回值
    def result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            Path = GetRootFileLocation().Result() + "\\Nist.db"
            return Path
        elif sys.platform == "linux" or sys.platform == "darwin":
            Path = GetRootFileLocation().Result() + "/Nist.db"
            return Path


class Binary:#对于原始二进制数据的类型转换
    def Bytes2String(self,BytesTypeData: bytes):  # 类型转换
        """
        只允许传入一下类型字符串
        字符串样式1:b'\xff'
        返回字符串格式
        '\\xff'
        """
        BytesTypeData=ast.literal_eval(repr(BytesTypeData).replace( "\\","\\\\"))
        try:
            BinaryData = ""
            for i in BytesTypeData:
                # 如果是bytes类型的字符串，for循环会读取单个16进制然后转换成10进制
                Data = hex(i)  # 转换会16进制
                Data = Data.replace('0x', '')
                if (len(Data) == 1):
                    Data = '0' + Data  # 位数补全
                BinaryData += '\\x' + Data

            return ast.literal_eval(repr(BinaryData).replace('\\\\', '\\'))#先repr将字符串转为python原生字符串，然后替换双斜杠，最后eval转回正常字符串
        except Exception as e:
            ErrorLog().Write("ClassCongregation_Binary(class)_Bytes2String(def)", e)

    def String2Bytes(self,StringTypeData: str):# 类型转换，一般用在需要对shellcode进行处理的时候，比如加密，异或之类的
        """
        支持一下两种字符串格式
        字符串样式1:'\xff'
        字符串样式2:'\\xff'
        返回字符串格式
        b'\xff'
        """
        StringTypeData=ast.literal_eval(repr(StringTypeData).replace("\\\\", "\\"))
        try:
            BinaryData = b""
            for i in StringTypeData:
                Code = hex(ord(i))
                Code = bytes(Code.replace('0x', ''), encoding="utf-8")
                if (len(Code) == 1):
                    Code = b'0' + Code  # 位数补全
                BinaryData += b'\\x' + Code

            return ast.literal_eval(repr(BinaryData).replace('\\\\', '\\'))

        except Exception as e:
            ErrorLog().Write("ClassCongregation_Binary(class)_String2Bytes(def)", e)

    def String2Nim(self,StringTypeData: str):
        """字符串转换成nim语言类型的shellcode
        样例：var shellcode: array[519, byte] = [ byte 72, 49]"""
        try:
            BinaryData = []
            for i in StringTypeData:
                Code = ord(i)
                BinaryData.append(Code)

            return str(len(BinaryData)),str(BinaryData).replace("[","[ byte ")#返回容器个数，和shellcode内容
        except Exception as e:
            ErrorLog().Write("ClassCongregation_Binary(class)_String2Nim(def)", e)

    def String2GoArray(self,StringTypeData: str):
        """
        支持一下两种字符串格式
        字符串样式1:'\xff\xfa\xfb\xfc\xfd\xfe\xff'
        字符串样式2:'\\xff\\xfa\\xfb\\xfc\\xfd\\xfe\\xff'
        返回字符串格式: 0xff,0xfa,0xfb,0xfc,0xfd,0xfe,0xff
        """
        try:
            StringTypeData = ast.literal_eval(repr(StringTypeData).replace("\\\\", "\\"))
            Shellcode = ""
            for i in StringTypeData:
                Shellcode+= hex(ord(i))+","
            return Shellcode[:-1]
        except Exception as e:
            ErrorLog().Write("ClassCongregation_Binary(class)_String2GoArray(def)", e)
    def String2GoHex(self,StringTypeData: str):
        """
        支持一下两种字符串格式
        字符串样式1:'\xff\xfa\xfb\xfc\xfd\xfe\xff'
        字符串样式2:'\\xff\\xfa\\xfb\\xfc\\xfd\\xfe\\xff'
        返回字符串格式: fffafbfcfdfeff
        """
        try:
            StringTypeData = ast.literal_eval(repr(StringTypeData).replace("\\\\", "\\"))
            BinaryData = ""
            for i in StringTypeData:
                BinaryData += hex(ord(i)).replace("0x", "")
            return BinaryData
        except Exception as e:
            ErrorLog().Write("ClassCongregation_Binary(class)_String2GoHex(def)", e)


class ShellCode:#shellcode的加解密函数
    def XOR(self,Value:int, RawShellcode:bytes):
        """
        只支持\xff格式的16进制
        """
        # #逐字节读取，二进制文件数据，单个字节为16进制
        # f=open("payload.bin","rb")
        # code = f.read(1)
        Shellcode = ''#Value的最大值为0XFF，也就是int值255
        try:
            for SingleByte in RawShellcode:
                #如果是bytes类型的字符串，for循环会读取单个16进制然后转换成10进制
                XORValue = SingleByte ^ Value#进行xor操作
                Code = hex(XORValue)#转换会16进制
                Code = Code.replace('0x','')
                if(len(Code) == 1):
                    Code = '0' + Code#位数补全
                Shellcode += '\\x' + Code
            return Shellcode
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ShellCode(class)_XOR(def)", e)
            return None
    def AESDecode(self,data, key):
        """
        key长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
        """
        try:
            # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
            aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器
            decrypted_text = aes.decrypt(base64.decodebytes(bytes(data, encoding='utf8'))).decode("utf8")  # 解密
            decrypted_text = decrypted_text[:-ord(decrypted_text[-1])]  # 去除多余补位
            return decrypted_text
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ShellCode(class)_AESDecode(def)", e)
            return None
    def AESEncode(self,data, key):
        """
        加密
        data传入格式：\\ff\\fa
        key长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
        """
        # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
        try:
            while len(data) % 16 != 0:  # 补足字符串长度为16的倍数
                data += (16 - len(data) % 16) * chr(16 - len(data) % 16)
            data = str.encode(data)
            aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器
            return str(base64.encodebytes(aes.encrypt(data)), encoding='utf8').replace('\n', '')  # 加密
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ShellCode(class)_AESEncode(def)", e)
            return None

class GetPluginsFilePath:  #  插件文件路径
    def Result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            Path = GetRootFileLocation().Result() + "\\Plugins\\"
            return Path
        elif sys.platform == "linux" or sys.platform == "darwin":
            Path = GetRootFileLocation().Result() + "/Plugins/"
            return Path

class Plugins:#扫描插件相关数据库,里面存放yml插件
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE Plugins\
                                (plugins_id INTEGER PRIMARY KEY,\
                                plugins_name TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_ClassCongregation_Plugins(class)_init(def)", e)
    def Write(self, DataSet:list) -> bool or None:  # 写入相关信息
        try:
            self.cur.executemany("INSERT INTO Plugins(plugins_name)\
                VALUES (?)", DataSet)
            # 提交
            self.con.commit()#只发送数据不结束
            return True
        except Exception as e:
            ErrorLog().Write("Web_ClassCongregation_Plugins(class)_Write(def)", e)
            return False

    def Query(self, **kwargs):  #查询单个插件
        PluginsName=kwargs.get("plugins_name")
        try:
            self.cur.execute("select * from Plugins where plugins_name =? ",
                             (PluginsName,))

            for i in self.cur.fetchall():
                self.con.close()
                return i[1]#返回单个插件结果
        except Exception as e:
            ErrorLog().Write("Web_ClassCongregation_Plugins(class)_Query(def)", e)
            return None
    def Read(self):#读取全部插件
        try:
            self.cur.execute("select * from Plugins",)
            result_list = []  # 存放json的返回结果列表用
            for i in self.cur.fetchall():
                result_list.append(i[1])
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_ClassCongregation_Plugins(class)_Read(def)", e)
            return None
    def Initialization(self):#初始化表格 清空表中的全部数据
        try:
            self.cur.execute("DELETE FROM Plugins",)
            return True
        except Exception as e:
            ErrorLog().Write("Web_ClassCongregation_Plugins(class)_Initialization(def)", e)
            return False

class GetTrojanModulesFilePath:  #  木马插件模块位置
    def Result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            Path = GetRootFileLocation().Result() + "\\Web\\TrojanOrVirus\\Modules\\"
            return Path
        elif sys.platform == "linux" or sys.platform == "darwin":
            Path = GetRootFileLocation().Result() + "/Web/TrojanOrVirus/Modules/"
            return Path

class GetMailUploadFilePath:  #  邮件附件位置
    def Result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            Path = GetRootFileLocation().Result() + "\\Web\\Email\\UploadFiles\\"
            return Path
        elif sys.platform == "linux" or sys.platform == "darwin":
            Path = GetRootFileLocation().Result() + "/Web/Email/UploadFiles/"
            return Path


class FileAcquisitionPath:  #  文件采集器文件路径
    def Result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            Path = GetRootFileLocation().Result() + "\\Web\\FileAcquisition\\File\\"
            return Path
        elif sys.platform == "linux" or sys.platform == "darwin":
            Path = GetRootFileLocation().Result() + "/Web/FileAcquisition/File/"
            return Path
class FileAcquisitionZipPath:  #  文件打包下载路径
    def Result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            Path = GetRootFileLocation().Result() + "\\Web\\FileAcquisition\\Zip\\"
            return Path
        elif sys.platform == "linux" or sys.platform == "darwin":
            Path = GetRootFileLocation().Result() + "/Web/FileAcquisition/Zip/"
            return Path
class PortableExecutableFilePath:  # 上传的PE文件路径
    def Result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            Path = GetRootFileLocation().Result() + "\\Web\\TrojanOrVirus\\PE\\"
            return Path
        elif sys.platform == "linux" or sys.platform == "darwin":
            Path = GetRootFileLocation().Result() + "/Web/TrojanOrVirus/PE/"
            return Path
class ShellcodeFilePath:  #  生成的shellcode文件路径
    def Result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            Path = GetRootFileLocation().Result() + "\\Web\\TrojanOrVirus\\Shellcode\\"
            return Path
        elif sys.platform == "linux" or sys.platform == "darwin":
            Path = GetRootFileLocation().Result() + "/Web/TrojanOrVirus/Shellcode/"
            return Path
class PE2ShellcodeFilePath:  #  获取PE2SHELLCODE路径
    def Result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            Path = GetRootFileLocation().Result() + "\\Web\\TrojanOrVirus\\"
            return Path
        elif sys.platform == "linux" or sys.platform == "darwin":
            Path = GetRootFileLocation().Result() + "/Web/TrojanOrVirus/"
            return Path

class Config:  # 配置数据表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE Config\
                                (config_id INTEGER PRIMARY KEY,\
                                fixed_data TEXT NOT NULL,\
                                data TEXT NOT NULL,\
                                update_time TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_ClassCongregation_Config(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Data= kwargs.get("data")
        FixedData = kwargs.get("fixed_data")


        try:
            self.cur.execute("INSERT INTO Config(data,fixed_data,update_time,creation_time)\
                VALUES (?,?,?,?)", (Data,FixedData,CreationTime,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_ClassCongregation_Config(class)_Write(def)", e)
            return False
    def Query(self):
        try:
            self.cur.execute("select data,fixed_data,update_time,creation_time  from Config WHERE config_id=?", (1,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["data"] = i[0]
                JsonValues["fixed_data"] = i[1]
                JsonValues["update_time"] = i[2]
                JsonValues["creation_time"] = i[3]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_ClassCongregation_Config(class)_Query(def)", e)
            return None
    def Update(self,**kwargs):
        UpdateTime=str(int(time.time()))
        FixedData = kwargs.get("fixed_data")
        try:
            self.cur.execute(
                """UPDATE Config SET fixed_data = ?,update_time=? WHERE config_id = ?""",
                (FixedData ,UpdateTime,1,))
            # 提交
            if self.cur.rowcount < 1:  # 用来判断是否更新成功
                self.con.commit()
                self.con.close()
                return False
            else:
                self.con.commit()
                self.con.close()
                return True

        except Exception as e:
            ErrorLog().Write("Web_ClassCongregation_Config(class)_Update(def)", e)
    def Statistics(self):  # 统计数据
        try:
            self.cur.execute("SELECT COUNT(1)  FROM Config ",)
            if self.cur.fetchall()[0][0]==0 :#获取数据个数
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_ClassCongregation_Config(class)_Statistics(def)", e)
            return False