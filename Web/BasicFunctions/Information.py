#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Web.DatabaseHub import UserInfo
from ClassCongregation import ErrorLog,Config,GetPath
from django.http import JsonResponse
import json
from Web.Workbench.LogRelated import RequestLogRecord,UserOperationLogRecord
import config
import requests
"""medusa_config_info
{
    "token": ""
}
"""
def ConfigInfo(request):#获取版本等信息
    RequestLogRecord(request, request_api="medusa_config_info")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None :  # 查到了UID
                UserOperationLogRecord(request, request_api="medusa_config_info", uid=Uid)
                Info=Config().Query()
                return JsonResponse({'message': Info, 'code': 200, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
            return JsonResponse({'message': '呐呐呐！莎酱被玩坏啦(>^ω^<)', 'code': 169, })
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })
"""medusa_config_update
{
	"token": "",
	"github_cve_monitor_job_time": 60,
	"github_cve_monitor_key": "CVE-20",
	"registration_function_status": true,
	"forgot_password_function_status": false,
	"secret_key_required_for_account_registration": "I_will_always_like_SoryuAsukaLangley",
	"forget_password_key": "I_will_always_like_KatsuragiMisato",
	"cross_site_script_uses_domain_names": "127.0.0.1:1234",
	"hardware_info_monitor_job_time": 20,
	"portable_execute_file_size": 20480,
	"domain_name_system_address": "dnslog.ascotbe.com",
	"nist_update_job_time": 7200,
	"nist_update_banner": false,
	"file_acquisition_size_max": 10240000,
	"request_log_record": false,
	"user_agent_browser_type": "chrome",
	"email_debug": false,
	"third_party_mail_host": "smtp.163.com",
	"third_party_mail_user": "ascotbe@163.com",
	"third_party_mail_pass": "hello_medusa",
	"email_bot": "",
	"ding_talk_bot_token": ""
}
"""
##经过测试celery启动的任务就无法自启动，也就是说修改定时任务相关配置只能重启celery才行，解决方案目前未知
def ConfigUpdate(request):#更新数据
    RequestLogRecord(request, request_api="medusa_config_update")
    if request.method == "POST":
        try:
            UserToken = json.loads(request.body)["token"]
            github_cve_monitor_job_time = json.loads(request.body)["github_cve_monitor_job_time"]
            github_cve_monitor_key = json.loads(request.body)["github_cve_monitor_key"]
            registration_function_status = json.loads(request.body)["registration_function_status"]
            forgot_password_function_status = json.loads(request.body)["forgot_password_function_status"]
            secret_key_required_for_account_registration = json.loads(request.body)["secret_key_required_for_account_registration"]
            forget_password_key = json.loads(request.body)["forget_password_key"]
            cross_site_script_uses_domain_names = json.loads(request.body)["cross_site_script_uses_domain_names"]
            hardware_info_monitor_job_time = json.loads(request.body)["hardware_info_monitor_job_time"]
            portable_execute_file_size = json.loads(request.body)["portable_execute_file_size"]
            domain_name_system_address = json.loads(request.body)["domain_name_system_address"]
            nist_update_job_time = json.loads(request.body)["nist_update_job_time"]
            nist_update_banner = json.loads(request.body)["nist_update_banner"]
            file_acquisition_size_max = json.loads(request.body)["file_acquisition_size_max"]
            request_log_record = json.loads(request.body)["request_log_record"]
            user_agent_browser_type = json.loads(request.body)["user_agent_browser_type"]
            email_debug = json.loads(request.body)["email_debug"]
            third_party_mail_host = json.loads(request.body)["third_party_mail_host"]
            third_party_mail_user = json.loads(request.body)["third_party_mail_user"]
            third_party_mail_pass = json.loads(request.body)["third_party_mail_pass"]
            email_bot = json.loads(request.body)["email_bot"]
            ding_talk_bot_token = json.loads(request.body)["ding_talk_bot_token"]
            Uid = UserInfo().QueryUidWithToken(UserToken)  # 如果登录成功后就来查询用户名
            if Uid != None :  # 查到了UID
                UserOperationLogRecord(request, request_api="medusa_config_update", uid=Uid)
                for i in [github_cve_monitor_job_time,hardware_info_monitor_job_time,portable_execute_file_size,nist_update_job_time,file_acquisition_size_max]:#判断数字类型数据
                    if isinstance(i, int) and (i is not None):
                        pass
                    else:
                        return JsonResponse({'message': "请传入正确的int类型", 'code': 503, })
                for x in [github_cve_monitor_key,secret_key_required_for_account_registration,forget_password_key,cross_site_script_uses_domain_names,domain_name_system_address,user_agent_browser_type,third_party_mail_host,third_party_mail_user,third_party_mail_pass,email_bot,ding_talk_bot_token]:# 判断字符串类型数据
                    if isinstance(x, str) and (x is not None):
                        pass
                    else:
                        return JsonResponse({'message': "请传入正确的str类型", 'code': 502, })
                for a in [registration_function_status,forgot_password_function_status,nist_update_banner,request_log_record,email_debug]:# 判断布尔类型数据
                    if isinstance(a, bool) and (a is not None):
                        pass
                    else:
                        return JsonResponse({'message': "请传入正确的bool类型", 'code': 504, })
                data = {
                    # 可以修改
                    "github_cve_monitor_job_time": github_cve_monitor_job_time,  # Github监控配置 60秒请求一次
                    "github_cve_monitor_key": github_cve_monitor_key,  # 监控的关键字
                    "registration_function_status": registration_function_status,  # 默认开启注册功能
                    "forgot_password_function_status": forgot_password_function_status,  # 默认关闭忘记密码功能
                    "secret_key_required_for_account_registration": secret_key_required_for_account_registration,
                    # 注册账号需要的秘钥,最好修改为250个随机字符串
                    "forget_password_key": forget_password_key,  # 修改密码所需要的key
                    "cross_site_script_uses_domain_names": cross_site_script_uses_domain_names,
                    # 这边填写你当前服务器的域名，IP也行包括端口，用户生成POC使用
                    "hardware_info_monitor_job_time": hardware_info_monitor_job_time,  # 机器硬件监控配置工作间隔
                    "portable_execute_file_size": portable_execute_file_size,  # WEB工具栏配置默认20M大小

                    "domain_name_system_address": domain_name_system_address,  # 用户用来接收数据的DNSLOG域名

                    "nist_update_job_time": nist_update_job_time,  # Nist数据配置工作间隔，网站每2小时更新一次数据
                    "nist_update_banner": nist_update_banner,  # 是否开启下载横幅提示，默认关闭
                    "file_acquisition_size_max": file_acquisition_size_max,  # 文件获取相关，文件接收最大值，过大文件不接受,默认文件100M
                    "request_log_record": request_log_record,  # 请求日志，默认关闭，记录请求完整数据，开启的话会记录完整的数据到数据库中，包括巨大的上传包也会写入
                    "user_agent_browser_type": user_agent_browser_type,  # 目前只支持如下浏览器，修改为其他的可能会导致无法使用。
                    # firefox、ie、msie、opera、chrome、AppleWebKit、Gecko、safari
                    "email_debug": email_debug,  # 是否开启测试模式，用户不必开启
                    "third_party_mail_host": third_party_mail_host,  # 设置第三方服务器
                    "third_party_mail_user": third_party_mail_user,  # 第三方用户名
                    "third_party_mail_pass": third_party_mail_pass,  # 第三方口令
                    "email_bot": email_bot,  # 消息推送邮件
                    "ding_talk_bot_token": ding_talk_bot_token  # 消息推送，钉钉密钥
                }
                Re=Config().Update(data=str(data))
                if Re:
                    ConfigData=Config().Query()
                    all_data = dict(ConfigData["data"], **ConfigData["fixed_data"])  # 合并数据
                    file_data = ""
                    for x in all_data:
                        if isinstance(all_data[x], int) or isinstance(all_data[x], bool):
                            # print(x + " = " + str(all_data[x]) + "\n")
                            file_data += x + " = " + str(all_data[x]) + "\n"
                        elif isinstance(all_data[x], str):
                            # print(x + " = " + "\"" + all_data[x] + "\"\n")
                            file_data += x + " = " + "\"" + all_data[x] + "\"\n"
                    f = open(GetPath().ConfigPath() + "config.py", "w+")
                    f.write(file_data)
                    f.close()
                    return JsonResponse({'message': "更新成功", 'code': 200, })
                else:
                    return JsonResponse({'message': "更新失败", 'code': 501, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write(e)
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
        ErrorLog().Write(e)
        return JsonResponse({'message': '自己去看报错日志！', 'code': 169, })


