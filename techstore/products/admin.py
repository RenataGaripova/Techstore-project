"""Setting up the admin-zone."""
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """Admin-zone for product model."""

    list_display = (
        'name',
        'description',
        'in_stock',
        'price',
        'category'
    )


class CategoryAdmin(admin.ModelAdmin):
    """Admin-zone for category model."""

    list_display = (
        'name',
        'description',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
