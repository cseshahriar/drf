from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer


class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid()
        user = serializer.validate_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        django_logout(request)
        return Response(status=204)
