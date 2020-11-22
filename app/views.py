from django.shortcuts import render, redirect
from app.forms import LoginForm, ImageForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "GET":
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)
    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
            else:
                context = {
                    'error': 'Wrong username or password!'
                }

                return render(request, 'login.html', context)
        else:
            context = {
                'form': form
            }

            return render(request, 'login.html', context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
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
