from rest_framework import serializers
from lessons.models.lesson import Lesson


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'description', 'link')

    def get_link(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/v1/lesson/{obj.id}')