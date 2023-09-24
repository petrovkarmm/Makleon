from django.contrib import admin
from .models.lesson import Lesson
from .models.lesson_status import LessonStatus

admin.site.register(Lesson)
admin.site.register(LessonStatus)
