#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.InformationLeakage import Git
from Modules.InformationLeakage import Druid
from Modules.InformationLeakage import CompressedFile
from Modules.InformationLeakage import Java
from Modules.InformationLeakage import JetBrains
from Modules.InformationLeakage import Options
from Modules.InformationLeakage import PhpApc
from Modules.InformationLeakage import PhoInfo
from Modules.InformationLeakage import SensitiveFile
from Modules.InformationLeakage import Sftp
from Modules.InformationLeakage import Svn
from ClassCongregation import Prompt


def Main(ThreadPool,**kwargs):

    ThreadPool.Append(Git.medusa, **kwargs)
    ThreadPool.Append(Druid.medusa, **kwargs)
    ThreadPool.Append(CompressedFile.medusa, **kwargs)
    ThreadPool.Append(Java.medusa, **kwargs)
    ThreadPool.Append(JetBrains.medusa, **kwargs)
    ThreadPool.Append(Options.medusa, **kwargs)
    ThreadPool.Append(PhpApc.medusa, **kwargs)
    ThreadPool.Append(PhoInfo.medusa,**kwargs)
    ThreadPool.Append(SensitiveFile.medusa, **kwargs)
    ThreadPool.Append(Sftp.medusa, **kwargs)
    ThreadPool.Append(Svn.medusa, **kwargs)
    Prompt("InformationLeakage")
