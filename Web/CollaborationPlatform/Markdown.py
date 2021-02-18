from Web.WebClassCongregation import UserInfo,MarkdownRelationship,MarkdownInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,GetImageFilePath
import json
import base64
import difflib
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import time
"""join_markdown_project
{
	"token": "xxxx",
    "markdown_project_invitation_code": "xxx"
}
"""
def JoinMarkdownProject(request):#通过邀请码加入项目
    RequestLogRecord(request, request_api="join_markdown_project")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            MarkdownProjectInvitationCode = json.loads(request.body)["markdown_project_invitation_code"]#传入邀请码
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if len(MarkdownProjectInvitationCode)==50:#判断邀请码的长度是否为50
                if Uid != None:  # 查到了UID
                    UserOperationLogRecord(request, request_api="join_markdown_project", uid=Uid)
                    #通过邀请码查询信息后写入到数据库中
                    ProjectInformation=MarkdownRelationship().InvitationCodeToQueryProjectInformation(markdown_project_invitation_code=MarkdownProjectInvitationCode)[0]#返回项目信息
                    if ProjectInformation!=None:#判断是否为空，也就是说查不到内容，或者报错了
                        if Uid!=ProjectInformation["uid"]:#判断是否是自己邀请自己
                            #还需要一个判断是否已经加入项目
                            if MarkdownRelationship().DetectionOfRepeatedAddition(markdown_name=ProjectInformation["markdown_name"],uid=Uid):#判断是否已经加入了

                                return JsonResponse({'message': "你已经加入过项目啦~拉卡拉卡~", 'code': 502, })
                            else:
                                MarkdownRelationship().Write(markdown_name=ProjectInformation["markdown_name"], uid=Uid,
                                                         markdown_project_name=ProjectInformation["markdown_project_name"],
                                                         markdown_project_owner="0",
                                                         markdown_project_invitation_code="")
                            return JsonResponse({'message': "加入项目成功啦~咕噜咕噜~", 'code': 200, })
                        else:
                            return JsonResponse({'message': "这就是你的项目，瞎鸡儿加个啥", 'code': 503, })
                    else:
                        return JsonResponse({'message': "小宝贝不要调皮哦(⊙x⊙;)", 'code': 404, })
                else:
                    return JsonResponse({'message': "小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
            else:
                return JsonResponse({'message': "小宝贝邀请码的长度不合规哦Σ(っ °Д °;)っ", 'code': 501, })
        except Exception as e:
            ErrorLog().Write("Web_CollaborationPlatform_Markdown_JoinMarkdownProject(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

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
            MarkdownProjectName = json.loads(request.body)["markdown_project_name"]#传入项目名称
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="create_markdown_project", uid=Uid)
                while True:  # 用来生成markdown文件名，防止重复
                    MarkdownName=randoms().result(250)#markdown文件名，随机生成
                    CheckName=MarkdownRelationship().CheckConflict(markdown_name=MarkdownName)
                    if not CheckName:  # 如果不冲突的话跳出循环
                        break
                while True: # 用来生成邀请码，防止重复
                    MarkdownProjectInvitationCode=randoms().result(50)#邀请码
                    CheckInvitationCode=MarkdownRelationship().CheckInvitationCode(MarkdownProjectInvitationCode=MarkdownProjectInvitationCode)
                    if not CheckInvitationCode:  # 如果不冲突的话跳出循环
                        break
                MarkdownRelationship().Write(markdown_name=MarkdownName,uid=Uid,markdown_project_name=MarkdownProjectName,markdown_project_owner="1",markdown_project_invitation_code=MarkdownProjectInvitationCode)
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
            ErrorLog().Write("Web_CollaborationPlatform_Markdown_QueryMarkdownProject(def)", e)
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
            ErrorLog().Write("Web_CollaborationPlatform_Markdown_SaveMarkdownData(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""query_markdown_data
{
	"token": "xxxx",
	"markdown_name": "xxx"
}
"""
def QueryMarkdownData(request):#用来查询协同作战数据
    RequestLogRecord(request, request_api="query_markdown_data")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            MarkdownName = json.loads(request.body)["markdown_name"]#传入文档名称
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="query_markdown_data", uid=Uid)
                CheckPermissionsResult=MarkdownRelationship().CheckPermissions(markdown_name=MarkdownName,uid=Uid)#检查是否有权限，也就是说这个项目是否属于该用户
                if CheckPermissionsResult:#如果属于该用户
                    CheckConflictResult=MarkdownInfo().CheckConflict(markdown_name=MarkdownName)#检查数据库这个文件是否存在
                    if CheckConflictResult:#如果文件已经有数据了
                        MarkdownInfoResult=MarkdownInfo().Query(markdown_name=MarkdownName)#文件数据查询
                        return JsonResponse({'message': MarkdownInfoResult, 'code': 200, })
                    else:#如果没有数据

                        return JsonResponse({'message': "", 'code': 200, })
                else:
                    return JsonResponse({'message': "小朋友不是你的东西别乱动哦~~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CollaborationPlatform_Markdown_QueryMarkdownData(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""markdown_image_upload
POST /api/markdown_image_upload/ HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryaFtQbWz7pBzNgCOv
token:XXXXXXXXXXXXXXXX

------WebKitFormBoundaryaFtQbWz7pBzNgCOv
Content-Disposition: form-data; name="file"; filename="test.jpeg"
Content-Type: image/jpeg

XXXXXXXXXXXXXXX
------WebKitFormBoundaryaFtQbWz7pBzNgCOv--
"""
def MarkdownImageUpload (request):#md文档专有上传位置
    RequestLogRecord(request, request_api="markdown_image_upload")
    Token =request.headers["token"]
    if request.method == "POST":
        try:
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="markdown_image_upload", uid=Uid)  # 查询到了在计入
                PictureData = request.FILES.get('file', None)#获取文件数据
                if 1024<PictureData.size:#最小值1KB
                    SaveFileName=randoms().result(50)+str(int(time.time()))+".jpg"#重命名文件
                    SaveRoute=GetImageFilePath().Result()+SaveFileName#获得保存路径
                    with open(SaveRoute, 'wb') as f:
                        for line in PictureData:
                            f.write(line)
                    return JsonResponse({'message': SaveFileName, 'code': 200,})#返回上传图片名称
                else:
                    return JsonResponse({'message': '它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)',  'code': 603,})
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CollaborationPlatform_Markdown_MarkdownImageUpload(def)", e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""markdown_data_comparison
{
	"token": "xxxx",
	"new_markdown_data": "xxxx",
	"markdown_name": "xxx"
}
"""
def MarkdownDataComparison (request):#md文档数据对比
    RequestLogRecord(request, request_api="markdown_data_comparison")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            MarkdownData = json.loads(request.body)["new_markdown_data"]#传入新文本数据
            MarkdownName = json.loads(request.body)["markdown_name"]  # 传入文档名称
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="markdown_data_comparison", uid=Uid)
                CheckPermissionsResult=MarkdownRelationship().CheckPermissions(markdown_name=MarkdownName,uid=Uid)#检查是否有权限，也就是说这个项目是否属于该用户
                if CheckPermissionsResult:#如果属于该用户

                    MarkdownDataResult=MarkdownInfo().QueryMarkdownData(markdown_name=MarkdownName)#文件数据查询
                    if MarkdownDataResult==None:
                        MarkdownDataResult=""#如果数据库中无数据
                    OldMarkdownData=base64.b64decode(str(MarkdownDataResult).encode('utf-8')).decode('utf-8').splitlines()
                    NewMarkdownData=MarkdownData.splitlines()
                    ComparisonResult=difflib.HtmlDiff().make_file(OldMarkdownData,NewMarkdownData)#对比结果
                    return JsonResponse({'message': ComparisonResult, 'code': 200, })

                else:
                    return JsonResponse({'message': "小朋友不是你的东西别乱动哦~~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_CollaborationPlatform_Markdown_MarkdownDataComparison(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


#数据对比函数，以及关系表中多人相关数据