from rest_framework import serializers
from .models import AppFieldUser

class AppFieldUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFieldUser
        fields = '__all__' 