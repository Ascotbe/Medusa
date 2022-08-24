#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import json
from Web.DatabaseHub import NistData
import urllib3
from ClassCongregation import GetPath,ErrorLog
import datetime
import time
import aiohttp
import aiofiles
import requests
import asyncio
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers={
    "Connection": "close",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "dnt": "1"
}
#https://nvd.nist.gov/vuln/data-feeds
async def NistFirstRunDownload(Year,TempFilePath):#第一次运行下载数据
        try:
            FileName="nvdcve-1.1-" + str(Year) + ".json.zip"#下载文件名
            Url="https://nvd.nist.gov/feeds/json/cve/1.1/"+FileName
            StartingTime=time.time()
            async with aiohttp.ClientSession() as session:
                async with session.get(Url, headers=headers) as DownloadFile:
                    #DownloadFile=requests.get(Url,headers=headers,  verify=False)
                    file=await aiofiles.open(TempFilePath+FileName, 'wb+')
                    await file.write(await DownloadFile.read())
                    print("[ + ] 下载文件：\033[36m" + FileName + "\033[0m 耗时：\033[34m" + str(
                        time.time() - StartingTime) + "S \033[0m")

        except Exception as e:
            print("[ ! ]"+str(Year) + "年数据下载出错 报错信息：" + str(e))
            ErrorLog().Write("Web_CVE_NistMonitoring_NistInitialization_FirstRunDownload(def)", e)


def ReportAnErrorAndRestartTheDownload(Year,TempFilePath):#报错下载，由于数据可能未下载成功重复运行
    try:
        FileName="nvdcve-1.1-" + str(Year) + ".json.zip"#下载文件名
        Url="https://nvd.nist.gov/feeds/json/cve/1.1/"+FileName
        StartingTime=time.time()
        print("[ + ] 正在重新下载文件：\033[36m" + FileName+ "\033[0m")
        DownloadFile=requests.get(Url,headers=headers,  verify=False,timeout=60)
        with open(TempFilePath+FileName, 'wb+') as file:
            file.write(DownloadFile.content)
        print("[ - ] 成功下载文件：\033[36m" + FileName + "\033[0m 耗时：\033[34m" + str(
            time.time() - StartingTime) + "S \033[0m")
        NistFirsRunProcessing(TempFilePath+FileName,FileName[:-4])#调用数据处理函数，传入文件路径和提取文件名
    except Exception as e:
        ReportAnErrorAndRestartTheDownload(Year, TempFilePath)#如果还是报错就再次循环自身
        ErrorLog().Write("Web_CVE_NistMonitoring_NistInitialization_FirstRunDownload(def)", e)



def NistFirsRunProcessing(ZipFilePath,ZipFileData):#第一次运行数据处理
    try:
        StartingTime = time.time()
        Nist=NistData()#初始化连接
        zipFile = zipfile.ZipFile(ZipFilePath, 'r')#获取下载好的数据

        ZipData = zipFile.read(ZipFileData).decode('utf-8')#读取到的byte类型进行转换到字符串类型
        ExtractData=json.loads(ZipData)["CVE_Items"]#提取需要的数据

        if len(ExtractData)==0:#判断文件是否下载错误
            ReportAnErrorAndRestartTheDownload(ZipFilePath[:-9], ZipFilePath[:-24])  # 如果下载错误就重新下载
            return 0
        DataSet=[]#存放500条tuple类型数据容器
        for Data in ExtractData:
            VulnerabilityNumber =Data["cve"]["CVE_data_meta"]["ID"]#提取CVE编号
            VulnerabilityDescription = Data["cve"]["description"]["description_data"][0]["value"]  # 漏洞说明
            #上述两个必定存在的值，下面的参数不一定存在
            try:
                V3BaseScore=Data["impact"]["baseMetricV3"]["cvssV3"]["baseScore"]#CVSS v3版本分值
            except:
                V3BaseScore=""
            try:
                V3BaseSeverity = Data["impact"]["baseMetricV3"]["cvssV3"]["baseSeverity"]  # CVSS v3等级分类
            except:
                V3BaseSeverity=""
            try:
                V2BaseScore = Data["impact"]["baseMetricV2"]["cvssV2"]["baseScore"]  # CVSS v2版本分值
            except:
                V2BaseScore=""
            try:
                V2BaseSeverity = Data["impact"]["baseMetricV2"]["severity"]  # CVSS v2等级分类
            except:
                V2BaseSeverity=""
            try:
                LastUpDate= Data["lastModifiedDate"].partition('T')[0]  #最后修改日期
            except:
                LastUpDate=""
            try:
                ConfigurationsNodes = Data["configurations"]["nodes"]
                Vendors=[]#存放供应商
                VendorsTmp= []  # 存放未进行大小写转换的供应商数据
                Products=[]#存放产品
                ProductsTmp = []  # 存放未进行大小写转换的产品数据
                for i in ConfigurationsNodes:
                    VendorsTmp.append(i["cpe_match"][0]["cpe23Uri"].split(":")[3])#对供应商数据进行提取分割
                    ProductsTmp.append(i["cpe_match"][0]["cpe23Uri"].split(":")[4])#对产品数据进行提取分割
                for i in VendorsTmp:#对供应商数据进行处理
                    Tmp=[]#临时数据
                    for x in i.split("_"):#进行数据分割
                        Tmp.append(x.capitalize())#首字母大写化
                    Vendors.append(' '.join(Tmp))#对数据进行拼接后发送到容器
                for i in ProductsTmp:#对供产品据进行处理
                    Tmp=[]#临时数据
                    for x in i.split("_"):#进行数据分割
                        Tmp.append(x.capitalize())#首字母大写化
                    Products.append(' '.join(Tmp))#对数据进行拼接后发送到容器
            except:
                Vendors=""
                Products=""
            if len(Vendors)==0:#判断是否有数据
                Vendors=""
            if len(Products)==0:
                Products = ""
            DataSet.append((VulnerabilityNumber, V3BaseScore, V3BaseSeverity, V2BaseScore,
                            V2BaseSeverity, LastUpDate, VulnerabilityDescription, str(Vendors), str(Products), str(Data)))
            if len(DataSet)==500:#500写入一次数据库
                Nist.Write(DataSet)
                DataSet.clear()#写入后清空数据库
        Nist.Write(DataSet)#函数循环结束后也写入一次数据库，防止不足500的数据没写入
        Nist.con.close()#关闭数据库连接
        print("[ ~ ] 写入文件：\033[36m"+ZipFilePath+"\033[0m 耗时：\033[34m" + str(time.time() - StartingTime) + "S \033[0m 数据量：\033[32m"+str(len(ExtractData))+"\033[0m条")
        zipFile.close()

    except Exception as e:
        ReportAnErrorAndRestartTheDownload(ZipFilePath[-13:-9], ZipFilePath[:-24])#如果文件不是zip文件，就是表明可能下载错误了
        ErrorLog().Write(
            "Web_CVE_NistMonitoring_NistInitialization_FirsRunProcessing(def)", e)

def InitialVerification(TempFilePath):#验证是否初始化
    try:
        File=open(TempFilePath+"initialization.lock", 'r+').read()
        if File.find("Super Invincible Cute Pieck Finger")!=-1:
            return True
        else:
            return False
    except:
        return False
def NistInitialization():#进行初始化处理
    TempFilePath = GetPath().TempFilePath()  # 获取TMP文件路径
    if not InitialVerification(TempFilePath):#如果不存在初始化
        print("[ + ]正在初始化CVE数据库，请不要结束进程，强制结束会导致CVE数据库数据不全")
        Loop = asyncio.get_event_loop()
        NistTasks = [NistFirstRunDownload(Year,TempFilePath) for Year in range(2002,datetime.datetime.now().year+1)]#获取当前年份进行循环下载
        Loop.run_until_complete(asyncio.wait(NistTasks))
        Loop.close()#下载完毕
        #进行数据写入

        for Year in range(2002, datetime.datetime.now().year + 1):#下载完后再写入
            try:
                FileName = "nvdcve-1.1-" + str(Year) + ".json.zip"  # 下载文件名
                NistFirsRunProcessing(TempFilePath + FileName, FileName[:-4])  # 调用数据处理函数，传入文件路径和提取文件名
            except Exception as e:
                ErrorLog().Write(
                    "Web_CVE_NistMonitoring_NistInitialization_NistInitialization(def)",
                    e)

        open(TempFilePath + "initialization.lock", 'w+').write("Super Invincible Cute Pieck Finger")#初始化后写入初始化锁
        print("CVE数据库初始化成功~")

