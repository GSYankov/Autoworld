from django.shortcuts import render, redirect
from app.forms import LoginForm, ImageForm, RegisterForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


# Create your views here.


def home(request):
    if request.user.groups.filter(name='customer').exists():
        return redirect('orders create')

    if request.user.groups.filter(name='trader').exists():
        return redirect('orders list')

    return render(request, 'home.html')


def register_user(request, role):
    if request.method == 'GET':
        context = {
            'form': RegisterForm(),
            'role': role
        }
        return render(request, 'auth/register.html', context)
    else:
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            user_group = Group.objects.get(name=role)
            user_group.user_set.add(user)
            login(request, user)

            return redirect('home')

        context = {
            'form': register_form
        }
        return render(request, 'auth/register.html', context)


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

        redirect_url = request.POST.get('next')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(redirect_url if redirect_url else 'home')
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


@login_required
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
