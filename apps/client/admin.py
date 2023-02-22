from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # fields = ['ism', 'familiya', 'telefon']
    list_display = ['id', 'ism', 'familiya', 'telefon', 'prava']

    # @staticmethod
    # def telefon(obj):
    #     return f"+{obj.phone}"
