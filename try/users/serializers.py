from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('last_name', 'name', 'middle_name', 'phone_number', 'address', 'rate')
