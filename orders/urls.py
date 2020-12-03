from orders.views import OrderCreateView, orders_list, MyOrdersList, make_offer
from django.urls import path, include


urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='orders create'),
    path('list/', orders_list, name='orders list'),
    path('my/', MyOrdersList.as_view(), name='my orders'),
    path('offer/<int:order_id>', make_offer, name='make offer'),
]
