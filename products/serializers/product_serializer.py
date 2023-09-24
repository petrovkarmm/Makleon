from rest_framework import serializers
from products.models.product import Product
from lessons.serializers.lesson_serializer import LessonSerializer


class ProductListSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    link = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'link', 'description', 'lessons')

    def get_link(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/v1/product/{obj.id}')
