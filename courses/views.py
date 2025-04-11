# views.py
from django.db import OperationalError
from django.shortcuts import render, get_object_or_404
from .models import Course


# Главная страница
def home(request):
    return render(request, 'courses/about.html')


# Страница со всеми курсами
def course_list(request):
    try:
        courses = Course.objects.all()
    except OperationalError:
        courses = None  # Возвращаем None или пустой список, если ошибка базы данных

    return render(request, 'courses/course_list.html', {'courses': courses})


# Детальная страница курса
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)  # Получаем курс по ID
    return render(request, 'courses/course_detail.html', {'course': course})
