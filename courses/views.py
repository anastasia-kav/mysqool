# views.py
from django.shortcuts import render
from .models import Course


# Главная страница
def home(request):
    return render(request, 'courses/about.html')


# Страница со всеми курсами
def course_list(request):
    courses = Course.objects.all()  # Получаем все курсы
    return render(request, 'courses/course_list.html', {'courses': courses})  # Рендерим шаблон с курсами


# Детальная страница курса
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)  # Получаем курс по ID
    return render(request, 'courses/course_detail.html', {'course': course})
