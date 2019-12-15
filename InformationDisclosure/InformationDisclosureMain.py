#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from tqdm import tqdm
from InformationDisclosure import Druid
from InformationDisclosure import Git
from InformationDisclosure import Phpinfo
from InformationDisclosure import PhpApc
from InformationDisclosure import Sftp
from InformationDisclosure import Svn
from InformationDisclosure import JetBrains
from InformationDisclosure import Options
from InformationDisclosure import JavaConfigurationFile
from InformationDisclosure import SensitiveFile

import ClassCongregation

def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    Medusa = [Druid.medusa(Url,RandomAgent,ProxyIp), SensitiveFile.medusa(Url,RandomAgent,ProxyIp),Git.medusa(Url, RandomAgent, ProxyIp),Phpinfo.medusa(Url,RandomAgent,ProxyIp),
              PhpApc.medusa(Url,RandomAgent,ProxyIp),Sftp.medusa(Url,RandomAgent,ProxyIp),Svn.medusa(Url,RandomAgent,ProxyIp),JetBrains.medusa(Url,RandomAgent,ProxyIp),
              Options.medusa(Url,RandomAgent,ProxyIp),JavaConfigurationFile.medusa(Url,RandomAgent,ProxyIp)]
    try:
        for i in tqdm(Medusa, ascii=True, desc="Information Disclosure plugin progress:"):
            WriteFile.Write(str(i))
    except:
        pass

