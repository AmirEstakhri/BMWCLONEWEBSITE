# payment/views.py

from django.shortcuts import render, redirect
from .forms import OrderForm
from main.models import Product, Customer, Order
from cart.cart import Cart
import stripe
from django.conf import settings

def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save the data or process it
            request.session['name'] = form.cleaned_data['name']
            request.session['address'] = form.cleaned_data['address']
            return redirect('order_summary')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

# payment/views.py

def order_summary(request):
    name = request.session.get('name')
    address = request.session.get('address')

    # Get the cart instance
    cart = Cart(request)

    # Calculate the total price from the cart
    total_price = cart.cart_total()  # Assuming this method returns the total price

    # Store the total price in the session
    request.session['total_price'] = total_price

    return render(request, 'order_summary.html', {
        'name': name,
        'address': address,
        'total_price': total_price
    })


# myapp/views.py


# Set up Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# myapp/views.py
import stripe
from django.conf import settings
from django.shortcuts import render, redirect

# Set up Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    # Retrieve the total amount from the session
    total_amount = request.session.get('total_price', 0) * 100  # Convert to cents

    if request.method == 'POST':
        token = request.POST.get('stripeToken')

        try:
            # Create a charge with Stripe
            charge = stripe.Charge.create(
                amount=total_amount,
                currency='usd',
                description='Order Payment',
                source=token,
            )

            # Payment was successful
            # Optionally, create an order here

            return redirect('order_confirmation')  # Redirect to a confirmation page

        except stripe.error.StripeError as e:
            # Handle error
            return render(request, 'checkout.html', {
                'error': str(e),
                'total_price': total_amount / 100,  # Convert back to dollars for display
            })

    # If it's a GET request
    return render(request, 'checkout.html', {'total_price': total_amount / 100})  # Display total in dollars


def home(request):
    return render(request, 'home.html')
