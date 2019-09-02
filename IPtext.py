# !/usr/bin/env python
# _*_ coding: utf-8 _*_
import requests
import re
from scrapy.selector import Selector

def crawl_ips():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/59.0.3071.115 Safari/537.36"}
    for i in range(1, 100):
        HttpUrl = 'http://www.xicidaili.com/wt/{0}'.format(i)
        req = requests.get(url=HttpUrl, headers=headers)
        selector = Selector(text=req.text)
        HttpAllTrs = selector.xpath('//*[@id="ip_list"]//tr')

        HttpIpLists = []
        for tr in HttpAllTrs[1:]:#过滤第一个tr标签里面是其他数据
            HttpIp = tr.xpath('td[2]/text()').extract()[0]
            HttpPort = tr.xpath('td[3]/text()').extract()[0]
            #proxy_type = tr.xpath('td[6]/text()').extract()[0].lower()
            HttpIpLists.append((HttpIp+':'+HttpPort))#存储到httpIP列表里面

        for ip in HttpIpLists:
            #print(ip)
            proxies = {
                "http": ip
            }
            try:

                if requests.get('https://www.baidu.com/', proxies=proxies, timeout=2).status_code == 200:
                    print('success %s' % ip)
                    # if proxy not in proxy_list:#如果代理IP不在列表里面就传到列表里
                    #     proxy_list.append(proxy)
            except:
                pass


crawl_ips()

