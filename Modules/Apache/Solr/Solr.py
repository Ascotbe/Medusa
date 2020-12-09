#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Apache.Solr import SolrVelocityTemplateRemoteCodeExecutionVulnerability
from Modules.Apache.Solr import SolrVelocityTemplateRemoteCodeExecutionVulnerability2
from Modules.Apache.Solr import SolrRemoteCodeExecutionVulnerability
from Modules.Apache.Solr import SolrRemoteCodeExecutionVulnerability2
from ClassCongregation import Prompt

def Main(Pool,**kwargs):
    Pool.Append(SolrVelocityTemplateRemoteCodeExecutionVulnerability.medusa,**kwargs)
    Pool.Append(SolrVelocityTemplateRemoteCodeExecutionVulnerability2.medusa, **kwargs)
    Pool.Append(SolrRemoteCodeExecutionVulnerability.medusa, **kwargs)
    Pool.Append(SolrRemoteCodeExecutionVulnerability2.medusa,**kwargs)
    Prompt("Solr")

