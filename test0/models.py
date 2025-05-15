from django.db import models
from django.db import models

# Create your models here.



class Clint_file(models.Model):
    CATEGORY=[('birds', 'طيور'),('dead', 'زراعه'),('sheeps', 'اغنام/اخري')]
    TICKET_TYPE = [
        ('Import', 'وارد'),
        ('Export', 'صادر'),
    ]
    clint_id = models.IntegerField(null=False, blank=False)
    clint_name = models.CharField(max_length=100, null=False, blank=False)
    ticket_type = models.CharField(max_length=10,choices=TICKET_TYPE, null=False, blank=False)
    category = models.CharField(max_length=100,choices=CATEGORY, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    come_from = models.CharField(max_length=100, null=False, blank=False)
    go_to = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.clint_name
    
    
    
    
class Car_info(models.Model):
    driver_name = models.CharField(max_length=100, null=False, blank=False)
    car_number = models.IntegerField( null=False, blank=False)
    first_wieght = models.CharField(max_length=100, null=False, blank=False)
    trailer_number = models.IntegerField( null=False, blank=False)
    car_type = models.CharField(max_length=100, null=False, blank=False)
    car_adds = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.car_number
    


class ScaleInfo(models.Model):
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)  
    notes = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.weight)
    
    
    
class BirdScale(models.Model):
    
    BIRD_STATUS_CHOICES = [
        ('alive', 'حي'),
        ('dead', 'نافق'),
    ]

    bird_status = models.CharField(max_length=10, choices=BIRD_STATUS_CHOICES,null=False, blank=False,default='alive')
    first_weight = models.DecimalField(max_digits=8, decimal_places=2 , null=False, blank=False,default=0.00)
    box_count = models.PositiveIntegerField(null=False, blank=False,default=0)

    def __str__(self):
        return f"{self.get_bird_status_display()} - {self.first_weight} كجم - {self.box_count} قفص"

