from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product


class CartQuerySet(models.QuerySet):
    """Cart QuerySet."""

    def total_price(self):
        return sum(cart.get_products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    """Cart Model."""

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartQuerySet().as_manager()

    def __str__(self):
        return f"{self.user.username}'s cart"

    def get_products_price(self):
        return round(self.product.sell_price * self.quantity, 2)
