from django.db import models
# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    appointment_time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True)
    category_id = models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE,
    )
    create_time = models.TimeField(auto_now=False, auto_now_add=False)
    state_location = models.CharField(max_length=250,blank=True)
    city_location = models.CharField(max_length=250,blank=True)
    area_location = models.CharField(max_length=250,blank=True)
    description = models.TextField()
class Employees(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    mobile = models.CharField(max_length=15)
    address=models.CharField(max_length=250, blank=True)
    create_joining_time=models.TimeField(auto_now=False, auto_now_add=False)
class Categories(models.Model):
    type_name=models.CharField(max_length=250, blank=True)
class Payment(models.Model):
    appointment_id=models.ForeignKey(
        'Appointments',
        on_delete=models.CASCADE,
    )
    price = models.FloatField(null=True)
    payment_type=models.CharField(max_length=250, blank=True)
    create_time=models.DateTimeField(auto_now_add=True)
class Appointments(models.Model):
    category_id=models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE,
    )
    customer_id=models.ForeignKey(
        'Customers',
        on_delete=models.CASCADE,
    )
    employee_id=models.ForeignKey(
        'Employees',
        on_delete=models.CASCADE,
    )
    timeslot=models.TimeField(auto_now=False, auto_now_add=False)
    price = models.FloatField(null=True)
    create_time=models.DateTimeField(auto_now_add=True)