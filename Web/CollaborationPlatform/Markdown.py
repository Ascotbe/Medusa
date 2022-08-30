#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo,MarkdownRelationship,MarkdownInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,GetPath
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
            token = json.loads(request.body)["token"]
            markdown_project_invitation_code = json.loads(request.body)["markdown_project_invitation_code"]#传入邀请码
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if len(markdown_project_invitation_code)==50:#判断邀请码的长度是否为50
                if uid != None:  # 查到了UID
                    UserOperationLogRecord(request, request_api="join_markdown_project", uid=uid)
                    #通过邀请码查询信息后写入到数据库中
                    project_information=MarkdownRelationship().InvitationCodeToQueryProjectInformation(markdown_project_invitation_code=markdown_project_invitation_code)[0]#返回项目信息
                    if project_information!=None:#判断是否为空，也就是说查不到内容，或者报错了
                        if uid!=project_information["uid"]:#判断是否是自己邀请自己
                            #还需要一个判断是否已经加入项目
                            if MarkdownRelationship().DetectionOfRepeatedAddition(markdown_name=project_information["markdown_name"],uid=uid):#判断是否已经加入了

                                return JsonResponse({'message': "你已经加入过项目啦~拉卡拉卡~", 'code': 502, })
                            else:
                                MarkdownRelationship().Write(markdown_name=project_information["markdown_name"], uid=uid,
                                                         markdown_project_name=project_information["markdown_project_name"],
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
            ErrorLog().Write(e)
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
            token = json.loads(request.body)["token"]
            markdown_project_name = json.loads(request.body)["markdown_project_name"]#传入项目名称
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="create_markdown_project", uid=uid)
                while True:  # 用来生成markdown文件名，防止重复
                    markdown_name=randoms().result(250)#markdown文件名，随机生成
                    check_name=MarkdownRelationship().CheckConflict(markdown_name=markdown_name)
                    if not check_name:  # 如果不冲突的话跳出循环
                        break
                while True: # 用来生成邀请码，防止重复
                    markdown_project_invitation_code=randoms().result(50)#邀请码
                    check_invitation_ode=MarkdownRelationship().CheckInvitationCode(MarkdownProjectInvitationCode=markdown_project_invitation_code)
                    if not check_invitation_ode:  # 如果不冲突的话跳出循环
                        break
                MarkdownRelationship().Write(markdown_name=markdown_name,
                                             uid=uid,
                                             markdown_project_name=markdown_project_name,
                                             markdown_project_owner="1",
                                             markdown_project_invitation_code=markdown_project_invitation_code)
                return JsonResponse({'message': "创建成功啦~玛卡玛卡~", 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""query_markdown_project
{
	"token": "xxxx",
	"number_of_pages":"1"
}
"""
def QueryMarkdownProject(request):#用来查询用户所有的项目信息
    RequestLogRecord(request, request_api="query_markdown_project")
    if request.method == "POST":
        try:
            token = json.loads(request.body)["token"]
            number_of_pages = json.loads(request.body)["number_of_pages"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="query_markdown_project", uid=uid)

                result=MarkdownRelationship().Query(uid=uid,number_of_pages=int(number_of_pages))#查询的结果返回
                return JsonResponse({'message': result, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""markdown_project_statistical
{
	"token": "xxx"
}
"""

def MarkdownProjectStatistical(request):#统计文档数据
    RequestLogRecord(request, request_api="markdown_project_statistical")
    if request.method == "POST":
        try:
            token=json.loads(request.body)["token"]
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="markdown_project_statistical", uid=uid)
                number=MarkdownRelationship().QueryStatistics(uid=uid)#获取当前用户的个数
                return JsonResponse({'message': number, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': "呐呐呐！莎酱被玩坏啦(>^ω^<)", 'code': 169, })

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
            token = json.loads(request.body)["token"]
            markdown_data = json.loads(request.body)["markdown_data"]#传入保存的数据
            markdown_name = json.loads(request.body)["markdown_name"]#传入文档名称
            bast64_data=base64.b64encode(str(markdown_data).encode('utf-8')).decode('utf-8')#转换成base64的数据
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="save_markdown_data", uid=uid)
                CheckPermissionsResult=MarkdownRelationship().CheckPermissions(markdown_name=markdown_name,uid=uid)#检查是否有权限，也就是说这个项目是否属于该用户
                if CheckPermissionsResult:#如果属于该用户
                    CheckConflictResult=MarkdownInfo().CheckConflict(markdown_name=markdown_name)#检查数据库这个文件是否存在
                    if CheckConflictResult:#如果文件已经有数据了
                        if not MarkdownInfo().Update(markdown_name=markdown_name,markdown_data=bast64_data):#就对数据进行更新，接着判断更新返回值
                            return JsonResponse({'message': "保存失败~玛卡巴卡~~", 'code': 503, })
                    else:#如果没有数据
                        MarkdownInfo().Write(markdown_name=markdown_name,markdown_data=bast64_data)#就对数据进行写入
                    return JsonResponse({'message': "保存成功啦~阿巴阿巴~", 'code': 200, })
                else:
                    return JsonResponse({'message': "小朋友不是你的东西别乱动哦~~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
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
            token = json.loads(request.body)["token"]
            markdown_name = json.loads(request.body)["markdown_name"]#传入文档名称
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="query_markdown_data", uid=uid)
                CheckPermissionsResult=MarkdownRelationship().CheckPermissions(markdown_name=markdown_name,uid=uid)#检查是否有权限，也就是说这个项目是否属于该用户
                if CheckPermissionsResult:#如果属于该用户
                    CheckConflictResult=MarkdownInfo().CheckConflict(markdown_name=markdown_name)#检查数据库这个文件是否存在
                    if CheckConflictResult:#如果文件已经有数据了
                        MarkdownInfoResult=MarkdownInfo().Query(markdown_name=markdown_name)#文件数据查询
                        return JsonResponse({'message': MarkdownInfoResult, 'code': 200, })
                    else:#如果没有数据

                        return JsonResponse({'message': "", 'code': 200, })
                else:
                    return JsonResponse({'message': "小朋友不是你的东西别乱动哦~~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
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
    token =request.headers["token"]
    if request.method == "POST":
        try:
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询UID
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="markdown_image_upload", uid=uid)  # 查询到了在计入
                picture_data = request.FILES.get('file', None)#获取文件数据
                if 1024<picture_data.size:#最小值1KB
                    save_file_name=randoms().result(50)+str(int(time.time()))+".jpg"#重命名文件
                    save_route=GetPath().ImageFilePath()+save_file_name#获得保存路径
                    with open(save_route, 'wb') as f:
                        for line in picture_data:
                            f.write(line)
                    return JsonResponse({'message': save_file_name, 'code': 200,})#返回上传图片名称
                else:
                    return JsonResponse({'message': '它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)',  'code': 603,})
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
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
            token = json.loads(request.body)["token"]
            new_markdown_data = json.loads(request.body)["new_markdown_data"]#传入新文本数据
            markdown_name = json.loads(request.body)["markdown_name"]  # 传入文档名称
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="markdown_data_comparison", uid=uid)
                permissions_result=MarkdownRelationship().CheckPermissions(markdown_name=markdown_name,uid=uid)#检查是否有权限，也就是说这个项目是否属于该用户
                if permissions_result:#如果属于该用户

                    result=MarkdownInfo().QueryMarkdownData(markdown_name=markdown_name)#文件数据查询
                    if result==None:
                        result=""#如果数据库中无数据
                    old_data=base64.b64decode(str(result).encode('utf-8')).decode('utf-8').splitlines()
                    new_data=new_markdown_data.splitlines()
                    comparison_result=difflib.HtmlDiff().make_file(old_data,new_data)#对比结果
                    return JsonResponse({'message': comparison_result, 'code': 200, })

                else:
                    return JsonResponse({'message': "小朋友不是你的东西别乱动哦~~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })



"""delete_markdown
{
	"token": "xxxx",
	"markdown_name": "xxx"
}
"""
def DeleteMarkdown (request):#删除文档项目
    RequestLogRecord(request, request_api="delete_markdown")
    if request.method == "POST":
        try:
            token = json.loads(request.body)["token"]
            markdown_name = json.loads(request.body)["markdown_name"]  # 传入文档名称
            uid = UserInfo().QueryUidWithToken(token)  # 如果登录成功后就来查询用户名
            if uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="delete_markdown", uid=uid)
                project_belongs_result=MarkdownRelationship().ProjectBelongs(markdown_name=markdown_name,uid=uid)#检查是否有权限，也就是说这个项目是否属于该用户
                if project_belongs_result:#检查项目所属
                    result=MarkdownRelationship().Delete(markdown_name=markdown_name,uid=uid)#删除表格
                    if not result:
                        return JsonResponse({'message': "项目删除错误", 'code': 171, })
                    else:
                        MarkdownInfo().Delete(markdown_name=markdown_name)  # 删除数据，有可能会有空数据的情况
                        return JsonResponse({'message': "项目删除成功~", 'code': 200, })
                else:
                    return JsonResponse({'message': "小朋友不是你的东西别乱动哦~~", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法操作哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

#数据对比函数，以及关系表中多人相关数据