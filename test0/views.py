from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.timezone import now

from .forms import *
from .models import ScaleInfo
from .consumers import clean_data

import socket


# ---- Constants ----
SCALE_IP = '192.168.1.56'
SCALE_PORT = 25


# ---- Helper function to read weight from scale ----
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


# ---- Login View ----
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


# ---- Home Page (requires login) ----
@login_required(login_url='login')
def index(request):
    return render(request, 'pages/index.html')


# ---- Sales Page ----
def sales_view(request):
    return render(request, 'pages/sales.html')


# ---- Birds Sale Form ----
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


# ---- Client File Form ----
def clint_file(request):
    if request.method == 'POST':
        form = ClintFileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم الحفظ بنجاح.")

            # ملاحظة: Clint_file غير معرف هنا، لو عايز تتأكد من التصنيف:
            # يمكنك تعديلها بالشكل التالي لو عايز شرط معين بناءً على البيانات:
            # if form.cleaned_data.get('category') == 'طيور':
            #     return redirect('birds')

            return redirect('birds')
    else:
        form = ClintFileForm()

    return render(request, 'pages/birds.html', {'form': form})


# ---- Registration View (مع حفظ البيانات مؤقتًا في Session) ----
def registration_view(request):
    if request.method == 'POST':
        if 'print_ticket' in request.POST:
            clint_form = ClintFileForm(request.POST)
            scale_form = ScaleInfoForm(request.POST)
            car_form = CarInfoForm(request.POST)
            bird_form = BirdSaleForm(request.POST)

            if all([clint_form.is_valid(), scale_form.is_valid(), car_form.is_valid(), bird_form.is_valid()]):
                # حفظ العميل، السيارة، الوزن، التذكرة (الوزن هنا محفوظ مع التاريخ created_at تلقائي)
                clint_instance = clint_form.save()
                scale_instance = scale_form.save()  # الوزن هنا بيتحفظ في الداتا بيز + created_at تلقائي
                car_instance = car_form.save()
                bird_instance = bird_form.save(commit=False)
                bird_instance.car = car_instance
                bird_instance.scale = scale_instance
                bird_instance.save()

                messages.success(request, "تم حفظ جميع البيانات وطباعة التذكرة.")
                return redirect('registration')
            else:
                print("ClintFileForm errors:", clint_form.errors)
                print("CarInfoForm errors:", car_form.errors)
                print("ScaleInfoForm errors:", scale_form.errors)
                print("BirdSaleForm errors:", bird_form.errors)
                messages.error(request, "هناك خطأ في البيانات، يرجى التحقق.")
            
        else:
            # الضغط على إضافة وزن لا يفعل الحفظ
            return redirect('registration')

    # في حالة GET نهيئ الفورمات خالية أو بقيم فارغة
    clint_form = ClintFileForm()
    car_form = CarInfoForm()
    scale_form = ScaleInfoForm()
    bird_form = BirdSaleForm()

    context = {
        'clint_form': clint_form,
        'scale_form': scale_form,
        'car_form': car_form,
        'bird_form': bird_form,
    }
    return render(request, 'pages/registration.html', context)


