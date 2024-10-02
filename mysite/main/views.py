from django.shortcuts import render ,redirect
from django.http import HttpResponse       
from rest_framework import generics
from .models import BlogPost
from .serializers import Blogpostserializer
from .models import Product , Category
from django.contrib.auth import aauthenticate , login , logout ,authenticate
from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import SignUpForm 


# def signup_user(request):
#     form = SignUpForm
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.cleaned_data['user']
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'] , password = password2 ) 
#             messages.success(request , 'User created successfully. You are now able to log in.')
#             user.save()
#             login(request, user) 
#           #  return redirect("home")
#           # # Log the user in after signup
#            # return redirect('home')  # Redirect to a home page or desired location
#     else:
#         messages.error(request, 'Form is not valid.')
#         form = SignUpForm()
    
#     return render(request, 'signup.html', {'form': form})

# 
from django.db import IntegrityError

def signup_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                user.save()  # Save the user after validation
                messages.success(request, 'User created successfully. You are now able to log in.')
                login(request, user) 
                return redirect("home")  # Redirect to a home page or desired location
            except IntegrityError:
                messages.error(request, 'Username already exists. Please choose another one.')
        else:
            messages.error(request, 'Form is not valid.')
    return render(request, 'signup.html', {'form': form})



class BlogpostListCreate (generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = Blogpostserializer
    
class BlogPostRetriaveUpdate (generics.RetrieveAPIView):
     queryset = BlogPost.objects.all()
     serializer_class = Blogpostserializer
     lookup_field = 'pk'


def category(request,cat):
    cat = cat.replace('-' , ' ')
    try :
        category = Category.objects.get(name__iexact=cat)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except Category.DoesNotExist:
        return HttpResponse("Category not found")
    

# 
def index(response):
    product = Product.objects.all()
    return   render (response, "home-1.html" , {'products': product})  
      #
          
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render (request, "product.html", {'product': product})  

def accountsprofile(request,):
    return render (request, "accountsprofile.html" )



# def login_user(request):
#     if request.method == "POST":     
        
#             email = request.POST.get['email']
#             password = request.POST.get['password']
            
#             user = authenticate( request , email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Login successful')
#                 return redirect ("index"  )
#             else :
#                 messages.error(request, 'Invalid credentials')
#                 return redirect ("login"  )      
#     else   :    
#             return   render (request, "login.html"  )  
# def login_user(request):
#     if request.method == "POST":
#         email = request.POST.get('email')  # Use parentheses here
#         password = request.POST.get('password')  # Use parentheses here
        
#         # Use 'username' instead of 'email' if you're using username field
#         user = authenticate(request, username=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Login successful')
#             return redirect("index")
#         else:
#             messages.error(request, 'Invalid credentials')
#             return redirect("login")
#     else:
#         return render(request, "login.html")

from django.contrib.auth.backends import ModelBackend  # Adjust based on your backends

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')  # Make sure this matches your form field
        password = request.POST.get('password')
        
        # Specify the backend here, if you're using a specific one
        user = authenticate(request, username=email, password=password, backend='your_backend_here')
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect("index")
        else:
            messages.error(request, 'Invalid credentials')
            return redirect("login")
    else:
        return render(request, "login.html")

def logout_user(request):
       logout(request)
       messages.success(request, 'Logged out successfully')
       return   redirect ("index"  )

def about(response):
    return render(response, "about.html")
#@property
#def image_url(self):
   # if self.image and hasattr(self.image, 'url'):
       # return self.image.url

def home(response):
    return render(response, "home-1.html")   

