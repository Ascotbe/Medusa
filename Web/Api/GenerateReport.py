from django.http import JsonResponse
from Web.WebClassCongregation import UserInfo,MedusaQuery,GetDownloadFolderLocation,ReportGenerationList
from ClassCongregation import ErrorLog
from Web.Workbench.ProcessingReport import GenerateWordReport
import json
from django.http import FileResponse
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord

"""
{
	"token": "XXX",
	"active_scan_id": "X"
}
"""
def GenerateWord(request):#生成word文档报告
    RequestLogRecord(request, request_api="generate_word")
    if request.method == "POST":
        try:
            #传入Sid和Token来进行创建任务
            ActiveScanId=json.loads(request.body)["active_scan_id"]
            UserToken=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="generate_word", uid=Uid)#查询到了在计入
                VulnerabilityDataList,Url = MedusaQuery().QueryBySid(active_scan_id=ActiveScanId,uid=Uid)#查询漏洞列表和URL
                WordDownloadFileName=GenerateWordReport(VulnerabilityDataList=VulnerabilityDataList,target_url=Url)
                if WordDownloadFileName != None:
                    ReportGenerationList().Write(active_scan_id=ActiveScanId,uid=Uid,file_name=WordDownloadFileName)#把相关数据写到数据库中
                    return JsonResponse({'message': WordDownloadFileName, 'code': 200, })
                else:
                    return JsonResponse({'message': '莎酱生不出小莎酱惹QAQ', 'code': 404, })
        except Exception as e:
            ErrorLog().Write("Web_Api_GenerateReport_GenerateWord(def)", e)
            return JsonResponse({'message': '莎酱被玩坏啦(>^ω^<)喵', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""
{
	"token": "XXX",
	"file_name": "X"
}
"""
def DownloadWord(request):#下载word报告
    # 设置响应文件类型数据的响应头
    RequestLogRecord(request, request_api="download_word")
    if request.method == "POST":
        try:
            #传入Sid和Token来进行创建任务
            FileName=json.loads(request.body)["file_name"]
            UserToken=json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询UID
            UserOperationLogRecord(request, request_api="download_word", uid=Uid)
            if Uid != None:  # 查到了UID
                QueryReturnValue=ReportGenerationList().Query(uid=Uid, file_name=FileName)  # 查询是否是该用户的
                if (QueryReturnValue!=None) and (QueryReturnValue!=False):
                    file = open(GetDownloadFolderLocation().Result()+FileName, 'rb')
                    response = FileResponse(file)
                    response['Content-Type'] = 'application/octet-stream'
                    response['Content-Disposition'] = 'attachment;filename='+FileName
                    return response
                else:
                    return JsonResponse({'message': '啊啊啊它不是你的小莎酱，别乱抱呀！', 'code': 404, })
        except Exception as e:
            ErrorLog().Write("Web_Api_GenerateReport_GenerateWord(def)", e)
            return JsonResponse({'message': '莎酱被玩坏啦(>^ω^<)喵', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


