from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,GetCrossSiteScriptTemplateFilePath
import json
import base64
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord

"""read_cross_site_scripting_template
{
	"token": ""
}
"""
def ReadTemplate(request):#用读取默认的模板文件
    RequestLogRecord(request, request_api="read_cross_site_scripting_template")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="read_cross_site_scripting_template", uid=Uid)

                DefaultTemplateFileName=["xss.js","test.js"]#默认模板名，目前只有两个测试数据
                DefaultTemplateFileData=[]#用来存放默认模板数据
                CrossSiteScriptTemplateFilePath=GetCrossSiteScriptTemplateFilePath().Result()#获取模板文件路径
                for FileName in DefaultTemplateFileName:
                    with open(CrossSiteScriptTemplateFilePath+FileName, 'r+') as f:#读取文件
                        FileData = f.read()
                    DefaultTemplateFileData.append({"FileName":base64.b64encode(str(FileData).encode('utf-8')).decode('utf-8')})#把读取到的数据加密后，转换成str类型后存入模板中
                return JsonResponse({'message': DefaultTemplateFileData, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_CrossSiteScriptMonitor_GenerateProject(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


def SaveTemplate(request):#用来保存模板数据
    RequestLogRecord(request, request_api="create_cross_site_scripting_project")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="create_cross_site_scripting_project", uid=Uid)
                return JsonResponse({'message': "欧拉欧拉欧拉欧拉欧拉欧拉欧拉欧拉(๑•̀ㅂ•́)و✧", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_CrossSiteScriptMonitor_GenerateProject(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })