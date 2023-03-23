from django.db import models
from client.models import phone_regex, Client
from django.core.validators import RegexValidator
from session.models import Category

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
        verbose_name_plural = 'Туманлар'
        verbose_name = 'Туманлар'


class Instructor(models.Model):
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    telefon = models.CharField(validators=[phone_regex], max_length=12)
    jins = models.CharField(max_length=5)
    tuman = models.CharField(max_length=255, null=True)
    toifa = models.ManyToManyField(Category, related_name='instructors')
    moshina = models.CharField(max_length=255, null=True)
    nomeri = models.CharField(max_length=11)
    balans = models.IntegerField(default=0)
    telegram_id = models.BigIntegerField()
    ratet = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=250, null=True)
    card = models.CharField(max_length=3, choices=(('Ҳа', 'Ҳа'), ('Йўқ', 'Йўқ')), default='Йўқ')

    def __str__(self):
        return f"{self.ism} {self.moshina}"

    @property
    def get_rating(self):
        obj = self.rating.all().count()
        if obj == 0:
            obj = 1
        rt = sum([item.rate for item in self.rating.all()])
        nd = round(rt / obj)
        if nd == 0:
            nd = 1
        self.ratet = nd
        self.save()
        return self.ratet

    class Meta:
        ordering = ['-ratet']
        verbose_name_plural = 'Инструкторлар'
        verbose_name = 'Инструкторлар'


class Rating(models.Model):
    class Meta:
        verbose_name_plural = 'Инструкторлар рейтинги'
        verbose_name = 'Инструкторлар рейтинги'

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


class Payment(models.Model):
    class Meta:
        verbose_name_plural = 'Тўловлар'
        verbose_name = 'Тўловлар'

    instructor = models.ForeignKey(Instructor, models.SET('Инструктор ўчиб кетган'), related_name='payments')
    summa = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.instructor.ism} {self.summa}"


class TextInsRegister(models.Model):
    ism = models.CharField(max_length=380)
    familiya = models.CharField(max_length=380)
    telefon = models.CharField(max_length=380)
    jins = models.CharField(max_length=380)
    telefon_qayta = models.CharField(max_length=380)
    manzil = models.CharField(max_length=380)
    categoriya = models.CharField(max_length=380)
    moshina = models.CharField(max_length=380)
    moshina_nomeri = models.CharField(max_length=380)
    moshina_nomeri_qayta = models.CharField(max_length=380)
    lacatsiya = models.CharField(max_length=380)
    karta = models.CharField(max_length=380)

    class Meta:
        verbose_name_plural = 'Техт Инструктор Регистер'
        verbose_name = 'Техт Инструктор Регистер'


class TextInsUpdater(models.Model):
    ism = models.CharField(max_length=380)
    familiya = models.CharField(max_length=380)
    telefon = models.CharField(max_length=380)
    telefon_qayta = models.CharField(max_length=380)
    manzil = models.CharField(max_length=380)
    categoriya = models.CharField(max_length=380)
    moshina = models.CharField(max_length=380)
    moshina_nomeri = models.CharField(max_length=380)
    moshina_nomeri_qayta = models.CharField(max_length=380)
    lacatsiya = models.CharField(max_length=380)
    karta = models.CharField(max_length=380)

    class Meta:
        verbose_name_plural = 'Техт Инструктор Изменет'
        verbose_name = 'Техт Инструктор Изменет'
