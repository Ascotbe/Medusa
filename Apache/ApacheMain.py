#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.Log4j import Log4j
from Apache.Flink import Flink
from Apache.ActiveMQ import ActiveMQ
from Apache.Solr import Solr
#from Apache.Tomcat import Tomcat

def Main(ThreadPool,Url,Values,ProxyIp):
    Solr.Main(ThreadPool,Url,Values,ProxyIp)
    ActiveMQ.Main(ThreadPool, Url, Values, ProxyIp)
    Flink.Main(ThreadPool, Url, Values, ProxyIp)
    #Log4j.Main(ThreadPool, Url, Values, ProxyIp)#暂时注释该插件
