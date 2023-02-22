from django.contrib import admin
from .models import Instructor, Tuman, Rating


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', 'ism', 'familiya', 'telefon', 'moshina']
    list_filter = ['toifa']
    fields = ['ism', 'familiya', 'telefon', 'jins', 'tuman', 'toifa', 'moshina', 'nomeri', 'balans', 'telegram_id']


@admin.register(Tuman)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomi']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_ismi', 'instructor_ismi', 'rate']

    def client_ismi(self, obj):
        return obj.client.ism

    def instructor_ismi(self, obj):
        return obj.instructor.ism
