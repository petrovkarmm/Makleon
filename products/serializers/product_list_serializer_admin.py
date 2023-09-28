from rest_framework import serializers
from products.models.product import Product


class ProductListSerializerAdmin(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'description', 'video_link', 'price')
