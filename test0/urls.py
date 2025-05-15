from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.my_login, name='login'),
    path('sales/', views.sales_view, name='sales'),
    path('birds/', views.birds_view, name='birds'),
    path('registration/', views.registration_view, name='registration'),
    
    ]