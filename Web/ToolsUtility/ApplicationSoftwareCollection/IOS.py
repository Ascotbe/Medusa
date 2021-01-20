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
from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
from lxml import etree
import re
from urllib import parse
import requests
from config import headers
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def ProgramCollection(request):  # IOS的程序收集
    RequestLogRecord(request, request_api="ios_program_collection")
    if request.method == "POST":
        try:
            Token = json.loads(request.body)["token"]
            ProcessNameList = json.loads(request.body)["process_name_list"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="ios_program_collection", uid=Uid)  # 查询到了在计入

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_ToolsUtility_AntivirusSoftware_Compared(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

def test():
    DownloadLinkList=[]#存放下载地址表
    ApplicationNameList=[]#存放应用名
    ApplicationDescriptionList=[]#存放应用说明
    IconList=[]#图标列表
    x="奇迹暖暖"
    InterfaceSplicing="https://itunes.apple.com/search?term="+parse.quote(x)+"&country=cn&media=software&entity=software&genreId=&limit=20&offset=0"#对API接口进行拼接

    GetDeveloperPage=requests.get(InterfaceSplicing,headers=headers,timeout=3,verify=False)#获取API中的信息

    DeveloperPage=GetDeveloperPage.json()["results"][0]["artistViewUrl"]#获取开发者页面信息

    GetAllApps=requests.get(DeveloperPage,headers=headers,timeout=3,verify=False)#获取所有应用
    GetAllApplicationFormattedData=etree.HTML(GetAllApps.text)#对结果进行格式化
    ExtractorConnection=GetAllApplicationFormattedData.xpath("""//section/div/a/@href""")#所有程序的连接
    for i in ExtractorConnection[:-2]:#对链接进行处理
        if re.match(r'^https?:/{2}\w.+$', i):
            DownloadLinkList.append(i)
    ExtractorName=GetAllApplicationFormattedData.xpath("""//section/div/a/div/div/div[@class="we-truncate we-truncate--single-line ember-view targeted-link__target"]/text()""")#程序名字
    for i in ExtractorName:#程序名处理
        ApplicationNameList.append(i.strip(' ').strip('\n'))
    ExtractionIntroduction=GetAllApplicationFormattedData.xpath("""//section/div/a/div/div[@class="we-truncate we-truncate--single-line ember-view we-lockup__subtitle targeted-link__target"]/text()""")#程序连接
    for i in ExtractionIntroduction:#程序说明处理
        ApplicationDescriptionList.append(i.strip(' ').strip('\n'))
    ExtractorIcon=GetAllApplicationFormattedData.xpath("""//section/div/a/picture/source[@class="we-artwork__source"][1]/@srcset""")#程序图标
    for i in ExtractorIcon:#程序图标处理
        IconList.append(i.split(',')[1].split(' 2x')[0])
    print(ExtractorIcon)
    print(ExtractorName)
    print(ExtractorConnection)
    print(ExtractionIntroduction)
    print(DeveloperPage)
    print(IconList)
    print(DownloadLinkList)
    print(ApplicationNameList)
    print(ApplicationDescriptionList)
    for x in ApplicationNameList:
        print(x)



#test()