from django.shortcuts import render ,redirect
from django.http import HttpResponse       
from rest_framework import generics
from .models import BlogPost
from .serializers import Blogpostserializer
from .models import Product , Category
from django.contrib.auth import aauthenticate , login , logout ,authenticate
from django.contrib import messages

from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import BlogPost, Product, Category
from .forms import BlogPostForm, ProductForm, CategoryForm
from django.shortcuts import render, redirect
from .forms import SignUpForm 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Product, Category
from .forms import ProductForm, CategoryForm
# main/views.py

from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost, Product, Category
from .forms import BlogPostForm, ProductForm, CategoryForm
from django.contrib.auth.models import User

from django.views.generic import ListView, UpdateView
from django.contrib.auth.models import User
from .forms import UserForm  # You will create this form
# main/views.py

from django.views.generic import ListView, UpdateView
from django.contrib.auth.models import User
from .forms import UserForm  # Ensure this form is defined
# main/views.py

from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('admin_dashboard')  # Redirect to admin dashboard or user list
    else:
        form = UserRegisterForm()
    return render(request, 'register_user.html', {'form': form})


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm  # Ensure this form is defined
    template_name = 'edit_user.html'
    success_url = reverse_lazy('user_list')


# User List View
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

# User Update View
class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm  # Make sure you create this form
    template_name = 'edit_user.html'
    success_url = reverse_lazy('user_list')


# List Views
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    context_object_name = 'blogposts'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

# Edit Views
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'edit_blogpost.html'
    success_url = reverse_lazy('blogpost_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit_product.html'
    success_url = reverse_lazy('product_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'edit_category.html'
    success_url = reverse_lazy('category_list')

# Delete Views
class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('product_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('category_list')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('admin_dashboard')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create_category.html'
    success_url = reverse_lazy('admin_dashboard')



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


# main/views.py


class AdminDashboardView(TemplateView):
    template_name = 'admin_dashboard.html'

class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create_blogpost.html'
    success_url = reverse_lazy('admin_dashboard')

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('admin_dashboard')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create_category.html'
    success_url = reverse_lazy('admin_dashboard')
