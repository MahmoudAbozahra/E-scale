from django.db import models
from django.db import models

# Create your models here.

class Drivers_Info(models.Model):
    driver_name = models.CharField(max_length=250, null=False, blank=False)
    driver_national_id = models.CharField(max_length=14, null=False, blank=False)
    driver_license = models.CharField(max_length=14, null=False, blank=False)
    notes = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.driver_name
    
    
    
class Customer_Info(models.Model):
    customer_name = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self):
        return self.customer_name
    
class Items_Info(models.Model):
    item_name = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self):
        return self.item_name

class Vehicle_Info(models.Model):
    vehicle_plate = models.CharField(max_length=10, null=False, blank=False,unique=True)
    vehicle_license = models.CharField(max_length=14, null=False, blank=False)
    license_weight = models.DecimalField(max_length=10,decimal_places=3 ,null=False, blank=False)
    first_wieght_saved = models.DecimalField(max_length=10,decimal_places=3, null=True, blank=True)
    notes = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.vehicle_plate
    

class Users(models.Model):
    user_role = models.CharField(max_length=80, null=False, blank=False)
    user_name = models.CharField(max_length=80, null=False, blank=False)
    user_password = models.CharField(max_length=80, null=False, blank=False)
    user_email = models.EmailField(max_length=80, null=False, blank=False)
    
    
    def __str__(self):
        return self.user_name
    
    
    
    
class Blocked_vehicles(models.Model):
    car_id = models.ForeignKey(Vehicle_Info, on_delete=models.SET_NULL, null=True, blank=True)
    driver_id = models.ForeignKey(Drivers_Info, on_delete=models.SET_NULL, null=True, blank=True)
    manipulative_value = models.DecimalField(max_digits=10, decimal_places=3, null=False, blank=False)
    manipulative_user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
    is_blocked = models.BooleanField(default=False)
    unblock_user_name = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
    unblock_date = models.DateTimeField(null=True, blank=True)
    unblocked_reson = models.CharField(max_length=50, null=True, blank=True)
    
    
    def __str__(self):
        return self.car_id
    
    
    
class Configirations(models.Model):
    scale_no = models.CharField(max_length=80, null=False, blank=False)
    scale_ip = models.CharField(max_length=80, null=False, blank=False)
    scale_port = models.IntegerField(max_length=7, null=False, blank=False)
    manipulation_threshold = models.DecimalField(max_digits=10, decimal_places=3, null=False, blank=False)

    def __str__(self):
        return self.scale_no
    


    
    
    
    
    
class Ticket_Data(models.Model):
    ticket_number = models.IntegerField(max_length=10, null=False, blank=False)
    scale = models.IntegerField(max_length=10, null=False, blank=False)
    ticket_type = models.CharField(max_length=10,choices=[('IN', 'التفريغ'),('OUT', 'المبيعات')], null=False, blank=False)
    customer_id = models.ForeignKey(Customer_Info, on_delete=models.SET_NULL, null=True, blank=True)
    driver_id = models.ForeignKey(Drivers_Info, on_delete=models.SET_NULL, null=True, blank=True)
    item_id = models.ForeignKey(Items_Info, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle_id = models.ForeignKey(Vehicle_Info, on_delete=models.SET_NULL, null=True, blank=True)
    trailer_plate = models.CharField(max_length=10, null=False, blank=False )
    sector = models.CharField(max_length=80,choices=[('طيور','زراعة ','اغنام/اخري')], null=False, blank=False)
    sector_type = models.CharField(max_length=80,choices=[('طيور حي','طيور نافق')], null=False, blank=False)
    vehicle_first_weight = models.ForeignKey(Vehicle_Info, on_delete=models.SET_NULL, null=True, blank=True, related_name='first_weight')
    v_first_w_date = models.DateTimeField(null=True, blank=True)
    trailer_first_weight = models.DecimalField(max_digits=10, decimal_places=3, null=False, blank=False)
    
    
    
    
    
    def __str__(self):
        return self.ticket_number




















# class Clint_file(models.Model):
#     CATEGORY=[('birds', 'طيور'),('dead', 'زراعه'),('sheeps', 'اغنام/اخري')]
#     TICKET_TYPE = [
#         ('Import', 'وارد'),
#         ('Export', 'صادر'),
#     ]
#     clint_id = models.IntegerField(null=False, blank=False)
#     clint_name = models.CharField(max_length=100, null=False, blank=False)
#     ticket_type = models.CharField(max_length=10,choices=TICKET_TYPE, null=False, blank=False)
#     category = models.CharField(max_length=100,choices=CATEGORY, null=False, blank=False)
#     city = models.CharField(max_length=100, null=False, blank=False)
#     come_from = models.CharField(max_length=100, null=False, blank=False)
#     go_to = models.CharField(max_length=100, null=False, blank=False)

#     def __str__(self):
#         return self.clint_name
    
    
    
    
# class Car_info(models.Model):
#     driver_name = models.CharField(max_length=100, null=False, blank=False)
#     car_number = models.IntegerField( null=False, blank=False)
#     first_wieght = models.CharField(max_length=100, null=False, blank=False)
#     trailer_number = models.IntegerField( null=False, blank=False)
#     car_type = models.CharField(max_length=100, null=False, blank=False)
#     car_adds = models.CharField(max_length=100, null=False, blank=False)

#     def __str__(self):
#         return str(self.car_number)
    


# class ScaleInfo(models.Model):
#     weight = models.FloatField()
#     created_at = models.CharField()  
#     notes = models.CharField(max_length=500, null=True, blank=True)

#     def __str__(self):
#         return str(self.weight)
    
    
    
# class BirdScale(models.Model):
    
#     BIRD_STATUS_CHOICES = [
#         ('alive', 'حي'),
#         ('dead', 'نافق'),
#     ]

#     bird_status = models.CharField(max_length=10, choices=BIRD_STATUS_CHOICES,null=False, blank=False,default='alive')
#     first_weight = models.DecimalField(max_digits=8, decimal_places=2 , null=False, blank=False,default=0.00)
#     box_count = models.PositiveIntegerField(null=False, blank=False,default=0)

#     def __str__(self):
#         return f"{self.get_bird_status_display()} - {self.first_weight} كجم - {self.box_count} قفص"

