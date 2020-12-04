from .models import Question
from .serializers import QuestionSerializers

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated
''' Generic Views '''


class PollListView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    ''' list api view '''
    serializer_class = QuestionSerializers
    queryset = Question.objects.all()
    # lookup_field = 'something'
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication
    ]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, *args, **kwargs):
        ''' list '''
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request, *args, **kwargs):
        ''' create '''
        return self.create(request)

    def perform_create(self, serializer):
        ''' post creating by current logged in user '''
        serializer.save(created_by=self.request.user)  # current user ref

    def put(self, request, pk=None, *args, **kwargs):
        ''' update '''
        return self.update(request, pk=pk)

    def perform_update(self, serializer):
        ''' post creating by current logged in user '''
        serializer.save(created_by=self.request.user)  # current user ref

    def delete(self, request, pk=None, *args, **kwargs):
        ''' delete '''
        return self.destroy(request, pk)


''' All APIViews '''


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
