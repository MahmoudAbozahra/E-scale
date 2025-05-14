from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
import socket
from django.utils.timezone import now
from django.shortcuts import render, redirect
from .forms import ScaleInfoForm
from .models import ScaleInfo



def my_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  
            return redirect('/')
    else:
        form = LoginForm() 

    return render(request, 'pages/login.html', {'form': form})


@login_required(login_url='login') 
def index(request):
    return render(request, 'pages/index.html')

def sales_view(request):
    return render(request, 'pages/sales.html')

def birds_view(request):
    if request.method == 'POST':
        form = BirdSaleForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "تم الحفظ بنجاح.")
           return redirect('birds')      
    else:
        form = BirdSaleForm()

    return render(request, 'pages/birds.html', {'form': form})
    
def car_reg(request):
    return render(request, 'pages/car_reg.html')



# def clint_file(request):
#     if request.method == 'POST':
#         form = ClintFileForm(request.POST)
#         if form.is_valid():
#            form.save()
#            messages.success(request, "تم الحفظ بنجاح.")
#            if Clint_file.category == 'طيور':
#                return redirect('birds')
               
#            return redirect('birds')      
#     else:
#         form = ClintFileForm()

#     return render(request, 'pages/birds.html', {'form': form})
    
# def car_reg(request):
#     return render(request, 'pages/registration.html')






SCALE_IP = '192.168.1.56' 
SCALE_PORT = 25           
def get_weight_from_scale():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((SCALE_IP, SCALE_PORT))
        data = sock.recv(1024)
        sock.close()
        return float(data.decode().strip())
    except Exception as e:
        print("Error reading from scale:", e)
        return None


def scale_info(request):
    saved = False
    saved_weight = None
    saved_time = None

  
    if request.method == 'POST':
        form = ScaleInfoForm(request.POST)
        if form.is_valid():
            scale = form.save(commit=False)
            scale.save()
            saved = True
            saved_weight = scale.weight
            saved_time = scale.created_at  
    else:
        
        live_weight = get_weight_from_scale()
        form = ScaleInfoForm(initial={'weight': live_weight})

    context = {
        'form': form,
        'saved': saved,
        'saved_weight': saved_weight,
        'saved_time': saved_time,
    }

    return render(request, 'pages/registration.html', context)
