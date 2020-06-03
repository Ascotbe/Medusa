#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Weblogic import WeblogicServerSideRequestForgeryVulnerability
from Modules.Weblogic import WeblogicWLSCoreComponentsDeserializationCommandExecutionVulnerability
from Modules.Weblogic import WebLogicXMLDecoderDeserializationVulnerability
from Modules.Weblogic import WeblogicArbitraryFileUploadVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(WeblogicServerSideRequestForgeryVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    ThreadPool.Append(WebLogicXMLDecoderDeserializationVulnerability.medusa, Url, Values, proxies=proxies, **kwargs)
    ThreadPool.Append(WeblogicArbitraryFileUploadVulnerability.medusa, Url, Values, proxies=proxies, **kwargs)
    #有问题无法复现
    #ThreadPool.Append(WeblogicWLSCoreComponentsDeserializationCommandExecutionVulnerability.medusa, Url, Values, proxies=proxies, **kwargs)
    Prompt("Weblogic")
