from django.db import models
from client.models import Client, Category
from instructor.models import Instructor


class Car(models.Model):
    class Meta:
        verbose_name_plural = 'Мошиналар'
        verbose_name = 'Мошиналар'

    nomi = models.CharField(max_length=255)
    categoriyasi = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return f"{self.nomi} {self.categoriyasi.toifa}"


class Percent(models.Model):
    class Meta:
        verbose_name_plural = 'Ботнинг хизмат ҳаққи'
        verbose_name = 'Ботнинг хизмат ҳаққи'

    percent = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.percent}"


class Session(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Машғулотлар'
        verbose_name = 'Машғулотлар'

    client = models.ForeignKey(Client, models.CASCADE, related_name='sessions')
    toifa = models.CharField(max_length=2)
    jins = models.CharField(max_length=15)
    moshina = models.ForeignKey(Car, models.SET_NULL, null=True)
    instructor = models.ForeignKey(Instructor, models.CASCADE, related_name='sessions')
    vaqt = models.DateTimeField()
    tulov_turi = models.CharField(max_length=15)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.ism}, vaqti: {self.vaqt.__format__('%B/%-m %H:%M')}"


class Price(models.Model):
    class Meta:
        verbose_name_plural = 'Категориялар нархи'
        verbose_name = 'Категориялар нархи'

    category = models.ForeignKey(Category, models.CASCADE, related_name='price')
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.price // 1000},000 сўм соатига"


class TextSes(models.Model):
    yaratish = models.CharField(max_length=380)
    yaratish_ru = models.CharField(max_length=380, null=True, blank=True)
    jins = models.CharField(max_length=380)
    jins_ru = models.CharField(max_length=380, null=True, blank=True)
    moshina = models.CharField(max_length=380)
    moshina_ru = models.CharField(max_length=380, null=True, blank=True)
    instructor = models.CharField(max_length=380)
    instructor_ru = models.CharField(max_length=380, null=True, blank=True)
    manzil = models.CharField(max_length=380)
    manzil_ru = models.CharField(max_length=380, null=True, blank=True)
    kun = models.CharField(max_length=380)
    kun_ru = models.CharField(max_length=380, null=True, blank=True)
    utgan_kun = models.CharField(max_length=380)
    utgan_kun_ru = models.CharField(max_length=380, null=True, blank=True)
    vaqt = models.CharField(max_length=380)
    vaqt_ru = models.CharField(max_length=380, null=True, blank=True)
    utgan_vaqt = models.CharField(max_length=380)
    utgan_vaqt_ru = models.CharField(max_length=380, null=True, blank=True)
    band_qilingan_vaqt = models.CharField(max_length=380)
    band_qilingan_vaqt_ru = models.CharField(max_length=380, null=True, blank=True)
    tulov = models.CharField(max_length=380)
    tulov_ru = models.CharField(max_length=380, null=True, blank=True)
    mashgulot_yaratilsa = models.CharField(max_length=380)
    mashgulot_yaratilsa_ru = models.CharField(max_length=380, null=True, blank=True)
    mashgulot_yaratilmasa = models.CharField(max_length=380)
    mashgulot_yaratilmasa_ru = models.CharField(max_length=380, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Машғулот техти'
        verbose_name = 'Машғулот техти'
