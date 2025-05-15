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
from .consumers import clean_data


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

    return render(request, 'pages/registration.html', {'form': form})
    


def clint_file(request):
    if request.method == 'POST':
        form = ClintFileForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "تم الحفظ بنجاح.")
           if Clint_file.category == 'طيور':
               return redirect('birds')
               
           return redirect('birds')      
    else:
        form = ClintFileForm()

    return render(request, 'pages/birds.html', {'form': form})
    from django.shortcuts import render, redirect


SCALE_IP = '192.168.1.56' 
SCALE_PORT = 25           

def get_weight_from_scale():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((SCALE_IP, SCALE_PORT))
        data = sock.recv(1024)
        sock.close()
        cleaned_data = clean_data(data.decode().strip())
        return float(cleaned_data) if cleaned_data else None
    except Exception as e:
        print("Error reading from scale:", e)
        return None

def registration_view(request):
    if request.method == 'POST':
        if 'print_ticket' in request.POST:
            clint_form = ClintFileForm(request.session.get('clint_form_data'))
            scale_form = ScaleInfoForm(request.session.get('scale_form_data'))
            car_form = CarInfoForm(request.session.get('car_form_data'))

            if all([clint_form.is_valid(), scale_form.is_valid(), car_form.is_valid()]):
                clint_form.save()
                scale_form.save()
                car_form.save()
                messages.success(request, "تم حفظ جميع البيانات وطباعة التذكرة.")
                return redirect('registration')

        else:
            # حفظ مؤقت في السيشن لكل فورم
            if 'save_clint' in request.POST:
                request.session['clint_form_data'] = request.POST

            elif 'save_scale' in request.POST:
                request.session['scale_form_data'] = request.POST

            elif 'save_car' in request.POST:
                request.session['car_form_data'] = request.POST

            return redirect('registration')

    # تهيئة الفورمات عند العرض
    clint_form = ClintFileForm(request.session.get('clint_form_data'))
    scale_form = ScaleInfoForm(request.session.get('scale_form_data', {'weight': get_weight_from_scale()}))
    car_form = CarInfoForm(request.session.get('car_form_data'))

    context = {
        'clint_form': clint_form,
        'scale_form': scale_form,
        'car_form': car_form,
    }
    return render(request, 'pages/registration.html', context)
