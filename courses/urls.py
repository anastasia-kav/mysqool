from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # Страница со всеми курсами
    path('<int:pk>/', views.course_detail, name='course_detail'),  # Страница с детальной информацией о курсе
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
