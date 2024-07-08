from django.contrib import admin
from .models import Service, Order, OrderItem, Payment
from checkpoint.models import Order

admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
