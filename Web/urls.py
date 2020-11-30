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
from Web.BasicFunctions import VulnerabilityScanning,VulnerabilityQuery,Registered,User,GenerateReport,ProxyScan,Home
from Web.CrossSiteScriptHub import CrossSiteScript,TemplateManagement
from Web.SystemInfo import HardwareInfo
from Web.CommonVulnerabilityDetection import Github
from Web.ToolsUtility import AntivirusSoftware,PortableExecuteStructureAnalysis
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/vulnerability_scanning/', VulnerabilityScanning.Scan),#扫描
    path('api/active_scan_list_query/', VulnerabilityQuery.ActiveScanListQuery),#主动扫描列表查询
    path('api/registered/', Registered.Registered),#注册
    path('api/login/', User.Login),#登录
    path('api/scan_information_query/', VulnerabilityQuery.ScanInformationQuery),  #主动扫描关系表
    path('api/medusa_query/', VulnerabilityQuery.MedusaValueQuery),  # 美杜莎单个漏洞查询
    path('api/generate_word/', GenerateReport.GenerateWord),  # 美杜莎报告生成接口
    path('api/download_word/', GenerateReport.DownloadWord),  # 美杜莎报告下载接口
    path('api/user_info/', User.PersonalInformation),  # 获取个人信息接口
    path('api/update_password/', User.UpdatePassword),  # 更新密码
    path('api/update_show_name/', User.UpdateShowName),  # 更新显示名称
    path('api/update_key/', User.UpdateKey),  # 更新Key
    path('api/create_proxy_scan_project/', ProxyScan.CreateProxyScanProject),  # 创建代理扫描项目
    path('api/homepage_default_data/', Home.HomepageDefaultData),  # 首页默认数据
    path('api/homepage_vulnerability_distributiont_data/', Home.HomepageVulnerabilityDistributiontData),  # 首页漏洞分布数据
    path('api/homepage_github_monitor_data/', Home.HomepageGithubMonitorData),  # 首页github监控数据
    path('api/upload_avatar/', User.UploadAvatar),  # 上传头像接口
    path('api/github_monitor/', Github.GithubQuery),  # GitHub监控数据
    path('api/forget_password/', User.ForgetPassword),  # 忘记密码API
    path('api/actively_scan_port_information/', VulnerabilityQuery.ActivelyScanPortInformation),  # 主动扫描中端口信息查询模块
    re_path(r'^a/().*?/$', CrossSiteScript.Monitor),  # XSS钓鱼数据监控功能
    path('api/create_cross_site_script_project/', CrossSiteScript.GenerateProject),  # 用来创建跨站脚本项目
    path('api/query_cross_site_script_project/', CrossSiteScript.QueryProject),  # 用来查询跨站脚本项目
    path('api/query_cross_site_script_project_data/', CrossSiteScript.QueryProjectData),  # 用来查询跨站脚本项目数据
    path('api/read_default_cross_site_script_template/', TemplateManagement.ReadDefaultTemplate),  # 读取默认模板数据
    path('api/read_cross_site_script_template/', TemplateManagement.ReadTemplate),  # 读取用户自定义模板数据
    path('api/save_cross_site_script_template/', TemplateManagement.SaveTemplate),  # 对模板数据进行覆盖，如果没有同名文件就进行写入
    path('api/system_hardware_initialization/', HardwareInfo.Initialization),  # 获取当前机器基础信息
    path('api/system_hardware_usage_query/', HardwareInfo.UsageQuery),  # 获取当前机器cpu和内存使用情况
    path('api/antivirus_software_compared/', AntivirusSoftware.Compared),  # 通过获取数据进行对比目标机器的杀软
    path('api/portable_execute_structure_analysis/', PortableExecuteStructureAnalysis.StructureExtraction),  # 文件上传后进行结构处理

]
