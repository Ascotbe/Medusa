#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from fake_useragent import UserAgent
import urllib.parse
import nmap
import requests
import sqlite3
from tqdm import tqdm
import logging
import os
import re
import base64
import random
import sys
import time
import multiprocessing
from typing import List, Dict, Tuple, Any
import threading
import subprocess
from config import ceye_dnslog_url, ceye_dnslog_key, debug_mode,dnslog_name

#########
# 全局变量
WriteFileUnixTimestamp = str(int(time.time()))


#########

def IpProcess(Url: str) -> str:
    if Url.startswith("http"):  # 记个小知识点：必须带上https://这个头不然urlparse就不能正确提取hostname导致后面运行出差错
        res = urllib.parse.urlparse(Url)  # 小知识点2：如果只导入import urllib包使用parse这个类的话会报错，必须在import requests导入这个包才能正常运行
    else:
        res = urllib.parse.urlparse('http://%s' % Url)
    return (res.hostname)



class NumberOfLoopholes:

    def WriteVulnerabilityName(self,FileName,Medusa):#把漏洞名字写到文件中
        self.FileName=FileName
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.FilePath = GetRootFileLocation().Result()+ "\\Temp\\" + self.FileName + ".txt"  # 不需要输入后缀，只要名字就好
        elif sys.platform == "linux" or sys.platform == "darwin":
            self.FilePath = GetRootFileLocation().Result() + "/Temp/" + self.FileName + ".txt"  # 不需要输入后缀，只要名字就好
        regular_match_results = re.search(r'存在([\w\u4e00-\u9fa5!@#$%^*()&-=+_`~/?.,<>\\|\[\]{}]*)', Medusa).group(
            0)  # 正则匹配，匹配存在后面的所有字符串，直到换行符结束
        with open(self.FilePath, 'a+', encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            if regular_match_results=="存在":
                pass
            else:
                f.write(regular_match_results + "\n")
    def Result(self,FileName):  # 漏洞个数输出函数以及名称的函数
        LoopholesList=[]#创建列表存放漏洞
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.FilePath = GetRootFileLocation().Result() + "\\Temp\\" + FileName + ".txt"  # 不需要输入后缀，只要名字就好
        elif sys.platform == "linux" or sys.platform == "darwin":
            self.FilePath = GetRootFileLocation().Result() + "/Temp/" + FileName + ".txt"  # 不需要输入后缀，只要名字就好
        try:
            with open(self.FilePath, encoding='utf-8') as f:
                for i in f:  # 设置头文件使用的字符类型和开头的名字
                    LoopholesList.append(i.strip("\r\n"))#传到列表里面
            print(
                "\033[32m[ ! ] The number of vulnerabilities scanned was:\033[0m" + "\033[36m {}             \033[0m".format(
                    len(LoopholesList)))
            for i in LoopholesList:
                time.sleep(0.1)  # 暂停不然瞬间刷屏
                print("\033[35m[ ! ] {}\033[0m".format(i))
            LoopholesList.clear()  # 清空容器这样就不会出问题了
        except Exception as e:
            ErrorLog().Write("NumberOfLoopholes(class)_Result(def)", e)
            print("\033[32m[ ! ] The number of vulnerabilities scanned was:\033[0m" + "\033[36m {}             \033[0m".format(
                    len(LoopholesList)))



class WriteFile:  # 写入文件类
    def result(self, TargetName: str, Medusa: str) -> None:
        self.FileName = time.strftime("%Y-%m-%d", time.localtime()) + "_" + TargetName + "_" + WriteFileUnixTimestamp
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.FilePath = GetRootFileLocation().Result()+ "\\ScanResult\\" + self.FileName + ".txt"  # 不需要输入后缀，只要名字就好
        elif sys.platform == "linux" or sys.platform == "darwin":
            self.FilePath = GetRootFileLocation().Result() + "/ScanResult/" + self.FileName + ".txt"  # 不需要输入后缀，只要名字就好
        with open(self.FilePath, 'a+', encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(Medusa + "\n")
        NumberOfLoopholes().WriteVulnerabilityName(self.FileName,Medusa)#把扫描到的漏洞全发送到这个函数中，然后把文件名也发送过去
    def GetFileName(self,Url):
        try:#会无法获取到一些数据导致报错，如果报错就返回空支付串
            scheme,url, port = UrlProcessing().result(Url)
            if self.FileName ==None:
                return ""
            self.result(url,"存在")
            return self.FileName
        except:
            return ""

class AgentHeader:  # 使用随机头类
    def result(self, Values: str) -> str:  # 使用随机头传入传入参数
        try:
            self.Values = Values
            if len(Values) > 11:
                return Values
            ua = UserAgent(verify_ssl=False)
            if self.Values == None:  # 如果参数为空使用随机头
                return (ua.random)
            elif self.Values.lower() == "firefox":  # 如果是火狐字符串使用火狐头
                return (ua.firefox)
            elif self.Values.lower() == "ie":  # IE浏览器
                return (ua.ie)
            elif self.Values.lower() == "msie":  # msie
                return (ua.msie)
            elif self.Values.lower() == "opera":  # Opera Software
                return (ua.opera)
            elif self.Values.lower() == "chrome":  # 谷歌浏览器
                return (ua.chrome)
            elif self.Values.lower() == "AppleWebKit":  # AppleWebKit
                return (ua.google)
            elif self.Values.lower() == "Gecko":  # Gecko
                return (ua.ff)
            elif self.Values.lower() == "safari":  # apple safari
                return (ua.safari)
            else:
                return (ua.random)  # 如果用户瞎几把乱输使用随机头
        except Exception as e:
            ErrorLog().Write("ClassCongregation_AgentHeader(class)_result(def)", e)
            return "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36"  # 报错使用随机头


class GetDatabaseFilePath:  # 数据库文件路径返回值
    def result(self) -> str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            DatabaseFilePath = GetRootFileLocation().Result() + "\\Medusa.db"
            return DatabaseFilePath
        elif sys.platform == "linux" or sys.platform == "darwin":
            DatabaseFilePath = GetRootFileLocation().Result() + "/Medusa.db"
            return DatabaseFilePath


class NmapScan:  # 扫描端口类
    def __init__(self, Url: str):
        Host = IpProcess(Url)  # 调用IP处理函数
        self.Host = Host  # 提取后的网址或者IP
        # self.Port = "445"#测试
        self.Port = "1-65535"  # 如果用户没输入就扫描全端口

    def ScanPort(self) -> None:
        try:
            Nmap = nmap.PortScanner()
            ScanResult = Nmap.scan(self.Host, self.Port, '-sS -Pn -n --open --min-hostgroup 4 --min-parallelism 1024 --host-timeout 30 -T4 -v')
            HostAddress = re.compile('{\'([\d.]+)\': {').findall(str(ScanResult['scan']))[0]  # 只能用正则取出ip的值
            for port in ScanResult['scan'][HostAddress]['tcp']:
                Nmaps = ScanResult['scan'][HostAddress]['tcp'][port]
                NmapDB(Nmaps, port, self.Host, HostAddress).Write()
        except IOError:
            print("Please enter the correct nmap scan command.")


# 为每个任务加个唯一的加密ID然后存入，后面和读取数据库后进行全量端口爆破做铺垫
class NmapDB:  # NMAP的数据库
    def __init__(self, Nmap, port: str, ip: str, domain: str):
        self.state = Nmap['state']  # 端口状态
        self.reason = Nmap['reason']  # 端口回复
        self.name = Nmap['name']  # 服务名称
        self.product = Nmap['product']  # 服务器类型
        self.version = Nmap['version']  # 版本
        self.extrainfo = Nmap['extrainfo']  # 其他信息
        self.conf = Nmap['conf']  # 配置
        self.cpe = Nmap['cpe']  # 消息头
        self.port = port  # 有哪些端口
        self.ip = ip  # 扫描的目标
        self.domain = domain  # 域名
        # 如果数据库不存在的话，将会自动创建一个 数据库
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE Nmap\
                        (domain TEXT,\
                        ip TEXT,\
                        port TEXTL,\
                        state TEXT,\
                        name TEXT,\
                        product TEXT,\
                        reason TEXT,\
                        version TEXT,\
                        extrainfo TEXT,\
                        conf TEXT,\
                        cpe TEXT)")
        except Exception as e:
            ErrorLog().Write("ClassCongregation_NmapDB(class)_init(def)", e)

    def Write(self) -> None:
        try:

            # sql_insert = """INSERT INTO Nmap (domain,ip,port,state,name,product,reason,version,extrainfo,conf,cpe) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.domain,self.ip,self.port,self.state,self.name,self.product,self.reason,self.version,self.extrainfo,self.conf,self.cpe)
            self.cur.execute(
                """INSERT INTO Nmap (domain,ip,port,state,name,product,reason,version,extrainfo,conf,cpe) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (self.domain, self.ip, self.port, self.state, self.name, self.product, self.reason, self.version,
                 self.extrainfo, self.conf, self.cpe,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
            ErrorLog().Write("ClassCongregation_NmapDB(class)_Write(def)", e)


class NmapRead:  # 读取Nmap扫描后的数据
    def __init__(self, id: str):
        self.id = id  # 每个任务唯一的ID值
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        self.cur = self.con.cursor()

    def Read(self) -> List[str]:
        try:
            port_list = []
            self.cur.execute("select * from Nmap where id =?", (self.id,))
            values = self.cur.fetchall()
            for i in values:
                if i[3] == "open":
                    port_list.append(i[2])  # 发送端口号到列表中
            self.con.close()
            return port_list
        except Exception as e:
            ErrorLog().Write("ClassCongregation_NmapRead(class)_Read(def)", e)


class GithubCveApi:  # CVE写入表
    def __init__(self, CveJsonList: Any):
        try:
            self.cve_id = CveJsonList["id"]  # 唯一的ID
            self.cve_name = CveJsonList["name"]  # 名字
            self.cve_html_url = CveJsonList["html_url"]  # 链接
            self.cve_created_at = CveJsonList["created_at"]  # 创建时间
            self.cve_updated_at = CveJsonList["updated_at"]  # 更新时间
            self.cve_pushed_at = CveJsonList["pushed_at"]  # push时间
            self.cve_forks_count = CveJsonList["forks_count"]  # fork人数
            self.cve_watchers_count = CveJsonList["watchers_count"]  # star人数
            self.cve_write_time = str(int(time.time()))  # 写入时间
            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(GetDatabaseFilePath().result())
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表
            try:
                # 如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
                self.cur.execute("CREATE TABLE GithubCVE\
                            (id INTEGER PRIMARY KEY,\
                            github_id TEXT NOT NULL,\
                            name TEXT NOT NULL,\
                            html_url TEXT NOT NULL,\
                            created_at TEXT NOT NULL,\
                            updated_at TEXT NOT NULL,\
                            pushed_at TEXT NOT NULL,\
                            forks_count TEXT NOT NULL,\
                            watchers_count TEXT NOT NULL,\
                            write_time TEXT NOT NULL,\
                            update_write_time TEXT NOT NULL)")
            except Exception as e:
                ErrorLog().Write("ClassCongregation_GithubCveApi(class)_init(def)_CREATE", e)
        except Exception as e:
            ErrorLog().Write("ClassCongregation_GithubCveApi(class)_init(def)", e)

    def Write(self):
        try:
            self.cur.execute("""INSERT INTO GithubCVE (github_id,name,html_url,created_at,updated_at,pushed_at,forks_count,watchers_count,write_time,update_write_time) \
    VALUES (?,?,?,?,?,?,?,?,?,?)""", (
            self.cve_id, self.cve_name, self.cve_html_url, self.cve_created_at, self.cve_updated_at, self.cve_pushed_at,
            self.cve_forks_count, self.cve_watchers_count, self.cve_write_time, self.cve_write_time,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
                ErrorLog().Write("ClassCongregation_GithubCveApi(class)_Write(def)", e)

    def Update(self, UpdateTime: str):
        self.cve_update_write_time = str(UpdateTime)  # 跟新时间
        try:
            self.cur.execute(
                """UPDATE GithubCVE SET forks_count = ?,updated_at=?,pushed_at=?,watchers_count=?,update_write_time=?  WHERE github_id = ?""",
                (self.cve_forks_count, self.cve_updated_at, self.cve_pushed_at, self.cve_watchers_count,
                 self.cve_update_write_time, self.cve_id,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
            ErrorLog().Write("ClassCongregation_GithubCveApi(class)_Update(def)", e)

    def Sekect(self) -> bool:

        self.cur.execute(
            """SELECT * FROM GithubCVE WHERE github_id=?""", (self.cve_id,))
        values = self.cur.fetchall()
        cve_query_results = None
        if len(values) == 0:
            cve_query_results = False
        if len(values) == 1:
            cve_query_results = True
        # 提交
        self.con.commit()
        self.con.close()
        return cve_query_results


class VulnerabilityDetails:  # 所有数据库写入都是用同一个类
    def __init__(self, medusa, url: str, **kwargs):
        try:
            self.url = str(url)  # 目标域名
            self.timestamp = str(int(time.time()))  # 获取时间戳
            self.name = medusa['name']  # 漏洞名称
            self.number = medusa['number']  # CVE编号
            self.author = medusa['author']  # 插件作者
            self.create_date = medusa['create_date']  # 插件编辑时间
            self.algroup = medusa['algroup']  # 插件名称
            self.rank = medusa['rank']  # 漏洞等级
            self.disclosure = medusa['disclosure']  # 漏洞披露时间，如果不知道就写编写插件的时间
            self.details = base64.b64encode(medusa['details'].encode(encoding="utf-8"))  # 对结果进行编码写入数据库，鬼知道数据里面有什么玩意
            self.affects = medusa['affects']  # 漏洞组件
            self.desc_content = medusa['desc_content']  # 漏洞描述
            self.suggest = medusa['suggest']  # 修复建议
            self.version = medusa['version']  # 漏洞影响的版本
            self.uid = kwargs.get("Uid")  # 传入的用户ID
            self.sid=kwargs.get("Sid")# 传入的父表SID
            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(GetDatabaseFilePath().result())
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表
            try:
                # 如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
                self.cur.execute("CREATE TABLE Medusa\
                            (ssid INTEGER PRIMARY KEY,\
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
                            sid TEXT NOT NULL,\
                            uid TEXT NOT NULL)")
            except Exception as e:
                ErrorLog().Write("ClassCongregation_VulnerabilityDetails(class)_init(def)_CREATETABLE", e)
        except Exception as e:
            ErrorLog().Write("ClassCongregation_VulnerabilityDetails(class)_init(def)", e)

    def Write(self):  # 统一写入
        try:
            self.cur.execute("""INSERT INTO Medusa (url,name,affects,rank,suggest,desc_content,details,number,author,create_date,disclosure,algroup,version,timestamp,sid,uid) \
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
                self.url, self.name, self.affects, self.rank, self.suggest, self.desc_content, self.details,
                self.number,
                self.author, self.create_date, self.disclosure, self.algroup, self.version, self.timestamp,
                self.sid,self.uid,))
            # 提交
            GetSsid = self.cur.lastrowid
            self.con.commit()
            self.con.close()
            # print(GetSsid)
            ScanInformation().Write(ssid=GetSsid,url=self.url,sid=self.sid,rank=self.rank,uid=self.uid,name=self.name)#调用web版数据表，写入ScanInformation关系表
        except Exception as e:
            ErrorLog().Write("ClassCongregation_VulnerabilityDetails(class)_Write(def)", e)

class Exploit:  # 所有漏洞利用使用同一个类
    def __init__(self, medusa, url: str, **kwargs):
        try:
            self.url = str(url)  # 目标域名
            self.timestamp = str(int(time.time()))  # 获取时间戳
            self.name = medusa['name']  # 漏洞名称
            self.number = medusa['number']  # CVE编号
            self.author = medusa['author']  # 插件作者
            self.create_date = medusa['create_date']  # 插件编辑时间
            self.algroup = medusa['algroup']  # 插件名称
            self.rank = medusa['rank']  # 漏洞等级
            self.disclosure = medusa['disclosure']  # 漏洞披露时间，如果不知道就写编写插件的时间
            self.details = base64.b64encode(medusa['details'].encode(encoding="utf-8"))  # 对结果进行编码写入数据库，鬼知道数据里面有什么玩意
            self.affects = medusa['affects']  # 漏洞组件
            self.desc_content = medusa['desc_content']  # 漏洞描述
            self.suggest = medusa['suggest']  # 修复建议
            self.version = medusa['version']  # 漏洞影响的版本
            self.uid = kwargs.get("Uid")  # 传入的用户ID
            self.command = kwargs.get("Command")  # 传入执行的命令
            self.sid=kwargs.get("Sid")# 传入的父表SID
            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(GetDatabaseFilePath().result())
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表
            try:
                # 如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
                self.cur.execute("CREATE TABLE Exploit\
                            (ssid INTEGER PRIMARY KEY,\
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
                            sid TEXT NOT NULL,\
                            command TEXT NOT NULL,\
                            uid TEXT NOT NULL)")
            except Exception as e:
                ErrorLog().Write("ClassCongregation_Exploit(class)_init(def)_CREATETABLE", e)
        except Exception as e:
            ErrorLog().Write("ClassCongregation_Exploit(class)_init(def)", e)

    def Write(self):  # 统一写入
        try:
            self.cur.execute("""INSERT INTO Exploit (url,name,affects,rank,suggest,desc_content,details,number,author,create_date,disclosure,algroup,version,timestamp,sid,command,uid) \
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
                self.url, self.name, self.affects, self.rank, self.suggest, self.desc_content, self.details,
                self.number,
                self.author, self.create_date, self.disclosure, self.algroup, self.version, self.timestamp,
                self.sid,self.command,self.uid,))
            # 提交
            #GetSsid = self.cur.lastrowid
            self.con.commit()
            self.con.close()
            # print(GetSsid)
            #ScanInformation().Write(ssid=GetSsid,url=self.url,sid=self.sid,rank=self.rank,uid=self.uid,name=self.name)#调用web版数据表，写入ScanInformation关系表
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
        # filename=os.path.realpath(__file__)#获取当前文件名
        log_format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        logging.basicConfig(filename=filename, filemode='a', level=logging.INFO,
                            format=log_format)  # 初始化配置信息

    def Write(self, Name, ErrorInfo):
        logging.info(Name)
        logging.warning(ErrorInfo)


class Dnslog:  # Dnslog判断
    def __init__(self):
        #该网站是通过PHPSESSID来判断dns归属谁的所有可以随机一个这个
        h = "abcdefghijklmnopqrstuvwxyz0123456789"
        salt_cookie = ""
        for i in range(26):
            salt_cookie += random.choice(h)
        self.headers = {
            "Cookie": "PHPSESSID="+salt_cookie
        }
        H = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        salt = ""
        for i in range(15):
            salt += random.choice(H)
        try:
            self.host = str(salt + "." + self.get_dnslog_url())
        except Exception as e:
            print("\033[31m[ ! ] Unable to get dnslog, please replace ceye! \033[0m")
            self.host=""
            ErrorLog().Write("ClassCongregation_Dnslog(class)_init_(def)", e)

    def dns_host(self) -> str:
        return str(self.host)

    def get_dnslog_url(self):
        if dnslog_name=="dnslog.cn":
            try:
                self.dnslog_cn=requests.get("http://www.dnslog.cn/getdomain.php",headers=self.headers,timeout=6).text
                return self.dnslog_cn
            except Exception as e:
                ErrorLog().Write("ClassCongregation_Dnslog(class)_get_dns_log_url(def)", e)
        elif dnslog_name=="ceye":
            return ceye_dnslog_url

    def result(self) -> bool:
        # DNS判断后续会有更多的DNS判断，保持准确性
        if dnslog_name=="dnslog.cn":
            return self.dnslog_cn_dns()
        elif dnslog_name=="ceye":
            return self.ceye_dns()

    def ceye_dns(self) -> bool:
        try:
            # status = requests.post('http://log.ascotbe.com/api/validate', timeout=2,data=data)
            # code=status.status_code
            # if code == 200:
            status = requests.get("http://api.ceye.io/v1/records?token=" + ceye_dnslog_key + "&type=dns&filter=",timeout=6)
            self.ceye_dnslog_text = status.text
            if self.ceye_dnslog_text.find(self.host) != -1:  # 如果找到Key
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write(self.host+"|| ceye_dns",e)

    def dnslog_cn_dns(self) -> bool:
        try:
            status = requests.get("http://www.dnslog.cn/getrecords.php?t="+self.dnslog_cn,headers=self.headers,  timeout=6)
            self.dnslog_cn_text = status.text
            if self.dnslog_cn_text.find(self.host) != -1:  # 如果找到Key
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write(self.host + "|| dnslog_cn_dns", e)

    def dns_text(self):
        if dnslog_name=="dnslog.cn":
            return self.dnslog_cn_text
        elif dnslog_name=="ceye":
            return self.ceye_dnslog_text


class randoms:  # 生成随机数
    def result(self, nub: int) -> str:
        H = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        salt = ""
        for i in range(nub):
            salt += random.choice(H)
        return salt


class UrlProcessing:  # URL处理函数
    def result(self, url: str) -> Tuple[str, str, int]:
        if url.startswith("http"):  # 判断是否有http头，如果没有就在下面加入
            res = urllib.parse.urlparse(url)
        else:
            res = urllib.parse.urlparse('http://%s' % url)
        return res.scheme, res.hostname, res.port


class Proxies:  # 代理处理函数
    def result(self, proxies_ip: str or None) -> Dict or None:
        if proxies_ip == None:
            return proxies_ip
        else:
            return {"http": "http://{}".format(proxies_ip), "https": "https://{}".format(proxies_ip)}

class ThreadPool:  # 线程池，适用于单个插件
    def __init__(self):
        self.ThreaList = []  # 存放线程列表
        self.text = 0  # 统计线程数

    def Append(self, plugin,**kwargs):
        self.text += 1
        self.ThreaList.append(threading.Thread(target=plugin,kwargs=kwargs))

    def Start(self,ThreadNumber):
        for t in self.ThreaList:  # 开启列表中的多线程
            t.start()
            while True:
                # 判断正在运行的线程数量,如果小于5则退出while循环,
                # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                if (len(threading.enumerate()) < ThreadNumber):
                    break
        for p in self.ThreaList:
            p.join()
        self.ThreaList.clear()  # 清空列表，防止多次调用导致重复使用

class ProcessPool:  # 进程池，解决pythonGIL锁问题，单核跳舞实在难受
    def __init__(self):
        self.ProcessList=[]#创建进程列表
        self.CountList = []  # 用来计数判断进程数
        self.text = 0  # 统计线程数

    def Append(self, Plugin, Url, Values,proxies,**kwargs):
        self.text += 1
        ua = AgentHeader().result(Values)
        Uid=kwargs.get("Uid")
        Sid=kwargs.get("Sid")
        self.ProcessList.append(multiprocessing.Process(target=Plugin, args=(Url, ua, proxies,),kwargs={"Uid":Uid,"Sid":Sid}))

    def NmapAppend(self, Plugin, Url):
        self.ProcessList.append(multiprocessing.Process(target=Plugin, args=(Url)))

    def Start(self, ProcessNumber):
        if debug_mode:  # 如果开了debug模式就不显示进度条
            for t in self.ProcessList:  # 开启列表中的多进程
                t.start()
                self.CountList.append(t)#发送到容器中用于判断
                while True:
                    # 判断正在运行的线程数量,如果小于5则退出while循环,
                    # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                    if len([p for p in self.CountList if p.exitcode is None])<ProcessNumber:
                        break
            for p in self.ProcessList:
                p.join()
        else:  # 如果没开Debug就改成进度条形式
            for t in tqdm(self.ProcessList, ascii=True,
                          desc="\033[32m[ + ] Medusa scan progress bar\033[0m"):  # 开启列表中的多线程
                t.start()
                while True:
                    # 判断正在运行的线程数量,如果小于5则退出while循环,
                    # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                    if len([p for p in self.CountList if p.exitcode is None]) < ProcessNumber:
                        break
            for p in tqdm(self.ProcessList, ascii=True, desc="\033[32m[ + ] Medusa cleanup thread progress\033[0m"):
                p.join()
        self.ProcessList.clear()  # 清空列表，防止多次调用导致重复使用


class Prompt:  # 输出横幅，就是每个组件加载后输出的东西
    def __init__(self, name: str):
        self.name = name
        if debug_mode:
            pass
        else:
            sizex, sizey = CommandLineWidth().getTerminalSize()
            prompt = "\033[32m[ + ] Loading attack module: \033[0m" + "\033[35m{}\033[0m".format(self.name)
            PromptSize = sizex - len(prompt) + 18#28
            FillString = ""
            for i in range(0, PromptSize):
                FillString = FillString + " "
            sys.stdout.write("\r" + prompt + FillString)
            time.sleep(0.1)
            sys.stdout.flush()


class CommandLineWidth:  # 输出横幅，就是每个组件加载后输出的东西
    def getTerminalSize(self):
        import platform  # 获取使用这个软件的平台
        current_os = platform.system()  # 获取操作系统的具体类型
        tuple_xy = None
        if current_os == 'Windows':
            tuple_xy = self._getTerminalSize_windows()
            if tuple_xy is None:
                tuple_xy = self._getTerminalSize_tput()
                # needed for window's python in cygwin's xterm!
        if current_os == 'Linux' or current_os == 'Darwin' or current_os.startswith('CYGWIN'):
            tuple_xy = self._getTerminalSize_linux()
        if tuple_xy is None:
            tuple_xy = (80, 25)  # default value
        return tuple_xy

    # 函数名前下划线代表这是一个私有方法 这样我们在导入我们的这个模块的时候 python是不会导入方法名前带有下划线的方法的
    def _getTerminalSize_windows(self):
        res = None
        try:
            from ctypes import windll, create_string_buffer
            """
            STD_INPUT_HANDLE = -10  获取输入的句柄
            STD_OUTPUT_HANDLE = -11 获取输出的句柄
            STD_ERROR_HANDLE = -12  获取错误的句柄
            """
            h = windll.kernel32.GetStdHandle(-12)  # 获得输入、输出/错误的屏幕缓冲区的句柄
            csbi = create_string_buffer(22)
            res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        except:
            return None
        if res:
            import struct
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
        else:
            return None

    # 函数名前下划线代表这是一个私有方法 这样我们在导入我们的这个模块的时候 python是不会导入方法名前带有下划线的方法的

    def _getTerminalSize_tput(self):
        try:
            import subprocess
            proc = subprocess.Popen(["tput", "cols"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            output = proc.communicate(input=None)
            cols = int(output[0])
            proc = subprocess.Popen(["tput", "lines"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            output = proc.communicate(input=None)
            rows = int(output[0])
            return (cols, rows)
        except:
            return None

    def _getTerminalSize_linux(self):
        def ioctl_GWINSZ(fd):
            try:
                import fcntl, termios, struct, os
                cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            except:
                return None
            return cr

        cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
        if not cr:
            try:
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = ioctl_GWINSZ(fd)
                os.close(fd)
            except:
                pass
        if not cr:
            try:
                env = os.environ
                cr = (env['LINES'], env['COLUMNS'])
            except:
                return None
        return int(cr[1]), int(cr[0])


class ErrorHandling:
    def Outlier(self, error, plugin_name):
        self.error = str(error)
        self.plugin_name = plugin_name
        if debug_mode:
            self.Process()
        else:
            pass

    def Process(self):
        if self.error.find("timed out") != -1:
            self.ErrorBanner(self.plugin_name, "connection timeout")
        elif self.error.find("Invalid URL") != -1:
            self.ErrorBanner(self.plugin_name, "prompts url")
        elif self.error.find("getaddrinfo failed") != -1:
            self.ErrorBanner(self.plugin_name, "get addr info failed")
        elif self.error.find("Invalid header") != -1:
            self.ErrorBanner(self.plugin_name, "prompts header")
        else:
            self.ErrorBanner(self.plugin_name, "unknown")

    def ErrorBanner(self, plugin_name, error):
        print("\033[31m[ X ] {} plugin {} error\033[0m".format(plugin_name, error))


class GetRootFileLocation:  # 获取当前文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            RootFileLocation = os.path.split(os.path.realpath(__file__))[0]
            return RootFileLocation
        elif system_type == "linux" or system_type == "darwin":
            RootFileLocation = os.path.split(os.path.realpath(__file__))[0]
            return RootFileLocation

class GetToolFilePath:  # 获取TOOL文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            ToolFileLocation = GetRootFileLocation().Result()+"\\Tool\\"
            return ToolFileLocation
        elif system_type == "linux" or system_type == "darwin":
            ToolFileLocation = GetRootFileLocation().Result()+"/Tool/"
            return ToolFileLocation

class GetTempFilePath:  # 获取Temp文件路径类
    def Result(self) -> str:
        system_type = sys.platform
        if system_type == "win32" or system_type == "cygwin":
            TempFileLocation = GetRootFileLocation().Result()+"\\Temp\\"
            return TempFileLocation
        elif system_type == "linux" or system_type == "darwin":
            TempFileLocation = GetRootFileLocation().Result()+"/Temp/"
            return TempFileLocation

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
                            sid TEXT NOT NULL,\
                            url TEXT NOT NULL,\
                            rank TEXT NOT NULL,\
                            ssid TEXT NOT NULL,\
                            uid TEXT NOT NULL,\
                            name TEXT NOT NULL,\
                            creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ScanInformation(class)_init(def)", e)
    def Write(self,**kwargs)->bool:#写入相关信息
        CreationTime = str(int(time.time())) # 创建时间
        Url=kwargs.get("url")
        Ssid=kwargs.get("ssid")
        Uid = kwargs.get("uid")
        Sid = kwargs.get("sid")
        Rank = kwargs.get("rank")
        Name= kwargs.get("name")
        try:
            self.cur.execute("INSERT INTO ScanInformation(sid,url,rank,ssid,uid,name,creation_time)\
            VALUES (?,?,?,?,?,?,?)",(Sid,Url,Rank,Ssid,Uid,Name,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True#获取主键的ID值，也就是sid的值
        except Exception as e:
            ErrorLog().Write("ClassCongregation_ScanInformation(class)_Write(def)", e)
            return False
    def Query(self,**kwargs)->str or None:#查询相关表内容

        Uid=kwargs.get("uid")
        Sid = kwargs.get("sid")
        try:
            self.cur.execute("select * from ScanInformation where uid =? and sid = ?", (Uid,Sid,))
            result_list = []  # 存放json的返回结果列表用
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["url"] = i[2]
                JsonValues["ssid"] = i[4]
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
            self.sid=kwargs.get("Sid")# 传入的父表SID
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
                            sid TEXT NOT NULL,\
                            uid TEXT NOT NULL)")
            except Exception as e:
                ErrorLog().Write("ClassCongregation_SubdomainTable(class)_init(def)_CREATETABLE", e)
        except Exception as e:
            ErrorLog().Write("ClassCongregation_SubdomainTable(class)_init(def)", e)

    def Write(self):  # 统一写入
        try:
            self.cur.execute("""INSERT INTO Subdomain (url,subdomain,timestamp,sid,uid) \
            VALUES (?,?,?,?,?)""", (self.url, self.subdomain,self.timestamp,self.sid,self.uid,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
            ErrorLog().Write("ClassCongregation_SubdomainTable(class)_Write(def)", e)

class ExploitOutput:#命令执行内容处理
    def Command(self):#子进程无法使用imput函数
        #print("\033[32m[ + ] Please enter the command to be executed: \033[0m")
        Command=input("\033[32m[ + ] Please enter the command to be executed: \033[0m")
        if Command=="QuitMedusa":
            print("\033[33m[ ! ] Command execution call has ended~ \033[0m")
            os._exit(0)  # 直接退出整个函数
        elif Command!=None:
            return str(Command)
        else:
            print("\033[31m[ ! ] Command cannot be empty! \033[0m")

    def Deserialization(self):
        LoadExploitURL=input("\033[32m[ + ] Please enter the exploit URL to be loaded \033[0m"+"\033[31m[Prohibit adding http or https ]\033[0m"+"\033[32m: \033[0m")
        if LoadExploitURL != None:
            return str(LoadExploitURL)
        else:
            print("\033[31m[ ! ] Please refer to the following example :\033[0m"+"\033[36m 127.0.0.1:80/exp \033[0m" )
    def OperatingSystem(self):
        OperatingSystem=input("\033[33m[ + ] Please enter the target operating system [windows / linux]: \033[0m").lower()#转换成小写

        if OperatingSystem != None and (OperatingSystem=="windows" or OperatingSystem=="linux"):
            return str(OperatingSystem)
        else:
            print("\033[31m[ ! ] Please enter windows or linux! \033[0m")
    def Banner(self,**kwargs):
        print("\033[32m[ + ] Command sent successfully, please refer to the returned data packet\033[0m")
        if kwargs.get("OutputData")==None:
            print("\033[36m[ + ] Return packet：The vulnerability is command execution without echo\033[0m")
        else:
            print("\033[36m[ + ] Return packet：\033[0m"+kwargs.get("OutputData"))