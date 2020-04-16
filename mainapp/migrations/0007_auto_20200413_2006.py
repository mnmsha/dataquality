# Generated by Django 3.0.4 on 2020-04-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_popularuty_m'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popularuty_m',
            name='popularuty',
        ),
        migrations.AddField(
            model_name='popularuty_m',
            name='popularuty_1',
            field=models.IntegerField(default=1, verbose_name='Оцените качество источника данных по шкале от 1 до 10, исходя из произведенной оценки'),
        ),
    ]