from django.shortcuts import render, redirect
from app.forms import ImageForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def customer(request):
    return render(request, 'home_loggedin_customer.html')


def file_form(request):
    if request.method == 'GET':
        context = {
            'form': ImageForm
        }
        return render(request, 'file_form.html', context)
    else:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.save()
            return redirect('home')

        context = {
            'form': form
        }

        return render(request, 'file_form.html', context)
