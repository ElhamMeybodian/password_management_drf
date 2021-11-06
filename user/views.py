from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile, UserPassword
from .serializers import CreateUserSerializer, UserPasswordSerializer, ChangePasswordSerializer


class UserList(viewsets.ModelViewSet):
    serializer_class = CreateUserSerializer
    queryset = UserProfile.objects.all()


class PasswordList(viewsets.ModelViewSet):
    serializer_class = UserPasswordSerializer
    queryset = UserPassword.objects.all()


class ChangePassword(viewsets.ModelViewSet):
    serializer_class = ChangePasswordSerializer
    print('-----------')
    queryset = UserPassword.objects.all()
    print('lllllllllll', queryset)

