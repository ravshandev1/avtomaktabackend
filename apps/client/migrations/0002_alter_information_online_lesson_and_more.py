# Generated by Django 4.1.7 on 2023-09-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='online_lesson',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='information',
            name='online_lesson_ru',
            field=models.TextField(),
        ),
    ]
