# Generated by Django 3.2.17 on 2023-03-09 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Мошиналар', 'verbose_name_plural': 'Мошиналар'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Права тоифалари', 'verbose_name_plural': 'Права тоифалари'},
        ),
        migrations.AddField(
            model_name='price',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='price', to='session.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='tulov_turi',
            field=models.CharField(choices=[('Накд', 'Накд'), ('Kaртa', 'Kaртa')], default='Накд', max_length=5),
        ),
    ]