from rest_framework import serializers
from .models import Client, TextClientUpdate, TextClientRegister


class TextRSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextClientRegister
        fields = '__all__'


class TextUSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextClientUpdate
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['ism', 'familiya', 'telefon', 'prava', 'telegram_id']

    telegram_id = serializers.IntegerField(write_only=True)
