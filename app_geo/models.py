from django.db import models
from django.utils.translation import gettext_lazy as _

from base.choises import RequestStatusChoice
from base.models import BaseModel


class Address(BaseModel):
    """
    Model for addresses

    Стандартная длина КН составляет 13 знаков.
    Встречаются КН, которые содержат 12 символов, а также обозначения, состоящие из 15-16 знаков.
    Это не считается нарушением, такие стандарты приняты Росреестром.
    """
    cad_number = models.CharField(
        _('Кадастровый номер'), max_length=16, unique=True,
        help_text=_("Максимальная длина кадастрового номера не должна превышать 16 знаков")
    )
    latitude = models.DecimalField(_('Широта'), max_digits=10, decimal_places=6, help_text=_("41.385064"))
    longitude = models.DecimalField(_('Долгота'), max_digits=10, decimal_places=6, help_text=_("-2.173403"))

    def __str__(self):
        return f'Кадастровый номер {self.cad_number}, координаты: {self.latitude}, {self.longitude}'

    class Meta:
        verbose_name = _('Адрес')
        verbose_name_plural = _('Адреса')


class Request(BaseModel):
    """
    Model for request
    """
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='request_address')

    response = models.CharField(_('Ответ'), max_length=5, choices=RequestStatusChoice.choices,
                                default=RequestStatusChoice.NA)

    def __str__(self):
        return f'{self.address} - {self.response}'

    class Meta:
        verbose_name = _('Запрос')
        verbose_name_plural = _('Запросы')
