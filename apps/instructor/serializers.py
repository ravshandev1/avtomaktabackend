from rest_framework import serializers
from .models import Instructor, Tuman


class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = ['id', 'nomi']


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['ism', 'familiya', 'telefon', 'jins', 'tuman', 'toifa', 'moshina', 'nomeri', 'balans', 'telegram_id',
                  'get_rating', 'location']
