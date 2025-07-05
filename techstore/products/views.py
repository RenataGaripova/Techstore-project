from django.shortcuts import render
from products.models import Category

CATEGORIES_PER_PAGE = 6


def category_base_view():
    return Category.objects.order_by('id')


def index(request):
    template_name = 'products/index.html'
    category_list = category_base_view()[:CATEGORIES_PER_PAGE]
    context = {
        'category_list': category_list,
    }
    return render(request, template_name, context)
