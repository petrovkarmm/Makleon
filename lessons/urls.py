from django.contrib import admin
from django.urls import path

app_name = 'lessons'

urlpatterns = [
    path('test-lessons/', admin.site.urls),
]
