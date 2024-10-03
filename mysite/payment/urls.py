# myapp/urls.py

from django.urls import path
from .views import order_form, order_summary, checkout, home

urlpatterns = [
    path('', home, name='home'),
    path('order/', order_form, name='order_form'),
    path('order/summary/', order_summary, name='order_summary'),
    path('checkout/', checkout, name='checkout'),
    
]
