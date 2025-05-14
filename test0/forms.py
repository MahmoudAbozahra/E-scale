from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import  *



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)



class BirdSaleForm(forms.ModelForm):
    class Meta:
        model = BirdSale
        fields = '__all__'
        labels = {
            'bird_status': 'نوع الطيور',
            'first_weight': 'الوزن الأولي',
            'box_count': 'عدد الأقفاص',
        }
        widgets = {
            'bird_status': forms.Select(attrs={'class': 'form-control'}),
            'first_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'box_count': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
        

class ClintFileForm(forms.ModelForm):
    class Meta:
        model = Clint_file
        fields = [ 'ticket_type','clint_name','clint_id','category','city','come_from','go_to']
        labels = {
            'clint_id': 'رقم العميل',
            'clint_name': 'اسم العميل',
            'ticket_type': 'نوع التذكرة',
            'category': 'الصنف',
            'city': 'المدينة',
            'come_from': ' وارد من',
            'go_to': 'وارد إلى ',
        }
        widgets = {
            'clint_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'clint_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ticket_type': forms.Select(attrs={'class': 'form-control'}),
            'bird_sale': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'come_from': forms.TextInput(attrs={'class': 'form-control'}),
            'go_to': forms.TextInput(attrs={'class': 'form-control'}),
        }

        
class CarInfoForm(forms.ModelForm):
    class Meta:
        model = Car_info
        fields = ['driver_name', 'car_number', 'first_wieght', 'trailer_number', 'car_type', 'car_adds']
        labels = {
            'driver_name': 'اسم السائق',
            'car_number': 'رقم السيارة',
            'first_wieght': 'الوزن السياره الفارغ اول مره',
            'trailer_number': 'رقم المقطورة',
            'car_type': 'نوع السيارة',
            'car_adds': 'اضافات السيارة',
        }
        widgets = {
            'driver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'car_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_wieght': forms.TextInput(attrs={'class': 'form-control'}),
            'trailer_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'car_type': forms.TextInput(attrs={'class': 'form-control'}),
            'car_adds': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class ScaleInfoForm(forms.ModelForm):
    class Meta:
        model = ScaleInfo
        fields = ['weight', 'notes']
        labels = {
            'weight': 'الوزن الاول ',
            'created_at': 'وقت الميزان',
            'notes': 'ملاحظات',
        }
    weight = forms.FloatField(disabled=True)
    