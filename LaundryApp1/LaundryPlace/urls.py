from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
path('', views.home, name='home'),
path('info/', views.info, name='info'),




path('services/', views.service_list, name='service_list'),
path('services/<int:service_id>/', views.service_detail, name='service_detail'),
path('services/create/', views.service_create, name='service_create'),
path('services/<int:service_id>/update/', views.service_update, name='service_update'),
path('services/<int:service_id>/delete/', views.service_delete, name='service_delete'),
path('orders/', views.order_list, name='order_list'),
path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
path('orders/create/', views.order_create, name='order_create'),
path('orders/<int:order_id>/update/', views.order_update, name='order_update'),
path('orders/<int:order_id>/delete/', views.order_delete, name='order_delete'),

]

