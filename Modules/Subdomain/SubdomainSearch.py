import re
import requests
import tldextract
import json
from ClassCongregation import ErrorLog,SubdomainTable
TheFirstDataCleaning=[]
Subdomain=[]

def GetHeaders(Agent:str):#处理请求头
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en',
        'User-Agent': Agent,
    }
    return headers

def GetDomainName(Url:str)->str:#处理URL
    DomainNameProcessing = tldextract.extract(Url)
    DomainName = DomainNameProcessing.domain + "." + DomainNameProcessing.suffix
    return DomainName

def CrtSubdomainSearch(DomainName:str,Headers:dict,Proxies:str=None)->None:
    try:
        Crt=requests.get("https://crt.sh/?q="+DomainName, headers=Headers, timeout=10, proxies=Proxies)
        RegularProcessing=re.compile('<TD>(.*?)</TD>').findall(Crt.text)
        for CrtA in RegularProcessing:
            RemoveLabel=CrtA.split("<BR>")
            for i in RemoveLabel:
                TheFirstDataCleaning.append(i)

        for CrtB in TheFirstDataCleaning:
            Data = CrtB.strip()
            if not Data.endswith(DomainName) or '*' in Data or '@' in Data:
                continue
            if Data not in Subdomain and Data != DomainName:
                Subdomain.append(Data.strip())
        TheFirstDataCleaning.clear()#清空数据
    except Exception as e:
        ErrorLog().Write("SubdomainSearch_CrtSubdomainSearch(def)", e)


def Sublist3rSubdomainSearch(DomainName:str,Headers:dict,Proxies:str=None)->None:
    try:
        Sublist3r = requests.get("https://api.sublist3r.com/search.php?domain=" + DomainName, headers=Headers, timeout=10, proxies=Proxies)
        con=Sublist3r.text
        for Data in json.loads(con):
            if Data not in Subdomain and Data != DomainName:
                Subdomain.append(Data.strip())
    except Exception as e:
        ErrorLog().Write("SubdomainSearch_Sublist3rSubdomainSearch(def)", e)

def SubdomainSearch(Url:str,RandomAgent:str,proxies=None,**kwargs)->None:#子域名搜索核心函数
    DomainName=GetDomainName(Url)
    Headers=GetHeaders(RandomAgent)
    CrtSubdomainSearch(DomainName,Headers,Proxies=proxies)
    Sublist3rSubdomainSearch(DomainName,Headers,Proxies=proxies)
    for i in Subdomain:#循环写入数据库
        SubdomainTable(DomainName,i,**kwargs).Write()


