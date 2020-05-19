# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sqlite3
from ClassCongregation import GetDatabaseFilePath,ErrorLog,randoms



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
                            token TEXT NOT NULL,\
                            show_name TEXT NOT NULL,\
                            passwd TEXT NOT NULL,\
                            email TEXT NOT NULL,\
                            img_path TEXT NOT NULL,\
                            key_update_time TEXT NOT NULL,\
                            passwd_update_time TEXT NOT NULL,\
                            email_update_time TEXT NOT NULL,\
                            show_name_update_time TEXT NOT NULL,\
                            img_path_update_time TEXT NOT NULL,\
                            token_update_time TEXT NOT NULL,\
                            creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_init(def)",e)
    def VerifyUsername(self,Name:str)->bool or None:#查询用户名是否存在，True表示有数据，False只表示用户不存在，None表示报错
        try:
            self.cur.execute("select * from UserInfo where name =? ", (Name,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_VerifyUsername(def)", e)
            return None
    def VerifyEmail(self,Email:str)->bool or None:#查询邮箱是否存在，True表示有数据，False表示邮箱不存在，None表示报错
        try:
            self.cur.execute("select * from UserInfo where email =?", (Email,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_VerifyEmail(def)", e)
            return None
    def UserLogin(self,Username,Passwd)->str or None:#用户登录，如果登录成功返回Token，如果失败返回None
        try:
            self.cur.execute("select * from UserInfo where name =? and passwd=?", (Username,Passwd,))
            for tuple in self.cur.fetchall():
                return tuple[4] # 返回Token
            return None
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UserLogin(def)", e)
            return None
    def WhetherTheKeyConflicts(self,Key:str)->bool:#查询用户kEY是否存在，True表示有数据，False表示各种问题
        try:
            self.cur.execute("select * from UserInfo where key =?", (Key,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_WhetherTheKeyConflicts(def)", e)
            return False
    def Write(self,**kwargs:str)->bool or None:#写入新用户，True表示成功，False表示用户已存在，None表示报错
        CreationTime = str(int(time.time())) # 创建时间
        Uid=randoms().result(100)
        Name=kwargs.get("name")
        ShowName=kwargs.get("show_name")
        Passwd=kwargs.get("passwd")
        Email=kwargs.get("email")
        ImgPath=kwargs.get("img_path")
        Key=randoms().result(40)
        Token=kwargs.get("token")#这个是用来验证用户登录的
        while True:#判断Key否存在
            if not self.WhetherTheKeyConflicts(Key):#如果未找到就跳出循环进行下去
                break
            Key = randoms().result(40)
        try:
            self.cur.execute("INSERT INTO UserInfo(uid,key,token,name,show_name,passwd,email,img_path,key_update_time,passwd_update_time,email_update_time,show_name_update_time,img_path_update_time,token_update_time,creation_time)\
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Uid,Key,Token,Name,ShowName, Passwd,Email,ImgPath,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)__Write(def)", e)
            return None
    def UpdatePasswd(self,**kwargs:str)->bool:#更新用户密码，True表示成功，False表示失败
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
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UpdatePasswd(def)", e)
                return False
        else:return False
    def UpdateShowName(self,**kwargs:str)->bool:#更新用户显示名字，True表示成功，False表示失败
        Name = kwargs.get("name")
        ShowName = kwargs.get("show_name")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and ShowName!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET show_name = ? , show_name_update_time = ? WHERE name= ?""", (ShowName,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UpdateShowName(def)", e)
                return False
        else:return False
    def UpdateEmail(self,**kwargs:str)->bool:#更新用户邮箱，True表示成功，False表示失败
        Name = kwargs.get("name")
        Email = kwargs.get("email")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and Email!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET email = ? , email_update_time = ? WHERE name= ?""", (Email,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UpdateEmail(def)", e)
                return False
        else:return False
    def UpdateImgPath(self,**kwargs:str)->bool:#更新用户头像路径，True表示成功，False表示各失败
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
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UpdateImgPath(def)", e)
                return False
        else:return False
    def UpdateKey(self,**kwargs:str)->bool:#更新用户Key，True表示成功，False表示失败
        Name = kwargs.get("name")
        Key= kwargs.get("key")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and Key!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET key = ? , key_update_time = ? WHERE name= ?""", (Key,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UpdateKey(def)", e)
                return False
        else:return False
    def UpdateToken(self,**kwargs:str)->bool:#更新用户Token，True表示成功，False表示失败
        Name = kwargs.get("name")
        Token= kwargs.get("token")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and Token!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET token = ? , token_update_time = ? WHERE name= ?""", (Token,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UpdateToken(def)", e)
                return False
        else:return False
    def QueryTokenCreationTime(self,**kwargs:str)->bool or None:#查询用户Token创建时间，True表示Token不能用，False表示Token还能用
        Name = kwargs.get("name")
        Token= kwargs.get("token")
        Time = int(time.time())  # 获取当前时间
        if Name!=None and Token!=None:
            try:
                self.cur.execute("select * from UserInfo where name =? and token = ?", (Name, Token,))
                for tuple in self.cur.fetchall():
                    ExpireDate=Time-int(tuple[14])#获取时间差
                    if ExpireDate<5000:
                        return False#返回False表示还可以用

                return True#如果为找到数据，返回True，表示需要重新写入或者登录
            except Exception as e:
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_QueryTokenCreationTime(def)", e)
                return None
        else:return True#报错返回True
    def TokenAuthentication(self,**kwargs:str)->bool or None:#查询用户Token是否存在,存在返回True,不存在返回False,报错返回None
        Token= kwargs.get("token")
        if Token!=None:
            try:
                self.cur.execute("select * from UserInfo where token =?", (Token,))
                if self.cur.fetchall():  # 判断是否有数据
                    self.con.close()
                    return True
                else:
                    return False
            except Exception as e:
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_TokenAuthentication(def)", e)
                return None
        else:return False
    def QueryTokenValidity(self,Token:str)->bool or None:#用来查询Token是否重复了
        try:
            self.cur.execute("select * from UserInfo where token =?", (Token,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_QueryTokenValidity(def)", e)
            return None
    def QueryUserNameWithToken(self,Token:str):#利用Token反向查用户名
        try:
            self.cur.execute("select * from UserInfo where token =?", (Token,))
            for tuple in self.cur.fetchall():
                return tuple[1]
            return None
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_QueryTokenValidity(def)", e)
            return None



class ActiveScanList:#用户主动扫描网站信息列表,写入父表中的SID
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
                            creation_time TEXT NOT NULL,\
                            proxy TEXT NOT NULL,\
                            status TEXT NOT NULL,\
                            threads TEXT NOT NULL,\
                            module TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_init(def)", e)
    def Write(self,**kwargs):#写入相关信息,如果写入成功返回Sid值，如果失败返回None
        CreationTime = str(int(time.time())) # 创建时间
        Uid=kwargs.get("uid")
        Url=kwargs.get("url")
        Proxy=kwargs.get("proxy")
        Status = kwargs.get("status")
        Module = kwargs.get("module")
        Threads = kwargs.get("threads")
        try:
            self.cur.execute("INSERT INTO ActiveScanList(uid,url,creation_time,proxy,status,threads,module)\
            VALUES (?,?,?,?,?,?,?)",(Uid,Url,CreationTime,Proxy,Status,Threads,Module,))
            # 提交
            GetSid=self.cur.lastrowid  # 获取主键的ID值，也就是sid的值
            self.con.commit()
            self.con.close()
            return GetSid#获取主键的ID值，也就是sid的值
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_Write(def)", e)
            return None
    def Query(self,**kwargs):#通过UID来查询信息
        Uid = kwargs.get("uid")
        try:
            self.cur.execute("select * from ActiveScanList where uid =? ", (Uid,))
            result_list = []  # 存放json的返回结果列表用
            for i in self.cur.fetchall():
                json_values = {}
                json_values["url"] = i[2]
                json_values["creation_time"] = i[3]
                json_values["proxy"] = i[4]
                json_values["status"] = i[5]
                json_values["threads"] = i[6]
                json_values["module"] = i[7]
                result_list.append(json_values)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_Query(def)", e)
            return None

    def UpdateStatus(self,Status:str,Sid:int)->bool:#利用主键ID来判断后更新数据
        try:
            self.cur.execute("""UPDATE UserInfo SET status = ? WHERE sid= ?""",(Status, str(Sid),))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_UpdateStatus(def)", e)
            return False

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
                            ssid TEXT NOT NULL,\
                            creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ScanInformation(class)_init(def)", e)
    def Write(self,**kwargs)->bool:#写入相关信息
        CreationTime = str(int(time.time())) # 创建时间
        Url=kwargs.get("url")
        Ssid=kwargs.get("ssid")
        Sid = kwargs.get("sid")
        try:
            self.cur.execute("INSERT INTO ScanInformation(sid,url,ssid,creation_time)\
            VALUES (?,?,?,?)",(Sid,Url,Ssid,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True#获取主键的ID值，也就是sid的值
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ScanInformation(class)_Write(def)", e)
            return False

#验证用户-》读取UID，然后用UID启动扫描，然后在用UID插入各个表中
class MedusaQuery:#单个漏洞的详细内容查询表，具体写入表在ClassCongregation文件中，改表是个查询数据表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
    def Query(self, **kwargs):
        try:
            Sid = kwargs.get("sid")
            Uid = kwargs.get("uid")
            self.cur.execute("select * from Medusa where uid =? and sid = ?", (Uid, Sid,))
            result_list = []  # 存放json的返回结果列表用
            for i in self.cur.fetchall():
                json_values = {}
                json_values["ssid"] = i[0]
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
                json_values["sid"] = i[15]
                json_values["uid"] = i[16]
                result_list.append(json_values)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MedusaQuery(class)_Query(def)", e)
            return None

class PassiveScanInformation:#用户被动扫描相关信息
    pass