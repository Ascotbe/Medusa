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
from ClassCongregation import Prompt,UrlProcessing
def Processing(Url):
    scheme, url, port = UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    payload_url = scheme + "://" + url + ":" + str(port)
    return payload_url

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    FilteredURL=Processing(Url)#对Url进行处理
    ThreadPool.Append(Git.medusa, FilteredURL, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(Druid.medusa, FilteredURL, Values,  proxies=proxies,**kwargs)
    ThreadPool.Append(CompressedFile.medusa, FilteredURL, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(Java.medusa, FilteredURL, Values,  proxies=proxies,**kwargs)
    ThreadPool.Append(JetBrains.medusa, FilteredURL, Values,  proxies=proxies,**kwargs)
    ThreadPool.Append(Options.medusa, FilteredURL, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(PhpApc.medusa, FilteredURL, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(PhoInfo.medusa, FilteredURL, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(SensitiveFile.medusa, FilteredURL, Values,  proxies=proxies,**kwargs)
    ThreadPool.Append(Sftp.medusa, FilteredURL, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(Svn.medusa, FilteredURL, Values, proxies=proxies,**kwargs)
    Prompt("InformationLeakage")


def ProxyMain(ThreadPool,Url,Values,proxies,**kwargs):#代理扫描调用
    ThreadPool.Append(Git.medusa, Url, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(Druid.medusa, Url,Values, proxies=proxies,**kwargs)
    ThreadPool.Append(CompressedFile.medusa, Url, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(Java.medusa, Url, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(JetBrains.medusa, Url, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(Options.medusa, Url, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(PhpApc.medusa, Url, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(PhoInfo.medusa, Url,Values, proxies=proxies,**kwargs)
    ThreadPool.Append(SensitiveFile.medusa, Url, Values, proxies=proxies,**kwargs)
    ThreadPool.Append(Sftp.medusa, Url,Values, proxies=proxies,**kwargs)
    ThreadPool.Append(Svn.medusa, Url, Values, proxies=proxies,**kwargs)