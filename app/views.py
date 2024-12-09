from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def home(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.warning(request, "Invalid Username or Password")
                return redirect('home')
        else:
            return render(request, 'home.html', {})
    else:
        return redirect('dashboard')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, "Invalid Username or Password")
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

    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    context = {
        'tasks': tasks,
        'form': form
    }
    
    return render(request, 'dashboard.html', context)

@login_required
def my_tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    return render(request, 'my_tasks.html', {'tasks':tasks})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.user.username == task.user.username:
        task.delete()
        messages.success(request, "Task has been removed")
        return redirect('dashboard')
    messages.warning(request, "You don't have the proper permissions to remove that task")
    return redirect('dashboard')

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.user.username != task.user.username:
        messages.error(request, "You don't have the proper permissions to edit that task")
        return redirect('dashboard')

    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task has been updated!")
            return redirect('dashboard')
    return redirect('dashboard')

@login_required
def update_status(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=pk, user=request.user)
        new_status = request.POST.get('status')

        if new_status in [Task.STATUS_NOT_STARTED, Task.STATUS_IN_PROGRESS, Task.STATUS_COMPLETED]:
            task.status = new_status
            task.save()
    return redirect('dashboard')

def about_page(request):
    return render(request, 'about.html', {})

def contact_us(request):
    return render(request, 'contact_us.html', {})

def profile_view(request):
    return render(request, 'profile.html', {
        'username': request.user.username,
        'email': request.user.email,
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        
        if form.is_valid():
            # Save the new password and update session
            form.save()
            update_session_auth_hash(request, form.user)  # Keep the user logged in after password change
            messages.success(request, "Your password has been successfully updated.")
            return redirect('profile')  # Redirect to the profile page
        else:
            # If form is invalid, display error message
            messages.error(request, "Your new password doesn't meet the required guidelines.")
    
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'change_password.html', {'form': form})