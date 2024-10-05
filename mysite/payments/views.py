# payments/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
import stripe
from main.models import Product
from .models import Order as PaymentOrder
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from cart.cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY

from django.shortcuts import render, redirect
from .models import PaymentOrder
from cart.cart import Cart  # Adjust the import as necessary

from django.shortcuts import render, redirect
from .models import PaymentOrder
from cart.cart import Cart  # Adjust the import as necessary

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PaymentOrder
from cart.cart import Cart  # Adjust the import as necessary

# from django.contrib.auth.decorators import login_required
# from django.db import IntegrityError
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .models import PaymentOrder
# from cart.cart import Cart  # Adjust the import as necessary
# import stripe
# from django.conf import settings

# stripe.api_key = settings.STRIPE_SECRET_KEY  # Use your Stripe secret key

# @login_required
# def process_payment(request):
#     cart = Cart(request)  # Initialize your cart
#     total_amount = cart.cart_total()  # Calculate total amount from the cart

#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         stripe_token = request.POST.get('stripeToken')

#         # Create a PaymentOrder instance and assign the user
#         payment_order = PaymentOrder(
#             user=request.user,
#             full_name=full_name,
#             email=email,
#             address=address,
#             total_amount=total_amount,
#         )

#         try:
#             payment_order.save()

#             # Charge the user's card
#             charge = stripe.Charge.create(
#                 amount=int(total_amount * 100),  # Amount in cents
#                 currency='usd',
#                 description='Payment for order {}'.format(payment_order.id),
#                 source=stripe_token,
#             )

#             # Redirect to the order confirmation page
#             return redirect('order_confirmation', order_id=payment_order.id)

#         except stripe.error.StripeError as e:
#             # Handle error and show a message to the user
#             return render(request, 'payments/error.html', {'error': str(e)})
#         except IntegrityError as e:
#             return HttpResponse("An error occurred while processing your payment.")

#     # If GET request or if there's an issue, redirect to checkout
#     return redirect('checkout')  # You might want to return a proper response here if needed

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import PaymentOrder
from cart.cart import Cart  # Adjust the import as necessary

@login_required
def process_payment(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        # Create a PaymentOrder instance
        payment_order = PaymentOrder(
            user=request.user,  # Set the user here
            full_name=full_name,
            email=email,
            address=address,
            total_amount=0.0,  # Set to 0.0 or your fixed amount since payment isn't being processed
            # other fields...
        )

        payment_order.save()  # Save the order

        # Redirect to the order status page immediately
        return redirect('order_status', order_id=payment_order.id)

    return redirect('checkout')  # Redirect to checkout if the request is not POST


def order_confirmation(request, order_id):
    order = PaymentOrder.objects.get(id=order_id)  # Retrieve the order
    return render(request, 'payments/order_confirmation.html', {'order': order})


def order_status(request, order_id):
    order = get_object_or_404(PaymentOrder, id=order_id)
    return render(request, 'payments/order_status.html', {'order': order})

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods  # Get cart products
    totals = cart.cart_total()  # Calculate total

    user_info = {}
    if request.method == 'POST':
        # Here, you'll collect user information if the form is submitted
        user_info['first_name'] = request.POST.get('first_name')
        user_info['last_name'] = request.POST.get('last_name')
        user_info['email'] = request.POST.get('email')

    return render(request, "checkout.html", {
        "cart_products": cart_products,
        "totals": totals,
        "user_info": user_info,
    })
