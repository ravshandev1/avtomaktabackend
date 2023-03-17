from django.contrib import admin
from .models import Instructor, Tuman, Payment, TextInsUpdater, TextInsRegister


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', 'ism', 'familiya', 'telefon', 'moshina']
    list_filter = ['toifa']
    # exclude = ['ratet']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['instructor', 'sum', 'created_at']
    list_filter = ['created_at']

    def sum(self, obj):
        return f"{int(obj.summa) // 1000},000 сўм"


@admin.register(Tuman)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomi']


@admin.register(TextInsRegister)
class Name(admin.ModelAdmin):
    pass


@admin.register(TextInsUpdater)
class Name(admin.ModelAdmin):
    pass
