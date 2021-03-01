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
from Web.celery import app
from Web.WebClassCongregation import UserInfo,ApplicationCollection
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
from bs4 import BeautifulSoup
from urllib import parse
import requests
from config import headers
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


"""apple_app_collection
{
	"token": "",
	"app_name":""
}
"""
def AppleAppCollection(request):  # IOS的程序收集
    RequestLogRecord(request, request_api="apple_app_collection")
    if request.method == "POST":
        try:
            Token = json.loads(request.body)["token"]
            AppName=json.loads(request.body)["app_name"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="apple_app_collection", uid=Uid)  # 查询到了在计入
                RedisId = AppleCollectionWork.delay(AppName,Uid)
                ApplicationCollection().Write(uid=Uid,
                                            program_type="Apple",
                                            status="0",
                                            application_data="",
                                            redis_id=str(RedisId),
                                            request_failed_application_name="",
                                            total_number_of_applications="",number_of_failures="")

                return JsonResponse({'message': "任务下发成功(๑•̀ㅂ•́)و✧", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法请求哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_ApplicationCollection_CollectionWork_AppleAppCollection(def)", e)
            return JsonResponse({'message': "出现未知错误，详情看日志文件", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""application_collection_query
{
	"token": ""
}
"""
def ApplicationCollectionQuery(request):#APP收集统一查询接口
    RequestLogRecord(request, request_api="application_collection_query")
    if request.method == "POST":
        try:
            Token = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="application_collection_query", uid=Uid)  # 查询到了在计入
                ApplicationCollectionResult=ApplicationCollection().Query(uid=Uid)#获取查询结果
                return JsonResponse({'message': ApplicationCollectionResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_ApplicationCollection_CollectionWork_ApplicationCollectionQuery(def)", e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

@app.task
def AppleCollectionWork(AppName,Uid):#ios收集工作程序
    ApplicationNameList=[]#存放应用名
    IdList=[]#存放APP id的列表
    ApplicationResultsList=[]#存放处理好的应用数据
    RequestFailedApplicationName=[]#存放请求失败文件名
    Headers=headers#获取配置文件中的头
    Headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    Headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    Headers["Referer"]= "https://apps.apple.com/"

    try:
        InterfaceSplicing="https://itunes.apple.com/search?term="+parse.quote(AppName)+"&country=cn&media=software&entity=software&genreId=&limit=20&offset=0"#对API接口进行拼接

        GetDeveloperPage=requests.get(InterfaceSplicing,headers=Headers,timeout=3,verify=False)#获取API中的信息

        DeveloperPage=GetDeveloperPage.json()["results"][0]["artistViewUrl"]#获取开发者页面信息

        GetAllApps=requests.get(DeveloperPage,headers=Headers,timeout=3,verify=False)#获取所有应用
        GetAllApplicationFormattedData=BeautifulSoup(GetAllApps.text, 'lxml')#对结果进行格式化
        ExtractValidData=json.loads(GetAllApplicationFormattedData.find('script', id='shoebox-ember-data-store').text)#提取带有全部ID的json数据
        AllAppsData = [ExtractValidData['data']['relationships']['macApps'],ExtractValidData['data']['relationships']['iPhoneApps'],
                       ExtractValidData['data']['relationships']['iPhoneiPadApps'] ]
        for Apps in AllAppsData:#提取ID值
            if Apps['data'] == []:
                continue
            for apps in Apps['data']:
                if apps['id'] not in IdList:
                    IdList.append(apps['id'])
    except Exception as e:
        ErrorLog().Write("Web_ApplicationCollection_CollectionWork_AppleCollectionWork(def)-GetDeveloperPage", e)

    DataAddress='https://uclient-api.itunes.apple.com/WebObjects/MZStorePlatform.woa/wa/lookup?version=2&caller=webExp&p=lockup&useSsl=true&cc=CN&id=' + ','.join(IdList)
    try:
        GetCompleteData=requests.get(DataAddress,headers=Headers,timeout=30,verify=False)
        for key in json.loads(GetCompleteData.text)['results']:
            ApplicationNameList.append(json.loads(GetCompleteData.text)['results'][key]['name'])  # 获取APP名字
    except Exception as e:
        ErrorLog().Write("Web_ApplicationCollection_CollectionWork_AppleCollectionWork(def)-GetCompleteData"  , e)


    for Name in ApplicationNameList:
        try:
            ApplyCompleteData = requests.get("https://itunes.apple.com/search?term=" + parse.quote(
                Name) + "&country=cn&media=software&entity=software&genreId=&limit=20&offset=0",headers=Headers,timeout=30,verify=False)  # 获取单个应用的数据
            TemporaryData = {}
            if (ApplyCompleteData != None) and (ApplyCompleteData.status_code != 200):
                if ApplyCompleteData.status_code == 403:
                    RequestFailedApplicationName.append(Name)#请求失败
                continue
            _=json.loads(ApplyCompleteData.text)#json格式化
            if _['resultCount'] == 0:
                continue
            _ = _['results'][0]
            TemporaryData['Icon'] = _['artworkUrl100']
            TemporaryData['AppName'] = _['trackName']
            TemporaryData['Description'] = _['description']
            TemporaryData['FileSizeBytes'] = _['fileSizeBytes']
            TemporaryData['SellerName'] = _['sellerName']
            TemporaryData['Advisories'] = _['advisories']
            TemporaryData['ReleaseDate'] = _['releaseDate']
            TemporaryData['Screenshot'] = _['screenshotUrls']
            TemporaryData['ArtistName'] = _['artistName']
            TemporaryData['ArtistViewUrl'] = _['artistViewUrl']
            TemporaryData['DownloadLink'] = _['trackViewUrl']
            ApplicationResultsList.append(TemporaryData)
            #time.sleep(3)#暂停3秒防止被封
        except Exception as e:
            RequestFailedApplicationName.append(Name)#请求超时
            ErrorLog().Write("Web_ApplicationCollection_CollectionWork_AppleCollectionWork(def)-ApplyCompleteData"+Name, e)
    # FinalResults["FinalResults"]=json.dumps(ApplicationResultsList)#对提取的数据进行json化
    # FinalResults["RequestFailedApplicationName"] =json.dumps(RequestFailedApplicationName)#请求失败数据
    # FinalResults["Total"]=int(len(ApplicationNameList))#总数
    # FinalResults["NumberOfFailures"]=int(len(RequestFailedApplicationName))#失败个数
    # print(ApplicationNameList)
    # print(IdList)
    # print(ApplicationResultsList)
    # print(FinalResults)
    ApplicationCollection().Update(uid=Uid,redis_id=AppleCollectionWork.request.id,application_data=str(json.dumps(ApplicationResultsList)),request_failed_application_name=str(RequestFailedApplicationName),total_number_of_applications=str(len(ApplicationNameList)),number_of_failures=str(len(RequestFailedApplicationName)))  # 收集结束更新任务



