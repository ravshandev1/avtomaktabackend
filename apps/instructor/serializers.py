from rest_framework import serializers
from .models import Instructor, Tuman, TextInsUpdater, TextInsRegister


class TextRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextInsRegister
        fields = '__all__'


class TextUpdaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextInsUpdater
        fields = '__all__'


class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = ['id', 'nomi']


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'ism', 'familiya', 'telefon', 'jins', 'tuman', 'toifa', 'toifa_name', 'moshina', 'nomeri',
                  'balans', 'telegram_id', 'get_rating', 'location', 'card']

    toifa_name = serializers.SerializerMethodField()

    def get_toifa_name(self, obj):
        return obj.toifa.first().toifa
