from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)  # Добавляем поле для изображения
    duration = models.IntegerField(verbose_name='Продолжительность (в часах)')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена (в рублях)')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

