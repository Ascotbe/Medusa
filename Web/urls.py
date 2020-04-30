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
# 官方库
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# 自己的库
from Web.api import VulnerabilityScanning, VulnerabilityQuery
from web_backend_user import views
from web_backend_user.views import UserViewSet


user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('api/Login/', login.index),#登录
    path('api/VulnerabilityScanning/', VulnerabilityScanning.register),  # 扫描 已过时
    path('api/VulnerabilityQuery/', VulnerabilityQuery.register),  # 查询 已过时

    path('', include(router.urls)),  # 根据路由上的地址来出地址
    path('api/auth/', include('djoser.urls.authtoken')),  # 登陆接口
]
