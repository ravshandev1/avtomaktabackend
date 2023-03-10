from django.db import models
from client.models import Client
from instructor.models import Instructor


class Category(models.Model):
    class Meta:
        verbose_name = 'Права тоифалари'
        verbose_name_plural = 'Права тоифалари'

    toifa = models.CharField(max_length=2)

    def __str__(self):
        return self.toifa


class Car(models.Model):
    class Meta:
        verbose_name_plural = 'Мошиналар'
        verbose_name = 'Мошиналар'

    nomi = models.CharField(max_length=255)
    categoriyasi = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return f"{self.nomi} {self.categoriyasi.toifa}"


class Percent(models.Model):
    percent = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.percent}"


class Session(models.Model):
    class Meta:
        ordering = ['id']

    PAYMENT = (
        ('Накд', 'Накд'),
        ('Карта', 'Карта'),
    )
    client = models.ForeignKey(Client, models.CASCADE, related_name='sessions')
    toifa = models.CharField(max_length=2)
    jins = models.CharField(max_length=5)
    moshina = models.ForeignKey(Car, models.SET_NULL, null=True)
    instructor = models.ForeignKey(Instructor, models.CASCADE, related_name='sessions')
    qayerdan = models.CharField(max_length=255)
    vaqt = models.DateTimeField()
    tulov_turi = models.CharField(max_length=5, choices=PAYMENT, default='Накд')
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.ism}, vaqti: {self.vaqt.__format__('%B/%-m %H:%M')}"


class Price(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, related_name='price')
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.price // 1000},000 сўм соатига"
