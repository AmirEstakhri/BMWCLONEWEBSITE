from django.shortcuts import render, get_object_or_404
from .cart import Cart
from main.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	totals = cart.cart_total()
	return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals})

def cart_add(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		# lookup product in DB
		product = get_object_or_404(Product, id=product_id)
		
		# Save to session
		cart.add(product=product, quantity=product_qty)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
		response = JsonResponse({'qty': cart_quantity})
		messages.success(request, ("Product Added To Cart..."))
		return response

def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		# Call delete Function in Cart
		cart.delete(product=product_id)

		response = JsonResponse({'product':product_id})
		#return redirect('cart_summary')
		messages.success(request, ("Item Deleted From Shopping Cart..."))
		return response


def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		cart.update(product=product_id, quantity=product_qty)

		response = JsonResponse({'qty':product_qty})
		#return redirect('cart_summary')
		messages.success(request, ("Your Cart Has Been Updated..."))
		return response

# def cart_total(self):
#     total = 0
#     product_ids = self.cart.keys()  # Get product IDs from the cart
#     products = Product.objects.filter(id__in=product_ids)  # Fetch product instances

#     for product in products:
#         qty = self.cart[str(product.id)]  # Access quantity from the cart
#         # Calculate total based on whether the product is on sale
#         if product.is_sales and product.sale_price != 0:
#             total += product.sale_price * qty
#         else:
#             total += product.price * qty

#     return total

def cart_total(cart):
    total = 0
    for item in cart:
        product = item['product']
        if product.is_sales:  # Use is_sales
            total += product.sales_price * item['quantity']  # Correct field name
        else:
            total += product.price * item['quantity']  # Regular price
    return total
