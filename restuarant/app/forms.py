from django import forms
from .models import ReservationProfile, Order
from django.forms import ModelForm, TextInput, DateInput, NumberInput, TimeInput

class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationProfile
        fields = ['visitor_name', 'visitor_phone_number', 'date', 'time', 'comments']
        widgets = {"visitor_name": TextInput(attrs={"class":"form-control", "placeholder":"Name and Surname"}),
                   "visitor_phone_number": NumberInput(attrs={"class":"form-control"}),
                   "date": DateInput(attrs={"class":"form-control","type":"date", "placeholder":"Date"}),
                   "time": TimeInput(attrs={"class":"form-control", "type":"time", "placeholder":"Time"}),
                   "comments": TextInput(attrs={"class":"form-control", "placeholder":"Comments"})
                   }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'address', 'comments', 'quantities', 'price']