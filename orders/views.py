import orders
from orders.models import Offer, Order
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.views.decorators.http import require_safe

class OrderCreateView(CreateView):
    model = Order
    template_name = 'orders/create-order.html'
    fields = ('description',)
    success_url = '/'
    def form_valid(self, form):
         order = form.save(commit=False)
         order.customer = self.request.user
         self.object = order.save()
         return super().form_valid(form)

@require_safe
def orders_list(request):
    orders=Order.objects.all()
    my_offered_orders_ids=[offer.id for offer in Offer.objects.filter(trader=request.user)]
    context={
        "orders": orders,
        "my_offered_orders_ids": my_offered_orders_ids
    }

    return render(request, 'orders/list-orders.html', context)

class MyOrdersList(ListView):
    model = Order
    template_name = 'orders/list-orders.html'
    
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

def make_offer(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(id=order_id)
        trader = request.user
        offer = Offer(trader=trader, order=order)
        offer.save()
        return redirect('orders list')

