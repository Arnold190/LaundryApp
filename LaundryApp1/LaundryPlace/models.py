from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.


current_datetime = timezone.now() 



class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name




class OrderItem(models.Model):
    order = models.ForeignKey('LaundryPlace.Order', related_name='items', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity_kg = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.quantity_kg} kg of {self.service.name} for order {self.order.id}"

class Payment(models.Model):
    order = models.OneToOneField('LaundryPlace.Order', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Payment for order {self.order.id}"
    

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    pickup_date = models.DateTimeField()  
    description = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.item} ({self.quantity}) - {self.status}"