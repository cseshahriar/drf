from rest_framework import serializers
from .models import Question


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
