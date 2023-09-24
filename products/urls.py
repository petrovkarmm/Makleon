from django.contrib import admin
from django.urls import path

from .views.product_list import ProductListAPIView
from .views.product_detail import ProductAPIView

app_name = 'products'

urlpatterns = [
    path('api/v1/product/', ProductListAPIView.as_view(), name='products-api'),
    path('api/v1/product/<uuid:product_id>/', ProductAPIView.as_view(), name='product-api'),
]
