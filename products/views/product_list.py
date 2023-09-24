from rest_framework.response import Response
from rest_framework.views import APIView
from products.models.product import Product
from products.serializers.product_list_serializer import ProductListSerializer


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True, context={'request': request})

        return Response({'products': serializer.data})