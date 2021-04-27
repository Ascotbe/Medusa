#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Weblogic import WeblogicServerSideRequestForgeryVulnerability
from Modules.Weblogic import WeblogicWLSCoreComponentsDeserializationCommandExecutionVulnerability
from Modules.Weblogic import WebLogicXMLDecoderDeserializationVulnerability
from Modules.Weblogic import WeblogicArbitraryFileUploadVulnerability
from Modules.Weblogic import WeblogicDeserializationCommandExecutionVulnerability
from Modules.Weblogic import WeblogicDeserializationCommandExecutionVulnerability2
from Modules.Weblogic import WeblogicDeserializationCommandExecutionVulnerability3
#from Modules.Weblogic import WeblogicT3DeserializationCommandExecutionVulnerability
from Modules.Weblogic import WebLogicRemoteCommandExecutionVulnerability
from Modules.Weblogic import WebLogicDeserializationRemoteCommandExecutionVulnerability
from Modules.Weblogic import WeblogicDeserializationCommandExecutionVulnerability4
from Modules.Weblogic import WebLogicRemoteCommandExecution
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(WeblogicServerSideRequestForgeryVulnerability.medusa,** kwargs)
    Pool.Append(WebLogicXMLDecoderDeserializationVulnerability.medusa,  **kwargs)
    Pool.Append(WeblogicArbitraryFileUploadVulnerability.medusa,  **kwargs)
    Pool.Append(WeblogicWLSCoreComponentsDeserializationCommandExecutionVulnerability.medusa,  **kwargs)
    Pool.Append(WeblogicDeserializationCommandExecutionVulnerability.medusa,  **kwargs)
    Pool.Append(WeblogicDeserializationCommandExecutionVulnerability2.medusa,  **kwargs)
    Pool.Append(WeblogicDeserializationCommandExecutionVulnerability3.medusa,  **kwargs)
    #Pool.Append(WeblogicT3DeserializationCommandExecutionVulnerability.medusa,  **kwargs)
    Pool.Append(WebLogicRemoteCommandExecutionVulnerability.medusa,  **kwargs)
    Pool.Append(WebLogicDeserializationRemoteCommandExecutionVulnerability.medusa,  **kwargs)
    Pool.Append(WeblogicDeserializationCommandExecutionVulnerability4.medusa,  **kwargs)
    Pool.Append(WebLogicRemoteCommandExecution.medusa,  **kwargs)
    Prompt("Weblogic")
