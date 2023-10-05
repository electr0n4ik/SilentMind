from django.db import models

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

    def __str__(self):
        return f"Курс {self.name}"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Generic-classes"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=127,
        verbose_name='Название')
    description = models.CharField(
        max_length=255,
        verbose_name='Описание')
    preview = models.ImageField(
        **NULLABLE,
        upload_to='knowledge/images',
        verbose_name='Картинка')
    url_video = models.URLField(**NULLABLE, verbose_name='Ссылка на видео')

    def __str__(self):
        return f"Урок {self.name}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
