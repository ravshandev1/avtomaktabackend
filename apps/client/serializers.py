from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['ism', 'familiya', 'telefon', 'prava', 'telegram_id']

    telegram_id = serializers.IntegerField(write_only=True)
