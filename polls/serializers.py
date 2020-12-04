from rest_framework import serializers
from .models import Question, Choice


class QuestionSerializers(serializers.ModelSerializer):
    ''' model serializers '''

    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'status',
            'created_by'
        ]


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
