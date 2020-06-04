#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Weblogic import WeblogicServerSideRequestForgeryVulnerability
from Modules.Weblogic import WeblogicWLSCoreComponentsDeserializationCommandExecutionVulnerability
from Modules.Weblogic import WebLogicXMLDecoderDeserializationVulnerability
from Modules.Weblogic import WeblogicArbitraryFileUploadVulnerability
from Modules.Weblogic import WeblogicDeserializationCommandExecutionVulnerability
from Modules.Weblogic import WeblogicDeserializationCommandExecutionVulnerability2
from Modules.Weblogic import WeblogicDeserializationCommandExecutionVulnerability3
from Modules.Weblogic import WeblogicT3DeserializationCommandExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(WeblogicServerSideRequestForgeryVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    ThreadPool.Append(WebLogicXMLDecoderDeserializationVulnerability.medusa, Url, Values, proxies=proxies, **kwargs)
    ThreadPool.Append(WeblogicArbitraryFileUploadVulnerability.medusa, Url, Values, proxies=proxies, **kwargs)
    ThreadPool.Append(WeblogicWLSCoreComponentsDeserializationCommandExecutionVulnerability.medusa, Url, Values, proxies=proxies, **kwargs)

    ThreadPool.Append(WeblogicDeserializationCommandExecutionVulnerability.medusa, Url, Values,
                      proxies=proxies, **kwargs)

    ThreadPool.Append(WeblogicDeserializationCommandExecutionVulnerability2.medusa, Url, Values,
                      proxies=proxies, **kwargs)

    ThreadPool.Append(WeblogicDeserializationCommandExecutionVulnerability3.medusa, Url, Values,
                      proxies=proxies, **kwargs)

    ThreadPool.Append(WeblogicT3DeserializationCommandExecutionVulnerability.medusa, Url, Values,
                      proxies=proxies, **kwargs)

    Prompt("Weblogic")
