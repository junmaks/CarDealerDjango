from django.db import models
import datetime


def year_choices(year_start):
    return [(r, r) for r in range(year_start, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


class Dealers(models.Model):
    CHOICE_YEAR = year_choices(1994)

    title = models.CharField(max_length=100, verbose_name='Название организации')
    location = models.CharField(max_length=50, verbose_name='Город')
    year = models.IntegerField(verbose_name='Год основания', choices=CHOICE_YEAR, default=current_year())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилеры'
        ordering = ['-year']


class Cars(models.Model):
    CHOICE_YEAR = year_choices(1954)

    brand = models.CharField(max_length=50, verbose_name='Марка')
    car_model = models.CharField(max_length=50, verbose_name='Модель')
    year_of_release = models.IntegerField(verbose_name='Год выпуска', choices=CHOICE_YEAR, default=current_year())
    dealer = models.ForeignKey('Dealers', on_delete=models.CASCADE, verbose_name='Дилерский центр')
    price = models.IntegerField(verbose_name='Цена', default=0.00)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['brand']
