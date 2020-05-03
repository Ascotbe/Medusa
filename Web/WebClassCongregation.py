import time
import sys
import os
import base64
import sqlite3
from ClassCongregation import GetDatabaseFilePath
class SessionKey:
    def __init__(self,username,session_key,session_time):
        self.username=username
        self.session_key=session_key
        self.session_time=session_time
        if sys.platform == "win32" or sys.platform == "cygwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
        elif sys.platform=="linux" or sys.platform=="darwin":
            self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "/Medusa.db")
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE session_key\
                        (username TEXT PRIMARY KEY,\
                        session_key TEXT,\
                        session_time TEXTL)")
        except:
            pass
    def write(self):#把验证后的两个session写入数据库中
        try:

            # sql_insert = """INSERT INTO Nmap (domain,ip,port,state,name,product,reason,version,extrainfo,conf,cpe) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.domain,self.ip,self.port,self.state,self.name,self.product,self.reason,self.version,self.extrainfo,self.conf,self.cpe)
            self.cur.execute("""INSERT INTO session_key (username,session_key,session_time) VALUES (?,?,?)""",(self.username, self.session_key, self.session_time,))
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass
    def read(self):#对传入的两个session进行验证
        try:
            self.cur.execute("select * from session_key where username =?", (self.username,))
            values = self.cur.fetchall()
            for i in values:
                if i[0]==self.username and self.session_key==i[1] and self.session_time==i[2]:
                    self.con.close()
                    return 1
            self.con.close()
            return 0
        except:
            return 0

class VulnerabilityInquire:#数据库查询仅限于web版
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
    def Inquire(self,token):
        try:
            self.cur.execute("select * from Medusa where token =?",(str(token),))
            values = self.cur.fetchall()
            result_list = []  # 存放json的返回结果列表用

            for i in values:
                json_values = {}
                json_values["url"] = i[1]
                json_values["name"] = i[2]
                json_values["affects"] = i[3]
                json_values["rank"] = i[4]
                json_values["suggest"] = i[5]
                json_values["desc_content"] = i[6]
                json_values["details"] = i[7]
                json_values["number"] = i[8]
                json_values["author"] = i[9]
                json_values["create_date"] = i[10]
                json_values["disclosure"] = i[11]
                json_values["algroup"] = i[12]
                json_values["version"] = i[13]
                json_values["timestamp"] = i[14]
                json_values["token"] = i[15]
                result_list.append(json_values)
            self.con.close()
            return result_list
        except:
            return ""

class login:#登录
    def __init__(self,username):
        self.username=username
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
    def logins(self):#根据数据进行查询用户名和数据库是否相等
        self.cur.execute("select * from user_info where user =?",(self.username,))
        values = self.cur.fetchall()
        try:
            global passwd
            for i in values:
                passwd= i[1]#获取密码
            if passwd!=None:#判断是否在数据库中
                self.con.close()
                return passwd
        except:
            return 0
class UserTable:#注册
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE UserInfo\
                            (id INTEGER PRIMARY KEY,\
                            username TEXT NOT NULL,\
                            password TEXT NOT NULL,\
                            mailbox TEXT NOT NULL,\
                            token TEXT NOT NULL,\
                            creation_time TEXT NOT NULL,\
                            update_time TEXT NOT NULL)")
        except:
            pass
    def WriteUser(self,username,password,mailbox,token):#写入新用户
        CreationTime = str(int(time.time())) # 创建时间
        self.AccountToken = token  # 生成的token
        try:
            self.cur.execute("INSERT INTO UserInfo(username,password,mailbox,token,creation_time,update_time)\
            VALUES (?,?,?,?,?,?)",(username, password,mailbox,token,CreationTime,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except:
            return False
    def UpdateUser(self,username,token,password):#更新用户密码token
        try:
            self.cur.execute("""UPDATE UserInfo SET password = ?,token=?,update_time=? WHERE username= ?""", (password,token,str(int(time.time())),username,))
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass
    def CheckUserPresence(self,inquire_user,inquire_mailbox):#查询用户是否存在
        try:
            self.cur.execute("select * from UserInfo where username =? and mailbox = ?",(inquire_user,inquire_mailbox,))
            if self.cur.fetchall():#判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except:
            return False
    def CheckUserToken(self,token):
        try:
            self.cur.execute("select * from UserInfo where token =?", (token,))
            if self.cur.fetchall():#判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except:
            return False

class UserScansWebsiteTable:#用户扫描了哪些网站，时间，模块
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE UserScansWebsite\
                            (id INTEGER PRIMARY KEY,\
                            token TEXT NOT NULL,\
                            url TEXT NOT NULL,\
                            creation_time TEXT NOT NULL,\
                            module TEXT NOT NULL)")
        except:
            pass
    def Write(self,token,url,creation_time,module):#写入新用户
        self.AccountToken = token  # 生成的token
        try:
            self.cur.execute("INSERT INTO UserScansWebsite(token,url,creation_time,module)\
            VALUES (?,?,?,?)",(token,url,creation_time,module,))
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass