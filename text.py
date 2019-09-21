import urllib
import logging
import requests
import tldextract


Url="www.baidu.gov.cn"
SubdomainCrawlingUrls = tldextract.extract(Url)
SubdomainCrawlingUrl = SubdomainCrawlingUrls.domain +"."+ SubdomainCrawlingUrls.suffix
print(SubdomainCrawlingUrl)