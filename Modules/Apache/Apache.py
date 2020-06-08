#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# from Apache.Log4j import Log4j
from Modules.Apache.Flink import Flink
from Modules.Apache.ActiveMQ import ActiveMQ
from Modules.Apache.Solr import Solr
from Modules.Apache.Tomcat import Tomcat
from Modules.Apache.Shiro import Shiro

def Main(ThreadPool,Url,Values,proxies,**kwargs):

    Solr.Main(ThreadPool,Url,Values,proxies,**kwargs)
    ActiveMQ.Main(ThreadPool,Url,Values,proxies,**kwargs)
    Flink.Main(ThreadPool,Url,Values,proxies,**kwargs)
    Tomcat.Main(ThreadPool,Url,Values,proxies,**kwargs)
    Shiro.Main(ThreadPool, Url, Values, proxies, **kwargs)
    #Log4j.Main(ThreadPool, Url, Values, Token)#暂时注释该插件
