#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import ClassCongregation

class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "KpLi0rn"  # 插件作者
        self.info['createDate'] = "2020-2-13"  # 插件编辑时间
        self.info['disclosure']='2018-07-04'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "CraftedWebCrossSiteScriptingVulnerability"  # 插件名称
        self.info['name'] ='CraftedWeb跨站脚本漏洞' #漏洞名称
        self.info['affects'] = "CraftedWeb"  # 漏洞组件
        self.info['desc_content'] = "2013-09-24之前版本中的aasp_includes/pages/notice.php文件存在跨站脚本漏洞"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "升级最新的系统"  # 修复建议
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果