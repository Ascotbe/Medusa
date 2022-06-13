#!/usr/bin/env python
# -*- coding: utf-8 -*-
############
#关于页面配置#
############
version="v1.0.101"


###########
#DNSLOG配置#
###########
#默认使用的是dnslog.cn模式
dnslog_name="dnslog.cn"#切换使用那个dnslog

#################
#Debug模式切换位置#
#################
debug_mode=False#如果自行搭建web版，请改为Ture，这样会快很多

##############
#线程数配置位置#
##############
thread_number=15 #默认线程数，线程最好别开太大容易被发现
thread_timeout_number=5#防止报错等操作导致的超时

#################
#requests请求配置#
#################
user_agent_randomization=False#是否开启headers头中的随机化，默认关闭
user_agent_browser_type="chrome"#目前只支持如下浏览器，修改为其他的可能会导致无法使用。
                                #firefox、ie、msie、opera、chrome、AppleWebKit、Gecko、safari
#默认请求头，里面保存必须数据，User-Agent头数据如果开启随机化会改变
#WEB版加个判断，如果用户传入header会对该header进行覆盖
headers={
    "Connection": "close",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "dnt": "1"
}
proxies=None
#如果想要使用代码把下面注释打开，填上你代理的值
# proxies = {
#   "http": "http://127.0.0.1:8080",
#   "https": "https://127.0.0.1:8080",
# }


##########
#Redis配置# <---------------（必须修改
##########
redis_host="localhost"#连接redis的地址，默认本地
redis_port="6379"#redis连接端口，默认6379
redis_db="6"#连接的数据库，默认为6
redis_password="I_will_always_like_AyanamiRei"#连接redis的密码


############
#端口扫描配置#
############
port_threads_number=20#端口扫描默认线程
port_timeout_period=2#端口扫描默认超时时间

###############
#Github监控配置#
###############
github_cve_monitor_job_time=60#60秒请求一次
github_cve_monitor_key="CVE-20"#监控的关键字


############
#代理扫描配置#
############
agent_scan_interval=3600#默认间隔1小时
proxy_scan_process=5#代理扫描进程数
proxy_scanned_by_proxy=None#代理扫描挂的代理默认为空，如果想用代理参考格式："127.0.0.1：8080"
proxy_scan_module_list=["Struts2","Confluence","Nginx","PHPStudy","Jenkins","Harbor","Rails","Kibana","Citrix","Mongo","Spring","FastJson","Windows","Liferay","Shiro","Flink","Log4j","ActiveMQ","Solr","Tomcat","Ruvar","Seeyou","Tongda","Weaver","Weblogic"]#代理扫描模块列表默认不添加子域名发现和CMS扫描还有信息探测功能

###############
#账号密码相关配置# <---------------（必须修改
###############
registration_function_status=True#默认开启注册功能
forgot_password_function_status=False#默认关闭忘记密码功能
secret_key_required_for_account_registration="I_will_always_like_SoryuAsukaLangley"#注册账号需要的秘钥,最好修改为250个随机字符串
forget_password_key="I_will_always_like_KatsuragiMisato"#修改密码所需要的key

############
#XSS项目配置#
############
cross_site_script_uses_domain_names="127.0.0.1:1234"#这边填写你当前服务器的域名，IP也行包括端口，用户生成POC使用


###############
#机器硬件监控配置#
###############
hardware_info_monitor_job_time=20#工作间隔


#############
#WEB工具栏配置#
#############
portable_execute_file_size=20480 #默认20M大小


###########
#DNSLOG配置# <---------------（必须修改
###########
domain_name_system_address="dnslog.ascotbe.com" #用户用来接收数据的DNSLOG域名


#############
#Nist数据配置#
#############
nist_update_job_time=7200#工作间隔，网站每2小时更新一次数据
nist_update_banner=False#是否开启下载横幅提示，默认关闭

###############
#钓鱼邮箱邮件配置# <---------------（必须修改
###############
email_test=False#测试用163
third_party_mail_host = "smtp.163.com"  # 设置第三方服务器
third_party_mail_user = "ascotbe@163.com"  # 第三方用户名
third_party_mail_pass = "hello_medusa"  #第三方口令

local_mail_host= "smtp.ascotbe.com"# 设本地的服务器
local_mail_user= "ascotbe@ascotbe.com" # 用户名

############
#文件获取相关#
############
file_acquisition_size_max=10240000 #文件接收最大值，过大文件不接受,默认文件100M

###########
#服务器相关# <---------------（必须修改
##########
server_ip="192.168.1.1" #填写你服务器的IP值

#########
#请求日志#
#########
#默认关闭，记录请求完整数据，开启的话会记录完整的数据到数据库中
#包括巨大的上传包也会写入
request_log_record=False