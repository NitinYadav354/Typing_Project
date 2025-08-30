from rest_framework import serializers
from .models import Text

class TypingTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'