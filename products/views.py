from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.db.models import Q
from .models import Product, Order, OrderItem


# 1. Home Page with Search and Category Filter
def home(request):
    products = Product.objects.all()

    search_query = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category', '').strip()

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__icontains=search_query)
        )

    if selected_category:
        products = products.filter(category=selected_category)

    categories = Product.objects.values_list(
        'category', flat=True
    ).distinct()

    return render(request, 'products/home.html', {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'selected_category': selected_category
    })


# 2. Product Details Page
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'products/product_detail.html', {
        'product': product
    })


# 3. Add to Cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_id = str(product.id)
    current_quantity = cart.get(product_id, 0)

    if current_quantity < product.stock:
        cart[product_id] = current_quantity + 1

    request.session['cart'] = cart

    return redirect('home')


# 4. Cart Page
def cart_view(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)

            subtotal = product.price * quantity
            total += subtotal

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })

        except Product.DoesNotExist:
            continue

    return render(request, 'products/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


# 5. Remove from Cart
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


# 6. Update Cart
def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    action = request.POST.get('action')

    if product_id in cart:
        product = get_object_or_404(Product, id=product_id)

        if action == 'increase':
            if cart[product_id] < product.stock:
                cart[product_id] += 1

        elif action == 'decrease':
            cart[product_id] -= 1

            if cart[product_id] <= 0:
                del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


# 7. Checkout Page and Order Processing
def checkout_view(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart')

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)

            subtotal = product.price * quantity
            total += subtotal

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })

        except Product.DoesNotExist:
            continue

    if not cart_items:
        request.session['cart'] = {}
        return redirect('cart')

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()

        if not all([customer_name, email, phone, address]):
            return render(request, 'products/checkout.html', {
                'cart_items': cart_items,
                'total': total,
                'error': 'Please fill in all customer details.'
            })

        try:
            with transaction.atomic():
                order_products = []
                order_total = 0

                for product_id, quantity in cart.items():
                    product = Product.objects.select_for_update().get(
                        id=product_id
                    )

                    if quantity <= 0 or product.stock < quantity:
                        raise ValueError(
                            f'Insufficient stock for {product.name}.'
                        )

                    subtotal = product.price * quantity
                    order_total += subtotal
                    order_products.append((product, quantity))

                order = Order.objects.create(
                    customer_name=customer_name,
                    email=email,
                    phone=phone,
                    address=address,
                    total_amount=order_total
                )

                for product, quantity in order_products:
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        product_name=product.name,
                        price=product.price,
                        quantity=quantity
                    )

                    product.stock -= quantity
                    product.save(update_fields=['stock'])

            request.session['cart'] = {}

            return redirect('order_success', order_id=order.id)

        except (Product.DoesNotExist, ValueError) as error:
            return render(request, 'products/checkout.html', {
                'cart_items': cart_items,
                'total': total,
                'error': str(error)
            })

    return render(request, 'products/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


# 8. Order Success Page
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'products/success.html', {
        'order': order
    })