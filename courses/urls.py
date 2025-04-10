from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # Страница со всеми курсами
    path('<int:pk>/', views.course_detail, name='course_detail'),  # Страница с детальной информацией о курсе
]
