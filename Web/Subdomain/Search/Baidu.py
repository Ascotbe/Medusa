import urllib3
from bs4 import BeautifulSoup
import time
import requests
from Subdomain.ClassCongregation import BasciClass

urllib3.disable_warnings()

def MatchLocation(Basic,Url):
    Resp = requests.head(Url, verify = Basic.Verify ,cookies = Basic.Cookies ,headers = Basic.Header ,proxies = Basic.Proxy
                         ,timeout = Basic.Timeout)
    Location = Resp.headers.get('location')
    return Location

def RedirectMatch(Basic,html):
    Bs = BeautifulSoup(html, 'html.parser')
    SubdomainsAll = set()
    # 获取搜索结果中所有的跳转URL地址
    for FindRes in Bs.find_all('a', {'class': 'c-showurl'}):
        Url = FindRes.get('href')
        Subdomains = MatchLocation(Basic,Url)
        SubdomainsAll.update(Subdomains)
    return SubdomainsAll

def Search(Basic, Domain, Addr, PerPageNum, LimitNum,FilteredSubdomain=''**kwargs):
    PageNum = 0  # 二次搜索重新置0
    while True:
        time.sleep(Basic.Delay)
        Header = Basic.GetHeader()
        Query = 'site:.' + Domain + FilteredSubdomain
        Params = {'wd': Query,
                  'pn': PageNum,
                  'rn': PerPageNum}
        Resp = requests.get(Addr, params=Params, verify=Basic.Verify, cookies=Basic.Cookies, headers=Header,
                             proxies=Basic.Proxy, timeout=Basic.Timeout)
        if not Resp:
            return
        if len(Domain) > 12:  # 解决百度搜索结果中域名过长会显示不全的问题
            Subdomains = RedirectMatch(Basic,Resp.text)
        else:
            Subdomains = Basic.DealSubdomains(Resp, Fuzzy=False)
        if not Basic.CheckSubdomains(Subdomains):
            break
        Basic.Subdomains.update(Subdomains)
        PageNum += PerPageNum
        # 搜索页面没有出现下一页时停止搜索
        if f'&pn={PageNum}&' not in Resp.text:
            break
        if PageNum >= LimitNum:  # 搜索条数限制
            break

def Run(Domain):
    PerPageNum = 50
    Addr = 'https://www.baidu.com/s'
    LimitNum = 750  # 限制搜索条数
    Basic = BasciClass()
    Basic.Domain = Domain
    try:
        Search(Basic,Domain,Addr,PerPageNum,LimitNum)
        for statement in Basic.Filter(Domain, Basic.Subdomains):
            Search(Basic,Domain,Addr,PerPageNum,LimitNum,FilteredSubdomain=statement)
        if Basic.Recursive_search:
            for subdomain in Basic.RecursiveSubdomain():
                Search(Basic,subdomain,Addr,PerPageNum,LimitNum)
        print(Basic.Subdomains)
    except Exception as e:
        return



if __name__ == '__main__':
    Run("mi.com")
