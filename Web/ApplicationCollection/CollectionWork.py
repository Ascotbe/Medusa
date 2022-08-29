#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from Web.DatabaseHub import UserInfo,ApplicationCollection
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
from bs4 import BeautifulSoup
from urllib import parse
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers={
    "Connection": "close",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "dnt": "1"
}

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
            token = json.loads(request.body)["token"]
            app_name=json.loads(request.body)["app_name"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="apple_app_collection", uid=uid)  # 查询到了在计入
                redis_id = AppleCollectionWork.delay(app_name,uid)
                ApplicationCollection().Write(uid=uid,
                                            program_type="Apple",
                                            status="0",
                                            application_data="",
                                            redis_id=str(redis_id),
                                            request_failed_application_name="",
                                            total_number_of_applications="",number_of_failures="")

                return JsonResponse({'message': "任务下发成功(๑•̀ㅂ•́)و✧", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法请求哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
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
            token = json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="application_collection_query", uid=uid)  # 查询到了在计入
                result=ApplicationCollection().Query(uid=uid)#获取查询结果
                return JsonResponse({'message': result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

@app.task
def AppleCollectionWork(app_name,uid):#ios收集工作程序
    application_name_list=[]#存放应用名
    id_list=[]#存放APP id的列表
    application_results_list=[]#存放处理好的应用数据
    request_failed_application_name=[]#存放请求失败文件名
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["Referer"]= "https://apps.apple.com/"

    try:
        interface_splicing="https://itunes.apple.com/search?term="+parse.quote(app_name)+"&country=cn&media=software&entity=software&genreId=&limit=20&offset=0"#对API接口进行拼接

        get_developer_page=requests.get(interface_splicing,headers=headers,timeout=3,verify=False)#获取API中的信息

        developer_page=get_developer_page.json()["results"][0]["artistViewUrl"]#获取开发者页面信息

        get_all_apps=requests.get(developer_page,headers=headers,timeout=3,verify=False)#获取所有应用
        get_all_application_formatted_data=BeautifulSoup(get_all_apps.text, 'lxml')#对结果进行格式化
        extract_valid_data=json.loads(get_all_application_formatted_data.find('script', id='shoebox-ember-data-store').text)#提取带有全部ID的json数据
        all_apps_data = [extract_valid_data['data']['relationships']['macApps'],extract_valid_data['data']['relationships']['iPhoneApps'],
                       extract_valid_data['data']['relationships']['iPhoneiPadApps'] ]
        for apps in all_apps_data:#提取ID值
            if apps['data'] == []:
                continue
            for app in apps['data']:
                if app['id'] not in id_list:
                    id_list.append(app['id'])
    except Exception as e:
        ErrorLog().Write(e)

    data_address='https://uclient-api.itunes.apple.com/WebObjects/MZStorePlatform.woa/wa/lookup?version=2&caller=webExp&p=lockup&useSsl=true&cc=CN&id=' + ','.join(id_list)
    try:
        get_complete_data=requests.get(data_address,headers=headers,timeout=30,verify=False)
        for key in json.loads(get_complete_data.text)['results']:
            application_name_list.append(json.loads(get_complete_data.text)['results'][key]['name'])  # 获取APP名字
    except Exception as e:
        ErrorLog().Write(e)


    for name in application_name_list:
        try:
            apply_complete_data = requests.get("https://itunes.apple.com/search?term=" + parse.quote(
                name) + "&country=cn&media=software&entity=software&genreId=&limit=20&offset=0",headers=headers,timeout=30,verify=False)  # 获取单个应用的数据
            temporary_data = {}
            if (apply_complete_data != None) and (apply_complete_data.status_code != 200):
                if apply_complete_data.status_code == 403:
                    request_failed_application_name.append(name)#请求失败
                continue
            _=json.loads(apply_complete_data.text)#json格式化
            if _['resultCount'] == 0:
                continue
            _ = _['results'][0]
            temporary_data['Icon'] = _['artworkUrl100']
            temporary_data['AppName'] = _['trackName']
            temporary_data['Description'] = _['description']
            temporary_data['FileSizeBytes'] = _['fileSizeBytes']
            temporary_data['SellerName'] = _['sellerName']
            temporary_data['Advisories'] = _['advisories']
            temporary_data['ReleaseDate'] = _['releaseDate']
            temporary_data['Screenshot'] = _['screenshotUrls']
            temporary_data['ArtistName'] = _['artistName']
            temporary_data['ArtistViewUrl'] = _['artistViewUrl']
            temporary_data['DownloadLink'] = _['trackViewUrl']
            application_results_list.append(temporary_data)
            #time.sleep(3)#暂停3秒防止被封
        except Exception as e:
            request_failed_application_name.append(name)#请求超时
            ErrorLog().Write(e)
    # FinalResults["FinalResults"]=json.dumps(ApplicationResultsList)#对提取的数据进行json化
    # FinalResults["RequestFailedApplicationName"] =json.dumps(RequestFailedApplicationName)#请求失败数据
    # FinalResults["Total"]=int(len(ApplicationNameList))#总数
    # FinalResults["NumberOfFailures"]=int(len(RequestFailedApplicationName))#失败个数
    # print(ApplicationNameList)
    # print(IdList)
    # print(ApplicationResultsList)
    # print(FinalResults)
    ApplicationCollection().Update(uid=uid,redis_id=AppleCollectionWork.request.id,
                                   application_data=str(json.dumps(application_results_list)),
                                   request_failed_application_name=str(request_failed_application_name),
                                   total_number_of_applications=str(len(application_name_list)),
                                   number_of_failures=str(len(request_failed_application_name)))  # 收集结束更新任务



