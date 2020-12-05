import os
from django.shortcuts import render
from django.conf import settings

# Our model
from .models import Image

# Our serializer
from .serializers import ImageSerializer

# DRF modules
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny

# OCR scripts
# from ocr import image, recognizer


class ImageList(ListAPIView):

    'List all images'

    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)
    queryset = Image.objects.all()


class ImageDetail(RetrieveAPIView):

    'Retrieve an image instance'

    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)
    queryset = Image.objects.all()


class ImageCreate(CreateAPIView):

    'Create a new image instance'

    serializer_class = ImageSerializer

    def post(self, request):

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():

            # Save request image in the database
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
