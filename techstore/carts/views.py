from django.shortcuts import redirect, render

from products.models import Product
from .models import Cart


def cart_add(request, product_slug):
    """Adding products into the cart."""
    if request.method == 'POST':
        product = Product.objects.get(slug=product_slug)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)
            product_quantity = int(request.POST.get('quantity'))
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += product_quantity
                    cart.save()
            else:
                Cart.objects.create(
                    user=request.user,
                    product=product,
                    quantity=product_quantity
                )

        return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    if request.method == 'POST':
        product = Product.objects.get(slug=product_slug)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)
            product_quantity = int(request.POST.get('quantity'))
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity = product_quantity
                    cart.save()
            else:
                Cart.objects.create(
                    user=request.user,
                    product=product,
                    quantity=product_quantity
                )

        return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, product_slug):
    if request.method == 'POST':
        product = Product.objects.get(slug=product_slug)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)
            if carts.exists():
                carts.delete()

        return redirect(request.META['HTTP_REFERER'])


def cart_items(request):
    template_name = 'carts/user_cart.html'
    carts = Cart.objects.filter(user=request.user).select_related('product')
    context = {
        'carts': carts,
    }
    return render(request, template_name, context)
