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
from Modules.Weblogic import WebLogicRemoteCommandExecutionVulnerability
from Modules.Weblogic import WebLogicDeserializationRemoteCommandExecutionVulnerability
from Modules.Weblogic import WeblogicDeserializationCommandExecutionVulnerability4
from Modules.Weblogic import WebLogicRemoteCommandExecution
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(WeblogicServerSideRequestForgeryVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Pool.Append(WebLogicXMLDecoderDeserializationVulnerability.medusa, Url, Values, proxies=proxies, **kwargs)
    Pool.Append(WeblogicArbitraryFileUploadVulnerability.medusa, Url, Values, proxies=proxies, **kwargs)
    Pool.Append(WeblogicWLSCoreComponentsDeserializationCommandExecutionVulnerability.medusa, Url, Values, proxies=proxies, **kwargs)

    Pool.Append(WeblogicDeserializationCommandExecutionVulnerability.medusa, Url, Values,
                      proxies=proxies, **kwargs)

    Pool.Append(WeblogicDeserializationCommandExecutionVulnerability2.medusa, Url, Values,
                      proxies=proxies, **kwargs)

    Pool.Append(WeblogicDeserializationCommandExecutionVulnerability3.medusa, Url, Values,
                      proxies=proxies, **kwargs)

    Pool.Append(WeblogicT3DeserializationCommandExecutionVulnerability.medusa, Url, Values,
                      proxies=proxies, **kwargs)
    Pool.Append(WebLogicRemoteCommandExecutionVulnerability.medusa, Url, Values,
                      proxies=proxies, **kwargs)
    Pool.Append(WebLogicDeserializationRemoteCommandExecutionVulnerability.medusa, Url, Values,
                      proxies=proxies, **kwargs)
    Pool.Append(WeblogicDeserializationCommandExecutionVulnerability4.medusa, Url, Values,
                      proxies=proxies, **kwargs)
    Pool.Append(WebLogicRemoteCommandExecution.medusa, Url, Values,
                      proxies=proxies, **kwargs)
    Prompt("Weblogic")
