from django.contrib.auth.models import User
from django.db import models
from .product import Product


class ProductAccess(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='product_user_accesses',
                             verbose_name='User accesses to product')

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='user_product_accesses',
                                verbose_name='Product accesses to user')

    product_get_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} has access to {self.product.name}'