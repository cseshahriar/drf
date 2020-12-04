from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from .serializers import (
    EmployeeSerializer,
    LoginSerializer,
    ProfileSerializer
)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
    ordering_fields = ('is_active', 'username')
    ordering = ('username')
    search_fields = ('username', 'first_name')
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    @action(detail=True, methods=['PUT'])
    def profile(self, request, pk=None):
        """ Image upload api """
        user = self.get_object()
        profile = user.profile
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        django_logout(request)
        return Response(status=204)
