from ClassCongregation import Plugins,GetTempFilePath,GetPluginsFilePath
import os

def InitialVerification(TempFilePath):#验证是否初始化
    try:
        File=open(TempFilePath+"InitializationPlugin.lock", 'r+').read()
        if File.find("Super Invincible Cute Neiru Aonuma")!=-1:
            return True
        else:
            return False
    except:
        return False


def Run():
    TempFilePath = GetTempFilePath().Result()  # 获取TMP文件路径
    PluginsFilePath=GetPluginsFilePath().Result()#获取插件文件路径
    PluginsDB = Plugins()  # 初始化连接
    FileNameList=[]#文件名列表
    if not InitialVerification(TempFilePath):#如果不存在初始化
        PluginsDB.Initialization()#初始化清空数据库表
        for Data in os.walk(PluginsFilePath):
            for i in Data[2]:
                FileNameList.append((i,))
                if len(FileNameList) == 500:  # 500写入一次数据库
                    PluginsDB.Write(FileNameList)
                    FileNameList.clear()  # 写入后清空数据列表
        PluginsDB.Write(FileNameList)#函数循环结束后也写入一次数据库，防止不足500的数据没写入
        PluginsDB.con.close()#关闭数据库连接
        open(TempFilePath + "InitializationPlugin.lock", 'w+').write("Super Invincible Cute Neiru Aonuma")  # 初始化后写入初始化锁

Run()




