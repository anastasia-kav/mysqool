from django.contrib import admin
from django.urls import path, include
from courses.views import home  # Импортируем представление для главной страницы
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),  # Все пути для курсов из приложения `courses`
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
