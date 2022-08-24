# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
import sqlite3
import json
from fake_useragent import UserAgent
from ClassCongregation import GetPath,ErrorLog,randoms
from config import domain_name_system_address,user_agent_browser_type

class AgentHeader:  # 使用随机头类
    def result(self) -> str:  # 使用随机头传入传入参数
        try:
            self.Values = user_agent_browser_type
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


class UserInfo:#用户表
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_init(def)",e)
    def VerifyUsername(self,name:str)->bool or None:#查询用户名是否存在，True表示有数据，False只表示用户不存在，None表示报错
        try:
            self.cur.execute("select * from UserInfo where name =? ", (name,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_VerifyUsername(def)", e)
            return None
    def VerifyEmail(self,email:str)->bool or None:#查询邮箱是否存在，True表示有数据，False表示邮箱不存在，None表示报错
        try:
            self.cur.execute("select * from UserInfo where email =?", (email,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_VerifyEmail(def)", e)
            return None
    def UserLogin(self,username,passwd)->str or None:#用户登录，如果登录成功返回Token，如果失败返回None
        try:
            self.cur.execute("select * from UserInfo where name =? and passwd=?", (username,passwd,))
            for tuple in self.cur.fetchall():
                return tuple[4] # 返回Token
            return None
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_UserLogin(def)", e)
            return None
    def WhetherTheKeyConflicts(self,key:str)->bool:#查询用户kEY是否存在，True表示有数据，False表示各种问题
        try:
            self.cur.execute("select * from UserInfo where key =?", (key,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_WhetherTheKeyConflicts(def)", e)
            return False
    def Write(self,**kwargs:str)->bool or None:#写入新用户，True表示成功，False表示用户已存在，None表示报错
        creation_time = str(int(time.time())) # 创建时间
        uid=kwargs.get("uid")
        name=kwargs.get("name")
        show_name=kwargs.get("show_name")
        passwd=kwargs.get("passwd")
        email=kwargs.get("email")
        avatar=kwargs.get("avatar")
        key=kwargs.get("key")
        token=kwargs.get("token")#这个是用来验证用户登录的
        while True:#判断Key否存在
            if not self.WhetherTheKeyConflicts(key):#如果未找到就跳出循环进行下去
                break
            key = randoms().result(40)
        try:
            self.cur.execute("INSERT INTO UserInfo(uid,key,token,name,show_name,passwd,email,avatar,key_update_time,passwd_update_time,email_update_time,show_name_update_time,avatar_update_time,token_update_time,creation_time)\
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(uid,key,token,name,show_name, passwd,email,avatar,creation_time,creation_time,creation_time,creation_time,creation_time,creation_time,creation_time,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_Write(def)", e)
            return None
    def UpdatePasswd(self,**kwargs:str)->bool:#更新用户密码，True表示成功，False表示失败
        name = kwargs.get("name")
        old_passwd = kwargs.get("old_passwd")
        new_passwd = kwargs.get("new_passwd")
        update_time = str(int(time.time()))  # 修改时间
        if name!=None and old_passwd!=None and new_passwd!=None:
            try:
                self.cur.execute("select * from UserInfo where name =? and passwd=?", (name,old_passwd))
                if self.cur.fetchall():  # 判断是否有数据
                    try:#有数据的话就改密码
                        self.cur.execute("""UPDATE UserInfo SET passwd = ? , passwd_update_time = ? WHERE name= ?""", (new_passwd,update_time,name,))
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
                        ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_UpdatePasswd(def)ChangePassword", e)
                        return False
                else:
                    return False
            except Exception as e:
                ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_UpdatePasswd(def)QueryPassword", e)
                return False
        else:return False
    def UpdateShowName(self,**kwargs:str)->bool:#更新用户显示名字，True表示成功，False表示失败
        uid = kwargs.get("uid")
        show_name = kwargs.get("show_name")
        update_time = str(int(time.time()))  # 修改时间
        if uid!=None and show_name!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET show_name = ? , show_name_update_time = ? WHERE uid= ?""", (show_name,update_time,uid,))
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
                ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_UpdateShowName(def)", e)
                return False
        else:return False
    def UpdateEmail(self,**kwargs:str)->bool:#更新用户邮箱，True表示成功，False表示失败
        name = kwargs.get("name")
        email = kwargs.get("email")
        update_time = str(int(time.time()))  # 修改时间
        if name!=None and email!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET email = ? , email_update_time = ? WHERE name= ?""", (email,update_time,name,))
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
                ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_UpdateEmail(def)", e)
                return False
        else:return False
    def UpdateAvatar(self,**kwargs:str)->bool:#更新用户头像路径，True表示成功，False表示各失败
        uid = kwargs.get("uid")
        avatar = kwargs.get("avatar")
        update_time = str(int(time.time()))  # 修改时间
        if uid!=None and avatar!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET avatar = ?, avatar_update_time = ? WHERE uid= ?""", (avatar,update_time,uid,))
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
                ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_UpdateImgPath(def)", e)
                return False
        else:return False
    def UpdateKey(self,**kwargs:str)->bool:#更新用户Key，True表示成功，False表示失败
        uid = kwargs.get("uid")
        key= kwargs.get("key")
        update_time = str(int(time.time()))  # 修改时间
        if uid!=None and key!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET key = ? , key_update_time = ? WHERE uid= ?""", (key,update_time,uid,))
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
                ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_UpdateKey(def)", e)
                return False
        else:return False
    def UpdateToken(self,**kwargs:str)->bool:#更新用户Token，True表示成功，False表示失败
        name = kwargs.get("name")
        token= kwargs.get("token")
        update_time = str(int(time.time()))  # 修改时间
        if name!=None and token!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET token = ? , token_update_time = ? WHERE name= ?""", (token,update_time,name,))
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
                ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_UpdateToken(def)", e)
                return False
        else:return False
    def QueryTokenCreationTime(self,**kwargs:str)->bool or None:#查询用户Token创建时间，True表示Token不能用，False表示Token还能用
        name = kwargs.get("name")
        token= kwargs.get("token")
        now_time = int(time.time())  # 获取当前时间
        if name!=None and token!=None:
            try:
                self.cur.execute("select * from UserInfo where name =? and token = ?", (name, token,))
                for tuple in self.cur.fetchall():
                    expire_date=now_time-int(tuple[14])#获取时间差
                    if expire_date<5000:
                        return False#返回False表示还可以用

                return True#如果为找到数据，返回True，表示需要重新写入或者登录
            except Exception as e:
                ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_QueryTokenCreationTime(def)", e)
                return None
        else:return True#报错返回True
    def QueryTokenValidity(self,token:str)->bool or None:#用来查询Token是否重复了
        try:
            self.cur.execute("select * from UserInfo where token =?", (token,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_QueryTokenValidity(def)", e)
            return None
    def QueryUidWithToken(self,token:str):#利用Token反向查唯一的UID
        try:
            self.cur.execute("select * from UserInfo where token =?", (token,))
            for tuple in self.cur.fetchall():
                return tuple[1]
            return None
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_QueryUidWithToken(def)", e)
            return None
    def QueryUserInfo(self,token:str):#利用Token,查询完整的用户信息，除了更新时间都有
        try:
            self.cur.execute("select * from UserInfo where token =?", (token,))
            for tuple in self.cur.fetchall():
                json_values = {}
                json_values["id"] = tuple[0]
                json_values["uid"] = tuple[1]
                json_values["key"] = tuple[2]
                json_values["name"] = tuple[3]
                json_values["token"] = tuple[4]
                json_values["show_name"] = tuple[5]
                json_values["passwd"] = tuple[6]
                json_values["email"] = tuple[7]
                json_values["avatar"] = tuple[8]
                return json_values#由于用户信息不可能有多个的所有这边直接返回
            return None#如果没查到数据就返回空
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_QueryUserInfo(def)", e)
            return None
    def ForgetPassword(self,**kwargs):#忘记密码函数
        name = kwargs.get("name")
        new_passwd=kwargs.get("new_passwd")
        email=kwargs.get("email")
        update_time = str(int(time.time()))  # 修改时间
        try:
            self.cur.execute("""UPDATE UserInfo SET passwd = ? , passwd_update_time = ? WHERE name= ? and email=?""",
                             (new_passwd, update_time, name,email,))
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
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_ForgetPassword(def)", e)
            return False
    def QueryUidWithKey(self,key:str):#利用Key反向查唯一的UID
        try:
            self.cur.execute("select * from UserInfo where key =?", (key,))
            for tuple in self.cur.fetchall():
                return tuple[1]
            return None
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_UserInfo(class)_QueryUidWithToken(def)", e)
            return None


class ActiveScanList:#用户主动扫描网站信息列表,写入父表中的SID
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_ActiveScanList(class)_init(def)", e)
    def Write(self,**kwargs):#写入相关信息,如果写入成功返回Sid值，如果失败返回None
        creation_time = str(int(time.time())) # 创建时间
        uid=kwargs.get("uid")
        url=kwargs.get("url")
        proxy=kwargs.get("proxy")
        status = kwargs.get("status")
        module = kwargs.get("module")
        process = kwargs.get("process")
        redis_id=""#先吧RedisID传空，后面在更新RedisID
        try:
            self.cur.execute("INSERT INTO ActiveScanList(uid,url,creation_time,proxy,status,process,module,redis_id)\
            VALUES (?,?,?,?,?,?,?,?)",(uid,url,creation_time,proxy,status,process,module,redis_id,))
            # 提交
            get_active_scan_id=self.cur.lastrowid  # 获取主键的ID值，也就是active_scan_id的值
            self.con.commit()
            self.con.close()
            return get_active_scan_id#获取主键的ID值，也就是sid的值
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_ActiveScanList(class)_Write(def)", e)
            return None
    def Query(self,**kwargs):#通过UID来查询信息
        uid = kwargs.get("uid")
        try:
            self.cur.execute("select * from ActiveScanList where uid =? ", (uid,))
            result_list = []  # 存放json的返回结果列表用
            for i in self.cur.fetchall():
                json_values = {}
                json_values["active_scan_id"] = i[0]
                json_values["url"] = i[2]
                json_values["creation_time"] = i[3]
                json_values["proxy"] = i[4]
                json_values["status"] = i[5]
                json_values["process"] = i[6]
                json_values["module"] = i[7]
                result_list.append(json_values)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_ActiveScanList(class)_Query(def)", e)
            return None

    def UpdateRedisId(self,**kwargs):#更新redis id的值后面用来更新扫描状态
        uid = kwargs.get("uid")
        active_scan_id=kwargs.get("active_scan_id")
        redis_id=kwargs.get("redis_id")
        try:
            self.cur.execute("""UPDATE ActiveScanList SET redis_id = ? WHERE active_scan_id= ? and uid=?""",(redis_id,active_scan_id,uid,))
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
            ErrorLog().Write("Web_DatabaseHub_ActiveScanList(class)_UpdateRedisId(def)", e)
            return False

    def UpdateStatus(self,**kwargs)->bool:#利用主键ID来判断后更新数据
        redis_id = kwargs.get("redis_id")
        try:
            self.cur.execute("""UPDATE ActiveScanList SET status = ? WHERE redis_id= ?""",("1", redis_id,))
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
            ErrorLog().Write("Web_DatabaseHub_ActiveScanList(class)_UpdateStatus(def)", e)
            return False


#
# #通过scan_info_id和uid来查询
# class MedusaQuery:#单个漏洞的详细内容查询表，具体写入表在ClassCongregation文件中，该表是个查询数据表
#     def __init__(self):
#         self.con = sqlite3.connect(GetPath().DatabaseFile())
#         # 获取所创建数据的游标
#         self.cur = self.con.cursor()
#     def Query(self, **kwargs)->None or list:
#         try:
#             ScanInfoId = kwargs.get("scan_info_id")
#             Uid = kwargs.get("uid")
#             self.cur.execute("select * from Medusa where uid =? and scan_info_id = ?", (Uid, ScanInfoId,))
#             result_list = []  # 存放json的返回结果列表用
#             for i in self.cur.fetchall():
#                 JsonValues = {}
#                 JsonValues["scan_info_id"] = i[0]
#                 JsonValues["url"] = i[1]
#                 JsonValues["name"] = i[2]
#                 JsonValues["affects"] = i[3]
#                 JsonValues["rank"] = i[4]
#                 JsonValues["suggest"] = i[5]
#                 JsonValues["desc_content"] = i[6]
#                 JsonValues["details"] = i[7]
#                 JsonValues["number"] = i[8]
#                 JsonValues["author"] = i[9]
#                 JsonValues["create_date"] = i[10]
#                 JsonValues["disclosure"] = i[11]
#                 JsonValues["algroup"] = i[12]
#                 JsonValues["version"] = i[13]
#                 JsonValues["timestamp"] = i[14]
#                 #JsonValues["active_scan_id"] = i[15]
#                 JsonValues["response_headers"] = i[17]
#                 JsonValues["response_text"] = i[18]
#                 JsonValues["response_byte"] = i[19]
#                 JsonValues["response_status_code"] = i[20]
#                 JsonValues["request_path_url"] = i[21]
#                 JsonValues["request_body"] = i[22]
#                 JsonValues["request_method"] = i[23]
#                 JsonValues["request_headers"] = i[24]
#                 result_list.append(JsonValues)
#             self.con.close()
#             return result_list
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_MedusaQuery(class)_Query(def)", e)
#             return None
#     def QueryBySid(self, **kwargs):#生成word文档数据查询
#         try:
#             ActiveScanId = kwargs.get("active_scan_id")
#             Uid = kwargs.get("uid")
#             self.cur.execute("select * from Medusa where uid =? and active_scan_id = ?", (Uid, ActiveScanId,))
#             result_list = []  # 存放json的返回结果列表用
#             url=""
#             for i in self.cur.fetchall():
#                 JsonValues = {}
#                 url= i[1]
#                 JsonValues["vulnerability_name"] = i[2]
#                 JsonValues["vulnerability_level"] = i[4]
#                 JsonValues["repair_suggestions"] = i[5]
#                 JsonValues["vulnerability_description"] = i[6]
#                 JsonValues["vulnerability_details"] = i[7]
#                 JsonValues["find_the_time"] = i[14]
#                 result_list.append(JsonValues)
#             self.con.close()
#             return result_list,url
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_MedusaQuery(class)_QueryBySid(def)", e)
#             return None

class RequestLog:#操作日志
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_RequestRecord(class)_init(def)", e)
    def Write(self,**kwargs)->bool or None:#写入相关信息,如果写入成功返回Sid值，如果失败返回None
        creation_time = str(int(time.time())) # 创建时间
        request_api=kwargs.get("request_api")
        header=kwargs.get("header")
        request_ip = kwargs.get("request_ip")
        request_method = kwargs.get("request_method")
        post_date = kwargs.get("post_date")
        request_url = kwargs.get("request_url")
        try:
            self.cur.execute("INSERT INTO RequestLog(request_api,creation_time,header,request_ip,request_method,request_url,post_date)\
            VALUES (?,?,?,?,?,?,?)",(request_api,creation_time,header,request_ip,request_method,request_url,post_date,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_RequestRecord(class)_Write(def)", e)
            return None

class UserOperationLog:#用户操作日志
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_UserOperationRecord(class)_init(def)", e)
    def Write(self,**kwargs)->bool or None:#写入相关信息,如果写入成功返回Sid值，如果失败返回None
        creation_time = str(int(time.time())) # 创建时间
        uid=kwargs.get("uid")
        request_api=kwargs.get("request_api")
        header=kwargs.get("header")
        request_ip = kwargs.get("request_ip")
        request_method = kwargs.get("request_method")
        post_date = kwargs.get("post_date")
        request_url = kwargs.get("request_url")
        try:
            self.cur.execute("INSERT INTO UserOperationLog(uid,request_api,creation_time,header,request_ip,request_method,request_url,post_date)\
            VALUES (?,?,?,?,?,?,?,?)",(uid,request_api,creation_time,header,request_ip,request_method,request_url,post_date,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_UserOperationRecord(class)_Write(def)", e)
            return None
#
# class ReportGenerationList:#报告生成相关表
#     def __init__(self):
#         self.con = sqlite3.connect(GetPath().DatabaseFile())
#         # 获取所创建数据的游标
#         self.cur = self.con.cursor()
#         # 创建表
#         try:
#             self.cur.execute("CREATE TABLE ReportGenerationList\
#                             (id INTEGER PRIMARY KEY,\
#                             file_name TEXT NOT NULL,\
#                             uid TEXT NOT NULL,\
#                             creation_time TEXT NOT NULL,\
#                             active_scan_id TEXT NOT NULL)")
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ReportGenerationList(class)_init(def)", e)
#
#     def Write(self, **kwargs) -> bool or None:  # 写入相关信息
#         CreationTime = str(int(time.time()))  # 创建时间
#         Uid = kwargs.get("uid")
#         FileName = kwargs.get("file_name")
#         ActiveScanId = kwargs.get("active_scan_id")
#         try:
#             self.cur.execute("INSERT INTO ReportGenerationList(file_name,uid,creation_time,active_scan_id)\
#             VALUES (?,?,?,?)",(FileName, Uid, CreationTime, ActiveScanId,))
#             # 提交
#             self.con.commit()
#             self.con.close()
#             return True
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ReportGenerationList(class)_Write(def)", e)
#             return None
#     def Query(self,**kwargs)->bool or None:#查询该文件是否是该用户所有
#         Uid = kwargs.get("uid")
#         FileName = kwargs.get("file_name")
#         try:
#             self.cur.execute("select * from ReportGenerationList where file_name =? and uid=?", (FileName,Uid,))
#             if self.cur.fetchall():  # 判断是否有数据
#                 self.con.close()
#                 return True
#             else:
#                 return False
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ReportGenerationList(class)_Query(def)", e)
#             return None

#
# class ProxyScanList:#代理列表，一个代理项目一条数据
#     def __init__(self):
#         self.con = sqlite3.connect(GetPath().DatabaseFile())
#         # 获取所创建数据的游标
#         self.cur = self.con.cursor()
#         # 创建表
#         try:
#             self.cur.execute("CREATE TABLE ProxyScanList\
#                                 (proxy_id TEXT NOT NULL,\
#                                 uid TEXT NOT NULL,\
#                                 creation_time TEXT NOT NULL,\
#                                 end_time TEXT NOT NULL,\
#                                 status TEXT NOT NULL,\
#                                 proxy_password TEXT NOT NULL,\
#                                 proxy_username TEXT NOT NULL,\
#                                 proxy_project_name TEXT NOT NULL)")
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ProxyScanList(class)_init(def)", e)
#
#     def Write(self, **kwargs) -> bool or None:  # 写入相关信息
#         CreationTime = str(int(time.time()))  # 创建时间
#         Uid = kwargs.get("uid")
#         EndTime= kwargs.get("end_time")
#         Status= 1#kwargs.get("status")#1表示启动0表示关闭
#         ProxyPassword= kwargs.get("proxy_password")
#         ProxyUsername= kwargs.get("proxy_username")
#         ProxyProjectName= kwargs.get("proxy_project_name")
#
#         try:
#             self.cur.execute("select creation_time from ProxyScanList")
#             ProxyId="P"+str(len(self.cur.fetchall())+1)#构建特殊的ProxyId
#             self.cur.execute("INSERT INTO ProxyScanList(proxy_id,uid,creation_time,end_time,status,proxy_password,proxy_username,proxy_project_name)\
#                 VALUES (?,?,?,?,?,?,?,?)", (ProxyId,Uid, CreationTime, EndTime,Status,ProxyPassword,ProxyUsername,ProxyProjectName,))
#             # 提交
#             self.con.commit()
#             self.con.close()
#             return True
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ProxyScanList(class)_Write(def)", e)
#             return None
#
#     def QueryProxyProjectName(self,**kwargs)->bool or None:#查询扫描项目是否冲突,一个项目不能存在相同的项目名和用户名
#         Uid = kwargs.get("uid")
#         ProxyProjectName = kwargs.get("proxy_project_name")
#         ProxyUsername = kwargs.get("proxy_username")
#         try:
#             self.cur.execute("select * from ProxyScanList where proxy_project_name =? and uid=? and proxy_username=?", (ProxyProjectName,Uid,ProxyUsername))
#             if self.cur.fetchall():  # 判断是否有数据
#                 self.con.close()
#                 return True
#             else:
#                 return False
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ProxyScanList(class)_QueryScanProjectName(def)", e)
#             return None
#     def ProxyAuthentication(self,**kwargs)->bool or None:#查询用来认证用户的账号和密码是否复核UID
#         ProxyUsername = kwargs.get("proxy_username")
#         ProxyPassword = kwargs.get("proxy_password")
#         try:
#             self.cur.execute("select * from ProxyScanList where proxy_username =? and proxy_password=?", (ProxyUsername,ProxyPassword,))
#             for i in self.cur.fetchall():
#                 JsonValues = {}
#                 JsonValues["proxy_id"] = i[0]
#                 JsonValues["uid"] = i[1]
#                 return JsonValues
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ProxyScanList(class)_ProxyAuthentication(def)", e)
#             return None
#
#     # def Query(self,**kwargs)->bool or None:#查询该文件是否是该用户所有
#     #     Uid = kwargs.get("uid")
#     #     FileName = kwargs.get("file_name")
#     #     try:
#     #         self.cur.execute("select * from ReportGenerationList where file_name =? and uid=?", (FileName,Uid,))
#     #         if self.cur.fetchall():  # 判断是否有数据
#     #             self.con.close()
#     #             return True
#     #         else:
#     #             return False
#     #     except Exception as e:
#     #         ErrorLog().Write("Web_DatabaseHub_ProxyScanList(class)_Query(def)", e)
#     #         return None
#

# class OriginalProxyData:#从代理中获取数据包进行存储
#     def __init__(self):
#         self.con = sqlite3.connect(GetPath().DatabaseFile())
#         # 获取所创建数据的游标
#         self.cur = self.con.cursor()
#         # 创建表
#         try:
#             self.cur.execute("CREATE TABLE OriginalProxyData\
#                                 (original_proxy_id INTEGER PRIMARY KEY,\
#                                 uid TEXT NOT NULL,\
#                                 proxy_id TEXT NOT NULL,\
#                                 creation_time TEXT NOT NULL,\
#                                 url TEXT NOT NULL,\
#                                 request_headers TEXT NOT NULL,\
#                                 request_date TEXT NOT NULL,\
#                                 request_method TEXT NOT NULL,\
#                                 response_headers TEXT NOT NULL,\
#                                 response_status_code TEXT NOT NULL,\
#                                 response_date_bytes TEXT NOT NULL,\
#                                 response_date_string TEXT NOT NULL,\
#                                 issue_task_status TEXT NOT NULL,\
#                                 redis_id TEXT NOT NULL)")
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_OriginalProxyData(class)_init(def)", e)
#
#     def Write(self, **kwargs) -> bool or None:  # 写入相关信息
#         CreationTime = str(int(time.time()))  # 创建时间
#         Uid = kwargs.get("uid")
#         ProxyId = kwargs.get("proxy_id")
#         Url= kwargs.get("url")
#         RequestHeaders= kwargs.get("request_headers")
#         RequestDate= kwargs.get("request_date")
#         RequestMethod=kwargs.get("request_method")
#         ResponseHeaders=kwargs.get("response_headers")
#         ResponseStatusCode=kwargs.get("response_status_code")
#         ResponseDateBytes=kwargs.get("response_date_bytes")
#         ResponseDateString=kwargs.get("response_date_string")
#         IssueTaskStatus= "0"#未扫描为0 已扫描为1
#         RedisId=kwargs.get("redis_id")
#
#         try:
#             self.cur.execute("INSERT INTO OriginalProxyData(uid,proxy_id,creation_time,url,request_headers,request_date,request_method,response_headers,response_status_code,response_date_bytes,response_date_string,issue_task_status,redis_id)\
#                 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (Uid, ProxyId, CreationTime, Url,RequestHeaders,RequestDate,RequestMethod,ResponseHeaders,ResponseStatusCode,ResponseDateBytes,ResponseDateString,IssueTaskStatus,RedisId,))
#             # 提交
#             self.con.commit()
#             self.con.close()
#             return True
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_OriginalProxyData(class)_Write(def)", e)
#             return None
#     def UpdateScanStatus(self, **kwargs) -> bool or None:#更新扫描状态
#         Uid = kwargs.get("uid")
#         RedisId = kwargs.get("redis_id")
#         try:
#             self.cur.execute("""UPDATE OriginalProxyData SET issue_task_status= ? WHERE uid = ? and redis_id = ? """,
#                              ( "1",Uid, RedisId,))
#             # 提交
#             if self.cur.rowcount < 1:  # 用来判断是否更新成功
#                 self.con.commit()
#                 self.con.close()
#                 return False
#             else:
#                 self.con.commit()
#                 self.con.close()
#                 return True
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ReportGenerationList(class)_QueryTokenValidity(def)", e)
#             return False
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
    #         ErrorLog().Write("Web_DatabaseHub_ReportGenerationList(class)_QueryTokenValidity(def)", e)
    #         return None
class HomeInfo:#查询首页信息表
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        self.info={}#用来存数据

    def NumberOfVulnerabilities(self,uid):#查询漏洞个数,以及各个等级相关个数，通过查询medusa表来获取所有个数
        try:
            #查询总个数
            self.cur.execute("select scan_info_id from Medusa where uid =? ", (uid,))
            self.info["number_of_vulnerabilities"]=str(len(self.cur.fetchall()))
            #查询高危个数
            self.cur.execute("select scan_info_id from Medusa where uid =? and rank='高危'", (uid,))
            self.info["high_risk_number"] = str(len(self.cur.fetchall()))
            #查询中危个数
            self.cur.execute("select scan_info_id from Medusa where uid =? and rank='中危'", (uid,))
            self.info["mid_risk_number"] = str(len(self.cur.fetchall()))
            #查询高危个数
            self.cur.execute("select scan_info_id from Medusa where uid =? and rank='低危'", (uid,))
            self.info["low_risk_number"] = str(len(self.cur.fetchall()))
        except Exception as e:#设置默认值
            ErrorLog().Write("Web_DatabaseHub_HomeInfo(class)_NumberOfVulnerabilities(def)", e)
            self.info["number_of_vulnerabilities"]="0"
            self.info["high_risk_number"] ="0"
            self.info["mid_risk_number"] ="0"
            self.info["low_risk_number"] ="0"

    def NumberOfWebsites(self, uid):#查询目标网站个数，通过ActiveScanList列表查询
        try:

            self.cur.execute("select active_scan_id from ActiveScanList where uid =? ", (uid,))

            #先对数据进行提取

            self.info["number_of_websites"]=str(len(self.cur.fetchall()))

        except Exception as e:#设置默认值
            ErrorLog().Write("Web_DatabaseHub_HomeInfo(class)_NumberOfWebsites(def)", e)
            self.info["number_of_websites"]="0"
    def NumberOfPorts(self, uid):#查询全部端口发现数量，通过PortInfo表查询
        try:

            self.cur.execute("select * from PortInfo where uid=?", (uid,))
            self.info["number_of_port"]=str(len(self.cur.fetchall()))
        except Exception as e:#设置默认值
            ErrorLog().Write("Web_DatabaseHub_HomeInfo(class)_NumberOfPorts(def)", e)
            self.info["number_of_port"] ="0"

    def NumberOfAgentTasks(self,uid):  # 查询代理扫描数量，暂无模块,所有返回值直接为0
        try:
            self.info["number_of_agent_tasks"] = "0"
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_HomeInfo(class)_GithubMonitorDate(def)", e)
            self.info["number_of_agent_tasks"] = "0"
    def GithubMonitor(self, **kwargs):#查询GitHub监控数据
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")
        try:
            self.cur.execute("select write_time from GithubMonitor where write_time<=? and write_time>=?", (end_time,start_time,))
            count_dict = {}
            tmp=[]

            for x in self.cur.fetchall():#先对数据进行提取
                tmp.append(x[0])
            for i in set(tmp):#在对数据进行统计
                count_dict[i] = tmp.count(i)
            #对数据进行排序
            sort_result = sorted(count_dict.items(), key=lambda item: item[0])
            return sort_result#直接返回数据
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_HomeInfo(class)_GithubMonitor(def)", e)
            return None

    def VulnerabilityDistribution(self, **kwargs):#查询时间段中，漏洞分布，通过查询medusa表来获取所有个数
        uid = kwargs.get("uid")
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")
        try:
            #查询时间段中数据分布
            self.cur.execute("select timestamp from Medusa where uid =? and timestamp<=? and timestamp>=?", (uid,end_time,start_time,))
            count_dict = {}
            tmp=[]

            for x in self.cur.fetchall():#先对数据进行提取
                tmp.append(x[0])
            for i in set(tmp):#在对数据进行统计
                count_dict[i] = tmp.count(i)
            #对数据进行排序
            sort_result = sorted(count_dict.items(), key=lambda item: item[0])
            return sort_result#直接返回数据
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_HomeInfo(class)_TimeDistribution(def)", e)
            return None

    def DefaultData(self,**kwargs):#返回默认数据，该数据恒定不变
        uid=kwargs.get("uid")
        self.NumberOfVulnerabilities(uid)#查询漏洞个数
        #self.TimeDistribution(Uid,StartTime,EndTime)#查询时间段中，漏洞分布
        self.NumberOfWebsites(uid)#查询目标网站个数
        self.NumberOfPorts(uid)#查询全部端口发现数量
        self.NumberOfAgentTasks(uid)#查询代理数量接口
        #self.GithubMonitorDate(StartTime,EndTime)#查询时间段中GitHub监控数据
        self.con.close()
        return self.info

#
# class ProxyTempUrl:#代理转储数据,为了防止重复下发任务做的
#     def __init__(self):
#         self.con = sqlite3.connect(GetPath().DatabaseFile())
#         # 获取所创建数据的游标
#         self.cur = self.con.cursor()
#         # 创建表
#         try:
#             self.cur.execute("CREATE TABLE ProxyTempUrl\
#                                 (proxy_temp_url_id INTEGER PRIMARY KEY,\
#                                 uid TEXT NOT NULL,\
#                                 proxy_temp_url TEXT NOT NULL,\
#                                 creation_time TEXT NOT NULL,\
#                                 proxy_id TEXT NOT NULL,\
#                                 redis_id TEXT NOT NULL)")
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ProxyTempUrl(class)_init(def)", e)
#
#     def Write(self, **kwargs) -> bool or None:  # 写入相关信息
#         CreationTime = str(int(time.time()))  # 创建时间
#         Uid = kwargs.get("uid")
#         ProxyTempUrl = kwargs.get("proxy_temp_url")
#         RedisId= kwargs.get("redis_id")
#         ProxyId = kwargs.get("proxy_id")
#         try:
#             self.cur.execute("INSERT INTO ProxyTempUrl(uid,proxy_temp_url,creation_time,proxy_id,redis_id)\
#                 VALUES (?,?,?,?,?)", (Uid, ProxyTempUrl, CreationTime, ProxyId,RedisId,))
#             # 提交
#             self.con.commit()
#             self.con.close()
#             return True
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ProxyTempUrl(class)_Write(def)", e)
#             return False
#
#     def Query(self, **kwargs):  # 查询查看url的创建时间
#         try:
#             ProxyTempUrl = kwargs.get("proxy_temp_url")
#             Uid = kwargs.get("uid")
#             ProxyId=kwargs.get("proxy_id")
#             self.cur.execute("select creation_time from ProxyTempUrl where uid =? and proxy_temp_url = ? and proxy_id= ?", (Uid, str(ProxyTempUrl),str(ProxyId),))
#             #self.cur.execute("select * from ProxyTempUrl where uid =? ", (Uid,))
#             return self.cur.fetchall()[-1][0]#返回最新的一条数据
#         except Exception as e:
#             ErrorLog().Write("Web_DatabaseHub_ProxyTempUrl(class)_Query(def)", e)
#             return None

class CrossSiteScriptInfo:#XSS钓鱼接收数据库
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptInfo(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        creation_time = str(int(time.time()))  # 创建时间
        headers= kwargs.get("headers").decode('utf-8')
        ip = kwargs.get("ip")
        project_associated_file_name= kwargs.get("project_associated_file_name")
        request_method = kwargs.get("request_method")
        full_url = kwargs.get("full_url")
        data_pack = kwargs.get("data_pack").decode('utf-8')
        try:
            self.cur.execute("INSERT INTO CrossSiteScript(headers,project_associated_file_name,ip,full_url,creation_time,request_method,data_pack)\
                VALUES (?,?,?,?,?,?,?)", (headers,project_associated_file_name, ip, full_url,creation_time, request_method,data_pack,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptInfo(class)_Write(def)", e)
            return False

    def Query(self, **kwargs):  # 查询查看XSS项目数据
        try:
            project_associated_file_name = kwargs.get("project_associated_file_name")
            number_of_single_pages = 100  # 单页数量
            number_of_pages = kwargs.get(
                "number_of_pages") - 1  # 查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select * from CrossSiteScript where project_associated_file_name=? limit ? offset ?", (project_associated_file_name, number_of_single_pages, number_of_pages * number_of_single_pages,))
            result_list=[]
            for i in self.cur.fetchall():
                jsonvalues = {}
                jsonvalues["headers"] = i[1]
                jsonvalues["project_associated_file_name"] = i[2]
                jsonvalues["ip"] = i[3]
                jsonvalues["full_url"] = i[4]
                jsonvalues["creation_time"] = i[5]
                jsonvalues["request_method"] = i[6]
                jsonvalues["data_pack"] = i[7]
                result_list.append(jsonvalues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScript(class)_Query(def)", e)
            return None
    def QueryStatistics(self, **kwargs):  #用来统计接收数据个数
        project_associated_file_name = kwargs.get("project_associated_file_name")
        try:
            self.cur.execute("SELECT COUNT(1)  FROM CrossSiteScript WHERE project_associated_file_name=?",(project_associated_file_name,))
            result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScript(class)_QueryStatistics(def)", e)
            return None

class CrossSiteScriptProject:#XSS钓鱼项目信息数据库
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptProject(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        creation_time = str(int(time.time()))  # 创建时间
        uid= kwargs.get("uid")
        file_name = kwargs.get("file_name")
        project_name=kwargs.get("project_name")
        try:
            self.cur.execute("INSERT INTO CrossSiteScriptProject(uid,project_name,file_name,creation_time)\
                VALUES (?,?,?,?)", (uid, project_name,file_name, creation_time,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptProject(class)_Write(def)", e)
            return False
    def Query(self, **kwargs):  # 查询查看XSS项目信息
        try:
            uid = kwargs.get("uid")
            number_of_single_pages = 100  # 单页数量
            number_of_pages = kwargs.get(
                "number_of_pages") - 1  # 查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select * from CrossSiteScriptProject where uid =? limit ? offset ?", (uid,number_of_single_pages, number_of_pages * number_of_single_pages))
            result_list=[]
            for i in self.cur.fetchall():
                json_values = {}
                json_values["project_name"] = i[2]
                json_values["file_name"] = i[3]
                json_values["creation_time"] = i[4]
                result_list.append(json_values)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptProject(class)_Query(def)", e)
            return None
    def QueryStatistics(self, **kwargs):  #用来项目个数
        uid = kwargs.get("uid")
        try:
            self.cur.execute("SELECT COUNT(1)  FROM CrossSiteScriptProject WHERE uid=?",(uid,))
            result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptProject(class)_QueryStatistics(def)", e)
            return None
    def RepeatInvestigation(self,**kwargs):#用来排查file_name是否重复

        try:
            file_name = kwargs.get("file_name")
            self.cur.execute("select * from CrossSiteScriptProject where  file_name=? ", (file_name,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptProject(class)_RepeatInvestigation(def)", e)
            return False

    def AuthorityCheck(self,**kwargs):#用来校检CrossSiteScript数据库中文件名和UID相对应

        try:
            file_name = kwargs.get("file_name")
            uid = kwargs.get("uid")
            self.cur.execute("select * from CrossSiteScriptProject where  file_name=? and uid=?", (file_name,uid,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptProject(class)_AuthorityCheck(def)", e)
            return False
    def Delete(self,**kwargs):#删除项目
        try:
            project_name = kwargs.get("project_name")
            uid=kwargs.get("uid")
            self.cur.execute("DELETE FROM CrossSiteScriptProject where project_name=? and uid=?", (project_name,uid,))
            if self.cur.rowcount < 1:  # 用来判断是否更新成功
                self.con.commit()
                self.con.close()
                return False
            else:
                self.con.commit()
                self.con.close()
                return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptProject(class)_Delete(def)", e)
            return None
class CrossSiteScriptTemplate:  # XSS钓鱼模板存放
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptProject(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        creation_time = str(int(time.time()))  # 创建时间
        update_time = str(int(time.time()))  # 更新时间
        uid = kwargs.get("uid")
        template_name = kwargs.get("template_name")
        template_data = kwargs.get("template_data")#base64加密过的数据
        try:
            self.cur.execute("INSERT INTO CrossSiteScriptTemplate(uid,template_name,template_data,creation_time,update_time)\
                VALUES (?,?,?,?,?)", (uid, template_name, template_data, creation_time,update_time,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptTemplate(class)_Write(def)", e)
            return False

    def Query(self, **kwargs):  # 查询查看XSS项目信息
        try:
            uid = kwargs.get("uid")
            self.cur.execute("select * from CrossSiteScriptTemplate where uid =?", (uid,))
            result_list = []
            for i in self.cur.fetchall():
                json_values = {}
                json_values["template_name"] = i[2]
                json_values["template_data"] = i[3]
                json_values["creation_time"] = i[4]
                json_values["update_time"] = i[5]
                result_list.append(json_values)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptTemplate(class)_Query(def)", e)
            return None
    def RepeatInvestigation(self,**kwargs):#用来排查template_name是否重复

        try:
            uid = kwargs.get("uid")
            template_name = kwargs.get("template_name")
            self.cur.execute("select * from CrossSiteScriptTemplate where uid =? and template_name=?", (uid,template_name,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptTemplate(class)_RepeatInvestigation(def)", e)
            return False
    def Update(self,**kwargs):
        update_time=str(int(time.time()))
        uid = kwargs.get("uid")
        template_name = kwargs.get("template_name")
        template_data = kwargs.get("template_data")  # base64加密过的数据
        try:
            self.cur.execute(
                """UPDATE CrossSiteScriptTemplate SET template_data = ?,update_time=? WHERE uid = ? and template_name=? """,
                (template_data,update_time,uid,template_name,))
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
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptTemplate(class)_Update(def)", e)
    def Delete(self,**kwargs):#删除项目
        try:
            template_name = kwargs.get("template_name")
            uid=kwargs.get("uid")
            self.cur.execute("DELETE FROM CrossSiteScriptTemplate where template_name=? and uid=?", (template_name,uid,))
            if self.cur.rowcount < 1:  # 用来判断是否更新成功
                self.con.commit()
                self.con.close()
                return False
            else:
                self.con.commit()
                self.con.close()
                return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_CrossSiteScriptTemplate(class)_Delete(def)", e)
            return None

class HardwareUsageRateInfo:  # 获取硬件中CPU和内存的使用情况
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_HardwareUsageRateInfo(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        creation_time = str(int(time.time()))  # 创建时间
        memory_used = kwargs.get("memory_used")
        memory_free = kwargs.get("memory_free")
        memory_percent = kwargs.get("memory_percent")
        central_processing_unit_usage_rate = kwargs.get("central_processing_unit_usage_rate")
        per_core_central_processing_unit_usage_rate = kwargs.get("per_core_central_processing_unit_usage_rate")
        try:
            self.cur.execute("INSERT INTO HardwareUsageRateInfo(memory_used,memory_free,memory_percent,creation_time,central_processing_unit_usage_rate,per_core_central_processing_unit_usage_rate)\
                VALUES (?,?,?,?,?,?)", (memory_used, memory_free, memory_percent, creation_time,central_processing_unit_usage_rate,per_core_central_processing_unit_usage_rate,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_HardwareUsageRateInfo(class)_Write(def)", e)
            return False

    def Query(self):  # 查询查看CPU和内存使用信息
        try:
            creation_time = str(int(time.time()))  # 获取当前时间

            self.cur.execute("select * from HardwareUsageRateInfo where creation_time<=? and creation_time>=?", (creation_time,str(int(creation_time)-3600),))#查询半小时之前的CPU使用率，和内存使用率
            result_list = []
            for i in self.cur.fetchall():
                json_values = {}
                json_values["memory_used"] = i[1]
                json_values["memory_free"] = i[2]
                json_values["memory_percent"] = i[3]
                json_values["creation_time"] = i[4]
                json_values["central_processing_unit_usage_rate"] = i[5]
                json_values["per_core_central_processing_unit_usage_rate"] = json.loads(i[6])
                result_list.append(json_values)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_HardwareUsageRateInfo(class)_Query(def)", e)
            return None

class PortableExecutableAnalyticalData:  # PE文件分析后数据存储
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_PortableExecutableAnalyticalData(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        creation_time = str(int(time.time()))  # 创建时间
        uid = kwargs.get("uid")
        file_size= kwargs.get("file_size")
        md5= kwargs.get("md5")
        sha1= kwargs.get("sha1")
        sha256= kwargs.get("sha256")
        save_file_name= kwargs.get("save_file_name")
        file_generation_time= kwargs.get("file_generation_time")
        image_dos_header= kwargs.get("image_dos_header")
        image_nt_headers= kwargs.get("image_nt_headers")
        image_file_header= kwargs.get("image_file_header")
        image_optional_header= kwargs.get("image_optional_header")
        image_section_header = kwargs.get("image_section_header")
        image_import_descriptor= kwargs.get("image_import_descriptor")
        image_export_directory= kwargs.get("image_export_directory")
        certificate_data_container= kwargs.get("certificate_data_container")
        image_resource_directory= kwargs.get("image_resource_directory")
        image_tls_directory= kwargs.get("image_tls_directory")

        try:
            self.cur.execute("INSERT INTO PortableExecutable(uid,file_size,md5,sha1,sha256,save_file_name,creation_time,file_generation_time,image_dos_header,image_nt_headers,image_file_header,image_optional_header,image_section_header,image_import_descriptor,image_export_directory,certificate_data_container,image_resource_directory,image_tls_directory)\
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (uid, file_size, md5, sha1,sha256,save_file_name,creation_time,file_generation_time,image_dos_header,image_nt_headers,image_file_header,image_optional_header,image_section_header ,image_import_descriptor,image_export_directory,certificate_data_container,image_resource_directory,image_tls_directory,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_PortableExecutableAnalyticalData(class)_Write(def)", e)
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
    #         ErrorLog().Write("Web_DatabaseHub_PortableExecutableAnalyticalData(class)_Query(def)", e)
    #         return None


class VerificationCode:#验证码相关数据库，用来验证验证码合法性
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_VerificationCode(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        creation_time = str(int(time.time()))  # 创建时间
        code = kwargs.get("code")#验证码字符串
        verification_code_key = kwargs.get("verification_code_key")#验证码相关联的Key
        verification_code_status=0#验证码是否使用过，如果使用过值为1，未使用过为1
        try:
            self.cur.execute("INSERT INTO VerificationCode(code,verification_code_key,creation_time,verification_code_status)\
                VALUES (?,?,?,?)", (code,verification_code_key,creation_time,verification_code_status,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_VerificationCode(class)_Write(def)", e)
            return False

    def Query(self, **kwargs):  #查询验证码是否正确
        try:
            creation_time = int(time.time())  # 获取当前时间
            code = kwargs.get("code")  # 验证码字符串
            verification_code_key = kwargs.get("verification_code_key")  # 验证码相关联的Key
            self.cur.execute("select * from VerificationCode where code =? and verification_code_key=?", (code,verification_code_key,))

            for i in self.cur.fetchall():
                if (creation_time-int(i[3]))>60:#操过60秒验证码失效
                    return False
                elif i[4]!="0":#判断如果验证码是使用过的
                    return False
                else:
                    self.cur.execute(
                        """UPDATE VerificationCode SET verification_code_status = ? WHERE  code = ? and verification_code_key=? """,
                        ("1",code, verification_code_key,))#查询成功后就把数据库值给更新了
                    self.con.commit()
                    self.con.close()
                    return True

        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_VerificationCode(class)_Query(def)", e)
            return None

class MarkdownInfo:#存放markdown文档的所有数据
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_MarkdownInfo(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        creation_time = str(int(time.time()))  # 创建时间
        markdown_name = kwargs.get("markdown_name")#生成的markdown文档名
        markdown_data = kwargs.get("markdown_data")#用户传入的markdown数据
        #MarkdownProjectData = kwargs.get("markdown_project_name")  # 用户传入的markdown数据
        try:
            self.cur.execute("INSERT INTO Markdown(markdown_name,markdown_data,creation_time,update_time)\
                VALUES (?,?,?,?)", (markdown_name,markdown_data,creation_time,creation_time,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownInfo(class)_Write(def)", e)
            return False
    def CheckConflict(self,**kwargs):#检查name是否会冲突
        try:
            markdown_name=kwargs.get("markdown_name")
            self.cur.execute("select * from Markdown where markdown_name=?", (markdown_name,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownInfo(class)_CheckConflict(def)", e)
            return None
    def Update(self, **kwargs) -> bool or None:  # 如果存在就进行更新
        update_time = str(int(time.time()))  # 当前时间
        markdown_name = kwargs.get("markdown_name")#生成的markdown文档名
        markdown_data = kwargs.get("markdown_data")#用户传入的markdown数据
        try:
            self.cur.execute(
                """UPDATE Markdown SET markdown_data = ?,update_time=? WHERE markdown_name = ? """,
                (markdown_data, update_time, markdown_name,))
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
            ErrorLog().Write("Web_DatabaseHub_MarkdownInfo(class)_Write(def)", e)
            return None
    def Query(self,**kwargs):  # 文本具体数据
        try:
            markdown_name=kwargs.get("markdown_name")
            self.cur.execute("select * from Markdown where markdown_name=?", (markdown_name,))
            result_list = []
            for i in self.cur.fetchall():
                json_values = {}
                json_values["markdown_name"] = i[1]
                json_values["markdown_data"] = i[2]
                json_values["creation_time"] = i[3]
                json_values["update_time"] = i[4]
                result_list.append(json_values)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownInfo(class)_Query(def)", e)
            return None
    def QueryMarkdownData(self,**kwargs):  # 只查询docker 数据
        try:
            markdown_name=kwargs.get("markdown_name")
            self.cur.execute("select * from Markdown where markdown_name=?", (markdown_name,))
            for i in self.cur.fetchall():
                self.con.close()
                return i[2]#直接返回数据
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownInfo(class)_Query(def)", e)
            return None
    def Delete(self,**kwargs):#删除项目
        try:
            markdown_name=kwargs.get("markdown_name")
            self.cur.execute("DELETE FROM Markdown where markdown_name=? ", (markdown_name,))
            if self.cur.rowcount < 1:  # 用来判断是否更新成功
                self.con.commit()
                self.con.close()
                return False
            else:
                self.con.commit()
                self.con.close()
                return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownInfo(class)_Delete(def)", e)
            return None

class MarkdownRelationship:#markdown文档和用户相关的数据表
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        creation_time = str(int(time.time()))  # 创建时间
        markdown_name = kwargs.get("markdown_name")#文件名确保唯一性
        uid = kwargs.get("uid")
        markdown_project_name = kwargs.get("markdown_project_name")#项目的名称
        markdown_project_owner = kwargs.get("markdown_project_owner")#项目是否是该用户所有，如果是值为1，如果不是值为0
        markdown_project_invitation_code = kwargs.get("markdown_project_invitation_code")#项目的邀请码，输入邀请码可以直接加入项目
        try:
            self.cur.execute("INSERT INTO MarkdownRelationship(uid,markdown_project_owner,markdown_project_invitation_code,markdown_project_name,markdown_name,creation_time)\
                VALUES (?,?,?,?,?,?)", (uid,markdown_project_owner,markdown_project_invitation_code,markdown_project_name,markdown_name,creation_time,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_Write(def)", e)
            return False
    def CheckInvitationCode(self,**kwargs):#检查邀请码是否会冲突
        try:
            markdown_project_invitation_code=kwargs.get("markdown_project_invitation_code")
            self.cur.execute("select * from MarkdownRelationship where markdown_project_invitation_code=?", (markdown_project_invitation_code,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_CheckInvitationCode(def)", e)
            return None
    def InvitationCodeToQueryProjectInformation(self,**kwargs):#通过验证码查询项目信息，用来加入项目使用
        try:
            markdown_project_invitation_code=kwargs.get("markdown_project_invitation_code")
            self.cur.execute("select * from MarkdownRelationship where markdown_project_invitation_code=?", (markdown_project_invitation_code,))  # 查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                json_values = {}
                json_values["uid"] = i[1]
                json_values["markdown_project_name"] = i[4]
                json_values["markdown_name"] = i[5]
                result_list.append(json_values)
            self.con.close()
            if result_list==[]:#判断是否为空数据
                return None
            else:
                return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_InvitationCodeToQueryProjectInformation(def)", e)
            return None
    def DetectionOfRepeatedAddition(self,**kwargs):#检测是否重复加入
        try:
            uid=kwargs.get("uid")
            markdown_name=kwargs.get("markdown_name")
            self.cur.execute("select * from MarkdownRelationship where markdown_name=? and uid=?", (markdown_name,uid,))  # 查询用户相关信息
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_InvitationCodeToQueryProjectInformation(def)", e)
            return None
    def CheckConflict(self,**kwargs):#检查name是否会冲突
        try:
            markdown_name=kwargs.get("markdown_name")
            self.cur.execute("select * from MarkdownRelationship where markdown_name=?", (markdown_name,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_CheckConflict(def)", e)
            return None
    def CheckPermissions(self,**kwargs):#检测用户是否有该项目的权限

        try:
            markdown_name=kwargs.get("markdown_name")
            uid=kwargs.get("uid")
            self.cur.execute("select * from MarkdownRelationship where markdown_name=? and uid=?", (markdown_name,uid,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_CheckPermissions(def)", e)
            return None

    def Query(self, **kwargs):  #用来查询用户所属项目的全部信息
        try:
            uid=kwargs.get("uid")
            number_of_single_pages = 100  # 单页数量
            number_of_pages = kwargs.get(
                "number_of_pages") - 1  # 查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select * from MarkdownRelationship where uid=? limit ? offset ?", (uid,number_of_single_pages, number_of_pages * number_of_single_pages,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                json_values = {}
                if i[2]==0:#判断项目是否属于用户，如果不属于就清空邀请码
                    json_values["markdown_project_invitation_code"] = ""
                else:
                    json_values["markdown_project_invitation_code"] = i[3]
                json_values["markdown_project_owner"] = i[2]
                json_values["markdown_project_name"] = i[4]
                json_values["markdown_name"] = i[5]
                json_values["creation_time"] = i[6]
                result_list.append(json_values)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_Query(def)", e)
            return None
    def QueryStatistics(self, **kwargs):  #用来统计用户所属项目个数
        uid = kwargs.get("uid")
        try:
            self.cur.execute("SELECT COUNT(1)  FROM MarkdownRelationship WHERE uid=?",(uid,))
            result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_QueryStatistics(def)", e)
            return None
    def ProjectBelongs(self,**kwargs):#检测项目是否属于该用户
        try:
            markdown_name=kwargs.get("markdown_name")
            uid=kwargs.get("uid")
            self.cur.execute("select markdown_project_owner from MarkdownRelationship where markdown_name=? and uid=?", (markdown_name,uid,))
            for i in self.cur.fetchall():
                if i[0]=="1":
                    self.con.close()
                    return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_ProjectBelongs(def)", e)
            return None
    def Delete(self,**kwargs):#删除项目
        try:
            markdown_name=kwargs.get("markdown_name")
            uid=kwargs.get("uid")
            self.cur.execute("DELETE FROM MarkdownRelationship where markdown_name=? and uid=?", (markdown_name,uid,))
            if self.cur.rowcount < 1:  # 用来判断是否更新成功
                self.con.commit()
                self.con.close()
                return False
            else:
                self.con.commit()
                self.con.close()
                return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MarkdownRelationship(class)_Delete(def)", e)
            return None
class ApplicationCollection:#存放收集到的应用所有数据
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
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
            ErrorLog().Write("Web_DatabaseHub_ApplicationCollection(class)_init(def)", e)
    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        uid = kwargs.get("uid")  # 用户id
        program_type = kwargs.get("program_type")#类型是ios还是安卓
        status = kwargs.get("status")#正在扫描还是已经完成
        application_data = kwargs.get("application_data")  # 获取的应用数据
        redis_id = kwargs.get("redis_id")  # Redis值
        request_failed_application_name = kwargs.get("request_failed_application_name")  # 获取失败的应用名
        total_number_of_applications = kwargs.get("total_number_of_applications")  # 全部应用数
        number_of_failures = kwargs.get("number_of_failures")  # 获取失败应用数
        try:
            self.cur.execute("INSERT INTO ApplicationCollection(uid,program_type,creation_time,status,application_data,redis_id,request_failed_application_name,total_number_of_applications,number_of_failures)\
                VALUES (?,?,?,?,?,?,?,?,?)", (uid,program_type,CreationTime,status,application_data,redis_id,request_failed_application_name,total_number_of_applications,number_of_failures,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_ApplicationCollection(class)_Write(def)", e)
            return False
    def Update(self, **kwargs) -> bool or None:  # 对数据进行更新
        uid = kwargs.get("uid")  # 用户id
        status = "1"#正在扫描还是已经完成
        application_data = kwargs.get("application_data")  # 获取的应用数据
        redis_id = kwargs.get("redis_id")  # Redis值
        request_failed_application_name = kwargs.get("request_failed_application_name")  # 获取失败的应用名
        total_number_of_applications = kwargs.get("total_number_of_applications")  # 全部应用数
        number_of_failures = kwargs.get("number_of_failures")  # 获取失败应用数
        try:
            self.cur.execute(
                """UPDATE ApplicationCollection SET status = ?,application_data=?,request_failed_application_name=?,total_number_of_applications=?,number_of_failures=? WHERE redis_id = ? and uid=? """,
                (status, application_data, request_failed_application_name,total_number_of_applications,number_of_failures,redis_id,uid,))
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
            ErrorLog().Write("Web_DatabaseHub_ApplicationCollection(class)_Update(def)", e)
            return None
    def Query(self, **kwargs):  #用来查询用户的项目
        try:
            uid=kwargs.get("uid")
            self.cur.execute("select * from ApplicationCollection where uid=?", (uid,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                json_values = {}
                json_values["program_type"] = i[2]
                json_values["creation_time"] = i[3]
                json_values["status"] = i[4]
                json_values["application_data"] = i[5]
                json_values["request_failed_application_name"] = i[7]
                json_values["total_number_of_applications"] = i[8]
                json_values["number_of_failures"] = i[9]
                result_list.append(json_values)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_ApplicationCollection(class)_Query(def)", e)
            return None

class NistData:#存放Nist发布的CVE数据
    def __init__(self):
        self.con = sqlite3.connect(GetPath().NistDatabase())
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
            ErrorLog().Write("Web_DatabaseHub_NistData(class)_init(def)", e)
    def Write(self, DataSet:list) -> bool or None:  # 写入相关信息

        try:
            self.cur.executemany("INSERT INTO CommonVulnerabilitiesAndExposures(vulnerability_number,v3_base_score,v3_base_severity,v2_base_score,v2_base_severity,last_up_date,vulnerability_description,vendors,products,raw_data)\
                VALUES (?,?,?,?,?,?,?,?,?,?)", DataSet)
            # 提交
            self.con.commit()#只发送数据不结束
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_NistData(class)_Write(def)", e)
            return False

    def BulkQuery(self, **kwargs):  #分页查询数据内容
        try:
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select vulnerability_number,v3_base_score,v3_base_severity,v2_base_score,v2_base_severity,last_up_date,vulnerability_description,vendors,products  from CommonVulnerabilitiesAndExposures ORDER BY common_vulnerabilities_and_exposures_id DESC limit ? offset ?", (NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息

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
            ErrorLog().Write("Web_DatabaseHub_NistData(class)_BulkQuery(def)", e)
            return None

    def StatisticalData(self):  # 整体个数统计
        try:
            self.cur.execute("SELECT COUNT(1)  FROM CommonVulnerabilitiesAndExposures",)  # 查询用户相关信息
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_NistData(class)_StatisticalData(def)", e)
            return None
    def DetailedQuery(self, **kwargs):  #单个CVE数据具体内容查询
        try:
            CommonVulnerabilitiesAndExposures=kwargs.get("common_vulnerabilities_and_exposures")#查询第几页
            self.cur.execute("select raw_data from CommonVulnerabilitiesAndExposures where vulnerability_number=? ORDER BY common_vulnerabilities_and_exposures_id DESC ", (CommonVulnerabilitiesAndExposures,))
            Result=self.cur.fetchall()[0][0]
            self.con.close()
            return Result#返回原始数据
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_NistData(class)_DetailedQuery(def)", e)
            return None

    def SearchStatistics(self,**kwargs):  #模糊查询统计个数
        try:
            Severity=kwargs.get("severity")#严重程度
            Key = "%" + kwargs.get("key") + "%"  # 查询字段
            self.cur.execute("select COUNT(1) from CommonVulnerabilitiesAndExposures WHERE v3_base_severity=? and (vulnerability_number LIKE ? OR vendors LIKE ? OR products LIKE ? OR vulnerability_description LIKE ?)", (Severity,Key,Key,Key,Key,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_NistData(class)_SearchStatistics(def)", e)
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
            ErrorLog().Write("Web_DatabaseHub_NistData(class)_Update(def)", e)
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
            ErrorLog().Write("Web_DatabaseHub_NistData(class)_UniqueInquiry(def)", e)
            return None
    def Search(self,**kwargs):  #模糊查询
        try:
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页
            Severity=kwargs.get("severity")#严重程度
            Key = "%"+kwargs.get("key")+"%"  # 查询字段
            self.cur.execute("select vulnerability_number,v3_base_score,v3_base_severity,v2_base_score,v2_base_severity,last_up_date,vulnerability_description,vendors,products  from CommonVulnerabilitiesAndExposures WHERE v3_base_severity=? and (vulnerability_number LIKE ? OR vendors LIKE ? OR products LIKE ? OR vulnerability_description LIKE ?) limit ? offset ?", (Severity,Key,Key,Key,Key,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))

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
            ErrorLog().Write("Web_DatabaseHub_NistData(class)_Search(def)", e)
            return None

class DomainNameSystemLog:  # 存放DNSLOG数据
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE DomainNameSystemLog\
                                (dnslog_id INTEGER PRIMARY KEY,\
                                domain_name TEXT NOT NULL,\
                                ip TEXT NOT NULL,\
                                type TEXT NOT NULL,\
                                request TEXT NOT NULL,\
                                response TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")


        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLog(class)_init(def)", e)

    def Write(self,**kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Ip = kwargs.get("ip")  # 请求IP不一定准确
        DomainName = kwargs.get("domain_name")  # 获取解析域名
        Type= kwargs.get("type")  # 获取解析类型
        Request= kwargs.get("request")  # 获取请求完整数据包
        Response= kwargs.get("response")  # 获取返回完整数据包
        try:
            if Type=="dns":
                DomainNameSystemAddressLength=len("."+domain_name_system_address)#获取长度，加点是为了截断域名
                TreatmentDomainName=DomainName[-DomainNameSystemAddressLength:]#进行截断处理
                if TreatmentDomainName=="."+domain_name_system_address:
                    try:
                        self.cur.execute("INSERT INTO DomainNameSystemLog(domain_name,ip,type,request,response,creation_time)\
                            VALUES (?,?,?,?,?,?)",(DomainName,Ip,Type,Request,Response,CreationTime,))
                        # 提交
                        self.con.commit()  # 只发送数据不结束
                        self.con.close()
                        return True
                    except Exception as e:
                        ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLog(class)_Write(def)", e)
                        return False
            elif Type=="http":
                try:
                    self.cur.execute("INSERT INTO DomainNameSystemLog(domain_name,ip,type,request,response,creation_time)\
                        VALUES (?,?,?,?,?,?)", (DomainName, Ip, Type, Request, Response, CreationTime,))
                    # 提交
                    self.con.commit()  # 只发送数据不结束
                    self.con.close()
                    return True
                except Exception as e:
                    ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLog(class)_Write(def)", e)
                    return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLog(class)_Write(def)-TreatmentDomainName", e)
            return None
    def Query2DNS(self, **kwargs):  #用来DNS类型查询数据
        try:
            NumberOfSinglePages=100#单页数量
            Key="%."+kwargs.get("key")
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select domain_name,ip,creation_time  from DomainNameSystemLog WHERE domain_name Like ? ORDER BY dnslog_id DESC limit ? offset ?", (Key,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询相关信息,倒叙查询
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
            ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLog(class)_Query2DNS(def)", e)
            return None
    def Statistical2DNS(self, **kwargs):  # 统计DNS类型的数量
        Key = "%." + kwargs.get("key")
        try:
            self.cur.execute("SELECT COUNT(1)  FROM DomainNameSystemLog WHERE domain_name Like ?",(Key,))  # 查询用户相关信息
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLog(class)_Statistical2DNS(def)", e)
            return None
    def Query2HTTP(self, **kwargs):  #用来查询HTTP类型数据
        try:
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select request,response,creation_time  from DomainNameSystemLog WHERE type= ? ORDER BY dnslog_id DESC limit ? offset ?", ("http",NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询相关信息,倒叙查询
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["request"] = i[0].decode()
                JsonValues["response"] = i[1].decode()
                JsonValues["creation_time"] = i[2]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLog(class)_Query2HTTP(def)", e)
            return None
    def Statistical2HTTP(self):  # 统计http类型的数量

        try:
            self.cur.execute("SELECT COUNT(1)  FROM DomainNameSystemLog WHERE type= ?",("http",))  # 查询用户相关信息
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLog(class)_Statistical2HTTP(def)", e)
            return None


class DomainNameSystemLogKeyword(object):
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE DomainNameSystemLogKeyword\
                                (dnslog_keyword_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                key TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")


        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLogKeyword(class)_init(def)", e)

    def Write(self,**kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")  # 用户UID
        Key = kwargs.get("key")  # 生成的key，值为5位
        try:
            self.cur.execute("INSERT INTO DomainNameSystemLogKeyword(uid,key,creation_time)\
                VALUES (?,?,?)", (Uid, Key, CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLogKeyword(class)_Write(def)", e)
            return False

    def Query(self, **kwargs):  #用来查询数据
        try:
            Uid = kwargs.get("uid")  # 用户UID
            self.cur.execute("select * from DomainNameSystemLogKeyword WHERE uid=?", (Uid,))
            for i in self.cur.fetchall():
                return i[2]
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_DomainNameSystemLogKeyword(class)_Query(def)", e)
            return None


class TrojanData:#免杀木马相关数据库
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE TrojanData\
                                (trojan_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                shellcode_name NOT NULL,\
                                shellcode_type TEXT NOT NULL,\
                                trojan_original_file_name TEXT NOT NULL,\
                                trojan_generate_file_name TEXT NOT NULL,\
                                compilation_status TEXT NOT NULL,\
                                redis_id TEXT NOT NULL,\
                                creation_time TEXT NOT NULL,\
                                shellcode_architecture TEXT NOT NULL,\
                                plugin TEXT NOT NULL)")


        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_TrojanData(class)_init(def)", e)
    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        Uid = kwargs.get("uid")
        TrojanOriginalFileName=kwargs.get("trojan_original_file_name")
        ShellcodeName = kwargs.get("shellcode_name")#项目名称
        ShellcodeType = kwargs.get("shellcode_type")#1为MSF类型的，2为CS类型的
        TrojanGenerateFileName = kwargs.get("trojan_generate_file_name")
        CompilationStatus = kwargs.get("compilation_status")#状态0为未完成，1完成，-1出错
        RedisId = kwargs.get("redis_id")
        CreationTime = str(int(time.time()))  # 创建时间
        ShellcodeArchitecture = kwargs.get("shellcode_architecture")#shellcode的架构类型 x86 或者x64
        Plugin = kwargs.get("plugin")#当前使用的插件名称
        try:
            self.cur.execute("INSERT INTO TrojanData(uid,shellcode_name,shellcode_type,trojan_original_file_name,trojan_generate_file_name,compilation_status,redis_id,creation_time,shellcode_architecture,plugin)\
                VALUES (?,?,?,?,?,?,?,?,?,?)", (Uid,ShellcodeName,ShellcodeType,TrojanOriginalFileName, TrojanGenerateFileName,CompilationStatus,RedisId, CreationTime,ShellcodeArchitecture,Plugin,))
            self.con.commit()  # 只发送数据不结束
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_TrojanData(class)_Write(def)", e)
            return False
    def StatisticalData(self,**kwargs):  # 当前用户个数统计
        Uid = kwargs.get("uid")
        try:
            self.cur.execute("SELECT COUNT(1)  FROM TrojanData WHERE uid=?",(Uid,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_TrojanData(class)_StatisticalData(def)", e)
            return None
    def UpdateStatus(self,**kwargs)->bool:#利用主键ID来判断后更新数据
        RedisId = kwargs.get("redis_id")
        CompilationStatus = kwargs.get("compilation_status")
        try:
            self.cur.execute("""UPDATE TrojanData SET compilation_status = ? WHERE redis_id= ?""",(CompilationStatus, RedisId,))
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
            ErrorLog().Write("Web_DatabaseHub_TrojanData(class)_UpdateStatus(def)", e)
            return False
    def Query(self, **kwargs):  #用来查询数据
        try:
            Uid = kwargs.get("uid")
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select * from TrojanData WHERE uid=? limit ? offset ? ", (Uid,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["trojan_id"] = i[0]
                JsonValues["shellcode_name"] = i[2]
                JsonValues["shellcode_type"] = i[3]
                JsonValues["trojan_original_file_name"] = i[4]
                JsonValues["trojan_generate_file_name"] = i[5]
                JsonValues["compilation_status"] = i[6]
                JsonValues["creation_time"] = i[8]
                JsonValues["shellcode_architecture"] = i[9]
                JsonValues["plugin"] = i[10]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_TrojanData(class)_Query(def)", e)
            return None
    def DownloadVerification(self, **kwargs):  # 用来验证下载数据是否属于用户
        try:
            Uid = kwargs.get("uid")
            TrojanId = kwargs.get("trojan_id")
            TrojanGenerateFileName = kwargs.get("trojan_generate_file_name")
            self.cur.execute("SELECT COUNT(1)  FROM TrojanData WHERE uid=? and trojan_id=? and trojan_generate_file_name=?",(Uid, TrojanId,TrojanGenerateFileName))  # 查询相关信息
            Result=self.cur.fetchall()[0][0]#获取数据个数
            if Result==0:
                self.con.close()
                return False
            else:
                self.con.close()
                return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_TrojanData(class)_DownloadVerification(def)", e)
            return None

class PortableExecutable2Shellcode:  # PE文件转换为shellcode表
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE PortableExecutable2Shellcode\
                                (shellcode_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                original_file_name TEXT NOT NULL,\
                                file_name TEXT NOT NULL,\
                                shellcode_file_name TEXT NOT NULL,\
                                status TEXT NOT NULL,\
                                redis_id TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_PortableExecutable2Shellcode(class)_init(def)", e)


    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")
        OriginalFileName= kwargs.get("original_file_name")#原始文件名
        FileName = kwargs.get("file_name")  # pe文件
        ShellcodeFileName= kwargs.get("shellcode_file_name")#shellcode文件名
        Status= 0 #状态
        RedisId= kwargs.get("redis_id")

        try:
            self.cur.execute("INSERT INTO PortableExecutable2Shellcode(uid,original_file_name,file_name,shellcode_file_name,status,redis_id,creation_time)\
                VALUES (?,?,?,?,?,?,?)", (Uid,OriginalFileName, FileName, ShellcodeFileName, Status,RedisId,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_PortableExecutable2Shellcode(class)_Write(def)", e)
            return False
    def UpdateStatus(self,**kwargs)->bool:#利用主键ID来判断后更新数据
        RedisId = kwargs.get("redis_id")
        Status = kwargs.get("status")
        try:
            self.cur.execute("""UPDATE PortableExecutable2Shellcode SET status = ? WHERE redis_id= ?""",(Status, RedisId,))
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
            ErrorLog().Write("Web_DatabaseHub_PortableExecutable2Shellcode(class)_UpdateStatus(def)", e)
            return False

class EmailProject:  # 邮件项目
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE EmailProject\
                                (email_project_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                goal_mailbox TEXT NOT NULL,\
                                end_time TEXT NOT NULL,\
                                project_key TEXT NOT NULL,\
                                project_name TEXT NOT NULL,\
                                mail_message TEXT NOT NULL,\
                                attachment TEXT NOT NULL,\
                                image TEXT NOT NULL,\
                                mail_title TEXT NOT NULL,\
                                sender TEXT NOT NULL,\
                                forged_address TEXT NOT NULL,\
                                redis_id TEXT NOT NULL,\
                                compilation_status TEXT NOT NULL,\
                                interval TEXT NOT NULL,\
                                project_status TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")
        EndTime= ""#项目结束时间，结束后不再接受任何数据
        ProjectKey= kwargs.get("project_key")#项目唯一关键字，用于判断接收数据所属
        ProjectName= ""#项目名称
        MailMessage= ""#正文内容，需要用base64加密
        Attachment= ""#附件文件，需要传入json格式，使用的是本地名称
        Image = ""  # 图片文件，使用列表形式窜入
        MailTitle= ""#邮件头
        Sender= ""#发送人名称
        GoalMailbox =""# 目标邮箱列表
        ForgedAddress = ""# 伪造的发件人地址
        RedisId ="" # id值
        CompilationStatus = "0"  # 状态0表示未完成，1表示完成，如果值为1那么就不再能够更新项目内容
        Interval ="" # 邮件发送间隔
        ProjectStatus="0"#项目状态，0表示未启动，1表示启动，启动中无法修改项目

        try:
            self.cur.execute("INSERT INTO EmailProject(uid,goal_mailbox,end_time,project_key,project_name,mail_message,attachment,image,mail_title,sender,forged_address,redis_id,compilation_status,interval,project_status,creation_time)\
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (Uid,str(GoalMailbox),str(EndTime), str(ProjectKey),str(ProjectName),MailMessage, str(Attachment), str(Image),MailTitle,Sender,str(ForgedAddress),RedisId,CompilationStatus,Interval,ProjectStatus,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_Write(def)", e)
            return False
    def Updata(self,**kwargs)->bool:#利用主键ID来判断后更新数据
        Uid = kwargs.get("uid")
        ProjectKey= kwargs.get("project_key")#项目唯一关键字，用于判断接收数据所属
        ProjectName= kwargs.get("project_name")#项目名称
        EndTime= kwargs.get("end_time")#项目结束时间，结束后不再接受任何数据
        MailMessage= kwargs.get("mail_message")#正文内容，需要用base64加密
        Attachment= kwargs.get("attachment")#附件文件，需要传入json格式，使用的是本地名称
        Image = kwargs.get("image")  # 图片文件，使用列表形式窜入
        MailTitle= kwargs.get("mail_title")#邮件头
        Sender= kwargs.get("sender")#发送人名称
        GoalMailbox = kwargs.get("goal_mailbox") # 目标邮箱列表
        ForgedAddress = kwargs.get("forged_address")  # 伪造的发件人地址
        Interval = kwargs.get("interval")  # 邮件发送间隔
        try:
            self.cur.execute("""UPDATE EmailProject SET end_time=?,project_name=?,mail_message=?,attachment=?,image=?,mail_title=?,sender=?,goal_mailbox=?,forged_address=?,interval=? WHERE uid= ? and project_key=?""",(str(EndTime),str(ProjectName),str(MailMessage),str(Attachment),str(Image) ,MailTitle,Sender,str(GoalMailbox),ForgedAddress ,Interval,Uid ,ProjectKey,))
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
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_Updata(def)", e)
            return False
    def ProjectStatus(self, **kwargs):#用来验证项目状态
        try:
            Uid = kwargs.get("uid")
            ProjectKey = kwargs.get("project_key")  # 项目唯一关键字，用于判断接收数据所属
            self.cur.execute("select project_status  from EmailProject WHERE uid=? and project_key=?", (Uid,ProjectKey,))
            for i in self.cur.fetchall():
                if i[0]=="1":
                    self.con.close()
                    return True
                elif i[0]=="0":
                    self.con.close()
                    return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_ProjectStatus(def)", e)
            return None

    def ModifyProjectStatus(self, **kwargs):#修改项目的状态
        Uid = kwargs.get("uid")
        ProjectKey= kwargs.get("project_key")#项目唯一关键字，用于判断接收数据所属
        ProjectStatus= kwargs.get("project_status")#项目状态，0表示未启动，1表示启动，启动中无法修改项目
        try:
            self.cur.execute("""UPDATE EmailProject SET project_status=? WHERE uid= ? and project_key=?""",(ProjectStatus,Uid ,ProjectKey,))
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
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_ModifyProjectStatus(def)", e)
            return False
    def CompilationStatus(self, **kwargs):#用来验证项目是否完成
        try:
            Uid = kwargs.get("uid")
            ProjectKey = kwargs.get("project_key")  # 项目唯一关键字，用于判断接收数据所属
            self.cur.execute("select compilation_status  from EmailProject WHERE uid=? and project_key=?", (Uid,ProjectKey,))
            for i in self.cur.fetchall():
                if i[0]=="1":
                    self.con.close()
                    return True
                elif i[0]=="0":
                    self.con.close()
                    return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_CompilationStatus(def)", e)
            return None
    def ModifyCompilationStatus(self, **kwargs):#修改项目是否完成
        Uid = kwargs.get("uid")
        ProjectKey= kwargs.get("project_key")#项目唯一关键字，用于判断接收数据所属
        CompilationStatus= kwargs.get("compilation_status")# 状态0表示未完成，1表示完成，如果值为1那么久不再能够更新项目内容
        try:
            self.cur.execute("""UPDATE EmailProject SET compilation_status=? WHERE uid= ? and project_key=?""",(CompilationStatus,Uid ,ProjectKey,))
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
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_ModifyCompilationStatus(def)", e)
            return False
    def ProjectCompletion(self, **kwargs):#通过redis值改把任务改为完工
        RedisId= kwargs.get("redis_id")#项目唯一关键字，用于判断接收数据所属
        try:
            self.cur.execute("""UPDATE EmailProject SET compilation_status=? WHERE redis_id=?""",("1",RedisId,))
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
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_ProjectCompletion(def)", e)
            return False
    def UpdataRedis(self,**kwargs)->bool:#更新redis id值
        Uid = kwargs.get("uid")
        ProjectKey= kwargs.get("project_key")#项目唯一关键字，用于判断接收数据所属
        RedisId= kwargs.get("redis_id")

        try:
            self.cur.execute("""UPDATE EmailProject SET redis_id=? WHERE uid= ? and project_key=?""",(RedisId,Uid ,ProjectKey,))
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
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_UpdataRedis(def)", e)
            return False
    def Summary(self, **kwargs):#邮件项目摘要
        try:
            Uid = kwargs.get("uid")
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select end_time,project_key,project_status,interval,compilation_status,creation_time,project_name  from EmailProject WHERE uid=? limit ? offset ?", (Uid,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["end_time"] = i[0]
                JsonValues["project_key"] = i[1]
                JsonValues["project_status"] = i[2]
                JsonValues["interval"] = i[3]
                JsonValues["compilation_status"] = i[4]
                JsonValues["creation_time"] = i[5]
                JsonValues["project_name"] = i[6]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_Summary(def)", e)
            return None
    def Query(self, **kwargs):#详情查询
        try:
            Uid = kwargs.get("uid")
            ProjectKey = kwargs.get("project_key")  # 项目唯一关键字，用于判断接收数据所属
            self.cur.execute("select * from EmailProject WHERE uid=? and project_key=?", (Uid,ProjectKey,))#查询用户相关信息
            for i in self.cur.fetchall():
                return i
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_Query(def)", e)
            return None
    def MonitorQuery(self, **kwargs):#用于查询监控数据
        try:
            ProjectKey = kwargs.get("project_key")  # 项目唯一关键字，用于判断接收数据所属
            self.cur.execute("select end_time from EmailProject WHERE project_key=?", (ProjectKey,))#查询用户相关信息
            for i in self.cur.fetchall():
                return i[0]
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_Query(def)", e)
            return None
    def Statistics(self,**kwargs):  # 统计项目数量
        Uid = kwargs.get("uid")
        try:
            self.cur.execute("SELECT COUNT(1)  FROM EmailProject  WHERE uid=?", (Uid,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailProject(class)_Statistics(def)", e)
            return None


class EmailDetails:  # 邮件详情，发送状态
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE EmailDetails\
                                (email_details INTEGER PRIMARY KEY,\
                                email TEXT NOT NULL,\
                                email_md5 TEXT NOT NULL,\
                                status TEXT NOT NULL,\
                                project_key TEXT NOT NULL,\
                                department  TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailDetails(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Email = kwargs.get("email") #目标
        Department=kwargs.get("department") #部门
        MD5= kwargs.get("email_md5")#目标的md5值
        Status= kwargs.get("status")#邮件是否发送成功1是成功，0是失败
        ProjectKey = kwargs.get("project_key")  # 项目key
        try:
            self.cur.execute("INSERT INTO EmailDetails(email,email_md5,status,project_key,department,creation_time)\
                VALUES (?,?,?,?,?,?)", (Email, MD5, Status, ProjectKey,Department,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailDetails(class)_Write(def)", e)
            return False
    def EmailAndDepartment(self, **kwargs) -> bool or None:  # 通过MD5和项目key查询email和部门
        MD5= kwargs.get("email_md5")#目标的md5值
        ProjectKey = kwargs.get("project_key")  # 项目key
        try:
            self.cur.execute("select email,department from EmailDetails WHERE email_md5=? and project_key=?", (MD5,ProjectKey,))#查询用户相关信息
            for i in self.cur.fetchall():
                return i

        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailDetails(class)_EmailQuery(def)", e)
            return None
    def Query(self, **kwargs):#查询邮件发送状态，全量数据
        try:
            ProjectKey = kwargs.get("project_key")  # 项目唯一关键字，用于判断接收数据所属
            FullData = kwargs.get("full_data")  # 是否是全量数据
            Status = kwargs.get("status")  # 如果不是全量数据进行筛选状态
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            if FullData:
                self.cur.execute("select email,email_md5,status,department,creation_time  from EmailDetails WHERE project_key=? limit ? offset ?", (ProjectKey,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息
                result_list = []
                for i in self.cur.fetchall():
                    JsonValues = {}
                    JsonValues["email"] = i[0]
                    JsonValues["email_md5"] = i[1]
                    JsonValues["status"] = i[2]
                    JsonValues["department"] = i[3]
                    JsonValues["creation_time"] = i[4]
                    result_list.append(JsonValues)
                self.con.close()
                return result_list
            else:
                self.cur.execute("select email,email_md5,status,department,creation_time  from EmailDetails WHERE project_key=? and status=? limit ? offset ?", (ProjectKey,Status,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息
                result_list = []
                for i in self.cur.fetchall():
                    JsonValues = {}
                    JsonValues["email"] = i[0]
                    JsonValues["email_md5"] = i[1]
                    JsonValues["status"] = i[2]
                    JsonValues["department"] = i[3]
                    JsonValues["creation_time"] = i[4]
                    result_list.append(JsonValues)
                self.con.close()
                return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailDetails(class)_Query(def)", e)
            return None
    def Statistics(self,**kwargs):  # 统计项目数量
        ProjectKey = kwargs.get("project_key")  # 项目唯一关键字，用于判断接收数据所属
        FullData = kwargs.get("full_data")  # 是否是全量数据
        Status = kwargs.get("status")  # 如果不是全量数据进行筛选状态
        try:
            if FullData:
                self.cur.execute("select count(*) from EmailDetails WHERE project_key=?", (ProjectKey,))
                Result = self.cur.fetchall()[0][0]  # 获取数据个数
                self.con.close()
                return Result
            else:
                self.cur.execute("SELECT COUNT(1)  FROM EmailDetails  WHERE project_key=? and status=? ", (ProjectKey,Status,))
                Result = self.cur.fetchall()[0][0]  # 获取数据个数
                self.con.close()
                return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailDetails(class)_Statistics(def)", e)
            return None

    def Verification(self, **kwargs):  # 验证是否有数据
        try:
            Email = kwargs.get("email")  # 目标
            Department = kwargs.get("department")  # 部门
            ProjectKey = kwargs.get("project_key")  # 项目key
            self.cur.execute("SELECT COUNT(1)  FROM EmailDetails WHERE project_key=? and email=? and department=?",(ProjectKey, Email,Department))  # 查询相关信息
            Result=self.cur.fetchall()[0][0]#获取数据个数
            if Result==0:
                self.con.close()
                return False
            else:
                self.con.close()
                return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailDetails(class)_Verification(def)", e)
            return None

    def Update(self,**kwargs)->bool:#利用主键ID来判断后更新数据
        CreationTime = str(int(time.time()))  # 创建时间
        Email = kwargs.get("email") #目标
        Department=kwargs.get("department") #部门
        Status= kwargs.get("status")#邮件是否发送成功1是成功，0是失败
        ProjectKey = kwargs.get("project_key")  # 项目key
        try:
            self.cur.execute("""UPDATE EmailDetails SET status=?,creation_time=? WHERE department= ? and project_key=? and email=?""",(Status,CreationTime,Department,ProjectKey,Email,))
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
            ErrorLog().Write("Web_DatabaseHub_EmailDetails(class)_Updata(def)", e)
            return False

    def ResendQuery(self, **kwargs):#重发邮件查询
        try:
            ProjectKey = kwargs.get("project_key")  # 项目唯一关键字，用于判断接收数据所属
            Status = kwargs.get("status")  # 如果不是全量数据进行筛选状态
            self.cur.execute("select email,department from EmailDetails WHERE project_key=? and status=?", (ProjectKey,Status,))#查询用户相关信息
            result_list = {}

            for i in self.cur.fetchall():
                Department = str(i[1])  # 部门
                Value = i[0]  # 目标
                # print(type(Value))
                if type(Value) == bytes:
                    Value = Value.decode("utf-8")   # 如果是bytes类型转换为str
                if Department in result_list.keys():  # 判断部门是否在键中
                    if Value not in result_list[Department]:#判断值是否在部门中
                        result_list[Department].append(Value)
                else:
                    result_list[Department] = [Value]
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailDetails(class)_Query(def)", e)
            return None
class MailAttachment:  # 所有钓鱼的上传文件都在这里
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE MailAttachment\
                                (mail_attachment_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                file_name TEXT NOT NULL,\
                                file_size TEXT NOT NULL,\
                                document_real_name TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MailAttachment(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")
        FileName= kwargs.get("file_name")#文件名
        FileSize = kwargs.get("file_size")  # 文件大小
        DocumentRealName= kwargs.get("document_real_name")#本地保存的文件名
        try:
            self.cur.execute("INSERT INTO MailAttachment(uid,file_name,file_size,document_real_name,creation_time)\
                VALUES (?,?,?,?,?)", (Uid, FileName, FileSize,DocumentRealName,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MailAttachment(class)_Write(def)", e)
            return False

    def Query(self, **kwargs):
        try:
            Uid = kwargs.get("uid")
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select file_name,file_size,document_real_name,creation_time  from MailAttachment WHERE uid=? limit ? offset ?", (Uid,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["file_name"] = i[0]
                JsonValues["file_size"] = i[1]
                JsonValues["document_real_name"] = i[2]
                JsonValues["creation_time"] = i[3]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MailAttachment(class)_Query(def)", e)
            return None
    def Quantity(self,**kwargs):  # 查看数量有哪些
        Uid = kwargs.get("uid")
        try:
            self.cur.execute("SELECT COUNT(1)  FROM MailAttachment  WHERE uid=?", (Uid,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MailAttachment(class)_Quantity(def)", e)
            return None

    def Verify(self,**kwargs):  # 验证图片是否为真的
        Uid = kwargs.get("uid")
        DocumentRealName = kwargs.get("document_real_name")  # 真实的文件名

        try:
            self.cur.execute("select *  from MailAttachment WHERE uid=? and document_real_name=?", (Uid,DocumentRealName,))#查询用户相关信息
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MailAttachment(class)_Verify(def)", e)
            return False
    def Verification(self,**kwargs):  # 验证文件名是否冲突
        Uid = kwargs.get("uid")
        DocumentRealName = kwargs.get("document_real_name")  # 真实的文件名

        try:
            self.cur.execute("select *  from MailAttachment WHERE uid=? and document_real_name=?", (Uid,DocumentRealName,))#查询用户相关信息
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_MailAttachment(class)_Verify(def)", e)
            return False


class EmailReceiveData:  # 邮件数据接收
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE EmailReceiveData\
                                (email_receive_data_id INTEGER PRIMARY KEY,\
                                email TEXT NOT NULL,\
                                department TEXT NOT NULL,\
                                project_key TEXT NOT NULL,\
                                full_url TEXT NOT NULL,\
                                request_method TEXT NOT NULL,\
                                target TEXT NOT NULL,\
                                data_pack_info TEXT NOT NULL,\
                                incidental_data TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailReceiveData(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Email= kwargs.get("email")#邮件
        Department = kwargs.get("department")  # 部门
        ProjectKey= kwargs.get("project_key")#项目key
        Target = kwargs.get("target")  # 目标，用来定位人
        FullUrl= kwargs.get("full_url")  # 完整的路径
        RequestMethod = kwargs.get("request_method")  # 请求模式
        DataPackInfo= kwargs.get("data_pack_info")# 完整数据内容
        IncidentalData = kwargs.get("incidental_data")  # 除了target以外附带的数据
        try:
            self.cur.execute("INSERT INTO EmailReceiveData(email,department,project_key,full_url,request_method,target,data_pack_info,incidental_data,creation_time)\
                VALUES (?,?,?,?,?,?,?,?,?)", (Email,Department,ProjectKey,FullUrl,RequestMethod, Target, DataPackInfo,IncidentalData,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailReceiveData(class)_Write(def)", e)
            return False
    def Query(self, **kwargs):#全量数据查询
        try:
            ProjectKey = kwargs.get("project_key")  # 项目key
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select * from EmailReceiveData WHERE project_key=? limit ? offset ?", (ProjectKey,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["email"] = i[1]
                JsonValues["department"] = i[2]
                JsonValues["full_url"] = i[4]
                JsonValues["request_method"] = i[5]
                JsonValues["data_pack_info"] = i[7]
                JsonValues["incidental_data"] = i[8]
                JsonValues["creation_time"] = i[9]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailReceiveData(class)_Query(def)", e)
            return None
    def Statistics(self,**kwargs):  # 全量数据统计
        ProjectKey= kwargs.get("project_key")#项目key
        try:
            self.cur.execute("SELECT COUNT(1)  FROM EmailReceiveData  WHERE project_key=?", (ProjectKey,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailReceiveData(class)_Statistics(def)", e)
            return None

    def Search(self,**kwargs):  #模糊查询
        try:
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页
            ProjectKey = kwargs.get("project_key")
            StartTime = kwargs.get("start_time")#开始时间
            EndTime = kwargs.get("end_time")#结束时间
            Email = "%"+kwargs.get("email")+"%"
            Department = "%"+kwargs.get("department")+"%"

            self.cur.execute("select * from EmailReceiveData WHERE project_key=? and creation_time<=? and creation_time>=? and email LIKE ? and department LIKE ? limit ? offset ?", (ProjectKey,EndTime,StartTime,Email,Department,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["email"] = i[1]
                JsonValues["department"] = i[2]
                JsonValues["full_url"] = i[4]
                JsonValues["request_method"] = i[5]
                JsonValues["data_pack_info"] = i[7]
                JsonValues["incidental_data"] = i[8]
                JsonValues["creation_time"] = i[9]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailReceiveData(class)_Search(def)", e)
            return None

    def SearchQuantity(self, **kwargs):  # 模糊查询统计数量
        try:
            ProjectKey = kwargs.get("project_key")
            StartTime = kwargs.get("start_time")#开始时间
            EndTime = kwargs.get("end_time")#结束时间
            Email = "%" + kwargs.get("email") + "%"
            Department = "%" + kwargs.get("department") + "%"
            self.cur.execute(
                "select COUNT(1) from EmailReceiveData WHERE project_key=? and creation_time<=? and creation_time>=? and email LIKE ? and department LIKE ?",
                (ProjectKey, EndTime,StartTime,Email, Department,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailReceiveData(class)_SearchQuantity(def)", e)
            return None

    def NotNull(self, **kwargs):  # 查询不为空的字段
        try:
            ProjectKey = kwargs.get("project_key")
            self.cur.execute(
                "select email,department from EmailReceiveData where trim(incidental_data) !='' AND project_key=?",
                (ProjectKey,))
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["email"] = i[0]
                JsonValues["department"] = i[1]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailReceiveData(class)_NotNull(def)", e)
            return None
    def IsNull(self, **kwargs):  # 查询为空的字段
        try:
            ProjectKey = kwargs.get("project_key")
            self.cur.execute(
                "select email,department from EmailReceiveData where trim(incidental_data) ='' AND project_key=?",
                (ProjectKey,))
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["email"] = i[0]
                JsonValues["department"] = i[1]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailReceiveData(class)_IsNull(def)", e)
            return None

class EmailGraph:  # 邮件数据接收
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE EmailGraph\
                                (email_graph_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                project_key TEXT NOT NULL,\
                                graph_data TEXT NOT NULL,\
                                status TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailGraph(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid= kwargs.get("uid")#用户ID
        ProjectKey= kwargs.get("project_key")#项目key
        GraphData = kwargs.get("graph_data")  # 数据内容
        Status="0"#0表示未完成 1表示完成

        try:
            self.cur.execute("INSERT INTO EmailGraph(uid,project_key,graph_data,status,creation_time)\
                VALUES (?,?,?,?,?)", (Uid,ProjectKey,GraphData,Status,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailGraph(class)_Write(def)", e)
            return False
    def Query(self, **kwargs):#全量数据查询
        try:
            Uid = kwargs.get("uid")  # 用户ID
            ProjectKey = kwargs.get("project_key")  #项目key
            self.cur.execute("select graph_data from EmailGraph WHERE project_key=? and uid=?", (ProjectKey,Uid,))#查询用户相关信息
            for i in self.cur.fetchall():
                return i[0]
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailGraph(class)_Query(def)", e)
            return None
    def Updata(self, **kwargs):#更新数据
        try:
            Uid = kwargs.get("uid")  # 用户ID
            ProjectKey = kwargs.get("project_key")  #项目key
            GraphData = kwargs.get("graph_data")  # 数据内容
            self.cur.execute("""UPDATE EmailGraph SET graph_data=?,status=? WHERE uid= ? and project_key=?""",
                                 (GraphData,"1",Uid, ProjectKey,))
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
            ErrorLog().Write("Web_DatabaseHub_EmailGraph(class)_Updata(def)", e)
            return None
    def Verification(self, **kwargs):#查询数据是否存在
        try:
            Uid = kwargs.get("uid")  # 用户ID
            ProjectKey = kwargs.get("project_key")  #项目key
            self.cur.execute("select COUNT(1) from EmailGraph WHERE project_key=? and uid=?", (ProjectKey,Uid,))#查询用户相关信息
            Result=self.cur.fetchall()[0][0]#获取数据个数
            if int(Result)==0:
                return False
            else:
                return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailGraph(class)_Verification(def)", e)
            return None

class EmailInfo:  # 邮件管理详情
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE EmailInfo\
                                (email_info_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                project_key TEXT NOT NULL,\
                                another_name TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailInfo(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid = kwargs.get("uid")  # 用户值
        ProjectKey = kwargs.get("project_key")  # 邮件key
        AnotherName= kwargs.get("another_name")#项目别名

        try:

            self.cur.execute("INSERT INTO EmailInfo(uid,project_key,another_name,creation_time)\
                VALUES (?,?,?,?)", (Uid,ProjectKey,AnotherName,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailInfo(class)_Write(def)", e)
            return False
    def Query(self, **kwargs):#项目查询
        try:
            Uid = kwargs.get("uid")  # 用户ID
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select project_key,another_name,creation_time from EmailInfo WHERE uid=? limit ? offset ?", (Uid,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["project_key"] = i[0]
                JsonValues["another_name"] = i[1]
                JsonValues["creation_time"] = i[2]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailInfo(class)_Query(def)", e)
            return None
    def Verification(self,**kwargs):  #验证所有者
        try:
            ProjectKey = kwargs.get("project_key")  # 邮件key
            Uid = kwargs.get("uid")  # 用户ID
            self.cur.execute("SELECT COUNT(1)  FROM EmailInfo WHERE uid=? and project_key= ?", (Uid,ProjectKey,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailInfo(class)_Verification(def)", e)
            return None
    def Statistics(self,**kwargs):  # 项目统计
        try:
            Uid = kwargs.get("uid")  # 用户ID
            self.cur.execute("SELECT COUNT(1)  FROM EmailInfo WHERE uid=?", (Uid,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailInfo(class)_Statistics(def)", e)
            return None

class EmailData:  # 邮件管理中的邮箱数据
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE EmailData\
                                (email_info_id INTEGER PRIMARY KEY,\
                                project_key TEXT NOT NULL,\
                                email TEXT NOT NULL,\
                                department TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailData(class)_init(def)", e)

    def Write(self, DataSet) -> bool or None:  # 写入相关信息
        try:
            self.cur.executemany("INSERT INTO EmailData(project_key,email,department)\
                VALUES (?,?,?)", DataSet)
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailData(class)_Write(def)", e)
            return False
    def Query(self, **kwargs):#项目查询
        try:
            ProjectKey = kwargs.get("project_key")  # 用户ID
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select email,department from EmailData WHERE project_key=? limit ? offset ?", (ProjectKey,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["email"] = i[0]
                JsonValues["department"] = i[1]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailData(class)_Query(def)", e)
            return None
    def Statistics(self,**kwargs):  # 项目统计
        try:
            ProjectKey = kwargs.get("project_key")  # 用户ID
            self.cur.execute("SELECT COUNT(1)  FROM EmailData WHERE project_key=?", (ProjectKey,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailData(class)_Statistics(def)", e)
            return None
    def QueryAll(self, **kwargs):#拉取全量数据
        try:
            ProjectKey = kwargs.get("project_key")  # 用户ID

            self.cur.execute("select email,department from EmailData WHERE project_key=?", (ProjectKey,))#查询用户相关信息
            Excel = {}  # 创建一个空字典,存储表格数据
            for i in self.cur.fetchall():
                Department=i[1]
                Value=i[0]
                if Department in Excel.keys():  # 判断部门是否在键中
                    Excel[Department].append(Value)
                else:
                    Excel[Department] = [Value]
            self.con.close()
            return Excel
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_EmailData(class)_QueryAll(def)", e)
            return None
class GithubCve:  # GitHub的CVE监控写入表
    def __init__(self,**kwargs):
        try:
            self.cve_id = kwargs.get("id")  # 唯一的ID
            self.cve_name = kwargs.get("name")   # 名字
            self.cve_html_url = kwargs.get("html_url")    # 链接
            self.cve_created_at = kwargs.get("created_at")  # 创建时间
            self.cve_updated_at = kwargs.get("updated_at")  # 更新时间
            self.cve_pushed_at = kwargs.get("pushed_at")  # push时间
            self.cve_forks_count = kwargs.get("forks_count")  # fork人数
            self.cve_watchers_count =kwargs.get("watchers_count")  # star人数
            self.cve_write_time = str(int(time.time()))  # 写入时间
            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(GetPath().DatabaseFile())
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表

            # 如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
            self.cur.execute("CREATE TABLE GithubMonitor\
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
            pass

    def Write(self):
        try:
            self.cur.execute("""INSERT INTO GithubMonitor (github_id,name,html_url,created_at,updated_at,pushed_at,forks_count,watchers_count,write_time,update_write_time) \
    VALUES (?,?,?,?,?,?,?,?,?,?)""", (
            self.cve_id, self.cve_name, self.cve_html_url, self.cve_created_at, self.cve_updated_at, self.cve_pushed_at,
            self.cve_forks_count, self.cve_watchers_count, self.cve_write_time, self.cve_write_time,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
                ErrorLog().Write("Web_DatabaseHub_GithubCve(class)_Write(def)", e)

    def Update(self):
        UpdateTime=str(int(time.time()))
        try:
            self.cur.execute(
                """UPDATE GithubMonitor SET forks_count = ?,updated_at=?,pushed_at=?,watchers_count=?,update_write_time=?  WHERE github_id = ?""",
                (self.cve_forks_count, self.cve_updated_at, self.cve_pushed_at, self.cve_watchers_count,
                 UpdateTime, self.cve_id,))
            # 提交
            self.con.commit()
            self.con.close()
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_GithubCve(class)_Update(def)", e)

    def Judgment(self) -> bool:#用于判断是否更新
        try:
            self.cur.execute(
                """SELECT * FROM GithubMonitor WHERE github_id=?""", (self.cve_id,))
            values = self.cur.fetchall()
            cve_query_results = True
            if len(values) == 0:
                cve_query_results = False
            else:
                cve_query_results = True
            # 提交
            self.con.commit()
            self.con.close()
            return cve_query_results
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_GithubCve(class)_Judgment(def)", e)
    def StatisticalData(self,**kwargs):  # 整体个数统计
        try:
            StatementProcessing = ""
            TupleContainer = ()  # 存放处理后的数据
            for x, i in enumerate(kwargs):
                if i == "number_of_pages":
                    continue
                if x == len(kwargs) - 1:  # 判断是不是最后一个参数
                    StatementProcessing += i + " like ? "
                else:
                    StatementProcessing += i + " like ? and "
                TupleContainer += (str(kwargs.get(i)),)
            if StatementProcessing!="":
                StatementProcessing=" WHERE "+StatementProcessing
            self.cur.execute("SELECT COUNT(1)  FROM GithubMonitor"+StatementProcessing,TupleContainer)
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_GithubCve(class)_StatisticalData(def)", e)
            return None

    def Query(self,**kwargs):#查询函数，可以进行联合查询
        NumberOfSinglePages = 100  # 单页数量
        NumberOfPages = kwargs.get(
            "number_of_pages") - 1  # 查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
        StatementProcessing = ""
        TupleContainer = ()#存放处理后的数据
        for x,i in enumerate(kwargs):
            if i=="number_of_pages":
                continue
            if x==len(kwargs)-1:#判断是不是最后一个参数
                StatementProcessing += i + " like ? "
            else:
                StatementProcessing += i + " like ? and "
            TupleContainer += (str(kwargs.get(i)),)
        try:
            ProcessedData=[]
            if StatementProcessing!="":
                StatementProcessing=" WHERE "+StatementProcessing
            self.cur.execute(
                "select *  from GithubMonitor "+StatementProcessing+" ORDER BY created_at DESC  limit ? offset ?",TupleContainer+(NumberOfSinglePages,NumberOfSinglePages*NumberOfPages,))  # 查询用户相关信息

            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["github_id"]= i[1]
                JsonValues["name"]= i[2]
                JsonValues["html_url"]= i[3]
                JsonValues["created_at"]= i[4]
                JsonValues["updated_at"]= i[5]
                JsonValues["pushed_at"]= i[6]
                JsonValues["forks_count"]= i[7]
                JsonValues["watchers_count"]= i[8]
                ProcessedData.append(JsonValues)

            return ProcessedData
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_GithubCve(class)_Query(def)", e)

class FileAcquisitionData:  # 文件接收数据库
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE FileAcquisition\
                                (file_acquisition_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                file_full_path TEXT NOT NULL,\
                                old_file_name TEXT NOT NULL,\
                                file_size TEXT NOT NULL,\
                                new_file_name TEXT NOT NULL,\
                                target_machine TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_FishingData(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid= kwargs.get("uid")
        FileFullPath= kwargs.get("file_full_path")  # 该文件在目标机器完整的路径
        OldFileName = kwargs.get("old_file_name")  # 该文件在目标机器的文件名
        FileSize= kwargs.get("file_size")   # 文件大小
        NewFileName = kwargs.get("new_file_name")  # 重命名后存储在本地的文件名
        TargetMachine = kwargs.get("target_machine")  # 目标值，来确认机器是那一台

        try:
            self.cur.execute("INSERT INTO FileAcquisition(uid,file_full_path,old_file_name,file_size,new_file_name,target_machine,creation_time)\
                VALUES (?,?,?,?,?,?,?)", (Uid,FileFullPath, OldFileName, FileSize,NewFileName,TargetMachine,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_FileAcquisition(class)_Write(def)", e)
            return False
    def DocumentAuthentication(self,Data) -> bool or None:  # 文件鉴权
        ReturnList=[]
        try:
            for i in Data:
                self.cur.execute("select * from FileAcquisition WHERE uid=? and new_file_name=?", i)#查询用户相关信息
                ReturnData=self.cur.fetchone()
                if ReturnData is None:#判断是否有空数据
                    return False
                else:
                    tmp=(ReturnData[3],ReturnData[5])
                    ReturnList.append(tmp)
            self.con.close()
            return ReturnList
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_FileAcquisition(class)_Write(def)", e)
            return False
    def Query(self, **kwargs):
        try:
            Uid = kwargs.get("uid")
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select file_full_path,old_file_name,file_size,new_file_name,target_machine,creation_time  from FileAcquisition WHERE uid=? limit ? offset ?", (Uid,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["file_full_path"] = i[0]
                JsonValues["old_file_name"] = i[1]
                JsonValues["file_size"] = i[2]
                JsonValues["new_file_name"] = i[3]
                JsonValues["target_machine"] = i[4]
                JsonValues["creation_time"] = i[5]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_FileAcquisition(class)_Query(def)", e)
            return None
    def Quantity(self,**kwargs):  # 查看数量有哪些
        Uid = kwargs.get("uid")
        try:
            self.cur.execute("SELECT COUNT(1)  FROM FileAcquisition  WHERE uid=?", (Uid,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_FileAcquisition(class)_Quantity(def)", e)
            return None

class FileAcquisitionPack:  # 打包接收函数
    def __init__(self):
        self.con = sqlite3.connect(GetPath().DatabaseFile())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE FileAcquisitionPack\
                                (file_acquisition_pack_id INTEGER PRIMARY KEY,\
                                uid TEXT NOT NULL,\
                                file_name TEXT NOT NULL,\
                                state TEXT NOT NULL,\
                                redis_id TEXT NOT NULL,\
                                creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_FileAcquisitionPack(class)_init(def)", e)

    def Write(self, **kwargs) -> bool or None:  # 写入相关信息
        CreationTime = str(int(time.time()))  # 创建时间
        Uid= kwargs.get("uid")
        FileName = kwargs.get("file_name")  # 存储在本地的文件名
        State = kwargs.get("state")  # 获取文件状态,1表示成功，0表示正在执行，-1表示失败
        RedisId = kwargs.get("redis_id")  # 获取redis值


        try:
            self.cur.execute("INSERT INTO FileAcquisitionPack(uid,file_name,state,redis_id,creation_time)\
                VALUES (?,?,?,?,?)", (Uid,FileName,State,RedisId,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_FileAcquisitionPack(class)_Write(def)", e)
            return False
    def UpdateStatus(self,**kwargs)->bool:#利用主键ID来判断后更新数据
        RedisId = kwargs.get("redis_id")
        FileName = kwargs.get("file_name")
        State = kwargs.get("state")
        try:
            self.cur.execute("""UPDATE FileAcquisitionPack SET state = ?,file_name=? WHERE redis_id= ?""",(State,FileName, RedisId,))
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
            ErrorLog().Write("Web_DatabaseHub_FileAcquisitionPack(class)_UpdateStatus(def)", e)
            return False
    def DownloadAuthentication(self,**kwargs)->bool:#下载鉴权
        Uid = kwargs.get("uid")
        FileName = kwargs.get("file_name")
        try:
            self.cur.execute("select *  from FileAcquisitionPack WHERE uid=? and file_name=?", (Uid,FileName,))

            if self.cur.fetchone() is None:  # 判断是否有空数据
                self.con.close()
                return False
            else:
                self.con.close()
                return True
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_FileAcquisitionPack(class)_DownloadAuthentication(def)", e)
            return False
    def Query(self, **kwargs):
        try:
            Uid = kwargs.get("uid")
            NumberOfSinglePages=100#单页数量
            NumberOfPages=kwargs.get("number_of_pages")-1#查询第几页，需要对页码进行-1操作，比如第1页的话查询语句是limit 100 offset 0，而不是limit 100 offset 100，所以还需要判断传入的数据大于0
            self.cur.execute("select file_name,state,creation_time  from FileAcquisitionPack WHERE uid=? limit ? offset ?", (Uid,NumberOfSinglePages,NumberOfPages*NumberOfSinglePages,))#查询用户相关信息
            result_list = []
            for i in self.cur.fetchall():
                JsonValues = {}
                JsonValues["file_name"] = i[0]
                JsonValues["state"] = i[1]
                JsonValues["creation_time"] = i[2]
                result_list.append(JsonValues)
            self.con.close()
            return result_list
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_FileAcquisitionPack(class)_Query(def)", e)
            return None
    def Quantity(self,**kwargs):  # 查看数量有哪些
        Uid = kwargs.get("uid")
        try:
            self.cur.execute("SELECT COUNT(1)  FROM FileAcquisitionPack  WHERE uid=?", (Uid,))
            Result=self.cur.fetchall()[0][0]#获取数据个数
            self.con.close()
            return Result
        except Exception as e:
            ErrorLog().Write("Web_DatabaseHub_FileAcquisitionPack(class)_Quantity(def)", e)
            return None
