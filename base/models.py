from django.db import models
from django.utils.translation import gettext_lazy as _


NULLABLE = {'blank': True, 'null': True}


class BaseModel(models.Model):
    """Base model"""
    objects = None
    created = models.DateTimeField(_('created at'), auto_now_add=True)
    updated = models.DateTimeField(_('updated at'), auto_now=True)
    is_deleted = models.BooleanField(_('is_deleted'), default=False)

    class Meta:
        abstract = True


class LowerCaseEmailField(models.EmailField):
    """Email in lowercase"""

    def get_prep_value(self, value):
        if value:
            return str(value).lower()
        return None
