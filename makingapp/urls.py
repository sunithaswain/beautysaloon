from django.urls import path
from django.views.generic import RedirectView
# import onlinebooking.booking.views as views
from .views import *

urlpatterns = [
    path('home/', homeview, name='homedetail'),
    path('appointment/', appointmentdetails, name='appointment_name'),
    path('massage/', massagedetials, name='massage_name'),
    path('payment/', paymentpagedetials, name='payment_name'),
    path('callback/', callbackpagedetials, name='callback_name'),
    path('cartdetials/', custompagedetials, name='custom_name'),
    path('custompytmlogin/', checkout, name='check_out'),

]