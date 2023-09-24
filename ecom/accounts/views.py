from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from ecom.accounts.forms import LoginForm, RegisterForm


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list products')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login_user.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list products')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register_user.html', context)


def logout_user(request):
    logout(request)
    return redirect('list products')