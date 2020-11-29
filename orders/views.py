from orders.models import Order
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

class OrderCreateView(CreateView):
    model = Order
    template_name = 'orders/create-order.html'
    fields = '__all__'
    success_url = 'home'