from .models import Question
from .serializers import QuestionSerializers
from rest_framework.parsers import JSONParser

from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response


class PollAPIView(APIView):

    def get(self, request, *args, **kwargs):
        ''' list api view '''
        qs = Question.objects.all()
        serializer = QuestionSerializers(qs, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        ''' create api view '''
        data = request.data
        serializer = QuestionSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PollDetailAPIView(APIView):

    def get_object(self, pk):
        ''' get current object '''
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist as e:
            return Response({'error': 'Object not found!'}, status=404)

    def get(self, request, *args, **kwargs):
        ''' detail api view '''
        instance = self.get_object(self.kwargs['pk'])
        serializer = QuestionSerializers(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(self.kwargs['pk'])
        data = request.data
        serializer = QuestionSerializers(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(self.kwargs['pk'])
        instance.delete()
        return Response(status=204)
