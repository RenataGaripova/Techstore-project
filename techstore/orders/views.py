"""Views for orders app."""
from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import ValidationError
from django.contrib import messages

from carts.models import Cart
from .models import OrderItem


@login_required
def create_order(request):
    """Create new order."""
    if request.method == 'POST':
        form = OrderForm(request.POST, request=request)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    carts = Cart.objects.filter(user=user)

                    if carts.exists():
                        order = form.save()
                    for cart in carts:
                        product = cart.product
                        name = cart.product.name
                        price = cart.product.sell_price
                        quantity = cart.quantity

                        if product.quantity < quantity:
                            raise ValidationError(
                                f"We don't have enough {name} in stock\
                                The remaining quantity is - {product.quantity}"
                            )

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )
                        product.quantity -= quantity
                        product.save()

                    carts.delete()
                    messages.success(request, 'Order has been placed!')
                    return redirect('accounts:profile', user.username)
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('orders:create_order')
    else:
        form = OrderForm()
        context = {
            'form': form,
        }
        return render(request, 'orders/order.html', context=context)
