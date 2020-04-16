from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.files import File
from .defs import availability_def, machinereadability_def, authority_def, class_dict_def, reliability_def, relevance_def, fullness_def

class Popularuty_m(models.Model):
    popularuty_1 = models.IntegerField(verbose_name = "Оцените качество источника данных по шкале от 1 до 10, исходя из произведенной оценки", default=None, blank=True, null=True)
    pk_Dataquality = models.IntegerField(default=None, blank=True, null=True)
    source_Dataquality = models.URLField(verbose_name = "Укажите его источник", max_length=200)



class Choices(models.Model):
    description = models.CharField(max_length=300)
    def __str__(self):
        return self.description


class Dataquality(models.Model):
    file = models.FileField(verbose_name = "Загрузите файл")
    source = models.URLField(verbose_name = "Укажите его источник", max_length=200)
    availability = models.FloatField(verbose_name = "Доступность", default=None, blank=True, null=True)
    authority = models.FloatField(verbose_name = "Авторитетность", default=None, blank=True, null=True)
    popularuty = models.FloatField(verbose_name = "Репутация", default=None, blank=True, null=True)
    machinereadability = models.FloatField(verbose_name = "Интерпретируемость", default=None, blank=True, null=True)
    reliability = models.FloatField(verbose_name = "Достоверность", default=None, blank=True, null=True)
    relevance = models.FloatField(verbose_name = "Актуальность", default=None, blank=True, null=True)
    fullness = models.CharField(max_length=200, verbose_name = "Полнота", default=None, blank=True, null=True)
    full_classificators=models.ManyToManyField(Choices, verbose_name = "Укажите данные, которые вам нужны")
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()
