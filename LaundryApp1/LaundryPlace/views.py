from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Service, Order, OrderItem
from .forms import ServiceForm, OrderForm, OrderItemForm
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order
from django.contrib import messages  # Import messages framework

def home(request):
    return render(request, 'LaundryPlace/home.html')

def info(request):
    return render(request, 'LaundryPlace/info.html')

@login_required
def dashboard(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('dashboard')
    else:
        form = OrderForm()

    orders = Order.objects.filter(user=request.user).order_by('created_at')
    context = {
        'form': form,
        'orders': orders
    }
    return render(request, 'LaundryPlace/dashboard.html', context)

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            messages.success(request, 'Order created successfully.')
            return redirect('LaundryPlace:dashboard')
    else:
        form = OrderForm()
    return render(request, 'LaundryPlace/dashboard.html')


def signup(request):
    return render(request, 'checkpoint/signup.html')


def login(request):
    return render(request, 'checkpoint/login.html')


def logout_view(request):
    return render(request, 'checkpoint/logout.html')





def service_list(request):
    services = Service.objects.all()
    return render(request, 'laundry/service_list.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'laundry/service_detail.html', {'service': service})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'laundry/service_form.html', {'form': form})

def service_update(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_detail', service_id=service.id)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'laundry/service_form.html', {'form': form})

def service_delete(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'laundry/service_confirm_delete.html', {'service': service})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'laundry/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'laundry/order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'laundry/order_form.html', {'form': form})

def order_update(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)
    return render(request, 'laundry/order_form.html', {'form': form})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'laundry/order_confirm_delete.html', {'order': order})

# Create your views here.

#def v1(response):
 #   return HttpResponse('Laundry Place v1')

