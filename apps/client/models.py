from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(
    regex=r"^998[378]{2}|9[01345789]\d{7}$",
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class Category(models.Model):
    class Meta:
        verbose_name = 'Права тоифалари'
        verbose_name_plural = 'Права тоифалари'

    toifa = models.CharField(max_length=2)

    def __str__(self):
        return self.toifa


class Client(models.Model):
    class Meta:
        verbose_name_plural = 'Ўрганувчилар'
        verbose_name = 'Ўрганувчилар'

    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    telefon = models.CharField(validators=[phone_regex], max_length=12)
    prava = models.CharField(max_length=4, default="Yo'q")
    telegram_id = models.BigIntegerField()

    def __str__(self):
        return f"{self.ism} {self.familiya}"


class TextClientRegister(models.Model):
    ism = models.CharField(max_length=380)
    familiya = models.CharField(max_length=380)
    telefon = models.CharField(max_length=380)
    prava = models.CharField(max_length=380)
    telefon_qayta = models.CharField(max_length=380)
    prava_bor = models.CharField(max_length=380)
    prava_yuq = models.CharField(max_length=380)

    class Meta:
        verbose_name = 'Техт регистер'
        verbose_name_plural = 'Техт регистер'


class TextClientUpdate(models.Model):
    ism = models.CharField(max_length=380)
    familiya = models.CharField(max_length=380)
    telefon = models.CharField(max_length=380)
    prava = models.CharField(max_length=380)
    telefon_qayta = models.CharField(max_length=380)

    class Meta:
        verbose_name = 'Техт изменет'
        verbose_name_plural = 'Техт изменет'
