from django.db import models
from client.models import phone_regex, Client
from django.core.validators import RegexValidator

car_number = RegexValidator(
    regex='^[0-9]{1}[0-5]{1}[ -][A-Z]{1}[ -][0-9]{3}[ -][A-Z]{2}$',
    message="Car number must be entered in the format: '[XX] [X] [XXX] [XX]'. Up to 8 characters allowed."
)
car_number2 = RegexValidator(
    regex='^[0-9]{1}[0-5]{1}[ -][0-9]{3}[ -][A-Z]{3}$',
    message="Car number must be entered in the format: '[XX] [XXX] [XXX]'. Up to 8 characters allowed."
)


class Tuman(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi

    class Meta:
        ordering = ['-id']


class Instructor(models.Model):
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    telefon = models.CharField(validators=[phone_regex], max_length=12)
    jins = models.CharField(max_length=5)
    tuman = models.CharField(max_length=255, null=True)
    toifa = models.CharField(max_length=2)
    moshina = models.CharField(max_length=255, null=True)
    nomeri = models.CharField(max_length=11)
    balans = models.IntegerField(default=0)
    telegram_id = models.BigIntegerField()
    ratet = models.FloatField(null=True)
    location = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f"{self.ism} {self.moshina}"

    @property
    def get_rating(self):
        obj = self.rating.all().count()
        if obj == 0:
            obj = 1
        rt = sum([item.rate for item in self.rating.all()])
        self.ratet = (rt / obj)
        self.save()
        return self.ratet

    class Meta:
        ordering = ['-ratet']


class Rating(models.Model):
    RATE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    instructor = models.ForeignKey(Instructor, models.CASCADE, related_name='rating')
    rate = models.IntegerField(choices=RATE, default=0)
    client = models.ForeignKey(Client, models.SET('o\'chib ketgan'), related_name='rating')

    def __str__(self):
        return f"{self.instructor.ism} {self.rate}"
