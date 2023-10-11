from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='почта')
    phone = models.CharField(
        **NULLABLE,
        unique=True,
        verbose_name='телефон')
    city = models.CharField(
        **NULLABLE,
        max_length=150,
        verbose_name='город')
    avatar = models.ImageField(
        **NULLABLE,
        upload_to='users/avatar',
        verbose_name='аватар')
    # subscription = models.BooleanField(default=False, verbose_name='подписка')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
