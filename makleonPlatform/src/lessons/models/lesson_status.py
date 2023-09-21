from django.contrib.auth.models import User
from django.db import models

from lessons.models.lesson import Lesson


class LessonStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='User lesson')
    watched_time = models.IntegerField(default=0, verbose_name='Watched time')
    is_watched = models.BooleanField(default=False, verbose_name='Is watched')

    def __str__(self):
        return f"{self.user.username} watched the {self.lesson.name} for {self.watched_time} seconds."