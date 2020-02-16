#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Solr import SolrVelocityTemplateRemoteCodeExecutionVulnerability
from Solr import SolrVelocityTemplateRemoteCodeExecutionVulnerability2
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(SolrVelocityTemplateRemoteCodeExecutionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SolrVelocityTemplateRemoteCodeExecutionVulnerability2.medusa, Url, Values, ProxyIp)
    print("Solr component payload successfully loaded")

