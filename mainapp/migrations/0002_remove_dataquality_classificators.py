# Generated by Django 3.0.4 on 2020-04-04 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataquality',
            name='classificators',
        ),
    ]