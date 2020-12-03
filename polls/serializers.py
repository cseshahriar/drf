from rest_framework import serializers
from .models import Question


class QuestionSerializers(serializers.Serializer):
    ''' model serializers '''

    class Meta:
        model = Question
        fields = [
            'title',
            'status',
            'created_by'
        ]
