from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Area


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'name', 'email', 'phone_number', 'language', 'currency',)


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ('id', 'provider', 'polygon', 'name', 'price',)
