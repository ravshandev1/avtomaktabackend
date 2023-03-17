from rest_framework import serializers
from .models import Session, Category, Car, Price, Percent, TextSes


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextSes
        fields = '__all__'


class PercentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percent
        fields = ['percent']


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['price', 'category']

    category = serializers.CharField(source='category.toifa')


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['client', 'toifa', 'jins', 'moshina', 'instructor', 'vaqt', 'tulov_turi']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['toifa']


class MoshinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'nomi']


class SessionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'client', 'vaqt', 'tulov_turi', 'c_telefoni', 'i_telefoni', 'instructor', 'moshina',
                  'jins', 'toifa']

    client = serializers.CharField(source='client.ism')
    instructor = serializers.CharField(source='instructor.ism')
    moshina = serializers.CharField(source='moshina.nomi')
    c_telefoni = serializers.CharField(source='client.telefon')
    i_telefoni = serializers.CharField(source='instructor.telefon')
    vaqt = serializers.DateTimeField(format="%-d-%B %H:%M")
