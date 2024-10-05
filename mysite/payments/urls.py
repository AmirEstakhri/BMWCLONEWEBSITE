

from django.urls import path
from .views import checkout, order_status , process_payment , order_confirmation

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('order-status/<int:order_id>/', order_status, name='order_status'),
    path('process_payment/', process_payment, name='process_payment'),
    path('order_status/<int:order_id>/', order_status, name='order_status'),
    path('order_confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),




]
