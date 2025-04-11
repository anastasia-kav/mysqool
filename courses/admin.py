from django.contrib import admin
from .models import Course, Lesson

from django.contrib import admin
from .models import Lesson
from django.utils.safestring import mark_safe


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'formatted_content')

    def formatted_content(self, obj):
        return mark_safe(obj.content.replace("\n", "<br>"))
    formatted_content.short_description = 'Содержание'


admin.site.register(Course)
admin.site.register(Lesson)
