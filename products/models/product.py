import uuid

from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          verbose_name='Product UUID')

    name = models.CharField(max_length=25,
                            blank=True,
                            verbose_name='Product name')

    description = models.TextField(max_length=150,
                                   blank=True,
                                   verbose_name='Product description')

    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='Product owner')

    def __str__(self):
        return self.name