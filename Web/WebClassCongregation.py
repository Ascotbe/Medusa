import time
import sys
import os
import sqlite3
from ClassCongregation import GetDatabaseFilePath,ErrorLog,randoms
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
class UserInfo:#用户表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE UserInfo\
                            (id INTEGER PRIMARY KEY,\
                            uid TEXT NOT NULL,\
                            key TEXT NOT NULL,\
                            name TEXT NOT NULL,\
                            show_name TEXT NOT NULL,\
                            passwd TEXT NOT NULL,\
                            email TEXT NOT NULL,\
                            img_path TEXT NOT NULL,\
                            key_update_time TEXT NOT NULL,\
                            passwd_update_time TEXT NOT NULL,\
                            email_update_time TEXT NOT NULL,\
                            show_name_update_time TEXT NOT NULL,\
                            img_path_update_time TEXT NOT NULL,\
                            creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("WebClass_UserInfo_init",e)
    def WhetherUsersConflict(self,Name,Email):#查询用户是否存在
        try:
            self.cur.execute("select * from UserInfo where name =? and email = ?",(Name,Email,))
            if self.cur.fetchall():#判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
                ErrorLog().Write("WebClass_UserInfo_WhetherUsersConflict", e)
    def WhetherTheKeyConflicts(self,Key):#查询用户kEY是否存在
        try:
            self.cur.execute("select * from UserInfo where key =?", (Key,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("WebClass_UserInfo_WhetherTheKeyConflicts", e)
    def Write(self,**kwargs:str)->bool:#写入新用户
        CreationTime = str(int(time.time())) # 创建时间
        Uid=randoms().result(100)
        Name=kwargs.get("name")
        ShowName=kwargs.get("show_name")
        Passwd=kwargs.get("passwd")
        Email=kwargs.get("email")
        ImgPath=kwargs.get("img_path")
        Key=randoms().result(40)
        UserInformationJudgment=self.WhetherUsersConflict(Name,Email)#判断用户是否存在
        while True:#判断Key否存在
            if not self.WhetherTheKeyConflicts(Key):#如果未找到就跳出循环进行下去
                break
            Key = randoms().result(40)

        if UserInformationJudgment:#如果找到返回False
            return False
        elif not UserInformationJudgment:#如果没找到写入数据
            try:
                self.cur.execute("INSERT INTO UserInfo(uid,key,name,show_name,passwd,email,img_path,key_update_time,passwd_update_time,email_update_time,show_name_update_time,img_path_update_time,creation_time)\
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(Uid,Key,Name,ShowName, Passwd,Email,ImgPath,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("WebClass_UserInfo_Write", e)
    def UpdatePasswd(self,**kwargs:str)->bool:#更新用户密码
        Name = kwargs.get("name")
        Passwd = kwargs.get("passwd")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and Passwd!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET passwd = ? , passwd_update_time = ? WHERE name= ?""", (Passwd,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("WebClass_UserInfo_UpdatePasswd", e)
        else:return False
    def UpdateShowName(self,**kwargs:str)->bool:#更新用户显示名字
        Name = kwargs.get("name")
        ShowName = kwargs.get("show_name")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and ShowName!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET show_name = ? , show_name_update_time = ?WHERE name= ?""", (ShowName,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("WebClass_UserInfo_UpdateShowName", e)
        else:return False
    def UpdateEmail(self,**kwargs:str)->bool:#更新用户邮箱
        Name = kwargs.get("name")
        Email = kwargs.get("email")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and Email!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET email = ? , email_update_time = ?WHERE name= ?""", (Email,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("WebClass_UserInfo_UpdateEmail", e)
        else:return False
    def UpdateImgPath(self,**kwargs:str)->bool:#更新用户头像路径
        Name = kwargs.get("name")
        ImgPath = kwargs.get("img_path")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and ImgPath!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET img_path = ?, img_path_update_time = ? WHERE name= ?""", (ImgPath,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("WebClass_UserInfo_UpdateImgPath", e)
        else:return False
    def UpdateKey(self,**kwargs:str)->bool:#更新用户Key
        Name = kwargs.get("name")
        Key= kwargs.get("key")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and Key!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET key = ? , key_update_time = ?WHERE name= ?""", (Key,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("WebClass_UserInfo_UpdateKey", e)
        else:return False



class ActiveScanList:#用户主动扫描相关信息表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE ActiveScanList\
                            (sid INTEGER PRIMARY KEY,\
                            uid TEXT NOT NULL,\
                            url TEXT NOT NULL,\
                            key TEXT NOT NULL,\
                            creation_time TEXT NOT NULL,\
                            proxy TEXT NOT NULL,\
                            status TEXT NOT NULL,\
                            module TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("WebClass_ActiveScanList_init", e)
    def Write(self,**kwargs)->int:#写入相关信息
        CreationTime = str(int(time.time())) # 创建时间
        Uid=kwargs.get("uid")
        Url=kwargs.get("url")
        Key=kwargs.get("key")
        Proxy=kwargs.get("proxy")
        Status = kwargs.get("status")
        Module = kwargs.get("module")
        try:
            self.cur.execute("INSERT INTO ActiveScanList(uid,url,key,creation_time,proxy,status,module)\
            VALUES (?,?,?,?,?,?,?)",(Uid,Url,Key,CreationTime,Proxy,Status,Module,))
            # 提交
            GetSid=self.cur.lastrowid  # 获取主键的ID值，也就是sid的值
            self.con.commit()
            self.con.close()
            return GetSid#获取主键的ID值，也就是sid的值
        except Exception as e:
            ErrorLog().Write("WebClass_ActiveScanList_Write", e)
    def UpdateStatus(self,Status:str,Sid:int)->bool:#利用主键ID来判断后更新数据
        try:
            self.cur.execute("""UPDATE UserInfo SET status = ? WHERE sid= ?""",(Status, str(Sid),))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("WebClass_ActiveScanList_UpdateStatus", e)
            return False

class ScanInformation:#单独网站详细扫描内容
    pass

class PassiveScanInformation:#用户被动扫描相关信息
    pass