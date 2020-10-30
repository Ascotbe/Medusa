from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,Md5Encryption,GetImageFilePath
import json
import time
from config import forget_password_key,forgot_password_function_status
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
"""login
{
	"username": "ascotbe",
	"passwd": "1"
}
"""
def Login(request):#用户登录，每次登录成功都会刷新一次Token
    RequestLogRecord(request, request_api="login")
    if request.method == "POST":
        try:
            Username=json.loads(request.body)["username"]
            Passwd=json.loads(request.body)["passwd"]
            Md5Passwd=Md5Encryption().Md5Result(Passwd)#对密码加密
            UserLogin=UserInfo().UserLogin(Username,Md5Passwd)
            if UserLogin is None:
                return JsonResponse({'message': '账号或密码错误', 'code': 604, })

            else:
                while True:#如果查询确实冲突了
                    Token = randoms().result(250)
                    QueryTokenValidity = UserInfo().QueryTokenValidity(Token)#用来查询Token是否冲突了
                    if not QueryTokenValidity:#如果不冲突的话跳出循环
                        break
                UpdateToken=UserInfo().UpdateToken(name=Username, token=Token)#接着更新Token
                if UpdateToken:#如果更新成功了
                    Uid = UserInfo().QueryUidWithToken(Token)  # 查询UID
                    UserOperationLogRecord(request, request_api="login", uid=Uid)
                    return JsonResponse({'message': Token, 'code': 200, })
        except Exception as e:
            ErrorLog().Write("Web_Api_User_LogIn(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""update_password
{
	"username": "ascotbe",
	"old_passwd": "1",
	"new_passwd": "1111"
}
"""
def UpdatePassword(request):#更新密码
    RequestLogRecord(request, request_api="update_password")
    if request.method == "POST":
        try:
            UserName=json.loads(request.body)["username"]
            OldPasswd=json.loads(request.body)["old_passwd"]
            NewPasswd = json.loads(request.body)["new_passwd"]
            Md5NewPasswd = Md5Encryption().Md5Result(NewPasswd)  # 对新密码加密
            Md5OldPasswd = Md5Encryption().Md5Result(OldPasswd)  # 对旧密码加密
            UpdatePassword=UserInfo().UpdatePasswd(name=UserName,old_passwd=Md5OldPasswd,new_passwd=Md5NewPasswd)
            if UpdatePassword:
                UserOperationLogRecord(request, request_api="update_password", uid=UserName)#如果修改成功写入数据库中
                return JsonResponse({'message': '好耶！修改成功~', 'code': 200, })
            else:
                return JsonResponse({'message': "输入信息有误重新输入", 'code': 404, })
        except Exception as e:
            ErrorLog().Write("Web_Api_User_UpdatePassword(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""update_show_name
{
	"token": "xxxxx",
	"new_show_name": "1"
}
"""
def UpdateShowName(request):#更新显示名字
    RequestLogRecord(request, request_api="update_show_name")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            NewShowName= json.loads(request.body)["new_show_name"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="update_show_name", uid=Uid)  # 查询到了在计入
                UpdateShowNameResult=UserInfo().UpdateShowName(uid=Uid,show_name=NewShowName)#获取值查看是否成功
                if UpdateShowNameResult:
                    return JsonResponse({'message': '好诶！修改成功~', 'code': 200, })
                else:
                    return JsonResponse({'message': "输入信息有误重新输入", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Api_User_UpdateShowName(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""update_key
{
	"token": "xxxxx"
}
"""
def UpdateKey(request):#更新Key
    RequestLogRecord(request, request_api="update_key")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            NewKey= randoms().result(40)#生成随机的key,有可能会重复，这边先暂时不管了，这概论太j8低了
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="update_key", uid=Uid)  # 查询到了在计入
                UpdateKeyResult=UserInfo().UpdateKey(uid=Uid,key=NewKey)#获取值查看是否成功
                if UpdateKeyResult:
                    return JsonResponse({'message': '呐呐呐呐！修改成功了呢~', 'code': 200, })
                else:
                    return JsonResponse({'message': "输入信息有误重新输入", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Api_User_UpdateKey(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

#还差更新邮箱和更新头像功能

"""user_info
{
	"token": ""
}
"""
def PersonalInformation(request):#用户个人信息
    RequestLogRecord(request, request_api="user_info")
    if request.method == "POST":
        try:
            Token=json.loads(request.body)["token"]
            Info=UserInfo().QueryUserInfo(Token)
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询用户名
            if Info is None:
                return JsonResponse({'message': '搁着闹呢？', 'code': 404, })
            elif Info != None and Uid!=None:
                UserOperationLogRecord(request, request_api="user_info", uid=Uid)
                JsonValues = {}#对数据进行二次处理
                JsonValues["id"] = Info["id"]
                JsonValues["key"] = Info["key"]
                JsonValues["name"] = Info["name"]
                JsonValues["token"] = Info["token"]
                JsonValues["show_name"] = Info["show_name"]
                JsonValues["email"] = Info["email"]
                JsonValues["avatar"] = Info["avatar"]
                return JsonResponse({'message': JsonValues, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })


        except Exception as e:
            ErrorLog().Write("Web_Api_User_PersonalInformation(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


"""upload_avatar
POST /api/upload_avatar/ HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryaFtQbWz7pBzNgCOv
token:XXXXXXXXXXXXXXXX

------WebKitFormBoundaryaFtQbWz7pBzNgCOv
Content-Disposition: form-data; name="file"; filename="test.jpeg"
Content-Type: image/jpeg

XXXXXXXXXXXXXXX
------WebKitFormBoundaryaFtQbWz7pBzNgCOv--
"""
def UploadAvatar(request):#文件上传功能
    RequestLogRecord(request, request_api="upload_avatar")
    Token =request.headers["token"]
    if request.method == "POST":
        try:
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="upload_avatar", uid=Uid)  # 查询到了在计入
                PictureData = request.FILES.get('file', None)#获取文件数据
                if 10240<PictureData.size:#最大值10MB，最小值10KB
                    SaveFileName=randoms().result(10)+str(int(time.time()))+".jpg"#重命名文件
                    SaveRoute=GetImageFilePath().Result()+SaveFileName#获得保存路径
                    with open(SaveRoute, 'wb') as f:
                        for line in PictureData:
                            f.write(line)
                    UserInfo().UpdateAvatar(avatar=SaveFileName,uid=Uid)#图片写到本地后更新用户头像
                    return JsonResponse({'message': SaveFileName, 'code': 200,})#返回上传图片名称
                else:
                    return JsonResponse({'message': '它实在是太小了，莎酱真的一点感觉都没有o(TヘTo)',  'code': 603,})
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Api_User_UploadAvatar(def)", e)
            return JsonResponse({'message': '你不对劲！为什么报错了？',  'code': 169,})
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

"""forget_password
{
	"key": "",
	"name": "",
	"new_passwd": "",
	"email": "",
}
"""
def ForgetPassword(request):#忘记密码接口
    RequestLogRecord(request, request_api="forget_password")
    if request.method == "POST":
        try:
            Key = json.loads(request.body)["key"]
            Name = json.loads(request.body).get("name")
            NewPasswd = json.loads(request.body).get("new_passwd")
            Email = json.loads(request.body).get("email")
            if forgot_password_function_status:  # 查看状态是否关闭
                if Key==forget_password_key:#如果传入的key相等
                    Md5Passwd = Md5Encryption().Md5Result(NewPasswd)  # 进行加密
                    ChangePasswordResult=UserInfo().ForgetPassword(name=Name,new_passwd=Md5Passwd,email=Email)#进行修改密码
                    if ChangePasswordResult:#如果修改成功
                        return JsonResponse({'message': "修改成功啦~建议去配置文件中关闭忘记密码功能哦~", 'code': 200, })
                    else:
                        return JsonResponse({'message': "这个数据你是认真的嘛(。﹏。)", 'code': 503, })
                else:
                    return JsonResponse({'message': "大黑阔别乱搞，莎莎好怕怕(*/ω＼*)", 'code': 404, })
            else:
                return JsonResponse({'message': "小宝贝你没有开启忘记密码功能哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_Api_User_RequestLogRecord(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })

