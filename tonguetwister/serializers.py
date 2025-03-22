from rest_framework import serializers
from .models import OldPolish

class OldPolishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldPolish
        fields = ['id', 'old_text', 'new_text'] # define available fields
