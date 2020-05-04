from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from web_backend_user.serializers import UserSerializer


# 用户管理（目前只读）
class UserViewSet(viewsets.ReadOnlyModelViewSet):

    # This viewset automatically provides `list` and `detail` actions.

    # 是否鉴权 鉴权类型可自定义 TODO 改成管理员（superuser）可用
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
