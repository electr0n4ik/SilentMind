from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """ViewSets"""
    title = models.CharField(
        max_length=127,
        verbose_name='название')
    description = models.TextField(
        max_length=255,
        verbose_name='описание')
    preview = models.ImageField(
        **NULLABLE,
        upload_to='knowledge/images',
        verbose_name='картинка')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"курс {self.title}"

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """Generic-classes"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=127,
        verbose_name='название')
    description = models.CharField(
        max_length=255,
        verbose_name='описание')
    preview = models.ImageField(
        **NULLABLE,
        upload_to='knowledge/images',
        verbose_name='картинка')
    url_video = models.URLField(**NULLABLE, verbose_name='ссылка на видео')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"урок {self.title}"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    METHOD_CHOICES = (
        ('cash', 'наличные'),
        ('non_cash', 'безналичный расчет'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_pay = models.DateField(verbose_name='дата оплаты')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    value_pay = models.IntegerField(verbose_name="сумма оплаты")
    method_pay = models.BooleanField(choices=METHOD_CHOICES, verbose_name="способ оплаты", blank=True, null=True)

    def __str__(self):
        return f"{self.lesson if self.lesson else self.course}"

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплата'


class CourseSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True)
