"""URL for products app."""
from django.urls import path

from . import views

app_name = 'products'


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.category_list_view, name='category_list'),
    path(
        'category/<int:category_id>/',
        views.products_by_category_view,
        name='category_products'
    ),
]
