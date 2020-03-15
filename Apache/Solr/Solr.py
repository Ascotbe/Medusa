#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Apache.Solr import SolrVelocityTemplateRemoteCodeExecutionVulnerability
from Apache.Solr import SolrVelocityTemplateRemoteCodeExecutionVulnerability2
from Apache.Solr import SolrRemoteCodeExecutionVulnerability
from Apache.Solr import SolrRemoteCodeExecutionVulnerability2
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(SolrVelocityTemplateRemoteCodeExecutionVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(SolrVelocityTemplateRemoteCodeExecutionVulnerability2.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(SolrRemoteCodeExecutionVulnerability.medusa, Url, Values,UnixTimestamp)
    ThreadPool.Append(SolrRemoteCodeExecutionVulnerability2.medusa, Url, Values, UnixTimestamp)
    Prompt("Solr")

