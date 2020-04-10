#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# from Apache.Log4j import Log4j
from Apache.Flink import Flink
from Apache.ActiveMQ import ActiveMQ
from Apache.Solr import Solr
from Apache.Tomcat import Tomcat

def Main(ThreadPool,Url,Values,Token,proxies):

    Solr.Main(ThreadPool,Url,Values,Token,proxies)
    ActiveMQ.Main(ThreadPool, Url, Values, Token,proxies)
    Flink.Main(ThreadPool, Url, Values, Token,proxies)
    Tomcat.Main(ThreadPool, Url, Values, Token, proxies)
    #Log4j.Main(ThreadPool, Url, Values, Token)#暂时注释该插件
