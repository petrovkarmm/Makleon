from django.contrib import admin
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('test-products/', admin.site.urls),
]
