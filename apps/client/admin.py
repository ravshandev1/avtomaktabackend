from django.contrib import admin
from .models import Client, TextClientUpdate, TextClientRegister


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'ism', 'familiya', 'telefon', 'prava']

    # @staticmethod
    # def telefon(obj):
    #     return f"+{obj.phone}"


@admin.register(TextClientRegister)
class Name(admin.ModelAdmin):
    pass


@admin.register(TextClientUpdate)
class Name(admin.ModelAdmin):
    pass
