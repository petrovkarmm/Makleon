from django.contrib.auth.models import User
from django.db import models
from .lesson import Lesson


class ProductAccess(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='lesson_user_accesses',
                             verbose_name='User accesses to lesson')

    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               related_name='user_lesson_accesses',
                               verbose_name='Lesson accesses to user')

    lesson_get_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} has access to {self.lesson.name}'