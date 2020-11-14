from django.shortcuts import render

# Create your views here.

def home(request):
   return render(request, 'home.html')

def login(request):
   return render(request, 'login.html')

def customer(request):
   return render(request, 'home_loggedin_customer.html')

def file_form(request):
   return render(request, 'file_form.html')