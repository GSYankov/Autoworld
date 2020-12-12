from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
import orders
from orders.models import Offer, Order
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.views.decorators.http import require_safe, require_POST
from orders.forms import OfferForm
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderCreateView(LoginRequiredMixin, CreateView):
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
    orders = Order.objects.all()
    my_offered_orders_ids = [
        offer.order.id for offer in Offer.objects.filter(trader=request.user)]
    context = {
        "orders": orders,
        "my_offered_orders_ids": my_offered_orders_ids
    }

    return render(request, 'orders/list-orders.html', context)


class MyOrdersList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/list-orders.html'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)


def make_offer(request, order_id):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid:
            offer = form.save(commit=False)
            offer.order = Order.objects.get(id=order_id)
            offer.trader = request.user
            offer.save()
        return redirect('orders list')


class MyOffersList(LoginRequiredMixin, ListView):
    model = Offer
    template_name = 'orders/list-offers.html'

    def get_queryset(self):
        return Offer.objects.filter(trader=self.request.user)


class MyOrdersCustomerList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/list-orders-customer.html'

    def get_queryset(self):
        queryset = Order.objects.filter(customer=self.request.user)
        # queryset = Order.objects.filter(offer__order__customer=self.request.user)

        return queryset


class GetOffersListByOrderId(LoginRequiredMixin, ListView):
    model = Offer
    template_name = 'orders/list-offers-by-order.html'

    def get_queryset(self):
        return Offer.objects.filter(order__id=self.kwargs['order_id'])


@require_POST
def accept_offer(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    offer.isAccepted = True
    offer.save()
    return redirect('my orders customer')


class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['description']
    template_name = 'orders/order-edit.html'
    success_url = '/'


class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('my offers')
    template_name = 'orders/order-delete.html'