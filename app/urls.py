from django.urls import path
from app.views import home, login_user, logout_user, register_user, customer, file_form

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/<role>', register_user, name='register'),
    path('customer/', customer, name='customer'),

    path('fform/', file_form, name='file-form'),
]
