from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone

current_datetime = timezone.now()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    terms_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


class Order(models.Model):
    STATUS_CHOICES = [
         ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkpoint_orders')
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    pickup_date = models.DateTimeField()  
    description = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.item} ({self.quantity}) - {self.status}"