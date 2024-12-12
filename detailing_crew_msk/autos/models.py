from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from detailing.models import ClientUser

from .validators import plate_validator


class AutoBrand(models.Model):
    name = models.CharField(
        max_length=32,
        blank=False
    )
    popular = models.BooleanField(
        default=False
    )
    
    class Meta:
        verbose_name = 'марка'
        verbose_name_plural = 'Марки'
        ordering = ['-popular']

    def __str__(self):
        return self.name


class AutoModel(models.Model):
    brand = models.ForeignKey(
        AutoBrand,
        on_delete=models.CASCADE,
        related_name='models'
    )
    name = models.CharField(
        max_length=32,
        blank=False,
    )

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name


class Auto(models.Model):
    brand = models.ForeignKey(
        AutoBrand,
        blank=False,
        on_delete=models.CASCADE,
        related_name='autos',
        verbose_name='Марка авто'
    )
    model = ChainedForeignKey(
        AutoModel,
        chained_field='brand',
        chained_model_field='brand',
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name='Модель авто',
        # https://django-smart-selects.readthedocs.io/en/latest/usage.html
    )
    plate = models.CharField(
        max_length=9,
        blank=True,
        validators=[plate_validator],
        verbose_name='ГРЗ',
        unique=True,
        help_text='Введите корректный ГРЗ в формате X999XX99 или X999XX199.'
    )
    owner = models.ForeignKey(
        ClientUser,
        blank=False,
        on_delete=models.CASCADE,
        related_name='autos',
        verbose_name='Владелец авто',
    )

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'Автомобили'
        # ordering = ['brand']

    def __str__(self):
        return f'{self.brand} {self.model}'
