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
from django.urls import path
from Web.Api import VulnerabilityScanning,VulnerabilityQuery,Registered,User,GenerateReport,UserInfo

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
    path('api/user_info/', UserInfo.PersonalInformation),  # 获取个人信息接口
    path('api/update_password/', User.UpdatePassword),  # 更新密码
    path('api/update_show_name/', User.UpdateShowName),  # 更新显示名称
    path('api/update_key/', User.UpdateKey),  # 更新Key




]
