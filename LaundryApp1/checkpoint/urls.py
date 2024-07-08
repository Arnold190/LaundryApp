from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('signup/', views.signup, name='signup'),  
    path('login/', auth_views.LoginView.as_view(template_name='checkpoint/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(template_name='checkpoint/logout.html'), name='logout'),
]
