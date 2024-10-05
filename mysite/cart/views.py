from django.shortcuts import render, get_object_or_404
from .cart import Cart
from main.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    """Render the cart summary page."""
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {
        "cart_products": cart_products,
        "quantities": quantities,
        "totals": totals
    })

def cart_add(request):
    """Add a product to the cart."""
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()
        messages.success(request, "Product added to cart.")
        return JsonResponse({'qty': cart_quantity})

def cart_delete(request):
    """Remove a product from the cart."""
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        messages.success(request, "Item deleted from shopping cart.")
        return JsonResponse({'product': product_id})

def cart_update(request):
    """Update the quantity of a product in the cart."""
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        messages.success(request, "Your cart has been updated.")
        return JsonResponse({'qty': product_qty})

def cart_total(cart):
    """Calculate the total price of items in the cart."""
    total = 0
    for item in cart:
        product = item['product']
        if product.is_sales:
            total += product.sales_price * item['quantity']
        else:
            total += product.price * item['quantity']
    return total
