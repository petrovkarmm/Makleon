from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models.product import Product
from products.serializers.product_list_serializer import ProductListSerializer
from products.serializers.product_list_serializer_admin import ProductListSerializerAdmin
from products.serializers.product_serializer import ProductSerializer


class ProductListAPIView(APIView):
    # TODO add path to admin lesson post after admin product post
    # lesson_url = ''
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True, context={'request': request})

        return Response({'products': serializer.data})

    def post(self, request):
        if request.user.is_superuser:
            current_user = request.user
            serializer = ProductListSerializerAdmin(data=request.data)
            if serializer.is_valid():
                product = serializer.save(owner=current_user)
                serializer_to_response = ProductSerializer(product)
                response_data = {
                    'You create a product': serializer_to_response.data,
                    'Created by': current_user.username,
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)