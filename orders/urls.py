from orders.views import OrderCreateView
from django.urls import path, include


urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='orders create')
]
