import nmap
import pymysql
import urllib.parse
import sqlite3
import os

def IpProcess(Url):
    if Url.startswith("http"):  # 记个小知识点：必须带上https://这个头不然urlparse就不能正确提取hostname导致后面运行出差错
        res = urllib.parse.urlparse(Url)  # 小知识点2：如果只导入import urllib包使用parse这个类的话会报错，必须在import requests导入这个包才能正常运行
    else:
        res = urllib.parse.urlparse('http://%s' % Url)
    return (res.hostname)


class NmapScan:#扫描端口类
    def __init__(self,Url,Port):
        Host=IpProcess(Url)#调用IP处理函数
        self.Host= Host#提取后的网址或者IP
        self.Port = "1-65535"#如果用户没输入就扫描全端口

    def ScanPort(self):
        try:
            Nmap = nmap.PortScanner()
            ScanResult = Nmap.scan(self.Host, self.Port, '-sV')

            for list in ScanResult['scan'][self.Host]['tcp']:
                FinalResults = list  # list为每个tcp列表的值(但是tcp列表里面还有值)
                state=ScanResult['scan'][self.Host]['tcp'][FinalResults]['state']
                name=ScanResult['scan'][self.Host]['tcp'][FinalResults]['name']
                print(FinalResults)
                print(state)
                print(name)


        except IOError:
             print("Please enter the correct nmap scan command.")


class NmapDB:#NMAP的数据库
    def __init__(self,Nmap,port,ip):
        self.state = Nmap['state']  # 漏洞名称
        self.reason = Nmap['reason']  # 结果
        self.name = Nmap['name']  # 漏洞组件
        self.product = Nmap['product']  # 漏洞组件
        self.version = Nmap['version']  # 漏洞组件
        self.extrainfo = Nmap['extrainfo']  # 漏洞组件
        self.conf = Nmap['conf']  # 漏洞组件
        self.cpe = Nmap['cpe']  # 漏洞组件
        self.port = port  # 漏洞组件
        self.port = ip  # 漏洞组件

        # 如果数据库不存在的话，将会自动创建一个 数据库
        self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE Nmap\
                        (ip INTEGER NOT NULL,\
                        state TEXT NOT NULL,\
                        port TEXT NOT NULL,\
                        reason TEXT,\
                        name TEXT,\
                        product TEXT,\
                        version TEXT,\
                        extrainfo TEXT,\
                        conf TEXT,\
                        cpe TEXT)")
        except:
            pass

    def serious(self):
        try:

            sql_insert = """INSERT INTO Medusa (id,name,affects,rank,suggest,desc_content,details) \
    VALUES (4,'{}','{}','严重','{}','{}','{}')""".format()
            self.cur.execute(sql_insert)
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass



NmapScan("127.0.0.1","445").ScanPort()