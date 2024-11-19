from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, "Invalid Username or Password")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Your account has been registered")
            return redirect('dashboard')

    return render(request, 'register.html', {'form':form})

@login_required
def dashboard(request):
    form = TaskForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task has been added!")
            return redirect('dashboard')

    tasks = Task.objects.all().order_by("-created_at")
    return render(request, 'dashboard.html', {'tasks':tasks, "form":form})

def my_tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    return render(request, 'my_tasks.html', {'tasks':tasks})