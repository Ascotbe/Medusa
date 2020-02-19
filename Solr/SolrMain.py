#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Solr import SolrVelocityTemplateRemoteCodeExecutionVulnerability
from Solr import SolrVelocityTemplateRemoteCodeExecutionVulnerability2
from Solr import SolrRemoteCodeExecutionVulnerability
from Solr import SolrRemoteCodeExecutionVulnerability2
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(SolrVelocityTemplateRemoteCodeExecutionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SolrVelocityTemplateRemoteCodeExecutionVulnerability2.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SolrRemoteCodeExecutionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SolrRemoteCodeExecutionVulnerability2.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] Solr component payload successfully loaded\033[0m")
    time.sleep(0.5)

