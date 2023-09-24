from django.db import models
from products.models.product import Product


class Lesson(models.Model):
    name = models.CharField(max_length=64, blank=True)
    description = models.TextField(max_length=128, blank=True)
    video_link = models.URLField(blank=True)
    duration = models.PositiveIntegerField(blank=True)

    products = models.ManyToManyField(Product, related_name='lessons')

    def __str__(self):
        return self.name