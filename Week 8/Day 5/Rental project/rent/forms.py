from django import forms
from .models import *

class AddVehicleForm(forms.Form):
    vehicle_type=forms.CharField(max_length=20)
    vehicle_size=forms.CharField(max_length=20)
    vehicle_cost=forms.FloatField()
# *________________________________________________

def vehicle_type():
    vehicle_type=VehicleType.objects.all()
    vehicle_type = [(vehicle.name ,vehicle.name.upper) for vehicle in vehicle_type]
    return vehicle_type

def customer():
    all_customers=Customer.objects.all()  
    names=[(f'{customer.first_name} {customer.last_name}',f'{customer.first_name} {customer.last_name}') for customer in all_customers]
    return names

def vehicle_size():
    vehicle_size=VehicleSize.objects.all()
    vehicle_size=[(vehicle.name,vehicle.name.upper) for vehicle in vehicle_size]
    return vehicle_size    

class AddRentalForm(forms.Form):
    vehicle_type=forms.ChoiceField(choices=vehicle_type())
    vehicle_size=forms.ChoiceField(choices=vehicle_size())
    customer=forms.ChoiceField(choices=customer())

# *________________________________________________
class AddCustomerForm(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=100)
    phone_number=forms.CharField(max_length=100)
    address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    country=forms.CharField(max_length=100)


    