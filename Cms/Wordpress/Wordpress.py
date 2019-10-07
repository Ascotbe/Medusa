#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import Cms.Wordpress.Wordpress_admin_ajax_filedownload
import Cms.Wordpress.Wordpress_plugin_azonpop_sqli
import Cms.Wordpress.Wordpress_plugin_mailpress_rce
import Cms.Wordpress.Wordpress_plugin_ShortCode_lfi
import Cms.Wordpress.Wordpress_woocommerce_code_exec

import ClassCongregation

def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    try:
        Medusa=Cms.Wordpress.Wordpress_admin_ajax_filedownload.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass


    try:
        Medusa=Cms.Wordpress.Wordpress_plugin_azonpop_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa=Cms.Wordpress.Wordpress_plugin_mailpress_rce.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass

    try:
        Medusa=Cms.Wordpress.Wordpress_plugin_ShortCode_lfi.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass

    try:
        Medusa=Cms.Wordpress.Wordpress_woocommerce_code_exec.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
