from django.db import models
from products.models.product import Product


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    video_link = models.URLField(blank=True)
    duration = models.IntegerField(blank=True)

    products = models.ManyToManyField(Product, related_name='lessons')

    def __str__(self):
        return self.name