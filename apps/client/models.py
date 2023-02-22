from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(
    regex=r"^998[378]{2}|9[01345789]\d{7}$",
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class Client(models.Model):
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    telefon = models.CharField(validators=[phone_regex], max_length=12)
    prava = models.CharField(max_length=4, default="Yo'q")
    telegram_id = models.BigIntegerField()

    def __str__(self):
        return f"{self.ism} {self.familiya}"
