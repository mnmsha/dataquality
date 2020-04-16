# Generated by Django 3.0.4 on 2020-04-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200405_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataquality',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataquality',
            name='fullness',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Полнота'),
        ),
        migrations.AlterField(
            model_name='dataquality',
            name='popularuty',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Репутация'),
        ),
    ]