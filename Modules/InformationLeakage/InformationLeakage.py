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

def Main(ThreadPool,Url,Values,Token,proxies):
    FilteredURL=Processing(Url)#对Url进行处理
    ThreadPool.Append(Git.medusa, FilteredURL, Values, Token,proxies=proxies)
    ThreadPool.Append(Druid.medusa, FilteredURL, Values, Token, proxies=proxies)
    ThreadPool.Append(CompressedFile.medusa, FilteredURL, Values, Token, proxies=proxies)
    ThreadPool.Append(Java.medusa, FilteredURL, Values, Token, proxies=proxies)
    ThreadPool.Append(JetBrains.medusa, FilteredURL, Values, Token, proxies=proxies)
    ThreadPool.Append(Options.medusa, FilteredURL, Values, Token, proxies=proxies)
    ThreadPool.Append(PhpApc.medusa, FilteredURL, Values, Token, proxies=proxies)
    ThreadPool.Append(PhoInfo.medusa, FilteredURL, Values, Token, proxies=proxies)
    ThreadPool.Append(SensitiveFile.medusa, FilteredURL, Values, Token, proxies=proxies)
    ThreadPool.Append(Sftp.medusa, FilteredURL, Values, Token, proxies=proxies)
    ThreadPool.Append(Svn.medusa, FilteredURL, Values, Token, proxies=proxies)
    Prompt("InformationLeakage")


def ProxyMain(ThreadPool,Url,Values,Token,proxies):#代理扫描调用
    ThreadPool.Append(Git.medusa, Url, Values, Token,proxies=proxies)
    ThreadPool.Append(Druid.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(CompressedFile.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(Java.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(JetBrains.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(Options.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(PhpApc.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(PhoInfo.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(SensitiveFile.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(Sftp.medusa, Url, Values, Token, proxies=proxies)
    ThreadPool.Append(Svn.medusa, Url, Values, Token, proxies=proxies)