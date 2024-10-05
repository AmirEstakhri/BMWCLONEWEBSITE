from django.urls import path ,include
from . import views
from .views import  about,login_user , logout_user , SignUpForm, signup_user
from .views import signup_user
from .views import AdminDashboardView, BlogPostCreateView, ProductCreateView, CategoryCreateView
from .views import (
    BlogPostListView, BlogPostUpdateView, BlogPostDeleteView,
    ProductListView, ProductUpdateView, ProductDeleteView,
    CategoryListView, CategoryUpdateView, CategoryDeleteView,
    UserListView, UserUpdateView 
)
from .views import register_user  



urlpatterns = [
path("", views.index, name="index"),
path("home-1/", views.index, name="home-1"), 
path("login/", views.login_user, name="login"),
path("logout/", views.logout_user , name="logout"),
path("about/", about, name="about"),
path('signup/', signup_user, name='signup'),
path('register/', register_user, name='register_user'),
path('blogposts/', BlogPostListView.as_view(), name='blogpost_list'),
path('blogpost/edit/<int:pk>/', BlogPostUpdateView.as_view(), name='edit_blogpost'),
path('blogpost/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete_blogpost'),

path('products/', ProductListView.as_view(), name='product_list'),
path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    
path('categories/', CategoryListView.as_view(), name='category_list'),
path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='edit_category'),
path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
   
path('users/', UserListView.as_view(), name='user_list'),
path('user/edit/<int:pk>/', UserUpdateView.as_view(), name='edit_user'),

path('accounts/profile/', views.accountsprofile, name='accountsprofile'),
path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
path('admin-dashboard/create-blogpost/', BlogPostCreateView.as_view(), name='create_blogpost'),
path('admin-dashboard/create-product/', ProductCreateView.as_view(), name='create_product'),
path('admin-dashboard/create-category/', CategoryCreateView.as_view(), name='create_category'),

path ('product/<int:pk>' , views.product , name="product"),
path ('category/<str:cat>' , views.category , name="category"),




]
