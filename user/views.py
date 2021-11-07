from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile, UserPassword
from .serializers import CreateUserSerializer, UserPasswordSerializer, ChangePasswordSerializer


class UserList(viewsets.ModelViewSet):
    serializer_class = CreateUserSerializer
    queryset = UserProfile.objects.all()

class PasswordList(APIView):
    def get_object(self, username):
        try:
            user = UserProfile.objects.get(username=username)
            print('ooo',user)
            return UserPassword.objects.filter(user=user)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username)
        print('uu', user)
        serializer = UserPasswordSerializer(user, many=True)
        return Response(serializer.data)

    def delete(self, request, username, format=None):
        try:
            UserProfile.objects.get(username=username).delete()
            user = self.get_object(username)
            print(user)
            for u in user:
                u.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except UserProfile.DoesNotExist:
            raise Http404


class ChangePassword(viewsets.ModelViewSet):
    serializer_class = ChangePasswordSerializer
    queryset = UserPassword.objects.all()
