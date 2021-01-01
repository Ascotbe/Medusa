from Web.WebClassCongregation import UserInfo,MarkdownRelationship,MarkdownInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms
import json
import base64
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""create_markdown_project
{
	"token": "xxxx",
    "markdown_project_name": "xxx"
}
"""
def CreateMarkdownProject(request):#用来创建markdown项目,目前只支持单用户，先用于测试
    RequestLogRecord(request, request_api="create_markdown_project")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            MarkdownProjectName = json.loads(request.body)["markdown_project_name"]#传入需要修改的模板名称
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="create_markdown_project", uid=Uid)
                while True:  # 如果查询确实冲突了
                    MarkdownName=randoms().result(250)#markdown文件名，随机生成
                    CheckName=MarkdownRelationship().CheckConflict(markdown_name=MarkdownName)
                    if not CheckName:  # 如果不冲突的话跳出循环
                        break
                MarkdownRelationship().Write(markdown_name=MarkdownName,uid=Uid,markdown_project_name=MarkdownProjectName)
                return JsonResponse({'message': "创建成功啦~玛卡玛卡~", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CollaborationPlatform_Markdown_CreateMarkdownProject(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""query_markdown_project
{
	"token": "xxxx"
}
"""
def QueryMarkdownProject(request):#用来查询用户所有的项目信息
    RequestLogRecord(request, request_api="query_markdown_project")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="query_markdown_project", uid=Uid)

                QueryResult=MarkdownRelationship().Query(uid=Uid)#查询的结果返回
                return JsonResponse({'message': QueryResult, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CollaborationPlatform_Markdown_CreateMarkdownProject(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""save_markdown_data
{
	"token": "xxxx",
	"markdown_data": "xxx",
	"markdown_name": "xxx"
}
"""
def SaveMarkdownData(request):#用来保存协同作战数据
    RequestLogRecord(request, request_api="save_markdown_data")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            MarkdownData = json.loads(request.body)["markdown_data"]#传入保存的数据
            MarkdownName = json.loads(request.body)["markdown_name"]#传入文档名称
            MarkdownDataToBast64=base64.b64encode(str(MarkdownData).encode('utf-8')).decode('utf-8')#转换成base64的数据
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="save_markdown_data", uid=Uid)
                CheckPermissionsResult=MarkdownRelationship().CheckPermissions(markdown_name=MarkdownName,uid=Uid)#检查是否有权限，也就是说这个项目是否属于该用户
                if CheckPermissionsResult:#如果属于该用户
                    CheckConflictResult=MarkdownInfo().CheckConflict(markdown_name=MarkdownName)#检查数据库这个文件是否存在
                    if CheckConflictResult:#如果文件已经有数据了
                        if not MarkdownInfo().Update(markdown_name=MarkdownName,markdown_data=MarkdownDataToBast64):#就对数据进行更新，接着判断更新返回值
                            return JsonResponse({'message': "保存失败~玛卡巴卡~~", 'code': 503, })
                    else:#如果没有数据
                        MarkdownInfo().Write(markdown_name=MarkdownName,markdown_data=MarkdownDataToBast64)#就对数据进行写入
                    return JsonResponse({'message': "保存成功啦~阿巴阿巴~", 'code': 200, })
                else:
                    return JsonResponse({'message': "小朋友不是你的东西别乱动哦~~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CollaborationPlatform_Markdown_CreateMarkdownProject(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

#数据对比函数，以及关系表中多人相关数据