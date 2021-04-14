# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
import base64
import sqlite3
import json
from ClassCongregation import GetDatabaseFilePath,ErrorLog,randoms,GetRootFileLocation,GetNistDatabaseFilePath
from config import domain_name_system_address

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
                            avatar TEXT NOT NULL,\
                            key_update_time TEXT NOT NULL,\
                            passwd_update_time TEXT NOT NULL,\
                            email_update_time TEXT NOT NULL,\
                            show_name_update_time TEXT NOT NULL,\
                            avatar_update_time TEXT NOT NULL,\
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
        Avatar=kwargs.get("avatar")
        Key=randoms().result(40)
        Token=kwargs.get("token")#这个是用来验证用户登录的
        while True:#判断Key否存在
            if not self.WhetherTheKeyConflicts(Key):#如果未找到就跳出循环进行下去
                break
            Key = randoms().result(40)
        try:
            self.cur.execute("INSERT INTO UserInfo(uid,key,token,name,show_name,passwd,email,avatar,key_update_time,passwd_update_time,email_update_time,show_name_update_time,avatar_update_time,token_update_time,creation_time)\
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Uid,Key,Token,Name,ShowName, Passwd,Email,Avatar,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_Write(def)", e)
            return None
    def UpdatePasswd(self,**kwargs:str)->bool:#更新用户密码，True表示成功，False表示失败
        Name = kwargs.get("name")
        OldPasswd = kwargs.get("old_passwd")
        NewPasswd = kwargs.get("new_passwd")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and OldPasswd!=None and NewPasswd!=None:
            try:
                self.cur.execute("select * from UserInfo where name =? and passwd=?", (Name,OldPasswd))
                if self.cur.fetchall():  # 判断是否有数据
                    try:#有数据的话就改密码
                        self.cur.execute("""UPDATE UserInfo SET passwd = ? , passwd_update_time = ? WHERE name= ?""", (NewPasswd,UpdateTime,Name,))
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
                        ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UpdatePasswd(def)ChangePassword", e)
                        return False
                else:
                    return False
            except Exception as e:
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UpdatePasswd(def)QueryPassword", e)
                return False
        else:return False
    def UpdateShowName(self,**kwargs:str)->bool:#更新用户显示名字，True表示成功，False表示失败
        Uid = kwargs.get("uid")
        ShowName = kwargs.get("show_name")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Uid!=None and ShowName!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET show_name = ? , show_name_update_time = ? WHERE uid= ?""", (ShowName,UpdateTime,Uid,))
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
                if self.cur.rowcount < 1:  # 用来判断是否更新成功
                    self.con.commit()
                    self.con.close()
                    return False
                else:
                    self.con.commit()
                    self.con.close()
                    return True
            except Exception as e:
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UpdateEmail(def)", e)
                return False
        else:return False
    def UpdateAvatar(self,**kwargs:str)->bool:#更新用户头像路径，True表示成功，False表示各失败
        Uid = kwargs.get("uid")
        Avatar = kwargs.get("avatar")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Uid!=None and Avatar!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET avatar = ?, avatar_update_time = ? WHERE uid= ?""", (Avatar,UpdateTime,Uid,))
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
                ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_UpdateImgPath(def)", e)
                return False
        else:return False
    def UpdateKey(self,**kwargs:str)->bool:#更新用户Key，True表示成功，False表示失败
        Uid = kwargs.get("uid")
        Key= kwargs.get("key")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Uid!=None and Key!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET key = ? , key_update_time = ? WHERE uid= ?""", (Key,UpdateTime,Uid,))
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
                if self.cur.rowcount < 1:  # 用来判断是否更新成功
                    self.con.commit()
                    self.con.close()
                    return False
                else:
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
    def QueryUidWithToken(self,Token:str):#利用Token反向查唯一的UID
        try:
            self.cur.execute("select * from UserInfo where token =?", (Token,))
            for tuple in self.cur.fetchall():
                return tuple[1]
            return None
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_QueryUidWithToken(def)", e)
            return None
    def QueryUserInfo(self,Token:str):#利用Token,查询完整的用户信息，除了更新时间都有
        try:
            self.cur.execute("select * from UserInfo where token =?", (Token,))
            for tuple in self.cur.fetchall():
                JsonValues = {}
                JsonValues["id"] = tuple[0]
                JsonValues["uid"] = tuple[1]
                JsonValues["key"] = tuple[2]
                JsonValues["name"] = tuple[3]
                JsonValues["token"] = tuple[4]
                JsonValues["show_name"] = tuple[5]
                JsonValues["passwd"] = tuple[6]
                JsonValues["email"] = tuple[7]
                JsonValues["avatar"] = tuple[8]
                return JsonValues#由于用户信息不可能有多个的所有这边直接返回
            return None#如果没查到数据就返回空
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_QueryUserInfo(def)", e)
            return None
    def ForgetPassword(self,**kwargs):#忘记密码函数
        Name = kwargs.get("name")
        NewPasswd=kwargs.get("new_passwd")
        Email=kwargs.get("email")
        UpdateTime = str(int(time.time()))  # 修改时间
        try:
            self.cur.execute("""UPDATE UserInfo SET passwd = ? , passwd_update_time = ? WHERE name= ? and email=?""",
                             (NewPasswd, UpdateTime, Name,Email,))
            # 提交
            if self.cur.rowcount < 1:#用来判断是否更新成功
                self.con.commit()
                self.con.close()
                return False
            else:
                self.con.commit()
                self.con.close()
                return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserInfo(class)_ForgetPassword(def)", e)
            return False



class ActiveScanList:#用户主动扫描网站信息列表,写入父表中的SID
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE ActiveScanList\
                            (active_scan_id INTEGER PRIMARY KEY,\
                            uid TEXT NOT NULL,\
                            url TEXT NOT NULL,\
                            creation_time TEXT NOT NULL,\
                            proxy TEXT NOT NULL,\
                            status TEXT NOT NULL,\
                            process TEXT NOT NULL,\
                            module TEXT NOT NULL,\
                            redis_id TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_init(def)", e)
    def Write(self,**kwargs):#写入相关信息,如果写入成功返回Sid值，如果失败返回None
        CreationTime = str(int(time.time())) # 创建时间
        Uid=kwargs.get("uid")
        Url=kwargs.get("url")
        Proxy=kwargs.get("proxy")
        Status = kwargs.get("status")
        Module = kwargs.get("module")
        Process = kwargs.get("process")
        RedisId=""#先吧RedisID传空，后面在更新RedisID
        try:
            self.cur.execute("INSERT INTO ActiveScanList(uid,url,creation_time,proxy,status,process,module,redis_id)\
            VALUES (?,?,?,?,?,?,?,?)",(Uid,Url,CreationTime,Proxy,Status,Process,Module,RedisId,))
            # 提交
            GetActiveScanId=self.cur.lastrowid  # 获取主键的ID值，也就是active_scan_id的值
            self.con.commit()
            self.con.close()
            return GetActiveScanId#获取主键的ID值，也就是sid的值
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_Write(def)", e)
            return None
    def Query(self,**kwargs):#通过UID来查询信息
        Uid = kwargs.get("uid")
        try:
            self.cur.execute("select * from ActiveScanList where uid =? ", (Uid,))
            result_list = []  # 存放json的返回结果列表用
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["active_scan_id"] = i[0]
                JsonValues["url"] = i[2]
                JsonValues["creation_time"] = i[3]
                JsonValues["proxy"] = i[4]
                JsonValues["status"] = i[5]
                JsonValues["process"] = i[6]
                JsonValues["module"] = i[7]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_Query(def)", e)
            return None

    def UpdateRedisId(self,**kwargs):#更新redis id的值后面用来更新扫描状态
        Uid = kwargs.get("uid")
        ActiveScanId=kwargs.get("active_scan_id")
        RedisId=kwargs.get("redis_id")
        try:
            self.cur.execute("""UPDATE ActiveScanList SET redis_id = ? WHERE active_scan_id= ? and uid=?""",(RedisId,ActiveScanId,Uid,))
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
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_UpdateRedisId(def)", e)
            return False

    def UpdateStatus(self,**kwargs)->bool:#利用主键ID来判断后更新数据
        RedisId = kwargs.get("redis_id")
        try:
            self.cur.execute("""UPDATE ActiveScanList SET status = ? WHERE redis_id= ?""",("1", RedisId,))
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
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_UpdateStatus(def)", e)
            return False



#通过scan_info_id和uid来查询
class MedusaQuery:#单个漏洞的详细内容查询表，具体写入表在ClassCongregation文件中，该表是个查询数据表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
    def Query(self, **kwargs)->None or list:
        try:
            ScanInfoId = kwargs.get("scan_info_id")
            Uid = kwargs.get("uid")
            self.cur.execute("select * from Medusa where uid =? and scan_info_id = ?", (Uid, ScanInfoId,))
            result_list = []  # 存放json的返回结果列表用
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["scan_info_id"] = i[0]
                JsonValues["url"] = i[1]
                JsonValues["name"] = i[2]
                JsonValues["affects"] = i[3]
                JsonValues["rank"] = i[4]
                JsonValues["suggest"] = i[5]
                JsonValues["desc_content"] = i[6]
                JsonValues["details"] = i[7]
                JsonValues["number"] = i[8]
                JsonValues["author"] = i[9]
                JsonValues["create_date"] = i[10]
                JsonValues["disclosure"] = i[11]
                JsonValues["algroup"] = i[12]
                JsonValues["version"] = i[13]
                JsonValues["timestamp"] = i[14]
                #JsonValues["active_scan_id"] = i[15]
                JsonValues["response_headers"] = i[17]
                JsonValues["response_text"] = i[18]
                JsonValues["response_byte"] = i[19]
                JsonValues["response_status_code"] = i[20]
                JsonValues["request_path_url"] = i[21]
                JsonValues["request_body"] = i[22]
                JsonValues["request_method"] = i[23]
                JsonValues["request_headers"] = i[24]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MedusaQuery(class)_Query(def)", e)
            return None
    def QueryBySid(self, **kwargs):#生成word文档数据查询
        try:
            ActiveScanId = kwargs.get("active_scan_id")
            Uid = kwargs.get("uid")
            self.cur.execute("select * from Medusa where uid =? and active_scan_id = ?", (Uid, ActiveScanId,))
            result_list = []  # 存放json的返回结果列表用
            url=""
            for i in self.cur.fetchall():
                JsonValues = {}
                url= i[1]
                JsonValues["vulnerability_name"] = i[2]
                JsonValues["vulnerability_level"] = i[4]
                JsonValues["repair_suggestions"] = i[5]
                JsonValues["vulnerability_description"] = i[6]
                JsonValues["vulnerability_details"] = i[7]
                JsonValues["find_the_time"] = i[14]
                result_list.append(JsonValues)
            self.con.close()
            return result_list,url
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MedusaQuery(class)_QueryBySid(def)", e)
            return None

class RequestLog:#操作日志
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE RequestLog\
                            (id INTEGER PRIMARY KEY,\
                            request_api TEXT NOT NULL,\
                            creation_time TEXT NOT NULL,\
                            header TEXT NOT NULL,\
                            request_ip TEXT NOT NULL,\
                            request_method TEXT NOT NULL,\
                            request_url TEXT NOT NULL,\
                            post_date TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_RequestRecord(class)_init(def)", e)
    def Write(self,**kwargs)->bool or None:#写入相关信息,如果写入成功返回Sid值，如果失败返回None
        CreationTime = str(int(time.time())) # 创建时间
        RequestApi=kwargs.get("request_api")
        Header=kwargs.get("header")
        RequestIp = kwargs.get("request_ip")
        RequestMethod = kwargs.get("request_method")
        PostDate = kwargs.get("post_date")
        RequestUrl = kwargs.get("request_url")
        try:
            self.cur.execute("INSERT INTO RequestLog(request_api,creation_time,header,request_ip,request_method,request_url,post_date)\
            VALUES (?,?,?,?,?,?,?)",(RequestApi,CreationTime,Header,RequestIp,RequestMethod,RequestUrl,PostDate,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_RequestRecord(class)_Write(def)", e)
            return None

class UserOperationLog:#用户操作日志
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE UserOperationLog\
                            (id INTEGER PRIMARY KEY,\
                            uid TEXT NOT NULL,\
                            request_api TEXT NOT NULL,\
                            creation_time TEXT NOT NULL,\
                            header TEXT NOT NULL,\
                            request_ip TEXT NOT NULL,\
                            request_method TEXT NOT NULL,\
                            request_url TEXT NOT NULL,\
                            post_date TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserOperationRecord(class)_init(def)", e)
    def Write(self,**kwargs)->bool or None:#写入相关信息,如果写入成功返回Sid值，如果失败返回None
        CreationTime = str(int(time.time())) # 创建时间
        Uid=kwargs.get("uid")
        RequestApi=kwargs.get("request_api")
        Header=kwargs.get("header")
        RequestIp = kwargs.get("request_ip")
        RequestMethod = kwargs.get("request_method")
        PostDate = kwargs.get("post_date")
        RequestUrl = kwargs.get("request_url")
        try:
            self.cur.execute("INSERT INTO UserOperationLog(uid,request_api,creation_time,header,request_ip,request_method,request_url,post_date)\
            VALUES (?,?,?,?,?,?,?,?)",(Uid,RequestApi,CreationTime,Header,RequestIp,RequestMethod,RequestUrl,PostDate,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_UserOperationRecord(class)_Write(def)", e)
            return None

class ReportGenerationList:#报告生成相关表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE ReportGenerationList\
                            (id INTEGER PRIMARY KEY,\
                            file_name TEXT NOT NULL,\
                            uid TEXT NOT NULL,\
                            creation_time TEXT NOT NULL,\
                            active_scan_id TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ReportGenerationList(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")
        FileName = kwargs.get("file_name")
        ActiveScanId = kwargs.get("active_scan_id")
        try:
            self.cur.execute("INSERT INTO ReportGenerationList(file_name,uid,creation_time,active_scan_id)\
            VALUES (?,?,?,?)",(FileName, Uid, CreationTime, ActiveScanId,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ReportGenerationList(class)_Write(def)", e)
            return None
    def Query(self,**kwargs)->bool or None:#查询该文件是否是该用户所有
        Uid = kwargs.get("uid")
        FileName = kwargs.get("file_name")
        try:
            self.cur.execute("select * from ReportGenerationList where file_name =? and uid=?", (FileName,Uid,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ReportGenerationList(class)_Query(def)", e)
            return None




class GetTemplateFolderLocation:
    def Result(self)->str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            TemplateFolderLocation = GetRootFileLocation().Result() + "\\Web\\Template\\"
            return TemplateFolderLocation
        elif sys.platform == "linux" or sys.platform == "darwin":
            TemplateFolderLocation = GetRootFileLocation().Result() + "/Web/Template/"
            return TemplateFolderLocation

class GetDownloadFolderLocation:
    def Result(self)->str:
        if sys.platform == "win32" or sys.platform == "cygwin":
            DownloadFolderLocation = GetRootFileLocation().Result() + "\\Web\\Download\\"
            return DownloadFolderLocation
        elif sys.platform == "linux" or sys.platform == "darwin":
            DownloadFolderLocation = GetRootFileLocation().Result() + "/Web/Download/"
            return DownloadFolderLocation


class ProxyScanList:#代理列表，一个代理项目一条数据
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE ProxyScanList\
                                (proxy_id TEXT NOT NULL,\
                                uid TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                end_time TEXT NOT NULL,\
                                status TEXT NOT NULL,\
                                proxy_password TEXT NOT NULL,\
                                proxy_username TEXT NOT NULL,\
                                proxy_project_name TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ProxyScanList(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")
        EndTime= kwargs.get("end_time")
        Status= 1#kwargs.get("status")#1表示启动0表示关闭
        ProxyPassword= kwargs.get("proxy_password")
        ProxyUsername= kwargs.get("proxy_username")
        ProxyProjectName= kwargs.get("proxy_project_name")

        try:
            self.cur.execute("select creation_time from ProxyScanList")
            ProxyId="P"+str(len(self.cur.fetchall())+1)#构建特殊的ProxyId
            self.cur.execute("INSERT INTO ProxyScanList(proxy_id,uid,creation_time,end_time,status,proxy_password,proxy_username,proxy_project_name)\
                VALUES (?,?,?,?,?,?,?,?)", (ProxyId,Uid, CreationTime, EndTime,Status,ProxyPassword,ProxyUsername,ProxyProjectName,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ProxyScanList(class)_Write(def)", e)
            return None

    def QueryProxyProjectName(self,**kwargs)->bool or None:#查询扫描项目是否冲突,一个项目不能存在相同的项目名和用户名
        Uid = kwargs.get("uid")
        ProxyProjectName = kwargs.get("proxy_project_name")
        ProxyUsername = kwargs.get("proxy_username")
        try:
            self.cur.execute("select * from ProxyScanList where proxy_project_name =? and uid=? and proxy_username=?", (ProxyProjectName,Uid,ProxyUsername))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ProxyScanList(class)_QueryScanProjectName(def)", e)
            return None
    def ProxyAuthentication(self,**kwargs)->bool or None:#查询用来认证用户的账号和密码是否复核UID
        ProxyUsername = kwargs.get("proxy_username")
        ProxyPassword = kwargs.get("proxy_password")
        try:
            self.cur.execute("select * from ProxyScanList where proxy_username =? and proxy_password=?", (ProxyUsername,ProxyPassword,))
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["proxy_id"] = i[0]
                JsonValues["uid"] = i[1]
                return JsonValues
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ProxyScanList(class)_ProxyAuthentication(def)", e)
            return None

    # def Query(self,**kwargs)->bool or None:#查询该文件是否是该用户所有
    #     Uid = kwargs.get("uid")
    #     FileName = kwargs.get("file_name")
    #     try:
    #         self.cur.execute("select * from ReportGenerationList where file_name =? and uid=?", (FileName,Uid,))
    #         if self.cur.fetchall():  # 判断是否有数据
    #             self.con.close()
    #             return True
    #         else:
    #             return False
    #     except Exception as e:
    #         ErrorLog().Write("Web_WebClassCongregation_ProxyScanList(class)_Query(def)", e)
    #         return None


class OriginalProxyData:#从代理中获取数据包进行存储
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE OriginalProxyData\
                                (original_proxy_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                proxy_id TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                url TEXT NOT NULL,\
                                request_headers TEXT NOT NULL,\
                                request_date TEXT NOT NULL,\
                                request_method TEXT NOT NULL,\
                                response_headers TEXT NOT NULL,\
                                response_status_code TEXT NOT NULL,\
                                response_date_bytes TEXT NOT NULL,\
                                response_date_string TEXT NOT NULL,\
                                issue_task_status TEXT NOT NULL,\
                                redis_id TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_OriginalProxyData(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")
        ProxyId = kwargs.get("proxy_id")
        Url= kwargs.get("url")
        RequestHeaders= kwargs.get("request_headers")
        RequestDate= kwargs.get("request_date")
        RequestMethod=kwargs.get("request_method")
        ResponseHeaders=kwargs.get("response_headers")
        ResponseStatusCode=kwargs.get("response_status_code")
        ResponseDateBytes=kwargs.get("response_date_bytes")
        ResponseDateString=kwargs.get("response_date_string")
        IssueTaskStatus= "0"#未扫描为0 已扫描为1
        RedisId=kwargs.get("redis_id")

        try:
            self.cur.execute("INSERT INTO OriginalProxyData(uid,proxy_id,creation_time,url,request_headers,request_date,request_method,response_headers,response_status_code,response_date_bytes,response_date_string,issue_task_status,redis_id)\
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (Uid, ProxyId, CreationTime, Url,RequestHeaders,RequestDate,RequestMethod,ResponseHeaders,ResponseStatusCode,ResponseDateBytes,ResponseDateString,IssueTaskStatus,RedisId,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_OriginalProxyData(class)_Write(def)", e)
            return None
    def UpdateScanStatus(self, **kwargs) -> bool or None:#更新扫描状态
        Uid = kwargs.get("uid")
        RedisId = kwargs.get("redis_id")
        try:
            self.cur.execute("""UPDATE OriginalProxyData SET issue_task_status= ? WHERE uid = ? and redis_id = ? """,
                             ( "1",Uid, RedisId,))
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
            ErrorLog().Write("Web_WebClassCongregation_ReportGenerationList(class)_QueryTokenValidity(def)", e)
            return False
#查询暂时无
    # def Query(self, **kwargs) -> bool or None:
    #     Uid = kwargs.get("uid")
    #     FileName = kwargs.get("file_name")
    #     try:
    #         self.cur.execute("select * from ReportGenerationList where file_name =? and uid=?", (FileName, Uid,))
    #         if self.cur.fetchall():  # 判断是否有数据
    #             self.con.close()
    #             return True
    #         else:
    #             return False
    #     except Exception as e:
    #         ErrorLog().Write("Web_WebClassCongregation_ReportGenerationList(class)_QueryTokenValidity(def)", e)
    #         return None
class HomeInfo:#查询首页信息表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        self.info={}#用来存数据

    def NumberOfVulnerabilities(self,Uid):#查询漏洞个数,以及各个等级相关个数，通过查询medusa表来获取所有个数
        try:
            #查询总个数
            self.cur.execute("select scan_info_id from Medusa where uid =? ", (Uid,))
            self.info["number_of_vulnerabilities"]=str(len(self.cur.fetchall()))
            #查询高危个数
            self.cur.execute("select scan_info_id from Medusa where uid =? and rank='高危'", (Uid,))
            self.info["high_risk_number"] = str(len(self.cur.fetchall()))
            #查询中危个数
            self.cur.execute("select scan_info_id from Medusa where uid =? and rank='中危'", (Uid,))
            self.info["mid_risk_number"] = str(len(self.cur.fetchall()))
            #查询高危个数
            self.cur.execute("select scan_info_id from Medusa where uid =? and rank='低危'", (Uid,))
            self.info["low_risk_number"] = str(len(self.cur.fetchall()))
        except Exception as e:#设置默认值
            ErrorLog().Write("Web_WebClassCongregation_HomeInfo(class)_NumberOfVulnerabilities(def)", e)
            self.info["number_of_vulnerabilities"]="0"
            self.info["high_risk_number"] ="0"
            self.info["mid_risk_number"] ="0"
            self.info["low_risk_number"] ="0"

    def NumberOfWebsites(self, Uid):#查询目标网站个数，通过ActiveScanList列表查询
        try:

            self.cur.execute("select active_scan_id from ActiveScanList where uid =? ", (Uid,))

            #先对数据进行提取

            self.info["number_of_websites"]=str(len(self.cur.fetchall()))

        except Exception as e:#设置默认值
            ErrorLog().Write("Web_WebClassCongregation_HomeInfo(class)_NumberOfWebsites(def)", e)
            self.info["number_of_websites"]="0"
    def NumberOfPorts(self, Uid):#查询全部端口发现数量，通过PortInfo表查询
        try:

            self.cur.execute("select * from PortInfo where uid=?", (Uid,))
            self.info["number_of_port"]=str(len(self.cur.fetchall()))
        except Exception as e:#设置默认值
            ErrorLog().Write("Web_WebClassCongregation_HomeInfo(class)_NumberOfPorts(def)", e)
            self.info["number_of_port"] ="0"

    def NumberOfAgentTasks(self,Uid):  # 查询代理扫描数量，暂无模块,所有返回值直接为0
        try:
            self.info["number_of_agent_tasks"] = "0"
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_HomeInfo(class)_GithubMonitorDate(def)", e)
            self.info["number_of_agent_tasks"] = "0"
    def GithubMonitor(self, **kwargs):#查询GitHub监控数据
        StartTime = kwargs.get("start_time")
        EndTime = kwargs.get("end_time")
        try:
            self.cur.execute("select write_time from GithubMonitor where write_time<=? and write_time>=?", (EndTime,StartTime,))
            CountDict = {}
            Tmp=[]

            for x in self.cur.fetchall():#先对数据进行提取
                Tmp.append(x[0])
            for i in set(Tmp):#在对数据进行统计
                CountDict[i] = Tmp.count(i)
            #对数据进行排序
            SortResult = sorted(CountDict.items(), key=lambda item: item[0])
            return SortResult#直接返回数据
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_HomeInfo(class)_GithubMonitor(def)", e)
            return None

    def VulnerabilityDistribution(self, **kwargs):#查询时间段中，漏洞分布，通过查询medusa表来获取所有个数
        Uid = kwargs.get("uid")
        StartTime = kwargs.get("start_time")
        EndTime = kwargs.get("end_time")
        try:
            #查询时间段中数据分布
            self.cur.execute("select timestamp from Medusa where uid =? and timestamp<=? and timestamp>=?", (Uid,EndTime,StartTime,))
            CountDict = {}
            Tmp=[]

            for x in self.cur.fetchall():#先对数据进行提取
                Tmp.append(x[0])
            for i in set(Tmp):#在对数据进行统计
                CountDict[i] = Tmp.count(i)
            #对数据进行排序
            SortResult = sorted(CountDict.items(), key=lambda item: item[0])
            return SortResult#直接返回数据
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_HomeInfo(class)_TimeDistribution(def)", e)
            return None

    def DefaultData(self,**kwargs):#返回默认数据，该数据恒定不变
        Uid=kwargs.get("uid")
        self.NumberOfVulnerabilities(Uid)#查询漏洞个数
        #self.TimeDistribution(Uid,StartTime,EndTime)#查询时间段中，漏洞分布
        self.NumberOfWebsites(Uid)#查询目标网站个数
        self.NumberOfPorts(Uid)#查询全部端口发现数量
        self.NumberOfAgentTasks(Uid)#查询代理数量接口
        #self.GithubMonitorDate(StartTime,EndTime)#查询时间段中GitHub监控数据
        self.con.close()
        return self.info


class ProxyTempUrl:#代理转储数据,为了防止重复下发任务做的
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE ProxyTempUrl\
                                (proxy_temp_url_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                proxy_temp_url TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                proxy_id TEXT NOT NULL,\
                                redis_id TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ProxyTempUrl(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")
        ProxyTempUrl = kwargs.get("proxy_temp_url")
        RedisId= kwargs.get("redis_id")
        ProxyId = kwargs.get("proxy_id")
        try:
            self.cur.execute("INSERT INTO ProxyTempUrl(uid,proxy_temp_url,creation_time,proxy_id,redis_id)\
                VALUES (?,?,?,?,?)", (Uid, ProxyTempUrl, CreationTime, ProxyId,RedisId,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ProxyTempUrl(class)_Write(def)", e)
            return False

    def Query(self, **kwargs):  # 查询查看url的创建时间
        try:
            ProxyTempUrl = kwargs.get("proxy_temp_url")
            Uid = kwargs.get("uid")
            ProxyId=kwargs.get("proxy_id")
            self.cur.execute("select creation_time from ProxyTempUrl where uid =? and proxy_temp_url = ? and proxy_id= ?", (Uid, str(ProxyTempUrl),str(ProxyId),))
            #self.cur.execute("select * from ProxyTempUrl where uid =? ", (Uid,))
            return self.cur.fetchall()[-1][0]#返回最新的一条数据
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ProxyTempUrl(class)_Query(def)", e)
            return None

class CrossSiteScriptInfo:#XSS钓鱼接收数据库
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE CrossSiteScript\
                                (cross_site_script_id INTEGER PRIMARY KEY,\
                                headers TEXT NOT NULL,\
                                project_associated_file_name TEXT NOT NULL,\
                                ip TEXT NOT NULL,\
                                full_url TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                request_method TEXT NOT NULL,\
                                data_pack TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptInfo(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Headers= kwargs.get("headers").decode('utf-8')
        Ip = kwargs.get("ip")
        ProjectAssociatedFileName= kwargs.get("project_associated_file_name")
        RequestMethod = kwargs.get("request_method")
        FullURL = kwargs.get("full_url")
        DataPack = kwargs.get("data_pack").decode('utf-8')
        try:
            self.cur.execute("INSERT INTO CrossSiteScript(headers,project_associated_file_name,ip,full_url,creation_time,request_method,data_pack)\
                VALUES (?,?,?,?,?,?,?)", (Headers,ProjectAssociatedFileName, Ip, FullURL,CreationTime, RequestMethod,DataPack,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptInfo(class)_Write(def)", e)
            return False

    def Query(self, **kwargs):  # 查询查看XSS项目数据
        try:
            ProjectAssociatedFileName = kwargs.get("project_associated_file_name")
            self.cur.execute("select * from CrossSiteScript where project_associated_file_name=?", (ProjectAssociatedFileName,))
            result_list=[]
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["headers"] = i[1]
                JsonValues["project_associated_file_name"] = i[2]
                JsonValues["ip"] = i[3]
                JsonValues["full_url"] = i[4]
                JsonValues["creation_time"] = i[5]
                JsonValues["request_method"] = i[6]
                JsonValues["data_pack"] = i[7]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScript(class)_Query(def)", e)
            return None


class CrossSiteScriptProject:#XSS钓鱼项目信息数据库
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE CrossSiteScriptProject\
                                (cross_site_script_project_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                project_name TEXT NOT NULL,\
                                file_name TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptProject(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid= kwargs.get("uid")
        FileName = kwargs.get("file_name")
        ProjectName=kwargs.get("project_name")
        try:
            self.cur.execute("INSERT INTO CrossSiteScriptProject(uid,project_name,file_name,creation_time)\
                VALUES (?,?,?,?)", (Uid, ProjectName,FileName, CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptProject(class)_Write(def)", e)
            return False
    def Query(self, **kwargs):  # 查询查看XSS项目信息
        try:
            Uid = kwargs.get("uid")
            self.cur.execute("select * from CrossSiteScriptProject where uid =? ", (Uid,))
            result_list=[]
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["project_name"] = i[2]
                JsonValues["file_name"] = i[3]
                JsonValues["creation_time"] = i[4]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptProject(class)_Query(def)", e)
            return None

    def RepeatInvestigation(self,**kwargs):#用来排查file_name是否重复

        try:
            FileName = kwargs.get("file_name")
            self.cur.execute("select * from CrossSiteScriptProject where  file_name=? ", (FileName,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptProject(class)_RepeatInvestigation(def)", e)
            return False

    def AuthorityCheck(self,**kwargs):#用来校检CrossSiteScript数据库中文件名和UID相对应

        try:
            FileName = kwargs.get("file_name")
            Uid = kwargs.get("uid")
            self.cur.execute("select * from CrossSiteScriptProject where  file_name=? and uid=?", (FileName,Uid,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptProject(class)_AuthorityCheck(def)", e)
            return False

class CrossSiteScriptTemplate:  # XSS钓鱼模板存放
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE CrossSiteScriptTemplate\
                                (cross_site_script_template_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                template_name TEXT NOT NULL,\
                                template_data TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                update_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptProject(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        UpdateTime = str(int(time.time()))  # 更新时间
        Uid = kwargs.get("uid")
        TemplateName = kwargs.get("template_name")
        TemplateData = kwargs.get("template_data")#base64加密过的数据
        try:
            self.cur.execute("INSERT INTO CrossSiteScriptTemplate(uid,template_name,template_data,creation_time,update_time)\
                VALUES (?,?,?,?,?)", (Uid, TemplateName, TemplateData, CreationTime,UpdateTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptTemplate(class)_Write(def)", e)
            return False

    def Query(self, **kwargs):  # 查询查看XSS项目信息
        try:
            Uid = kwargs.get("uid")
            self.cur.execute("select * from CrossSiteScriptTemplate where uid =?", (Uid,))
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["template_name"] = i[2]
                JsonValues["template_data"] = i[3]
                JsonValues["creation_time"] = i[4]
                JsonValues["update_time"] = i[5]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptTemplate(class)_Query(def)", e)
            return None
    def RepeatInvestigation(self,**kwargs):#用来排查template_name是否重复

        try:
            Uid = kwargs.get("uid")
            TemplateName = kwargs.get("template_name")
            self.cur.execute("select * from CrossSiteScriptTemplate where uid =? and template_name=?", (Uid,TemplateName,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptTemplate(class)_RepeatInvestigation(def)", e)
            return False
    def Update(self,**kwargs):
        UpdateTime=str(int(time.time()))
        Uid = kwargs.get("uid")
        TemplateName = kwargs.get("template_name")
        TemplateData = kwargs.get("template_data")  # base64加密过的数据
        try:
            self.cur.execute(
                """UPDATE CrossSiteScriptTemplate SET template_data = ?,update_time=? WHERE uid = ? and template_name=? """,
                (TemplateData,UpdateTime,Uid,TemplateName,))
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
            ErrorLog().Write("Web_WebClassCongregation_CrossSiteScriptTemplate(class)_Update(def)", e)


class HardwareUsageRateInfo:  # 获取硬件中CPU和内存的使用情况
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE HardwareUsageRateInfo\
                                (hardware_usage_rate_id INTEGER PRIMARY KEY,\
                                memory_used TEXT NOT NULL,\
                                memory_free TEXT NOT NULL,\
                                memory_percent TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                central_processing_unit_usage_rate TEXT NOT NULL,\
                                per_core_central_processing_unit_usage_rate TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_HardwareUsageRateInfo(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        MemoryUsed = kwargs.get("memory_used")
        MemoryFree = kwargs.get("memory_free")
        MemoryPercent = kwargs.get("memory_percent")
        CentralProcessingUnitUsageRate = kwargs.get("central_processing_unit_usage_rate")
        PerCoreCentralProcessingUnitUsageRate = kwargs.get("per_core_central_processing_unit_usage_rate")
        try:
            self.cur.execute("INSERT INTO HardwareUsageRateInfo(memory_used,memory_free,memory_percent,creation_time,central_processing_unit_usage_rate,per_core_central_processing_unit_usage_rate)\
                VALUES (?,?,?,?,?,?)", (MemoryUsed, MemoryFree, MemoryPercent, CreationTime,CentralProcessingUnitUsageRate,PerCoreCentralProcessingUnitUsageRate,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_HardwareUsageRateInfo(class)_Write(def)", e)
            return False

    def Query(self):  # 查询查看CPU和内存使用信息
        try:
            CurrentTime = str(int(time.time()))  # 获取当前时间

            self.cur.execute("select * from HardwareUsageRateInfo where creation_time<=? and creation_time>=?", (CurrentTime,str(int(CurrentTime)-3600),))#查询半小时之前的CPU使用率，和内存使用率
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["memory_used"] = i[1]
                JsonValues["memory_free"] = i[2]
                JsonValues["memory_percent"] = i[3]
                JsonValues["creation_time"] = i[4]
                JsonValues["central_processing_unit_usage_rate"] = i[5]
                JsonValues["per_core_central_processing_unit_usage_rate"] = json.loads(i[6])
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_HardwareUsageRateInfo(class)_Query(def)", e)
            return None

class PortableExecutableAnalyticalData:  # PE文件分析后数据存储
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE PortableExecutable\
                                (portable_executable_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                file_size TEXT NOT NULL,\
                                md5 TEXT NOT NULL,\
                                sha1 TEXT NOT NULL,\
                                sha256 TEXT NOT NULL,\
                                save_file_name TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                file_generation_time TEXT NOT NULL,\
                                image_dos_header TEXT NOT NULL,\
                                image_nt_headers TEXT NOT NULL,\
                                image_file_header TEXT NOT NULL,\
                                image_optional_header TEXT NOT NULL,\
                                image_section_header TEXT NOT NULL,\
                                image_import_descriptor TEXT NOT NULL,\
                                image_export_directory TEXT NOT NULL,\
                                certificate_data_container TEXT NOT NULL,\
                                image_resource_directory TEXT NOT NULL,\
                                image_tls_directory TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_PortableExecutableAnalyticalData(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")
        FileSize= kwargs.get("file_size")
        Md5= kwargs.get("md5")
        Sha1= kwargs.get("sha1")
        Sha256= kwargs.get("sha256")
        SaveFileName= kwargs.get("save_file_name")
        FileGenerationTime= kwargs.get("file_generation_time")
        ImageDosHeader= kwargs.get("image_dos_header")
        ImageNewTechnologyHeaders= kwargs.get("image_nt_headers")
        ImageFileHeader= kwargs.get("image_file_header")
        ImageOptionalHeader= kwargs.get("image_optional_header")
        ImageSectionHeader = kwargs.get("image_section_header")
        ImageImportDescriptor= kwargs.get("image_import_descriptor")
        ImageExportDirectory= kwargs.get("image_export_directory")
        CertificateDataContainer= kwargs.get("certificate_data_container")
        ImageResourceDirectory= kwargs.get("image_resource_directory")
        ImageTransportLayerSecurityDirectory= kwargs.get("image_tls_directory")

        try:
            self.cur.execute("INSERT INTO PortableExecutable(uid,file_size,md5,sha1,sha256,save_file_name,creation_time,file_generation_time,image_dos_header,image_nt_headers,image_file_header,image_optional_header,image_section_header,image_import_descriptor,image_export_directory,certificate_data_container,image_resource_directory,image_tls_directory)\
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (Uid, FileSize, Md5, Sha1,Sha256,SaveFileName,CreationTime,FileGenerationTime,ImageDosHeader,ImageNewTechnologyHeaders,ImageFileHeader,ImageOptionalHeader,ImageSectionHeader ,ImageImportDescriptor,ImageExportDirectory,CertificateDataContainer,ImageResourceDirectory,ImageTransportLayerSecurityDirectory,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_PortableExecutableAnalyticalData(class)_Write(def)", e)
            return False

    # def Query(self):
    #     try:
    #         CurrentTime = str(int(time.time()))  # 获取当前时间
    #
    #         self.cur.execute("select * from HardwareUsageRateInfo where creation_time<=? and creation_time>=?", (CurrentTime,str(int(CurrentTime)-3600),))#查询半小时之前的CPU使用率，和内存使用率
    #         result_list = []
    #         for i in self.cur.fetchall():
    #             JsonValues = {}
    #             JsonValues["memory_used"] = i[1]
    #             JsonValues["memory_free"] = i[2]
    #             JsonValues["memory_percent"] = i[3]
    #             JsonValues["central_processing_unit_usage_rate"] = i[5]
    #             JsonValues["per_core_central_processing_unit_usage_rate"] = i[6]
    #             result_list.append(JsonValues)
    #         self.con.close()
    #         return result_list
    #     except Exception as e:
    #         ErrorLog().Write("Web_WebClassCongregation_PortableExecutableAnalyticalData(class)_Query(def)", e)
    #         return None


class VerificationCode:#验证码相关数据库，用来验证验证码合法性
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE VerificationCode\
                                (verification_code_id INTEGER PRIMARY KEY,\
                                code TEXT NOT NULL,\
                                verification_code_key TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                verification_code_status TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_VerificationCode(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Code = kwargs.get("code")#验证码字符串
        VerificationCodeKey = kwargs.get("verification_code_key")#验证码相关联的Key
        VerificationCodeStatus=0#验证码是否使用过，如果使用过值为1，未使用过为1
        try:
            self.cur.execute("INSERT INTO VerificationCode(code,verification_code_key,creation_time,verification_code_status)\
                VALUES (?,?,?,?)", (Code,VerificationCodeKey,CreationTime,VerificationCodeStatus,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_VerificationCode(class)_Write(def)", e)
            return False

    def Query(self, **kwargs):  #查询验证码是否正确
        try:
            CurrentTime = int(time.time())  # 获取当前时间
            Code = kwargs.get("code")  # 验证码字符串
            VerificationCodeKey = kwargs.get("verification_code_key")  # 验证码相关联的Key
            self.cur.execute("select * from VerificationCode where code =? and verification_code_key=?", (Code,VerificationCodeKey,))

            for i in self.cur.fetchall():
                if (CurrentTime-int(i[3]))>60:#操过60秒验证码失效
                    return False
                elif i[4]!="0":#判断如果验证码是使用过的
                    return False
                else:
                    self.cur.execute(
                        """UPDATE VerificationCode SET verification_code_status = ? WHERE  code = ? and verification_code_key=? """,
                        ("1",Code, VerificationCodeKey,))#查询成功后就把数据库值给更新了
                    self.con.commit()
                    self.con.close()
                    return True

        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_VerificationCode(class)_Query(def)", e)
            return None

class MarkdownInfo:#存放markdown文档的所有数据
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE Markdown\
                                (markdown_id INTEGER PRIMARY KEY,\
                                markdown_name TEXT NOT NULL,\
                                markdown_data TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                update_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownInfo(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        MarkdownName = kwargs.get("markdown_name")#生成的markdown文档名
        MarkdownData = kwargs.get("markdown_data")#用户传入的markdown数据
        #MarkdownProjectData = kwargs.get("markdown_project_name")  # 用户传入的markdown数据
        try:
            self.cur.execute("INSERT INTO Markdown(markdown_name,markdown_data,creation_time,update_time)\
                VALUES (?,?,?,?)", (MarkdownName,MarkdownData,CreationTime,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownInfo(class)_Write(def)", e)
            return False
    def CheckConflict(self,**kwargs):#检查name是否会冲突
        try:
            MarkdownName=kwargs.get("markdown_name")
            self.cur.execute("select * from Markdown where markdown_name=?", (MarkdownName,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownInfo(class)_CheckConflict(def)", e)
            return None
    def Update(self, **kwargs) -> bool or None:  # 如果存在就进行更新
        UpdateTime = str(int(time.time()))  # 当前时间
        MarkdownName = kwargs.get("markdown_name")#生成的markdown文档名
        MarkdownData = kwargs.get("markdown_data")#用户传入的markdown数据
        try:
            self.cur.execute(
                """UPDATE Markdown SET markdown_data = ?,update_time=? WHERE markdown_name = ? """,
                (MarkdownData, UpdateTime, MarkdownName,))
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
            ErrorLog().Write("Web_WebClassCongregation_MarkdownInfo(class)_Write(def)", e)
            return None
    def Query(self,**kwargs):  # 文本具体数据
        try:
            MarkdownName=kwargs.get("markdown_name")
            self.cur.execute("select * from Markdown where markdown_name=?", (MarkdownName,))
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["markdown_name"] = i[1]
                JsonValues["markdown_data"] = i[2]
                JsonValues["creation_time"] = i[3]
                JsonValues["update_time"] = i[4]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownInfo(class)_Query(def)", e)
            return None
    def QueryMarkdownData(self,**kwargs):  # 只查询docker 数据
        try:
            MarkdownName=kwargs.get("markdown_name")
            self.cur.execute("select * from Markdown where markdown_name=?", (MarkdownName,))
            for i in self.cur.fetchall():
                self.con.close()
                return i[2]#直接返回数据
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownInfo(class)_Query(def)", e)
            return None

class MarkdownRelationship:#markdown文档和用户相关的数据表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE MarkdownRelationship\
                                (markdown_relationship_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                markdown_project_owner TEXT NOT NULL,\
                                markdown_project_invitation_code TEXT NOT NULL,\
                                markdown_project_name TEXT NOT NULL,\
                                markdown_name TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownRelationship(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        MarkdownName = kwargs.get("markdown_name")#文件名确保唯一性
        Uid = kwargs.get("uid")
        MarkdownProjectName = kwargs.get("markdown_project_name")#项目的名称
        MarkdownProjectOwner = kwargs.get("markdown_project_owner")#项目是否是该用户所有，如果是值为1，如果不是值为0
        MarkdownProjectInvitationCode = kwargs.get("markdown_project_invitation_code")#项目的邀请码，输入邀请码可以直接加入项目
        try:
            self.cur.execute("INSERT INTO MarkdownRelationship(uid,markdown_project_owner,markdown_project_invitation_code,markdown_project_name,markdown_name,creation_time)\
                VALUES (?,?,?,?,?,?)", (Uid,MarkdownProjectOwner,MarkdownProjectInvitationCode,MarkdownProjectName,MarkdownName,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownRelationship(class)_Write(def)", e)
            return False
    def CheckInvitationCode(self,**kwargs):#检查邀请码是否会冲突
        try:
            MarkdownProjectInvitationCode=kwargs.get("markdown_project_invitation_code")
            self.cur.execute("select * from MarkdownRelationship where markdown_project_invitation_code=?", (MarkdownProjectInvitationCode,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownRelationship(class)_CheckInvitationCode(def)", e)
            return None
    def InvitationCodeToQueryProjectInformation(self,**kwargs):#通过验证码查询项目信息，用来加入项目使用
        try:
            MarkdownProjectInvitationCode=kwargs.get("markdown_project_invitation_code")
            self.cur.execute("select * from MarkdownRelationship where markdown_project_invitation_code=?", (MarkdownProjectInvitationCode,))  # 查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["uid"] = i[1]
                JsonValues["markdown_project_name"] = i[4]
                JsonValues["markdown_name"] = i[5]
                result_list.append(JsonValues)
            self.con.close()
            if result_list==[]:#判断是否为空数据
                return None
            else:
                return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownRelationship(class)_InvitationCodeToQueryProjectInformation(def)", e)
            return None
    def DetectionOfRepeatedAddition(self,**kwargs):#检测是否重复加入
        try:
            Uid=kwargs.get("uid")
            MarkdownName=kwargs.get("markdown_name")
            self.cur.execute("select * from MarkdownRelationship where markdown_name=? and uid=?", (MarkdownName,Uid,))  # 查询用户相关信息
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownRelationship(class)_InvitationCodeToQueryProjectInformation(def)", e)
            return None
    def CheckConflict(self,**kwargs):#检查name是否会冲突
        try:
            MarkdownName=kwargs.get("markdown_name")
            self.cur.execute("select * from MarkdownRelationship where markdown_name=?", (MarkdownName,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownRelationship(class)_CheckConflict(def)", e)
            return None
    def CheckPermissions(self,**kwargs):#检测用户是否有该项目的权限

        try:
            MarkdownName=kwargs.get("markdown_name")
            Uid=kwargs.get("uid")
            self.cur.execute("select * from MarkdownRelationship where markdown_name=? and uid=?", (MarkdownName,Uid,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownRelationship(class)_CheckPermissions(def)", e)
            return None

    def Query(self, **kwargs):  #用来查询用户所属项目的全部信息
        try:
            Uid=kwargs.get("uid")
            self.cur.execute("select * from MarkdownRelationship where uid=?", (Uid,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                if i[2]==0:#判断项目是否属于用户，如果不属于就清空邀请码
                    JsonValues["markdown_project_invitation_code"] = ""
                else:
                    JsonValues["markdown_project_invitation_code"] = i[3]
                JsonValues["markdown_project_owner"] = i[2]
                JsonValues["markdown_project_name"] = i[4]
                JsonValues["markdown_name"] = i[5]
                JsonValues["creation_time"] = i[6]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_MarkdownRelationship(class)_Query(def)", e)
            return None

class ApplicationCollection:#存放收集到的应用所有数据
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE ApplicationCollection\
                                (application_collection_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                program_type TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                status TEXT NOT NULL,\
                                application_data TEXT NOT NULL,\
                                redis_id TEXT NOT NULL,\
                                request_failed_application_name TEXT NOT NULL,\
                                total_number_of_applications TEXT NOT NULL,\
                                number_of_failures TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ApplicationCollection(class)_init(def)", e)
    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")  # 用户id
        ProgramType = kwargs.get("program_type")#类型是ios还是安卓
        Status = kwargs.get("status")#正在扫描还是已经完成
        ApplicationData = kwargs.get("application_data")  # 获取的应用数据
        RedisId = kwargs.get("redis_id")  # Redis值
        RequestFailedApplicationName = kwargs.get("request_failed_application_name")  # 获取失败的应用名
        TotalNumberOfApplications = kwargs.get("total_number_of_applications")  # 全部应用数
        NumberOfFailures = kwargs.get("number_of_failures")  # 获取失败应用数
        try:
            self.cur.execute("INSERT INTO ApplicationCollection(uid,program_type,creation_time,status,application_data,redis_id,request_failed_application_name,total_number_of_applications,number_of_failures)\
                VALUES (?,?,?,?,?,?,?,?,?)", (Uid,ProgramType,CreationTime,Status,ApplicationData,RedisId,RequestFailedApplicationName,TotalNumberOfApplications,NumberOfFailures,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ApplicationCollection(class)_Write(def)", e)
            return False
    def Update(self, **kwargs) -> bool or None:  # 对数据进行更新
        Uid = kwargs.get("uid")  # 用户id
        Status = "1"#正在扫描还是已经完成
        ApplicationData = kwargs.get("application_data")  # 获取的应用数据
        RedisId = kwargs.get("redis_id")  # Redis值
        RequestFailedApplicationName = kwargs.get("request_failed_application_name")  # 获取失败的应用名
        TotalNumberOfApplications = kwargs.get("total_number_of_applications")  # 全部应用数
        NumberOfFailures = kwargs.get("number_of_failures")  # 获取失败应用数
        try:
            self.cur.execute(
                """UPDATE ApplicationCollection SET status = ?,application_data=?,request_failed_application_name=?,total_number_of_applications=?,number_of_failures=? WHERE redis_id = ? and uid=? """,
                (Status, ApplicationData, RequestFailedApplicationName,TotalNumberOfApplications,NumberOfFailures,RedisId,Uid,))
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
            ErrorLog().Write("Web_WebClassCongregation_ApplicationCollection(class)_Update(def)", e)
            return None
    def Query(self, **kwargs):  #用来查询用户的项目
        try:
            Uid=kwargs.get("uid")
            self.cur.execute("select * from ApplicationCollection where uid=?", (Uid,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["program_type"] = i[2]
                JsonValues["creation_time"] = i[3]
                JsonValues["status"] = i[4]
                JsonValues["application_data"] = i[5]
                JsonValues["request_failed_application_name"] = i[7]
                JsonValues["total_number_of_applications"] = i[8]
                JsonValues["number_of_failures"] = i[9]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ApplicationCollection(class)_Query(def)", e)
            return None

class NistData:#存放Nist发布的CVE数据
    def __init__(self):
        self.con = sqlite3.connect(GetNistDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE CommonVulnerabilitiesAndExposures\
                                (common_vulnerabilities_and_exposures_id INTEGER PRIMARY KEY,\
                                vulnerability_number TEXT NOT NULL,\
                                v3_base_score TEXT NOT NULL,\
                                v3_base_severity TEXT NOT NULL,\
                                v2_base_score TEXT NOT NULL,\
                                v2_base_severity TEXT NOT NULL,\
                                last_up_date TEXT NOT NULL,\
                                vulnerability_description TEXT NOT NULL,\
                                vendors TEXT NOT NULL,\
                                products TEXT NOT NULL,\
                                raw_data TEXT NOT NULL)")


        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_init(def)", e)
    def Write(self, DataSet:list) -> bool or None:  # 写入相关信息

        try:
            self.cur.executemany("INSERT INTO CommonVulnerabilitiesAndExposures(vulnerability_number,v3_base_score,v3_base_severity,v2_base_score,v2_base_severity,last_up_date,vulnerability_description,vendors,products,raw_data)\
                VALUES (?,?,?,?,?,?,?,?,?,?)", DataSet)
            # 提交
            self.con.commit()#只发送数据不结束
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_Write(def)", e)
            return False

    def BulkQuery(self, **kwargs):  #分页查询数据内容
        try:
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select vulnerability_number,v3_base_score,v3_base_severity,v2_base_score,v2_base_severity,last_up_date,vulnerability_description,vendors,products  from CommonVulnerabilitiesAndExposures limit ? offset ?", (NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息

            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["vulnerability_number"] = i[0]
                JsonValues["v3_base_score"] = i[1]
                JsonValues["v3_base_severity"] = i[2]
                JsonValues["v2_base_score"] = i[3]
                JsonValues["v2_base_severity"] = i[4]
                JsonValues["last_up_date"] = i[5]
                JsonValues["vulnerability_description"] = i[6]
                JsonValues["vendors"] = i[7]
                JsonValues["products"] = i[8]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_BulkQuery(def)", e)
            return None

    def StatisticalData(self):  # 整体个数统计
        try:
            self.cur.execute("SELECT COUNT(1)  FROM CommonVulnerabilitiesAndExposures",)  # 查询用户相关信息
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_StatisticalData(def)", e)
            return None
    def DetailedQuery(self, **kwargs):  #单个CVE数据具体内容查询
        try:
            CommonVulnerabilitiesAndExposures=kwargs.get("common_vulnerabilities_and_exposures")#查询第几页
            self.cur.execute("select raw_data from CommonVulnerabilitiesAndExposures where vulnerability_number=?", (CommonVulnerabilitiesAndExposures,))
            Result=self.cur.fetchall()[0][0]
            self.con.close()
            return Result#返回原始数据
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_DetailedQuery(def)", e)
            return None
    def ModuleDataStatistics(self,**kwargs):  #模块的个数统计
        try:
            ModuleName =kwargs.get("module_name")#模块名称。危险的SQL拼接，容易出事，禁止用户传入
            ModuleContent=kwargs.get("module_content")#模块内容
            self.cur.execute("SELECT COUNT(1)  FROM CommonVulnerabilitiesAndExposures where "+ModuleName+" like ?",(ModuleContent,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_ModuleDataStatistics(def)", e)
            return None
    def SeverityQuery(self, **kwargs):  #严重程度数据查询
        try:
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页
            Severity=kwargs.get("severity")#验证程度
            self.cur.execute("select vulnerability_number,v3_base_score,v3_base_severity,v2_base_score,v2_base_severity,last_up_date,vulnerability_description,vendors,products  from CommonVulnerabilitiesAndExposures WHERE v3_base_severity=? limit ? offset ?", (Severity,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))

            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["vulnerability_number"] = i[0]
                JsonValues["v3_base_score"] = i[1]
                JsonValues["v3_base_severity"] = i[2]
                JsonValues["v2_base_score"] = i[3]
                JsonValues["v2_base_severity"] = i[4]
                JsonValues["last_up_date"] = i[5]
                JsonValues["vulnerability_description"] = i[6]
                JsonValues["vendors"] = i[7]
                JsonValues["products"] = i[8]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_SeverityQuery(def)", e)
            return None
    def VendorsQuery(self, **kwargs):  #供应商数据查询
        try:
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页
            Vendors=kwargs.get("vendors")#尝试名称
            self.cur.execute("select vulnerability_number,v3_base_score,v3_base_severity,v2_base_score,v2_base_severity,last_up_date,vulnerability_description,vendors,products  from CommonVulnerabilitiesAndExposures WHERE vendors like ? limit ? offset ?",('%{}%'.format(Vendors),NumberOfSinglePages,NumberOfSinglePages*NumberOfPages,))#通过link %xx%来模糊查询
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["vulnerability_number"] = i[0]
                JsonValues["v3_base_score"] = i[1]
                JsonValues["v3_base_severity"] = i[2]
                JsonValues["v2_base_score"] = i[3]
                JsonValues["v2_base_severity"] = i[4]
                JsonValues["last_up_date"] = i[5]
                JsonValues["vulnerability_description"] = i[6]
                JsonValues["vendors"] = i[7]
                JsonValues["products"] = i[8]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_VendorsQuery(def)", e)
            return None
    def ProductsQuery(self, **kwargs):  #产品数据查询
        try:
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页
            Products=kwargs.get("products")#尝试名称
            self.cur.execute("select vulnerability_number,v3_base_score,v3_base_severity,v2_base_score,v2_base_severity,last_up_date,vulnerability_description,vendors,products  from CommonVulnerabilitiesAndExposures WHERE products like ? limit ? offset ?",('%{}%'.format(Products),NumberOfSinglePages,NumberOfSinglePages*NumberOfPages,))#通过link %xx%来模糊查询
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["vulnerability_number"] = i[0]
                JsonValues["v3_base_score"] = i[1]
                JsonValues["v3_base_severity"] = i[2]
                JsonValues["v2_base_score"] = i[3]
                JsonValues["v2_base_severity"] = i[4]
                JsonValues["last_up_date"] = i[5]
                JsonValues["vulnerability_description"] = i[6]
                JsonValues["vendors"] = i[7]
                JsonValues["products"] = i[8]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_ProductsQuery(def)", e)
            return None
    def Update(self, UpdateData) -> bool or None:  # 对数据进行更新

        try:
            self.cur.executemany(
                """UPDATE CommonVulnerabilitiesAndExposures SET vulnerability_number = ?,v3_base_score=?,v3_base_severity=?,v2_base_score=?,v2_base_severity=?,last_up_date=?,vulnerability_description=?,vendors=?,products=?,raw_data=? WHERE vulnerability_number=? """,
                UpdateData)
            if self.cur.rowcount < 1:  # 用来判断是否更新成功
                self.con.commit()
                return False
            else:
                self.con.commit()
                return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_Update(def)", e)
            return False
    def UniqueInquiry(self, **kwargs) -> bool or None:  # 对更新的数据进行检查，判断数据库中是否是唯一的
        try:
            VulnerabilityNumber=kwargs.get("vulnerability_number")
            self.cur.execute("select vulnerability_number  from CommonVulnerabilitiesAndExposures where vulnerability_number=?", (VulnerabilityNumber,))
            if self.cur.fetchall():  # 判断是否有数据
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_NistData(class)_UniqueInquiry(def)", e)
            return None


class DomainNameSystemLog:  # 存放DNSLOG数据
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE DomainNameSystemLog\
                                (dnslog_id INTEGER PRIMARY KEY,\
                                domain_name TEXT NOT NULL,\
                                ip TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")


        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_DomainNameSystemLog(class)_init(def)", e)

    def Write(self,**kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Ip = kwargs.get("ip")  # 请求IP不一定准确
        DomainName = kwargs.get("domain_name")  # 获取解析域名
        try:
            DomainNameSystemAddressLength=len("."+domain_name_system_address)#获取长度，加点是为了截断域名
            TreatmentDomainName=DomainName[-DomainNameSystemAddressLength:]#进行截断处理
            if TreatmentDomainName=="."+domain_name_system_address:
                try:
                    self.cur.execute("INSERT INTO DomainNameSystemLog(domain_name,ip,creation_time)\
                        VALUES (?,?,?)",(DomainName,Ip,CreationTime,))
                    # 提交
                    self.con.commit()  # 只发送数据不结束
                    self.con.close()
                    return True
                except Exception as e:
                    ErrorLog().Write("Web_WebClassCongregation_DomainNameSystemLog(class)_Write(def)", e)
                    return False
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_DomainNameSystemLog(class)_Write(def)-TreatmentDomainName", e)
            return None
    def Query(self, **kwargs):  #用来查询数据
        try:
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select domain_name,ip,creation_time  from DomainNameSystemLog limit ? offset ?", (NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["domain_name"] = i[0]
                JsonValues["ip"] = i[1]
                JsonValues["creation_time"] = i[2]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_DomainNameSystemLog(class)_Query(def)", e)
            return None
    def StatisticalData(self):  # 整体个数统计
        try:
            self.cur.execute("SELECT COUNT(1)  FROM DomainNameSystemLog",)  # 查询用户相关信息
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_DomainNameSystemLog(class)_StatisticalData(def)", e)
            return None

class AntiAntiVirusData:#免杀病毒相关数据库
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE AntiAntiVirus\
                                (anti_anti_virus_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                shellcode_type TEXT NOT NULL,\
                                virus_original_file_name TEXT NOT NULL,\
                                virus_generate_file_name TEXT NOT NULL,\
                                compilation_status TEXT NOT NULL,\
                                redis_id TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")


        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_AntiAntiVirusData(class)_init(def)", e)
    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        Uid = kwargs.get("uid")
        VirusOriginalFileName=kwargs.get("virus_original_file_name")
        ShellcodeType = kwargs.get("shellcode_type")#1为MSF类型的，2为CS类型的
        VirusGenerateFileName = kwargs.get("virus_generate_file_name")
        CompilationStatus = kwargs.get("compilation_status")#状态0为未完成，1完成，-1出错
        RedisId = kwargs.get("redis_id")
        CreationTime = str(int(time.time()))  # 创建时间
        try:
            self.cur.execute("INSERT INTO AntiAntiVirus(uid,shellcode_type,virus_original_file_name,virus_generate_file_name,compilation_status,redis_id,creation_time)\
                VALUES (?,?,?,?,?,?,?)", (Uid,ShellcodeType,VirusOriginalFileName, VirusGenerateFileName,CompilationStatus,RedisId, CreationTime,))
            self.con.commit()  # 只发送数据不结束
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_AntiAntiVirusData(class)_Write(def)", e)
            return False
    def StatisticalData(self,**kwargs):  # 当前用户个数统计
        Uid = kwargs.get("uid")
        try:
            self.cur.execute("SELECT COUNT(1)  FROM AntiAntiVirus WHERE uid=?",(Uid,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_AntiAntiVirusData(class)_StatisticalData(def)", e)
            return None
    def UpdateStatus(self,**kwargs)->bool:#利用主键ID来判断后更新数据
        RedisId = kwargs.get("redis_id")
        CompilationStatus = kwargs.get("compilation_status")
        try:
            self.cur.execute("""UPDATE AntiAntiVirus SET compilation_status = ? WHERE redis_id= ?""",(CompilationStatus, RedisId,))
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
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_UpdateStatus(def)", e)
            return False
    def Query(self, **kwargs):  #用来查询数据
        try:
            Uid = kwargs.get("uid")
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select * from AntiAntiVirus WHERE uid=? limit ? offset ? ", (Uid,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["shellcode_type"] = i[2]
                JsonValues["virus_original_file_name"] = i[3]
                JsonValues["virus_generate_file_name"] = i[4]
                JsonValues["compilation_status"] = i[5]
                JsonValues["creation_time"] = i[7]

                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_WebClassCongregation_ActiveScanList(class)_Query(def)", e)
            return None