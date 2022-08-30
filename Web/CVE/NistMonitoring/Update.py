#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import json
from Web.DatabaseHub import NistData
import urllib3
from ClassCongregation import GetPath,ErrorLog
from config import nist_update_banner
import time
import requests
from celery import shared_task

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
temp_file_path = GetPath().TempFilePath()  # 获取TMP文件路径
headers={
    "Connection": "close",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "dnt": "1"
}
@shared_task
def Download():#更新数据下载
    try:
        file_name="nvdcve-1.1-" + str("modified") + ".json.zip"#下载文件名
        save_file_name="nvdcve-1.1-" + str("modified") +str(int(time.time()))+ ".json.zip"
        url="https://nvd.nist.gov/feeds/json/cve/1.1/"+file_name
        start_time=time.time()
        if nist_update_banner:
            print("[ + ] 正在重新下载文件：\033[36m" + file_name+ "\033[0m")
        download_file=requests.get(url,headers=headers,  verify=False,timeout=60)
        with open(temp_file_path+save_file_name, 'wb+') as file:
            file.write(download_file.content)
        if nist_update_banner:
            print("[ - ] 成功下载文件：\033[36m" + file_name + "\033[0m 耗时：\033[34m" + str(
            time.time() - start_time) + "S \033[0m")
        NistUpdateProcessing(temp_file_path+save_file_name,file_name[:-4])#调用数据处理函数，传入文件路径和提取文件名
    except Exception as e:
        Download(temp_file_path)#如果还是报错就再次循环自身
        ErrorLog().Write(e)


def NistUpdateProcessing(zip_file_path,zip_file_data):#更新数据库处理函数
    try:
        start_time = time.time()
        nist=NistData()#初始化连接

        get_zip_file = zipfile.ZipFile(zip_file_path, 'r')#获取下载好的数据

        zip_data = get_zip_file.read(zip_file_data).decode('utf-8')#读取到的byte类型进行转换到字符串类型
        extract_data=json.loads(zip_data)["CVE_Items"]#提取需要的数据

        if len(extract_data)==0:#判断文件是否下载错误
            Download(temp_file_path)  # 如果下载错误就重新下载
            return 0
        data_set=[]#存放所有tuple类型数据容器
        update_data = []  # 存放所有需要更新的数据
        insert_data = []  # 存放所有需要插入的数据
        update_count=0#更新数据计数
        insert_count=0#插入数据计数
        for data in extract_data:
            vulnerability_number =data["cve"]["CVE_data_meta"]["ID"]#提取CVE编号
            vulnerability_description = data["cve"]["description"]["description_data"][0]["value"]  # 漏洞说明
            #上述两个必定存在的值，下面的参数不一定存在
            try:
                v3_base_score=data["impact"]["baseMetricV3"]["cvssV3"]["baseScore"]#CVSS v3版本分值
            except:
                v3_base_score=""
            try:
                v3_base_severity = data["impact"]["baseMetricV3"]["cvssV3"]["baseSeverity"]  # CVSS v3等级分类
            except:
                v3_base_severity=""
            try:
                v2_base_score = data["impact"]["baseMetricV2"]["cvssV2"]["baseScore"]  # CVSS v2版本分值
            except:
                v2_base_score=""
            try:
                v2_base_severity = data["impact"]["baseMetricV2"]["severity"]  # CVSS v2等级分类
            except:
                v2_base_severity=""
            try:
                last_up_date= data["lastModifiedDate"].partition('T')[0]  #最后修改日期
            except:
                last_up_date=""
            try:
                configurations_nodes = data["configurations"]["nodes"]
                vendors=[]#存放供应商
                vendors_tmp= []  # 存放未进行大小写转换的供应商数据
                products=[]#存放产品
                products_tmp = []  # 存放未进行大小写转换的产品数据
                for i in configurations_nodes:
                    vendors_tmp.append(i["cpe_match"][0]["cpe23Uri"].split(":")[3])#对供应商数据进行提取分割
                    products_tmp.append(i["cpe_match"][0]["cpe23Uri"].split(":")[4])#对产品数据进行提取分割
                for i in vendors_tmp:#对供应商数据进行处理
                    Tmp=[]#临时数据
                    for x in i.split("_"):#进行数据分割
                        Tmp.append(x.capitalize())#首字母大写化
                    vendors.append(' '.join(Tmp))#对数据进行拼接后发送到容器
                for i in products_tmp:#对供产品据进行处理
                    Tmp=[]#临时数据
                    for x in i.split("_"):#进行数据分割
                        Tmp.append(x.capitalize())#首字母大写化
                    products.append(' '.join(Tmp))#对数据进行拼接后发送到容器
            except:
                vendors=""
                products=""
            if len(vendors)==0:#判断是否有数据
                vendors=""
            if len(products)==0:
                products = ""
            data_set.append((vulnerability_number, v3_base_score, v3_base_severity, v2_base_score,
                            v2_base_severity, last_up_date, vulnerability_description, str(vendors), str(products), str(data)))

        for i in data_set:
            search_result=nist.UniqueInquiry(vulnerability_number=i[0])#获取查询结果
            if search_result:#如果有数据
                update_data.append(i+(i[0],))#在后面添加上vulnerability_number值用来作为更新的key
            else:
                insert_data.append(i)

            if len(update_data)==500:#500写入一次数据库
                nist.Update(update_data)
                update_count+=500
                update_data.clear()#写入后清空数据库
            if len(insert_data)==500:#500写入一次数据库
                nist.Write(insert_data)
                insert_count += 500
                insert_data.clear()#写入后清空数据库


        #不足500的数据写入
        nist.Update(update_data)
        update_count+=len(update_data)
        update_data.clear()#写入后清空数据库
        nist.Write(insert_data)
        insert_count+=len(insert_data)
        insert_data.clear()#写入后清空数据库
        if nist_update_banner:
            print("[ ~ ] 更新文件来源：\033[36m"+zip_file_path+"\033[0m 耗时：\033[34m" + str(time.time() - start_time) + "S \033[0m 更新数据：\033[32m"+str(update_count)+"\033[0m条"+" 插入数据：\033[32m"+str(insert_count)+"\033[0m条")
        get_zip_file.close()

    except Exception as e:
        Download(temp_file_path)#如果文件不是zip文件，就是表明可能下载错误了
        ErrorLog().Write(e)
