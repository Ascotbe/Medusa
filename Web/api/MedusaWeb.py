#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import hashlib
import ClassCongregation
import time

# # def api(request):
# #     return JsonResponse({"result": 0, "msg": "执行成功"})
#
# # def get(request):
# #     id = request.GET.get("id")
# #     pid = request.GET.get("pid")
# #     return HttpResponse("获得数据 %s %s"%(id,pid))
# def hash_code(s, salt='Asc0e6e'):# 加点盐
#     h = hashlib.sha256()
#     s += salt
#     h.update(s.encode())  # update方法只接收bytes类型
#     return h.hexdigest()
#
# def global_scan(request):
#     if request.POST.get("task")=="1":#用户ID保留模块
#         if request.POST.get("mod") == "medusa":
#             post_url_value=request.POST.get("url")
#             mian.delay(post_url_value)
#     return JsonResponse({"result": 0, "msg": "%s"})
#
#
# def independent_scan(request):
#     user_token=request.POST.get("task")
#     independent_mod_name=request.POST.get("value")
#     independent_url=request.POST.get("url")
#     independent.delay(independent_url,independent_mod_name)
#     return JsonResponse({"result": 0, "msg": "执行成功"})
#
# def result_query(request):#通过ID查询API
#     user_token=request.GET.get("task")
#     pid=request.GET.get("id")#SQL中唯一的id值
#     name=request.GET.get("name")#通过漏洞名字查找
#     user=request.GET.get("user")#通过用户ID查找
#     rank=request.GET.get("rank")#通过危害等级查找
#     if rank!=None:#判断不为空调用相对应的函数
#         print(rank)
#     elif name!=None:
#         print(rank)
#     elif user != None:
#         print(rank)
#     info=result.delay(user_token,pid).result
#     return HttpResponse(info)#用JS返回值具体的等查询语句改好写
#
#
# def verification_session(username,sessionKey_key,sessionKey_time):#用来查询数据库中的session
#     return ClassCongregation.SessionKey(username, sessionKey_key, sessionKey_time).read()
#
#
# def index(request):
#     return render(request,'login/index.html')
#
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         message = "所有字段都必须填写！"
#         if username and password:  # 确保用户名和密码都不为空
#             username = username.strip()
#             # 用户名字符合法性验证
#             # 密码长度验证
#             # 更多的其它验证.....
#             try:
#                 hash_passwd=hash_code(password)
#                 login_inquire=ClassCongregation.login(username,).logins()#查询数据库中的密码并返回
#                 if login_inquire == hash_passwd:
#                     #a=request.session['csrftoken']
#                     return redirect('/index/')
#                 else:
#                     message = "用户名不存在或密码不正确！"
#             except:
#                 message = "用户名不存在或密码不正确！"
#         return render(request, 'login/login.html', {"message": message})
#     return render(request, 'login/login.html')
#
# def register(request):
#     if request.method == "POST":
#         username = request.POST.get('username', None)
#         password1 = request.POST.get('password1', None)
#         password2 = request.POST.get('password2', None)
#         emil = request.POST.get('emil', None)
#         if password1 != password2:  # 判断两次密码是否相同
#             message = "两次输入的密码不同！"
#             return render(request, 'login/register.html', locals())
#         else:
#             user_presence=ClassCongregation.register(username, password1, emil).register_inquire_user()  # 判断user是否存在
#             emil_presence=ClassCongregation.register(username,password1,emil).register_inquire_emil()#判断emil是否存在
#             if user_presence:  # 用户名唯一
#                 message = '用户已经存在，请重新选择用户名！'
#                 return render(request, 'login/register.html', locals())
#             elif emil_presence:  # 邮箱地址唯一
#                 message = '该邮箱地址已被注册，请使用别的邮箱！'
#                 return render(request, 'login/register.html', locals())
#             else:
#                 hash_passwd = hash_code(password1)#加密后写入
#                 print(hash_passwd)
#                 write_presence=ClassCongregation.register(username, hash_passwd, emil).register_write()
#                 if write_presence:
#                     return redirect('/login/')  # 注册成功自动跳转到登录页面
#                 else:
#                     message="请确保没问题"
#                     return render(request, 'login/register.html', locals())
#     return render(request, 'login/register.html', locals())
#
# def logout(request):
#     pass
#     return redirect('/index/')