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

    def __str__(self):
        return f"урок {self.title}"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
