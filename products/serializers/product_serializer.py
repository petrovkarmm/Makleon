from rest_framework import serializers
from products.models.product import Product
from lessons.serializers.lesson_serializer import LessonSerializer


class ProductSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'lessons')
