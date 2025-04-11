from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)  # Добавляем поле для изображения
    duration = models.IntegerField(verbose_name='Продолжительность (в часах)')
    price = models.IntegerField(verbose_name='Цена (в рублях)')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.lessons = None

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    duration = models.IntegerField(verbose_name='Продолжительность (в неделях)')

    def __str__(self):
        return self.title

