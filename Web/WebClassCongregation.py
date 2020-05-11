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
            ErrorLog().Write("WebClass_UserInfo_init",e)
    def WhetherUsersConflict(self,Name,Email):#查询用户是否存在，True表示有数据，False表示各种问题
        try:
            self.cur.execute("select * from UserInfo where name =? and email = ?",(Name,Email,))
            if self.cur.fetchall():#判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("WebClass_UserInfo_WhetherUsersConflict", e)
            return False
    def WhetherTheKeyConflicts(self,Key):#查询用户kEY是否存在，True表示有数据，False表示各种问题
        try:
            self.cur.execute("select * from UserInfo where key =?", (Key,))
            if self.cur.fetchall():  # 判断是否有数据
                self.con.close()
                return True
            else:
                return False
        except Exception as e:
            ErrorLog().Write("WebClass_UserInfo_WhetherTheKeyConflicts", e)
            return False
    def Write(self,**kwargs:str)->bool:#写入新用户，True表示成功，False表示各种问题
        CreationTime = str(int(time.time())) # 创建时间
        Uid=randoms().result(100)
        Name=kwargs.get("name")
        ShowName=kwargs.get("show_name")
        Passwd=kwargs.get("passwd")
        Email=kwargs.get("email")
        ImgPath=kwargs.get("img_path")
        Key=randoms().result(40)
        Token=kwargs.get("token")
        UserInformationJudgment=self.WhetherUsersConflict(Name,Email)#判断用户是否存在
        while True:#判断Key否存在
            if not self.WhetherTheKeyConflicts(Key):#如果未找到就跳出循环进行下去
                break
            Key = randoms().result(40)

        if UserInformationJudgment:#如果找到返回False
            return False
        elif not UserInformationJudgment:#如果没找到写入数据
            try:
                self.cur.execute("INSERT INTO UserInfo(uid,key,token,name,show_name,passwd,email,img_path,key_update_time,passwd_update_time,email_update_time,show_name_update_time,img_path_update_time,token_update_time,creation_time)\
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Uid,Key,Token,Name,ShowName, Passwd,Email,ImgPath,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,CreationTime,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("WebClass_UserInfo_Write", e)
                return False
    def UpdatePasswd(self,**kwargs:str)->bool:#更新用户密码，True表示成功，False表示各种问题
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
                return False
        else:return False
    def UpdateShowName(self,**kwargs:str)->bool:#更新用户显示名字，True表示成功，False表示各种问题
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
                ErrorLog().Write("WebClass_UserInfo_UpdateShowName", e)
                return False
        else:return False
    def UpdateEmail(self,**kwargs:str)->bool:#更新用户邮箱，True表示成功，False表示各种问题
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
                ErrorLog().Write("WebClass_UserInfo_UpdateEmail", e)
                return False
        else:return False
    def UpdateImgPath(self,**kwargs:str)->bool:#更新用户头像路径，True表示成功，False表示各种问题
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
                return False
        else:return False
    def UpdateKey(self,**kwargs:str)->bool:#更新用户Key，True表示成功，False表示各种问题
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
                ErrorLog().Write("WebClass_UserInfo_UpdateKey", e)
                return False
        else:return False
    def UpdateToken(self,**kwargs:str)->bool:#更新用户Token，True表示成功，False表示各种问题
        Name = kwargs.get("name")
        Token= kwargs.get("token")
        UpdateTime = str(int(time.time()))  # 修改时间
        if Name!=None and Token!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET token = ? , token_update_time = ?WHERE name= ?""", (Token,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("WebClass_UserInfo_UpdateToken", e)
                return False
        else:return False
    def QueryTokenCreationTime(self,**kwargs:str)->bool:#查询用户Token创建时间，True表示不正常，False表示正常
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
                ErrorLog().Write("WebClass_UserInfo_QueryTokenCreationTime", e)
        else:return True#报错返回True
    def TokenAuthentication(self,**kwargs:str)->bool:#查询用户Token是否存在
        Name = kwargs.get("name")
        Token= kwargs.get("token")

        if Name!=None and Token!=None:
            try:
                self.cur.execute("""UPDATE UserInfo SET token = ? , token_update_time = ?WHERE name= ?""", (Token,UpdateTime,Name,))
                # 提交
                self.con.commit()
                self.con.close()
                return True
            except Exception as e:
                ErrorLog().Write("WebClass_UserInfo_TokenAuthentication", e)
        else:return False


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

class ScanInformation:#ActiveScanList的子表，单独网站详细扫描内容,写入父表中的SID和UID
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
        # 创建表
        try:
            self.cur.execute("CREATE TABLE ScanInformation\
                            (ssid INTEGER PRIMARY KEY,\
                            sid TEXT NOT NULL,\
                            uid TEXT NOT NULL,\
                            url TEXT NOT NULL,\
                            creation_time TEXT NOT NULL)")
        except Exception as e:
            ErrorLog().Write("WebClass_ScanInformation_init", e)
    def Write(self,**kwargs)->bool:#写入相关信息
        CreationTime = str(int(time.time())) # 创建时间
        Url=kwargs.get("url")
        Ssid=kwargs.get("ssid")
        Uid = kwargs.get("uid")
        try:
            self.cur.execute("INSERT INTO ScanInformation(sid,uid,url,creation_time)\
            VALUES (?,?,?,?,?)",(Ssid,Uid,Url,CreationTime,))
            # 提交
            self.con.commit()
            self.con.close()
            return True#获取主键的ID值，也就是sid的值
        except Exception as e:
            ErrorLog().Write("WebClass_ScanInformation_Write", e)
            return False

#验证用户-》读取UID，然后用UID启动扫描，然后在用UID插入各个表中
class MedusaQuery:#ScanInformation的子表，单个漏洞的详细内容，具体写入表在ClassCongregation文件中，改表是个查询数据表
    def __init__(self):
        self.con = sqlite3.connect(GetDatabaseFilePath().result())
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
    def Query(self, **kwargs):
        try:
            Url = kwargs.get("url")
            Ssid = kwargs.get("ssid")
            Uid = kwargs.get("uid")
            self.cur.execute("select * from Medusa where token =?", (str(token),))
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

class PassiveScanInformation:#用户被动扫描相关信息
    pass