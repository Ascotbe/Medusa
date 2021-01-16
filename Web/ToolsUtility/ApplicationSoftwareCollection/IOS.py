# coding:utf-8
"""
搜索关键字获取结果
https://www.apple.com.cn/cn/search/%E5%BF%AB%E6%89%8B?src=serp

匹配关键字获取APP详情
https://apps.apple.com/cn/app/快手/id440948110
检索信息 [文件大小,供应商,截屏,广告词]

通过供应商获取其他相关APP资产
https://apps.apple.com/cn/developer/beijing-kwai-technology-co-ltd/id440948113

https://itunes.apple.com/search?term=苏宁&country=cn&media=software&entity=software&genreId=&limit=20&offset=0

https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/

"""
from lxml import etree
import re
text,text2,text3="1"
html = etree.HTML(text)
html2 = etree.HTML(text2)
# import requests
# aa=requests.get("https://apps.apple.com/cn/app/%E5%BF%AB%E6%89%8B/id440948110#see-all/developer-other-apps")
html3 = etree.HTML(text3)

res2 = html.xpath("""//*[@id="exploreCurated"]/div[1]/div[1]/img/@src""")#图标
res3 = html.xpath("""//*[@id="exploreCurated"]/div[1]/div[2]/ul/li/a/@href""")#APP连接
print(res2)
print(res3)
a=re.findall(r'http[s]://apps.apple.com/cn/app/(.*?)/', res3[0])#名字
print(a)

res4 = html2.xpath("""//*[@data-test-content-section="developerOtherApps"]/div[1]/a/@href""")#APP id
print(res4)

res5=html3.xpath("""//section/div/a/@href""")#所有程序的连接

for i in res5[:-2]:
    if re.match(r'^https?:/{2}\w.+$', i):
        print("合法url:"+i)

res6=html3.xpath("""//section/div/a/div/div/div[@class="we-truncate we-truncate--single-line ember-view targeted-link__target"]/text()""")#程序名字
print(res6)

res7=html3.xpath("""//section/div/a/div/div[@class="we-truncate we-truncate--single-line ember-view we-lockup__subtitle targeted-link__target"]/text()""")#程序名字
print(res7)

res8=html3.xpath("""//section/div/a/picture/source[@class="we-artwork__source"][1]/@srcset""")#程序图标

for i in res8:
    print(i.split(',')[1].split(' 2x')[0])