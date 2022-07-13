from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout

def index(request):
    post = Post.objects.all()
    return render(request, 'forum/index.html', {'post': post, 'title': 'список'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'forum/login.html', {'form': form, })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'forum/register.html', {"form": form, })