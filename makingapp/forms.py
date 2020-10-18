from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.admin import widgets
class Customersform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    password=forms.CharField(max_length=50)
    mobile=forms.CharField(max_length=50)
    statelocation=forms.CharField(max_length=200)
    citylocation=forms.CharField(max_length=200)
    time=forms.TimeField(widget=widgets.AdminTimeWidget)
    #price= forms.DecimalField()
