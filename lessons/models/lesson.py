import uuid

from django.db import models
from products.models.product import Product


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          verbose_name='Lesson UUID')

    name = models.CharField(max_length=64, blank=True)
    description = models.TextField(max_length=128, blank=True)
    video_link = models.URLField(blank=True)
    duration = models.PositiveIntegerField(blank=True)
    price = models.PositiveIntegerField(blank=True, default=0)

    products = models.ManyToManyField(Product, related_name='lessons')

    def __str__(self):
        return self.name