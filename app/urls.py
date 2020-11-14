from django.urls import path
from app.views import home, login, customer, file_form

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('customer/', customer, name='customer'),

    path('fform/', file_form, name='file-form'),
]
