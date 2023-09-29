from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models.product import Product
from products.serializers.product_list_serializer_admin import ProductListSerializerAdmin
from products.serializers.product_serializer import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product, context={'request': request})

        return Response(serializer.data)

    def patch(self, request, product_id):
        if request.user.is_superuser:
            product = get_object_or_404(Product, id=product_id)
            serializer = ProductListSerializerAdmin(product, data=request.data, partial=True)
            if serializer.is_valid():
                product = serializer.save()
                serializer_to_response = ProductSerializer(product)
                response_data = {
                    'Product after update': serializer_to_response.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        error_data = {
            'error': 'User is not a admin.'
        }
        return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        if request.user.is_superuser:
            product = get_object_or_404(Product, id=product_id)
            if product:
                response_data = {
                    'deleted product info': {
                        'product id': product.id,
                        'product name': product.name
                    }
                }
                product.delete()
                return Response(response_data, status=status.HTTP_200_OK)
            error_data = {
                'error': 'There is no product with this ID.'
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)
        error_data = {
            'error': 'User is not a admin.'
        }
        return Response(error_data, status=status.HTTP_400_BAD_REQUEST)