# checkpoint/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomLoginForm, OrderForm
from django.contrib.auth import login
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Order
from django.views.decorators.http import require_POST

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your profile was created successfully. Please log in.')
            return redirect('login')  # Redirect to the login page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'checkpoint/signup.html', {'form': form})  # Use the sign-up template

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()
    return render(request, 'checkpoint/login.html', {'form': form})  # Use the login template


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Associate order with logged-in user
            order.save()
            messages.success(request, 'Order created successfully.')
            return redirect('dashboard')
    else:
        form = OrderForm()

    orders = Order.objects.filter(user=request.user).order_by('created_at')
    context = {
        'form': form,
        'orders': orders
    }
    return render(request, 'LaundryPlace/dashboard.html', context)


@require_http_methods(["POST"])
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('logout')

