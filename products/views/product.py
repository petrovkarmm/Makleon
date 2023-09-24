from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models.product import Product
from products.serializers.product_serializer import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product, context={'request': request})

        return Response(serializer.data)