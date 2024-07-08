from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile
from .models import Order

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    terms_accepted = forms.BooleanField(required=True, help_text='You must accept the terms and conditions.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
                user_profile = UserProfile(user=user, terms_accepted=self.cleaned_data['terms_accepted'])
                user_profile.save()
            return user

class CustomLoginForm(AuthenticationForm):
    email = forms.CharField(label='email', max_length=254)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='email / Username', required=True)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item', 'quantity','pickup_date', 'description']
        widgets = {
            'pickup_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }