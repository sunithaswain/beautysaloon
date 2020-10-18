from django.contrib import admin
from .models import Customers, Employees,Categories,Payment,Appointments
# Register your models here.
class CustomersAdmin(admin.ModelAdmin):
    list_display= ('name','email','mobile','appointment_time','category_id','create_time','state_location','city_location')
    search_fields = ('name','email')
admin.site.register(Customers, CustomersAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display= ('category_id','customer_id','employee_id','timeslot','price','create_time')
admin.site.register(Appointments, AppointmentAdmin)

class EmployeesAdmin(admin.ModelAdmin):
    list_display= ('name','password','email','mobile','address','create_joining_time')
admin.site.register(Employees, EmployeesAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display= ('type_name',)
admin.site.register(Categories, CategoriesAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display= ('appointment_id','price','payment_type','create_time')
admin.site.register(Payment, PaymentAdmin)

