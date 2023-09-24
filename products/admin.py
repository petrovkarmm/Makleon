from django.contrib import admin
from .models.product import Product
from .models.product_access_user import ProductAccess

admin.site.register(Product)
admin.site.register(ProductAccess)