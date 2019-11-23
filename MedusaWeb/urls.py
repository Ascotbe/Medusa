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
from MedusaWeb.deploy import MedusaWeb#导入文件夹中的文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', MedusaWeb.api),
    path('get/', MedusaWeb.get),
    path('test/', MedusaWeb.yibu),
]
