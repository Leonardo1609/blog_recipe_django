from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import LoginForm, RegisterForm
from users.models import Profile
from categories.models import Category


def index(request):
    page_title = 'Home'
    categories = Category.objects.all()
    categories = [{ 'name': category.name, 'slug': category.slug } for category in list(categories)]

    return render(request,'index.html', { 'title': page_title, 'categories': categories })

def login_view(request):

    if request.user.is_authenticated:
        return redirect('index')

    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login_form()

        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user}')
            return redirect('index')
        else:
            messages.error(request, 'Credenciales inválidas')

    return render(request,'users/login.html', { 'login_form': form, 'title': 'Login' })
     
    
def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = RegisterForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.save()
        Profile.objects.create(user=user)

        if user:
            login(request,user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'users/register.html', { 'register_form': form, 'title': 'Register' })

def logout_view(request):
    logout(request)
    messages.success(request, 'Ha finalizado sesión correctamente')
    return redirect('login')
