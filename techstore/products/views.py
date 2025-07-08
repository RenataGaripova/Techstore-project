"""View приложения products."""
from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings

from products.models import Category, Product


def get_page_object(
        objects,
        page_number,
        objects_count=settings.ITEMS_PER_PAGE
):
    """Paginator function."""
    paginator = Paginator(objects, objects_count)
    return paginator.get_page(page_number)


def category_base_view():
    """Function retrieving categories queryset."""
    return Category.objects.order_by('id')


def products_base_view(order_field):
    """Functionto retrieving products queryset."""
    if order_field is None:
        order_field = 'rating'
    return Product.objects.select_related('category').order_by(order_field)


def index(request):
    """View for the main page."""
    template_name = 'products/index.html'
    category_list = category_base_view()[:settings.CATEGORIES_PER_PAGE]
    context = {
        'category_list': category_list,
    }
    return render(request, template_name, context)


def category_list_view(request):
    """View for categories page."""
    template_name = 'products/category_list.html'

    if request.method == 'POST':
        pattern = request.POST.get('pattern')
        category_list = category_base_view().filter(name__contains=pattern)
    else:
        category_list = category_base_view()

    page_obj = get_page_object(
            category_list,
            request.GET.get('page'),
            settings.CATEGORIES_PER_PAGE,
    )

    context = {
        'page_obj': page_obj,
    }
    return render(request, template_name, context)


def products_by_category_view(request, category_id):
    """View for list of products by category."""
    template_name = 'products/products_by_category_list.html'

    if request.method == 'POST':
        pattern = request.POST.get('pattern')
        product_list = products_base_view().filter(
            category=category_id).filter(name__contains=pattern)
    elif request.method == 'GET':
        model_filtering = request.GET.get('model-filter')
        product_list = products_base_view(
            order_field=model_filtering
        ).filter(category=category_id)

    page_obj = get_page_object(
            product_list,
            request.GET.get('page'),
            settings.CATEGORIES_PER_PAGE,
    )

    category = Category.objects.get(pk=category_id)

    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, template_name, context)
