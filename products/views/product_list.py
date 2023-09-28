from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models.product import Product
from products.serializers.product_list_serializer import ProductListSerializer
from products.serializers.product_list_serializer_admin import ProductListSerializerAdmin


class ProductListAPIView(APIView):
    # TODO add path to admin lesson post after admin product post
    # lesson_url = ''
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True, context={'request': request})

        return Response({'products': serializer.data})

    def post(self, request):
        self.permission_classes = [IsAdminUser]
        serializer = ProductListSerializerAdmin(data=request.data)
        if serializer.is_valid():
            product = serializer.save(owner=request.user)
            response_data = {
                'name': product.name,
                'description': product.description
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, product_id):
    #     self.permission_classes = [IsAdminUser]
    #     product = get_object_or_404(Product, id=product_id)
    #     serializer = ProductListSerializerAdmin(product, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)