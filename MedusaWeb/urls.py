#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
path(route, view, kwargs=None, name=None)
route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。
view: 用于执行与正则表达式匹配的 URL 请求。
kwargs: 视图使用的字典类型的参数。
name: 用来反向获取 URL。
'''
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from MedusaWeb.deploy import MedusaWeb#导入文件夹中的文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/global/', MedusaWeb.global_scan),#全局扫描
    path('api/independent/', MedusaWeb.independent_scan),#单个API扫描
    path('api/result/', MedusaWeb.result_query),  #数据库查询
    path('index/',MedusaWeb.index),
    path('login/', MedusaWeb.login),
    path('register/',MedusaWeb.register),
    path('logout/', MedusaWeb.logout),
]
