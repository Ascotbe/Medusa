#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from Web.BasicFunctions import VulnerabilityScanning,VulnerabilityQuery,GenerateReport,ProxyScan
from Web.BasicFunctions import Registered,User,Home,VerificationCode,Information
from Web.CrossSiteScriptHub import CrossSiteScript,TemplateManagement
from Web.SystemInfo import HardwareInfo
from Web.CVE.GithubMonitoring import Github
from Web.CVE.NistMonitoring import Nist
from Web.ToolsUtility.AntivirusSoftwareMatching import AntivirusSoftware
from Web.ToolsUtility.BinaryAnalysis import PortableExecute
#from Web.ApplicationCollection import CollectionWork
from Web.CollaborationPlatform import Markdown
from Web.DomainNameSystemLog import Data
from Web.TrojanOrVirus import TrojanInterface
from Web.Email import EmailProject,Attachment,ReceiveData,Graph,EmailList
from Web.FileAcquisition import Receive,Query

urlpatterns = [
    #用户相关
    path('api/registered/', Registered.Registered),  # 注册
    path('api/login/', User.Login),  # 登录
    path('api/user_info/', User.PersonalInformation),  # 获取个人信息接口
    path('api/update_password/', User.UpdatePassword),  # 更新密码
    path('api/update_show_name/', User.UpdateShowName),  # 更新显示名称
    path('api/update_key/', User.UpdateKey),  # 更新Key
    path('api/forget_password/', User.ForgetPassword),  # 忘记密码API
    path('api/upload_avatar/', User.UploadAvatar),  # 上传头像接口
    #验证码相关
    path('api/get_verification_code/', VerificationCode.GenerateVerificationCode),  # 获取验证码api
    #首页相关
    path('api/homepage_default_data/', Home.HomepageDefaultData),  # 首页默认数据
    path('api/homepage_vulnerability_distributiont_data/', Home.HomepageVulnerabilityDistributiontData),  # 首页漏洞分布数据
    path('api/homepage_github_monitor_data/', Home.HomepageGithubMonitorData),  # 首页github监控数据
    #主动扫描相关
    # path('api/vulnerability_scanning/', VulnerabilityScanning.Scan),#扫描
    # path('api/active_scan_list_query/', VulnerabilityQuery.ActiveScanListQuery),#主动扫描列表查询
    # path('api/scan_information_query/', VulnerabilityQuery.ScanInformationQuery),  #主动扫描关系表
    # path('api/medusa_query/', VulnerabilityQuery.MedusaValueQuery),  # 美杜莎单个漏洞查询
    # path('api/generate_word/', GenerateReport.GenerateWord),  # 美杜莎报告生成接口
    # path('api/download_word/', GenerateReport.DownloadWord),  # 美杜莎报告下载接口
    # path('api/actively_scan_port_information/', VulnerabilityQuery.ActivelyScanPortInformation),  # 主动扫描中端口信息查询模块
    #被动扫描相关
    #path('api/create_proxy_scan_project/', ProxyScan.CreateProxyScanProject),  # 创建代理扫描项目
    #监控相关
    path('api/system_hardware_usage_query/', HardwareInfo.UsageQuery),  # 获取当前机器cpu和内存使用情况
    path('api/system_hardware_initialization/', HardwareInfo.Initialization),  # 获取当前机器基础信息
    #XSS相关
    re_path(r'^a/().*?/$', CrossSiteScript.Monitor),  # XSS钓鱼数据监控功能
    path('api/create_cross_site_script_project/', CrossSiteScript.GenerateProject),  # 用来创建跨站脚本项目
    path('api/modify_cross_site_script_project/', CrossSiteScript.ModifyProject),  # 用来修改项目生成的文件
    path('api/query_cross_site_script_project/', CrossSiteScript.QueryProject),  # 用来查询跨站脚本项目
    path('api/delete_cross_site_script_project/', CrossSiteScript.DeleteProject),  # 用来删除跨站脚本项目
    path('api/statistical_cross_site_script_project/', CrossSiteScript.StatisticalCrossSiteScriptProject),  # 统计用户所有的协同作战项目
    path('api/query_cross_site_script_project_data/', CrossSiteScript.QueryProjectData),  # 用来查询跨站脚本项目接收的数据
    path('api/statistical_cross_site_script_project_data/', CrossSiteScript.StatisticalCrossSiteScriptProjectData),  # 用来查询跨站脚本项目接收的数据
    path('api/query_cross_site_script_project_info/', CrossSiteScript.QueryProjectInfo),  # 用来查询跨站脚本项目详细信息
    path('api/read_default_cross_site_script_template/', TemplateManagement.ReadDefaultTemplate),  # 读取默认模板数据
    path('api/read_cross_site_script_template/', TemplateManagement.ReadTemplate),  # 读取用户自定义模板数据
    path('api/save_cross_site_script_template/', TemplateManagement.SaveTemplate),  # 保存模板数据
    path('api/modify_cross_site_script_template/', TemplateManagement.ModifyTemplate),  # 修改模板数据
    path('api/delete_cross_site_script_template/', TemplateManagement.DeleteTemplate),  # 删除模板数据
    #杂项工具相关
    path('api/antivirus_software_compared/', AntivirusSoftware.Compared),  # 通过获取数据进行对比目标机器的杀软
    path('api/windows_portable_execute_analysis/', PortableExecute.Windows),  # windows文件上传后进行结构处理
    # path('api/linux_executable_linkable_format_analysis/', ExecutableLinkableFormat.Linux),# Linux文件上传后进行结构处理
    #APP收集相关
    # path('api/apple_app_collection/', CollectionWork.AppleAppCollection),  # IOS搜集下发接口
    # path('api/application_collection_query/', CollectionWork.ApplicationCollectionQuery),  # 应用收集统一查询接口
    #协同作战相关
    path('api/create_markdown_project/', Markdown.CreateMarkdownProject),  # 创建协同作战项目
    path('api/join_markdown_project/', Markdown.JoinMarkdownProject),  # 加入协同作战项目
    path('api/query_markdown_project/', Markdown.QueryMarkdownProject),  # 查询用户所有的协同作战项目
    path('api/markdown_project_statistical/', Markdown.MarkdownProjectStatistical),  # 统计用户所有的协同作战项目
    path('api/save_markdown_data/', Markdown.SaveMarkdownData),  # 保存协同作战文档
    path('api/query_markdown_data/', Markdown.QueryMarkdownData),  # 查询协同作战中文档数据
    path('api/markdown_image_upload/', Markdown.MarkdownImageUpload),  # 文档中的上传图片接口
    path('api/markdown_data_comparison/', Markdown.MarkdownDataComparison),  # 文档中的数据对比接口
    path('api/delete_markdown/', Markdown.DeleteMarkdown),  # 删除项目使用
    #CVE监控相关
    path('api/github_monitor_search/', Github.GithubQuery),  # GitHub漏洞利用监控数据模糊搜索功能
    path('api/nist_data_bulk_query/', Nist.NistDataBulkQuery),  # Nist全量数据查询
    path('api/nist_data_detailed_query/', Nist.NistDataDetailedQuery),  # Nist数据中单个CVE详情查询
    path('api/nist_search/', Nist.NistSearch),  # Nist模糊搜索接口
    #DNSLOG
    path('api/domain_name_system_log/', Data.DNSQuery),  # 获取DNS类型的数据
    path('api/domain_name_system_log_statistics/', Data.DNSStatistics),  # DNS类型数据统计
    path('api/http_domain_name_system_log/', Data.HTTPQuery),  # 获取HTTPS类型的数据
    path('api/http_domain_name_system_log_statistics/', Data.HTTPStatistics),  # HTTPS类型数据统计
    path('api/get_domain_name_system_log/', Data.GetDNSLog),  # 获取当前用户的DNSLOG值
    #免杀生成
    path('api/shellcode_to_trojan/', TrojanInterface.ShellcodeToTrojan),  # 通过shellcode来进行代码生成
    path('api/trojan_data_query/', TrojanInterface.TrojanDataQuery),  # 查询当前用户的数据
    path('api/trojan_data_statistical/', TrojanInterface.TrojanDataStatistical),  # 对当前用户病毒数量统计
    path('api/get_trojan_plugins/', TrojanInterface.GetTrojanPlugins),  # 获取用户插件方法
    path('api/trojan_file_download_verification/', TrojanInterface.TrojanFileDownloadVerification),  # 进行生成木马文件下载
    path('api/pe2shellcode/', TrojanInterface.PE2Shellcode),  # PE文件转换为shellcode文件

    # path('api/get_auto_start/', TrojanInterface.GetAutoStart),# 获取内置类函数中自启动的列表
    # path('api/get_anti_sandbox/', TrojanInterface.GetAntiSandbox),# 获取内置类函数中反沙箱的列表
    #邮件相关
    path('api/create_email_project/', EmailProject.Creation),  # 创建邮件项目
    path('api/updata_email_project/', EmailProject.Updata),  # 更新项目数据
    path('api/run_email_project/', EmailProject.Run),  # 启动项目
    path('api/stop_email_project/', EmailProject.Stop),  # 停止项目
    path('api/email_project_details/', EmailProject.Details),  # 邮件内容详情
    path('api/email_project_summary/', EmailProject.Summary),  # 邮件项目内容摘要查询
    re_path(r'^b/().*?/$', ReceiveData.Monitor),  # 邮件接收数据监控
    path('api/email_sending_status/', EmailProject.Status),  # 查询邮件发送状态，是否发送成功，可查全量以及不同状态
    path('api/email_sending_status_statistics/', EmailProject.StatusStatistics),  # 邮件发送状态统计数量
    path('api/resend_failure_email/', EmailProject.Resend),  # 重新发送发送失败邮件
    path('api/send_test_email/', EmailProject.Test),  # 发送测试邮件
    path('api/email_file_upload/', Attachment.UploadFiles),  # 文件上传
    path('api/email_attachment_details/', Attachment.EmailAttachmentQuery),  # 邮件附件详情
    path('api/email_image_preview/', Attachment.EmailImagePreview),  # 加载预览图片
    path('api/email_receive_data_statistics/', ReceiveData.Statistics),  # 接收数据全量数据统计
    path('api/email_receive_data_details/', ReceiveData.Details),  # 接收数据全量数据详情查询
    path('api/email_receive_data_search/', ReceiveData.Search),  # 接收数据模糊查询
    path('api/email_receive_data_search_quantity/', ReceiveData.SearchQuantity),  # 接收数据模糊查询统计
    path('api/email_data_graph_statistics/', Graph.Statistics),  # 数据表格统计
    path('api/email_data_graph_query/', Graph.Query),  # 数据表格查询
    path('api/upload_email_list/',EmailList.Upload ),  # 上传邮件列表数据
    path('api/download_email_list_template/', EmailList.Download),  # 下载邮件列表模板
    path('api/statistics_email_project_list/', EmailList.StatisticsProject),  # 统计邮件管理项目
    path('api/query_email_project_list/', EmailList.QueryProject),  # 查询邮件管理项目
    path('api/query_email_list/', EmailList.Query),  # 查询邮件管理中的邮箱数据
    path('api/update_email_data/', EmailList.Update),  # 更新邮件管理中的某一条数据
    path('api/delete_email_data/', EmailList.Delete),  # 删除邮件管理中的某一条数据
    path('api/search_email_data/', EmailList.Search),  # 邮件管理模糊搜索数据

    #项目相关信息
    path('api/medusa_config_info/', Information.ConfigInfo),  # 获取项目相关数据
    path('api/medusa_config_update/', Information.ConfigUpdate),  # 更新项目相关数据
    #path(api/medusa_update/', Information.Update),  # test网站

    #数据接收相关
    path('api/file_acquisition_receive/', Receive.Upload),  # 获取其他地方上传的数据
    path('api/file_acquisition_file_pack/', Receive.FilePack),  # 下发任务打包文件
    path('api/file_acquisition_pack_download/', Receive.Download),  # 下载打包文件
    path('api/file_acquisition_pack_query/', Query.PockQuery),  # 打包文件查询
    path('api/file_acquisition_pack_attachment/', Query.PackAttachment),  # 打包文件个数统计
    path('api/file_acquisition_query/', Query.Query),  # 获取文件查询
    path('api/file_acquisition_attachment/', Query.Attachment),  # 获取文件个数查询



]
urlpatterns += staticfiles_urlpatterns()