# Generated by Django 4.1.7 on 2023-03-11 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('familiya', models.CharField(max_length=255)),
                ('telefon', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed.", regex='^998[378]{2}|9[01345789]\\d{7}$')])),
                ('prava', models.CharField(default="Yo'q", max_length=4)),
                ('telegram_id', models.BigIntegerField()),
            ],
        ),
    ]
