from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializers
from django.http import Http404, JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


@csrf_exempt
def poll(request):
    if request.method == 'GET':
        ''' list api '''
        qs = Question.objects.all()
        serializer = QuestionSerializers(qs, many=True)
        return JsonResponse(serializer.data, safe=False)  # list to json

    elif request.method == 'POST':
        ''' create api '''
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = QuestionSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def poll_details(request, pk):
    try:
        instance = Question.objects.get(pk=pk)
    except Question.DoesNotExist as e:
        return HttpResponse({'error': 'Object not found!'}, status=404)

    if request.method == 'GET':
        ''' list api '''
        serializer = QuestionSerializers(instance)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        ''' create api '''
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = QuestionSerializers(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        ''' create api '''
        instance.delete()
        return HttpResponse(status=204)
