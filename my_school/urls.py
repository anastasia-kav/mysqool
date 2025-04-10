from django.contrib import admin
from django.urls import path, include

from courses.views import course_list

urlpatterns = [
    path('', course_list, name='home'),  # ⬅️ корневая страница
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
]
