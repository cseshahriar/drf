
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Image
        fields = ('pk', 'image', 'timestamp')
