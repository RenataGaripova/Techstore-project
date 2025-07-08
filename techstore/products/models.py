"""Setting up models."""
from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    """Category model."""

    name = models.CharField(max_length=128)
    description = models.TextField()
    photo = models.ImageField(upload_to='category_images')

    class Meta:
        """Meta class."""

        verbose_name_plural = 'Categories'

    def __str__(self):
        """Magic method to show name of a category."""
        return self.name


class Product(models.Model):
    """Product model."""

    name = models.CharField(max_length=128)
    model = models.CharField(max_length=256, blank=True)
    producer = models.CharField(max_length=128, blank=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_images')
    in_stock = models.IntegerField()
    rating = models.FloatField(blank=True, default=0.0)
    price = models.FloatField(
        validators=[MinValueValidator(1.0)]
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    class Meta:
        """Meta class."""

        default_related_name = 'products'

    def __str__(self):
        """Magic method to show product's name."""
        return self.name
