#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import json
from Web.DatabaseHub import NistData
import urllib3
from ClassCongregation import GetPath, ErrorLog
import datetime
import time
import aiohttp
import aiofiles
import requests
import asyncio

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {
    "Connection": "close",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "dnt": "1"
}


# https://nvd.nist.gov/vuln/data-feeds
async def NistFirstRunDownload(year, temp_file_path):  # 第一次运行下载数据
    try:
        file_name = "nvdcve-1.1-" + str(year) + ".json.zip"  # 下载文件名
        url = "https://nvd.nist.gov/feeds/json/cve/1.1/" + file_name
        start_time = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as DownloadFile:
                # DownloadFile=requests.get(Url,headers=headers,  verify=False)
                file = await aiofiles.open(temp_file_path + file_name, 'wb+')
                await file.write(await DownloadFile.read())
                print("[ + ] 下载文件：\033[36m" + file_name + "\033[0m 耗时：\033[34m" + str(
                    time.time() - start_time) + "S \033[0m")

    except Exception as e:
        print("[ ! ]" + str(year) + "年数据下载出错 报错信息：" + str(e))
        ErrorLog().Write(e)


def ReportAnErrorAndRestartTheDownload(year, temp_file_path):  # 报错下载，由于数据可能未下载成功重复运行
    try:
        file_name = "nvdcve-1.1-" + str(year) + ".json.zip"  # 下载文件名
        url = "https://nvd.nist.gov/feeds/json/cve/1.1/" + file_name
        start_time = time.time()
        print("[ + ] 正在重新下载文件：\033[36m" + file_name + "\033[0m")
        download_file = requests.get(url, headers=headers, verify=False, timeout=60)
        with open(temp_file_path + file_name, 'wb+') as file:
            file.write(download_file.content)
        print("[ - ] 成功下载文件：\033[36m" + file_name + "\033[0m 耗时：\033[34m" + str(
            time.time() - start_time) + "S \033[0m")
        NistFirsRunProcessing(temp_file_path + file_name, file_name[:-4])  # 调用数据处理函数，传入文件路径和提取文件名
    except Exception as e:
        ReportAnErrorAndRestartTheDownload(year, temp_file_path)  # 如果还是报错就再次循环自身
        ErrorLog().Write(e)


def NistFirsRunProcessing(zip_file_path, zip_file_data):  # 第一次运行数据处理
    try:
        start_time = time.time()
        nist = NistData()  # 初始化连接
        get_zip_file = zipfile.ZipFile(zip_file_path, 'r')  # 获取下载好的数据

        zip_data = get_zip_file.read(zip_file_data).decode('utf-8')  # 读取到的byte类型进行转换到字符串类型
        extract_data = json.loads(zip_data)["CVE_Items"]  # 提取需要的数据

        if len(extract_data) == 0:  # 判断文件是否下载错误
            ReportAnErrorAndRestartTheDownload(zip_file_path[:-9], zip_file_path[:-24])  # 如果下载错误就重新下载
            return 0
        data_set = []  # 存放500条tuple类型数据容器
        for data in extract_data:
            vulnerability_number = data["cve"]["CVE_data_meta"]["ID"]  # 提取CVE编号
            vulnerability_description = data["cve"]["description"]["description_data"][0]["value"]  # 漏洞说明
            # 上述两个必定存在的值，下面的参数不一定存在
            try:
                v3_base_score = data["impact"]["baseMetricV3"]["cvssV3"]["baseScore"]  # CVSS v3版本分值
            except:
                v3_base_score = ""
            try:
                v3_base_severity = data["impact"]["baseMetricV3"]["cvssV3"]["baseSeverity"]  # CVSS v3等级分类
            except:
                v3_base_severity = ""
            try:
                v2_base_score = data["impact"]["baseMetricV2"]["cvssV2"]["baseScore"]  # CVSS v2版本分值
            except:
                v2_base_score = ""
            try:
                v2_base_severity = data["impact"]["baseMetricV2"]["severity"]  # CVSS v2等级分类
            except:
                v2_base_severity = ""
            try:
                last_up_date = data["lastModifiedDate"].partition('T')[0]  # 最后修改日期
            except:
                last_up_date = ""
            try:
                configurations_nodes = data["configurations"]["nodes"]
                vendors = []  # 存放供应商
                vendors_tmp = []  # 存放未进行大小写转换的供应商数据
                products = []  # 存放产品
                products_tmp = []  # 存放未进行大小写转换的产品数据
                for i in configurations_nodes:
                    vendors_tmp.append(i["cpe_match"][0]["cpe23Uri"].split(":")[3])  # 对供应商数据进行提取分割
                    vendors_tmp.append(i["cpe_match"][0]["cpe23Uri"].split(":")[4])  # 对产品数据进行提取分割
                for i in vendors_tmp:  # 对供应商数据进行处理
                    tmp = []  # 临时数据
                    for x in i.split("_"):  # 进行数据分割
                        tmp.append(x.capitalize())  # 首字母大写化
                    vendors.append(' '.join(tmp))  # 对数据进行拼接后发送到容器
                for i in products_tmp:  # 对供产品据进行处理
                    tmp = []  # 临时数据
                    for x in i.split("_"):  # 进行数据分割
                        tmp.append(x.capitalize())  # 首字母大写化
                    products.append(' '.join(tmp))  # 对数据进行拼接后发送到容器
            except:
                vendors = ""
                products = ""
            if len(vendors) == 0:  # 判断是否有数据
                vendors = ""
            if len(products) == 0:
                products = ""
            data_set.append((vulnerability_number, v3_base_score, v3_base_severity, v2_base_score,
                             v2_base_severity, last_up_date, vulnerability_description, str(vendors), str(products),
                             str(data)))
            if len(data_set) == 500:  # 500写入一次数据库
                nist.Write(data_set)
                data_set.clear()  # 写入后清空数据库
        nist.Write(data_set)  # 函数循环结束后也写入一次数据库，防止不足500的数据没写入
        nist.con.close()  # 关闭数据库连接
        print("[ ~ ] 写入文件：\033[36m" + zip_file_path + "\033[0m 耗时：\033[34m" + str(
            time.time() - start_time) + "S \033[0m 数据量：\033[32m" + str(len(extract_data)) + "\033[0m条")
        get_zip_file.close()

    except Exception as e:
        ReportAnErrorAndRestartTheDownload(zip_file_path[-13:-9], zip_file_path[:-24])  # 如果文件不是zip文件，就是表明可能下载错误了
        ErrorLog().Write(e)


def InitialVerification(temp_file_path):  # 验证是否初始化
    try:
        file = open(temp_file_path + "initialization.lock", 'r+').read()
        if file.find("Super Invincible Cute Pieck Finger") != -1:
            return True
        else:
            return False
    except:
        return False


def NistInitialization():  # 进行初始化处理
    temp_file_path = GetPath().TempFilePath()  # 获取TMP文件路径
    if not InitialVerification(temp_file_path):  # 如果不存在初始化
        print("[ + ]正在初始化CVE数据库，请不要结束进程，强制结束会导致CVE数据库数据不全")
        loop = asyncio.get_event_loop()
        nist_tasks = [NistFirstRunDownload(year, temp_file_path) for year in
                     range(2002, datetime.datetime.now().year + 1)]  # 获取当前年份进行循环下载
        loop.run_until_complete(asyncio.wait(nist_tasks))
        loop.close()  # 下载完毕
        # 进行数据写入

        for year in range(2002, datetime.datetime.now().year + 1):  # 下载完后再写入
            try:
                file_name = "nvdcve-1.1-" + str(year) + ".json.zip"  # 下载文件名
                NistFirsRunProcessing(temp_file_path + file_name, file_name[:-4])  # 调用数据处理函数，传入文件路径和提取文件名
            except Exception as e:
                ErrorLog().Write(e)

        open(temp_file_path + "initialization.lock", 'w+').write("Super Invincible Cute Pieck Finger")  # 初始化后写入初始化锁
        print("CVE数据库初始化成功~")
