#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo
from ClassCongregation import ErrorLog
from django.http import JsonResponse
import json
from Web.Workbench.LogRelated import RequestLogRecord,UserOperationLogRecord
import config
import requests
"""medusa_info
{
    "token": ""
}
"""

info={
    "version":config.version,#版本号
    "latest_version":"https://github.com/Ascotbe/Medusa/releases",#最新版本
    "official_documentation":"https://medusa.ascotbe.com/",#官方文档
    "registration_function_status":config.registration_function_status,#注册功能状态
    "forgot_password_function_status":config.forgot_password_function_status,#忘记密码状态
    "cross_site_script_uses_domain_names":
    {
        "state":False,
        "value":config.cross_site_script_uses_domain_names
    },#XSS域名配置
    "domain_name_system_address":
    {
        "state":False,
        "value":config.domain_name_system_address
    },#DNSLOG域名配置
    "local_mail_host":
     {
        "state":False,
        "value":config.local_mail_host
    }# 自建邮件服务
}
def Config(request):#获取版本等信息
    RequestLogRecord(request, request_api="medusa_info")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None :  # 查到了UID
                UserOperationLogRecord(request, request_api="delete_cross_site_script_project", uid=Uid)
                if config.cross_site_script_uses_domain_names!="127.0.0.1:1234":
                    info["cross_site_script_uses_domain_names"]["state"]=True
                if config.domain_name_system_address!="dnslog.ascotbe.com":
                    info["domain_name_system_address"]["state"]=True
                if config.local_mail_host!="smtp.ascotbe.com":
                    info["local_mail_host"]["state"]=True
                return JsonResponse({'message': info, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_BasicFunctions_Information_Config(def)", e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


def Update(request):#更新版本

    try:
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        }
        GitApi = requests.get("https://api.github.com/repos/ascotbe/medusa/releases/latest",
            headers=headers, timeout=10)
        GitApiJson = json.loads(GitApi.text)
        LatestVersion = GitApiJson["tag_name"]
        #不用类型转换，字符串就能毕竟大小，离谱
        if config.version[1:]<LatestVersion[1:]:
            return JsonResponse({'message': "发现最新版本！", 'code': 200, })
        else:
            return JsonResponse({'message': "已经是最新版本了！", 'code': 200, })

    except Exception as e:
        ErrorLog().Write("Web_CVE_GithubMonitoring_Github_Monitor(def)", e)

