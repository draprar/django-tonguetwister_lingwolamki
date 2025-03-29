from rest_framework import serializers
from .models import OldPolish, Articulator, Funfact

class OldPolishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldPolish
        fields = ['id', 'old_text', 'new_text']

class ArticulatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulator
        fields = ['id', 'text']

class FunfactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funfact
        fields = ['id', 'text']
