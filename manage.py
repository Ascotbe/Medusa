#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Django's command-line utility for administrative tasks."""
import os
import sys
from ClassCongregation import Config
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Web.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def InitialConfiguration():  # 先判断是否有数据，如果没有就写入并生成config文件，如果有就pass
    if Config().Statistics():#如果没有数据

        data = {
            # 可以修改
            "github_cve_monitor_job_time": 60,  # Github监控配置 60秒请求一次
            "github_cve_monitor_key": "CVE-20",  # 监控的关键字
            "registration_function_status": True,  # 默认开启注册功能
            "forgot_password_function_status": False,  # 默认关闭忘记密码功能
            "secret_key_required_for_account_registration": "I_will_always_like_SoryuAsukaLangley",
            # 注册账号需要的秘钥,最好修改为250个随机字符串
            "forget_password_key": "I_will_always_like_KatsuragiMisato",  # 修改密码所需要的key
            "cross_site_script_uses_domain_names": "127.0.0.1:1234",  # 这边填写你当前服务器的域名，IP也行包括端口，用户生成POC使用
            "hardware_info_monitor_job_time": 20,  # 机器硬件监控配置工作间隔
            "portable_execute_file_size": 20480,  # WEB工具栏配置默认20M大小

            "domain_name_system_address": "dnslog.ascotbe.com",  # 用户用来接收数据的DNSLOG域名

            "nist_update_job_time": 7200,  # Nist数据配置工作间隔，网站每2小时更新一次数据
            "nist_update_banner": False,  # 是否开启下载横幅提示，默认关闭
            "file_acquisition_size_max": 10240000,  # 文件获取相关，文件接收最大值，过大文件不接受,默认文件100M
            "request_log_record": False,  # 请求日志，默认关闭，记录请求完整数据，开启的话会记录完整的数据到数据库中，包括巨大的上传包也会写入
            "user_agent_browser_type": "chrome",  # 目前只支持如下浏览器，修改为其他的可能会导致无法使用。
            # firefox、ie、msie、opera、chrome、AppleWebKit、Gecko、safari
            "email_debug": False,  # 是否开启测试模式，用户不必开启
            "third_party_mail_host": "smtp.163.com",  # 设置第三方服务器
            "third_party_mail_user": "ascotbe@163.com",  # 第三方用户名
            "third_party_mail_pass": "hello_medusa",  # 第三方口令
            "bot_email": "",  # 消息推送邮件
            "ding_talk_bot_token": ""  # 消息推送，钉钉密钥
        }
        fixed_data = {  # 禁止修改
            "version": "v1.0.159",  # 版本号
            "redis_host": "localhost",  # 连接redis的地址，默认本地
            "redis_port": "6379",  # redis连接端口，默认6379
            "redis_db": "6",  # 连接的数据库，默认为6
            "redis_password": "I_will_always_like_AyanamiRei",  # 连接redis的密码
            "server_ip": "192.168.1.1",  # 填写你服务器的IP值
            "local_mail_host": "smtp.ascotbe.com",  # 设本地的邮件服务器
            "local_mail_user": "ascotbe@ascotbe.com",  # 设本地的邮件用户名
        }
        Config().Write(fixed_data=fixed_data,data=data)
        all_data = dict(data, **fixed_data)#合并数据
        file_data = ""
        for x in all_data:
            if isinstance(all_data[x], int) or isinstance(all_data[x], bool):
                #print(x + " = " + str(all_data[x]) + "\n")
                file_data+=x + " = " + str(all_data[x]) + "\n"
            elif isinstance(all_data[x], str):
                #print(x + " = " + "\"" + all_data[x] + "\"\n")
                file_data +=x + " = " + "\"" + all_data[x] + "\"\n"
        f=open("config.py","w+")
        f.write(file_data)
        f.close()


if __name__ == '__main__':
    main()




