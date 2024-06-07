from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from base.models import LowerCaseEmailField


class User(AbstractUser):
    """User model"""
    username = None

    email = LowerCaseEmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        ordering = ('email',)
