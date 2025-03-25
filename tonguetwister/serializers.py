from drf_yasg.utils import swagger_serializer_method
from drf_yasg import openapi
from rest_framework import serializers
from .models import OldPolish

class OldPolishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldPolish
        fields = ['id', 'old_text', 'new_text']

    @swagger_serializer_method(serializer_or_field=openapi.Schema(
        type=openapi.TYPE_STRING,
        description="Example of an old Polish phrase"
    ))
    def old_text(self, obj):
        return obj.old_text