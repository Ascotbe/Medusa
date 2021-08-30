# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from Web.celery import app
# from Modules.Confluence import Confluence
# from Modules.Struts2 import Struts2
# from Modules.Nginx import Nginx
# from Modules.Jenkins import Jenkins
# from Modules.Cms import Cms
# from Modules.FastJson import FastJson
# from Modules.Harbor import Harbor
# from Modules.Citrix import Citrix
# from Modules.InformationLeakage import InformationLeakage
# from Modules.Rails import Rails
# from Modules.Kibana import Kibana
# from Modules.BaoTa import BaoTa
# from Modules.PHPStudy import PHPStudy
# from Modules.Mongo import Mongo
# from Modules.Liferay import Liferay
# from Modules.Weblogic import Weblogic
# from Modules.OA.Seeyou import Seeyou
# from Modules.OA.Tongda import Tongda
# from Modules.OA.Weaver import Weaver
# from Modules.OA.Ruvar import Ruvar
# from Modules.Windows import Windows
# from Modules.Spring import Spring
# from Modules.Apache.Shiro import Shiro
# from Modules.Apache.Flink import Flink
# from Modules.Apache.Log4j import Log4j
# from Modules.Apache.ActiveMQ import ActiveMQ
# from Modules.Apache.Solr import Solr
# from Modules.BIG_IP import BIG_IP
# from Modules.Apache.Tomcat import Tomcat
# from ClassCongregation import ProcessPool,UrlProcessing
# from Web.WebClassCongregation import OriginalProxyData,ActiveScanList
# from config import proxy_scan_module_list,proxy_scan_process,proxy_scanned_by_proxy
# MedusaVulnerabilityList={
# "Struts2":Struts2.Main,
# "Confluence":Confluence.Main,
# "Nginx":Nginx.Main,
# "PHPStudy": PHPStudy.Main,
# "Cms": Cms.Main,
# "Jenkins": Jenkins.Main,
# "Harbor": Harbor.Main,
# "Rails":Rails.Main,
# "Kibana":Kibana.Main,
# "Citrix":Citrix.Main,
# "Mongo":Mongo.Main,
# "Spring":Spring.Main,
# "FastJson":FastJson.Main,
# "Windows":Windows.Main,
# "Liferay":Liferay.Main,
# "Shiro":Shiro.Main,
# "Flink":Flink.Main,
# "Log4j":Log4j.Main,
# "ActiveMQ":ActiveMQ.Main,
# "Solr":Solr.Main,
# "Tomcat":Tomcat.Main,
# "Ruvar":Ruvar.Main,
# "Seeyou":Seeyou.Main,
# "Tongda":Tongda.Main,
# "Weaver":Weaver.Main,
# "Weblogic":Weblogic.Main,
# "BIG-IP":BIG_IP.Main,
# "InformationLeakage":InformationLeakage.Main,
# "BaoTa":BaoTa.Main
# }
#
# @app.task
# def MedusaScan(Url,Module,Process,Headers,Proxies,Uid,ActiveScanId):
#
#     scheme, url, port = UrlProcessing().result(Url)
#     if port is None and scheme == 'https':
#         port = 443
#     elif port is None and scheme == 'http':
#         port = 80
#     else:
#         port = port
#     Url=scheme + "://" + url + ":" + str(port)#处理后的URL
#     WebProcessPool =ProcessPool()#定义一个线程池
#     if Module=="all":
#         for MedusaVulnerability in MedusaVulnerabilityList:
#             MedusaVulnerabilityList[MedusaVulnerability](WebProcessPool,ActiveScanId=ActiveScanId,Uid=Uid,Headers=Headers,Url=Url,Proxies=Proxies)#调用列表里面的值
#
#     else:
#         try:
#             MedusaVulnerabilityList[Module](WebProcessPool,ActiveScanId=ActiveScanId,Uid=Uid,Headers=Headers,Url=Url,Proxies=Proxies)  # 调用列表里面的值
#         except:#如果传入非法字符串会调用出错
#             pass
#     WebProcessPool.Start(Process)
#     ActiveScanList().UpdateStatus(redis_id=MedusaScan.request.id)#扫描结束更新任务
#
#
#
#
#
#
# # @app.task
# # def ProxyScan(Url,AgentHeader,**kwargs):
# #     ProxuProcessPool = ProcessPool()  # 定义一个线程池
# #     for Module in proxy_scan_module_list:
# #         try:
# #             MedusaVulnerabilityList[Module](ProxuProcessPool, Url, eval(AgentHeader), proxy_scanned_by_proxy, **kwargs)  # 调用列表里面的值
# #         except:  # 如果传入非法字符串会调用出错
# #             pass
# #     ProxuProcessPool.Start(proxy_scan_process)
# #     OriginalProxyData().UpdateScanStatus(uid=kwargs.get("Uid"), redis_id=ProxyScan.request.id)  # 获取RedisID后进行更新数据库
# #
