from orders.views import OrderCreateView, orders_list, MyOrdersList, make_offer, MyOffersList, MyOrdersCustomerList
from django.urls import path, include


urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='orders create'),
    path('list/', orders_list, name='orders list'),
    path('my/orders/', MyOrdersList.as_view(), name='my orders'),
    path('my/orders/customer', MyOrdersCustomerList.as_view(), name='my orders customer'),
    path('offer/<int:order_id>', make_offer, name='make offer'),
    path('my/offers/', MyOffersList.as_view(), name='my offers'),
]
