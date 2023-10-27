from typing import Any
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework import serializers, exceptions
from api import models

class User(object):
    def __init__(self, name=None, role=None) -> None:
        self.name = name
        self.role = role

        

class MineAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        role = request.query_params.get('role')
        if not token:
            raise exceptions.AuthenticationFailed("认证失败")

        return (User("immmor", role), None,)

        
    def authenticate_header(self, request):
        return "API"


class MinePermission(BasePermission):
    def has_permission(self, request, view):
        # print("判断权限", request.user.role)
        from django.conf import settings
        permission_dict = settings.PERMISSIONS[request.user.role]
        # print(request.resolver_match.url_name, request.method)
        url_name = request.resolver_match.url_name
        method = request.method

        method_list = permission_dict.get(url_name)
        if not method_list:
            return False
        if method in method_list:
            return True
        return False

    
    def has_object_permission(self, request, view, obj):
        return True




class DepartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Depart
        fields = "__all__"


class DepartView(ModelViewSet):
    queryset = models.Depart.objects.all()
    serializer_class = DepartSerializer

    authentication_classes = [MineAuthentication,]
    permission_classes = [MinePermission, ]

    

