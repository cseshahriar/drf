from rest_framework import serializers
from .models import Question, Choice


class ChoicesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    # must for updating, otherwis not update, instade of new created

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

    def update(self, instance, validated_data):
        """ multi model object update """
        choices = validated_data.pop('choices')
        # main model
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        # child model objects
        keep_choices = []
        choices_ids = [c.id for c in instance.choices]
        for choice in choices:
            # if objects exitsts
            if "id" in choice.keys():
                if Choice.objects.filter(id=choice["id"]).exists():
                    # get obj
                    c = Choice.objects.get(id=choice["id"])
                    c.title = choice.get('title', c.title)
                    c.save()
                    keep_choices.append(c.id)
                else:  # if not exist obj
                    continue
            else:  # if not exists, create new object
                c = Choice.objects.create(**choice, question=instance)  #
                keep_choices.append(c.id)
        # delete
        for choice in instance.choices:
            if choice.id not in keep_choices:
                choice.delete()

        return instance
