from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers
from .documents import OldPolishDocument
from .models import OldPolish

class OldPolishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldPolish
        fields = ['id', 'old_text', 'new_text']

class OldPolishESSerializer(DocumentSerializer):
    class Meta:
        document = OldPolishDocument
        fields = ['id', 'old_text', 'new_text']