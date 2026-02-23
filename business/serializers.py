from rest_framework import serializers
from .models import *


class BusinessSerializer(serializers.models):
    class Meta:
        model=Business
        fields='__all__'
        read_only_fields = ("owner","created_at")


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        ffields='__all__'
        read_only_fields = ("business")
