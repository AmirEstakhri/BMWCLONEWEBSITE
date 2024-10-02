from django.urls import path ,include
from . import views
from .views import  about,login_user , logout_user , SignUpForm, signup_user
from .views import signup_user



urlpatterns = [
path("", views.index, name="index"),
path("home-1/", views.index, name="index"),
path("blogposts/", views.BlogpostListCreate.as_view() , name="blogposts-view-create"),
path("blogpost/<int:pk>/", views.BlogPostRetriaveUpdate.as_view() , name="blogpost-retriave-update"),
#path ('product/' , views.Product , name="product-view"),
path("login/", views.login_user, name="login"),
path("logout/", views.logout_user , name="logout"),
path("about/", about, name="about"),
path('signup/', signup_user, name='signup'),

path('accounts/profile/', views.accountsprofile, name='accountsprofile'),


path ('product/<int:pk>' , views.product , name="product"),
path ('category/<str:cat>' , views.category , name="category"),




]
