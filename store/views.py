from decimal import ROUND_HALF_UP, Decimal

import stripe
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SignUpForm
from .models import Category, Order, OrderItem, Product, UserProfile

stripe.api_key = settings.STRIPE_SECRET_KEY


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    recommended = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'store/product_detail.html', {'product': product, 'recommended': recommended})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'store/signup.html', {'form': form})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_key = str(product_id)
    if product_key in cart:
        del cart[product_key]
        request.session['cart'] = cart
    return redirect('cart_detail')


def save_for_later(request, product_id):
    cart = request.session.get('cart', {})
    saved_items = request.session.get('saved_items', {})
    product_key = str(product_id)
    if product_key in cart:
        quantity = cart.pop(product_key)
        saved_items[product_key] = saved_items.get(product_key, 0) + quantity
        request.session['cart'] = cart
        request.session['saved_items'] = saved_items
    return redirect('cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = Decimal('0.00')
    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(pk=product_id)
            item_total = product.price * quantity
            total += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
            })
        except Product.DoesNotExist:
            pass
    return render(request, 'store/cart_detail.html', {'cart_items': cart_items, 'total': total})


def checkout(request):
    cart = request.session.get('cart', {})
    total = Decimal('0.00')
    products = []
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total += product.price * quantity
        products.append({'product': product, 'quantity': quantity})
    # Calculate tax (8.5%) on the total (in dollars)
    tax = (total * Decimal('0.085')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    grand_total = total + tax
    return render(request, 'store/checkout.html', {
        'products': products,
        'total': total,
        'tax': tax,
        'grand_total': grand_total,
    })


def payment(request):
    cart = request.session.get('cart', {})
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        price_in_cents = int(product.price * Decimal('100'))
        total += price_in_cents * quantity
    # Calculate tax as 8.5% of the total in cents
    tax = (Decimal(total) * Decimal('0.085')).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    grand_total = total + int(tax)
    intent = stripe.PaymentIntent.create(
        amount=grand_total,
        currency='usd',
        metadata={'integration_check': 'accept_a_payment'},
    )
    return render(request, 'store/payment.html', {
        'client_secret': intent.client_secret,
        'total': grand_total / 100,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    })


@login_required
def process_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('product_list')
    order = Order.objects.create(user=request.user, paid=True)
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        OrderItem.objects.create(order=order, product=product, price=product.price, quantity=quantity)
    request.session['cart'] = {}
    return render(request, 'store/order_confirmation.html', {'order': order})


def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        from django.contrib.postgres.search import SearchVector
        results = Product.objects.annotate(
            search=SearchVector('name', 'description'),
        ).filter(search=query)
    return render(request, 'store/search_results.html', {'results': results, 'query': query})


def recommendations(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recommended = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'store/recommendations.html', {'recommended': recommended})


@login_required
def profile(request):
    return render(request, 'store/profile.html')


def custom_logout(request):
    print("Logout method:", request.method)  # Debug print
    if request.method == 'POST':
        logout(request)
        return redirect('product_list')
    return HttpResponseNotAllowed(['POST'])
