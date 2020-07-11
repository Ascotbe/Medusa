#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
import requests
import urllib3
from config import thread_number
from ClassCongregation import VulnerabilityDetails, UrlProcessing, ErrorLog, WriteFile, ErrorHandling, Proxies,ThreadPool

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-2-19"  # 插件编辑时间
        self.info['disclosure'] = '2019-9-19'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "SensitiveCompressedFileDownloadVulnerability" # 插件名称
        self.info['name'] ="敏感压缩文件下载漏洞" #漏洞名称
        self.info['affects'] = "CompressedFile"  # 漏洞组件
        self.info['desc_content'] = "敏感文件未删除，导致用户可以访问或者下载，造成大量的数据或源码泄露。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['suggest'] = "删除文件或者对对路径限制访问"  # 修复建议
        self.info['details'] = Medusa  # 结果


def medusa(Url:str,RandomAgent:str,proxies:str=None,**kwargs)->None:
    proxies=Proxies().result(proxies)
    scheme, url, port = UrlProcessing().result(Url)
    suffixs = [".zip", ".rar", ".tar.gz", ".tgz", ".7z",".wim",".lzh",".cab",".arj",".lz4",".db",".gz",".bz2 ",".tar.bz2",".xz ",".tar.xz",".z ",".tar.z",".zipx"]
    payloads = ["/www.root",
                "/bbs",
                "/www",
                "/wwwroot",
                "/web",
                "/root",
                "/database",
                "/db",
                "/website",
                "/config_ucenter.php",
                "/config_global.php",
                "/1",
                "/123",
                "/a",
                "/新建文件夹",
                ]
    headers = {
        'User-Agent': RandomAgent,
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
    }
    Pool=ThreadPool()
    try:
        for suffix in suffixs:#域名加上后缀
            payload_url = Url +"/" +url + suffix
            file_name = url + suffix
            Pool.Append(task, url=url, file_name=file_name,headers=headers, proxies=proxies, payload_url=payload_url, Uid=kwargs.get("Uid"),
                        Sid=kwargs.get("Sid"))
        for payload in payloads:
            for suffix in suffixs:
                payload_url = Url+ payload+suffix
                file_name = payload+suffix
                Pool.Append(task,url=url,file_name=file_name,headers=headers,proxies=proxies,payload_url=payload_url,Uid=kwargs.get("Uid"),Sid=kwargs.get("Sid"))
        Pool.Start(thread_number)  # 启动线程池
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorLog().Write("Plugin Name:" + _ + " ThreadPool ", e)  # 调用写入类传入URL和错误插件名


# "377ABCAF271C"  b'7z\xbc\xaf\'\x1c# 7z
# "4D5357494D"  b"MSWIM"#wim
# "002D6C68372D14"  b"\x00-lh7-" #LZH
# "526172211A07"  b"Rar!\x1a\x07"#rar
# "4D534346" b"MSCF"#cab
# "60EA" b"`\xea"#arj
#"04224D18"  b'\x04"=\x18'#lz4
# "53514c69746520666f726d6174203300"  b"SQLite format 3"# SQLite format 3.
# "1f8b"  b"\x1f\x8b"# gz tar.gz
# "425A68"  b"BZh" # bz2 tar.bz2
# "FD377A585A0000"  b"\xfd7zXZ\x00\x00"# xz tar.xz
# "1F9D"  b"\x1d\x90"# z tar.z
# "1FA0"  b"\x1d\xa0"# z tar.z
# "504B0304" b"PK\x03\x04" # zip zipx
def task(**kwargs):
    payload_url=kwargs.get("payload_url")
    headers=kwargs.get("headers")
    proxies=kwargs.get("proxies")
    url=kwargs.get("url")
    file_name=kwargs.get("file_name").lstrip('/')
    try:
        resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=6, verify=False)
        con = resp.text
        bin=resp.content[:30]
        bt=resp.content
        code = resp.status_code
        if code == 200 and (bin.find(b"PK\x03\x04") != -1 or bin.find(b"7z\xbc\xaf\'\x1c") != -1 or bin.find(
                b"BZh") != -1 or bin.find(b"\x1f\x8b") != -1 or bin.find(b"\xfd7zXZ\x00\x00") != -1 or bin.find(
                b"MSWIM") != -1 or bin.find(b"\x00-lh7-") != -1 or bin.find(b"Rar!\x1a\x07") != -1 or bin.find(
                b"MSCF") != -1 or bin.find(b"`\xea") != -1 or bin.find(b'\x04"=\x18') != -1 or bin.find(
                b"\x1d\x90") != -1 or bin.find(b"\x1d\xa0") != -1 or bin.find(b"SQLite format 3") != -1):
            Medusa = "{}存在敏感压缩文件下载漏洞\r\n验证数据:\r\n漏洞位置:{}\r\n漏洞详情:{}\r\n文件名:{}\r\n文件二进制数据{}\r\n".format(url, payload_url,
                                                                                                       con, file_name,
                                                                                                       bt)
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url, Uid=kwargs.get("Uid"),Sid=kwargs.get("Sid")).Write()   # 传入url和扫描到的数据
            WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:" + _ + " || Target Url:" + url, e)  # 调用写入类

