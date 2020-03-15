#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.Log4j import Log4j
from Apache.Flink import Flink
from Apache.ActiveMQ import ActiveMQ
from Apache.Solr import Solr
#from Apache.Tomcat import Tomcat

def Main(ThreadPool,Url,Values,UnixTimestamp):
    Solr.Main(ThreadPool,Url,Values,UnixTimestamp)
    ActiveMQ.Main(ThreadPool, Url, Values, UnixTimestamp)
    Flink.Main(ThreadPool, Url, Values, UnixTimestamp)
    #Log4j.Main(ThreadPool, Url, Values, UnixTimestamp)#暂时注释该插件
