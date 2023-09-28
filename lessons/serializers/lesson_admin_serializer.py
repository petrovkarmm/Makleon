from rest_framework import serializers
from lessons.models.lesson import Lesson


class LessonAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'