from django.contrib import admin
from django.urls import path

from .views.get_products_list import ProductListAPIView

app_name = 'products'

urlpatterns = [
    path('api/v1/product/', ProductListAPIView.as_view(), name='products-api'),
]
