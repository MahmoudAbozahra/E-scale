from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.my_login, name='login'),
    path('sales/', views.sales_view, name='sales'),
    path('birds/', views.birds_view, name='birds'),
    path('car_reg/', views.car_reg, name='car_reg'),
    path('registration/', views.scale_info, name='registration'),
    
    ]