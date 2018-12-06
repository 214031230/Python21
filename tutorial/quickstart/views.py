from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializers, GroupSerializers


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    '''
    允许用户查看或编辑API的路径
    '''

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    '''
       允许用户查看或编辑API的路径
    '''

    queryset = Group.objects.all()
    serializer_class = GroupSerializers
