from rest_framework.response import Response
from rest_framework.views import APIView
from products.models.product import Product
from products.serializers.product_serializer import ProductListSerializer
from lessons.models.lesson import Lesson


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True, context={'request': request})

        return Response({'products': serializer.data})