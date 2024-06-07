from django.db import models
from django.utils.translation import gettext_lazy as _


class RequestStatusChoice(models.TextChoices):
    """Статус ответа"""
    TRUE = 'true', _('Положительный ответ')
    FALSE = 'false', _('Отрицательный ответ')
    NA = 'n/a', _('Нет данных')
