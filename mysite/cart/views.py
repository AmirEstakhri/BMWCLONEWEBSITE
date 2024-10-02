from django.shortcuts import render , get_object_or_404
from . import urls
from .cart  import Cart 

from main.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    return render(request , "cart_summary.html" , {})
    
# def cart_add(request, pk):
#     cart = Cart(request)
#     if request.POST.get ('action') == 'post' :
#          property_id =  int(request.POST.get('property_id') ) 
#          product =get_object_or_404(Product, id=pk)
         
#          cart.add(product=product)             v1
#          print("toch")
#          respose  = JsonResponse({'prosuct_name' : product.name  })
#          return respose 
         
 # Adjust this import based on your project structure

def cart_add(request, pk):
    cart = Cart(request)
    if request.method == 'GET':
        product = get_object_or_404(Product, id=pk)
        
        # Adding the product to the cart
        cart.add(product=product)
        print("Product added to cart")
        
        cart_quantity = cart.__len__()
        # Return a JSON response
       # response = JsonResponse({'product_name': product.name})
        response = JsonResponse({'qnt': cart_quantity})

        return response

    # If it's not a POST request, you can return an error response
    return JsonResponse({'error': 'Invalid request'}, status=400)

  # Ensure to import your Cart class

def cart_add(request, pk):
    cart = Cart(request)
    if request.method == 'GET':
        product = get_object_or_404(Product, id=pk)
        
        # Adding the product to the cart
        cart.add(product=product)
        print("Product added to cart")
        
        cart_quantity = cart.__len__()  # Get the total number of items in the cart
        
        # Return a JSON response with quantity and success status
        response = JsonResponse({
            'status': 'success',  # Indicate success
            'cart_quantity': cart_quantity,  # Include the cart quantity
            'product_name': product.name  # Optionally include product name
        })

        return response
    print("Product  not added to cart")

    # If it's not a GET request, you can return an error response
    return JsonResponse({'error': 'Invalid request'}, status=400) 


         
def cart_delete(request):
    pass

def cart_update(request):
    pass