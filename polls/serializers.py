from rest_framework import serializers
from .models import Question, Choice


class ChoicesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Choice
        fields = [
            'id',
            'title',
            'question'
        ]
        read_only_fields = ['question']
        # depth = 1  # it return question detail objects
        # depth = 2  # it's return choices with question and question user
        # 1 means one level data return(single object)


class QuestionSerializers(serializers.ModelSerializer):
    """ model serializers """

    # return all choices for this question
    # nested serializers
    # must be define top or before
    # if not required make required=false
    choices = ChoicesSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'status',
            'created_by',
            'choices'
        ]

    def create(self, validated_data):
        """ question create with choice """
        """ remove choice data from question object,
            because choices are not direct field
        """
        choices = validated_data.pop('choices')
        # only question object
        question = Question.objects.create(**validated_data)
        # save choices
        for choice in choices:
            Choice.objects.create(**choice, question=question)  # ** is dict
        return question


# question has many choices
# creation data multi model with single serializer

# get/create Question with choices
