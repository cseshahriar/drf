from rest_framework import serializers
from .models import Question, Choice


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'id',
            'title',
            'question'
        ]
        read_only_fields = ['question']
        # depth = 1  # it return question detail objects
        depth = 2  # it's return choices with question and question user
        # 1 means one level data return(single object)


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


# question has many choices
# creation data multi model with single serializer

# get/create Question with choices
