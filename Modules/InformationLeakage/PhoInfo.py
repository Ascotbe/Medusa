#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,ThreadPool,ErrorLog,WriteFile,ErrorHandling,Proxies
import urllib3
import requests
from config import thread_number
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-2-19"  # 插件编辑时间
        self.info['disclosure'] = '2019-9-19'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "PhpInfoTestScriptLeakVulnerability" # 插件名称
        self.info['name'] ="PhpInfo测试脚本泄露漏洞" #漏洞名称
        self.info['affects'] = "PhpInfo"  # 漏洞组件
        self.info['desc_content'] = "敏感文件未删除，导致用户可以访问或者下载，造成大量的数据或源码泄露。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['suggest'] = "删除文件或者对对路径限制访问"  # 修复建议
        self.info['details'] = Medusa  # 结果


def medusa(Url:str,RandomAgent:str,proxies:str=None,**kwargs)->None:
    proxies=Proxies().result(proxies)
    list = [
        '/index.php',
        '/1.php',
        '/2.php',
        '/3.php',
        '/4.php',
        '/5.php',
        '/6.php',
        '/7.php',
        '/8.php',
        '/9.php',
        '/10.php',
        '/11.php',
        '/12.php',
        '/13.php',
        '/123.php',
        '/1234.php',
        '/12345.php',
        '/123456.php',
        '/a.php',
        '/b.php',
        '/c.php',
        '/d.php',
        '/e.php',
        '/f.php',
        '/g.php',
        '/h.php',
        '/i.php',
        '/j.php',
        '/k.php',
        '/l.php',
        '/m.php',
        '/n.php',
        '/o.php',
        '/p.php',
        '/q.php',
        '/r.php',
        '/s.php',
        '/t.php',
        '/u.php',
        '/v.php',
        '/w.php',
        '/x.php',
        '/y.php',
        '/z.php',
        '/php.php',
        '/abc.php',
        '/test.php',
        '/test1.php',
        '/test2.php',
        '/test3.php',
        '/test123.php',
        '/info.php',
        '/phpinfo.php',
        '/iProber.php',
        '/iProber1.php',
        '/iProber2.php',
        '/iProber3.php',
        '/test_phpinfo.php',
        '/tools/info.php',
        '/ship/phpinfo.php',
        '/web/info.php',
        '/web/phpinfo.php',
        '/xampp/info.php',
        '/xampp/phpinfo.php',
        '/index.php?act=phpinfo',
        '/dashboard/phpinfo.php'
    ]
    Pool=ThreadPool()
    headers = {
        'User-Agent': RandomAgent,
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
    }
    try:
        for payload in list:
            payload_url = Url+payload
            Pool.Append(task,Url=Url,headers=headers,proxies=proxies,payload_url=payload_url,Uid=kwargs.get("Uid"),Sid=kwargs.get("Sid"))
        Pool.Start(thread_number)  # 启动线程池
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorLog().Write("Plugin Name:" + _ + " ThreadPool ", e)  # 调用写入类传入URL和错误插件名


def task(**kwargs):
    payload_url=kwargs.get("payload_url")
    headers=kwargs.get("headers")
    proxies=kwargs.get("proxies")
    url=kwargs.get("Url")
    try:
        resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=6, verify=False)
        con = resp.text
        code = resp.status_code
        if code == 200 and con.find('<title>phpinfo()</title>') != -1 and con.find('System') != -1:
            Medusa = "{} 存在PhpInfo测试脚本泄露漏洞\r\n验证数据:\r\n漏洞位置:{}\r\n漏洞详情:{}\r\n".format(url, payload_url, con)
            _t = VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url, Uid=kwargs.get("Uid"),Sid=kwargs.get("Sid")).Write()   # 传入url和扫描到的数据
            WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:" + _ + " || Target Url:" + url, e)  # 调用写入类

