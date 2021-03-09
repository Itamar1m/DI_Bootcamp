from django.shortcuts import render,redirect
from .models import *
from .forms import *


def customer(request):
    customers=Customer.objects.all().order_by('last_name')
    return render(request,'customer.html',{'customers':customers})
# *_________________________________________________________

def vehicle(request):
    vehicles=VehicleType.objects.all()
    context={
        'vehicles':vehicles,  
    }
    return render (request,'vehicle.html',context)
# *_________________________________________________________
def check_vehicle(vehicle_type):
    all_vehicles=VehicleType.objects.all()
    for vehicle in all_vehicles:
        if vehicle.name == vehicle_type:
            return vehicle
    
def check_vehicle_size(vehicle_size):
    vehicle_sizes=VehicleSize.objects.all()
    for vehicle in vehicle_sizes:
        if vehicle.name == vehicle_size:
            return vehicle
    
def add_vehicle(request):
    my_form=AddVehicleForm()

    if request.method =='GET':
        return render(request,'add_vehicle.html',{'add_vehicle':my_form})

    if request.method=='POST':
        myform=AddVehicleForm(request.POST)

        if myform.is_valid():
            vehicle_type=myform.cleaned_data['vehicle_type']
            vehicle_size=myform.cleaned_data['vehicle_size']
            vehicle_cost=myform.cleaned_data['vehicle_cost']

      
            cost=Vehicle(real_cost=vehicle_cost,vehicle_type=check_vehicle(vehicle_type),size=check_vehicle_size(vehicle_size))
            cost.save()
       

            return redirect('vehicle')    
# *_________________________________________________________

def add_rental(request):
    my_form=AddRentalForm()
    if request.method=='GET':
        return render(request,'new_rental.html',{'add_rental':my_form})

#     if request.method=='POST'
#         my_form=AddRentalForm(request.POST)
#         all_customers[customer.id for customer in] 

#             if my_form is_valid():


def add_customer(request):
    my_form=AddCustomerForm()

    if request.method=='GET':
        return render(request,'add_customer.html',{'add_customer':my_form})

    if request.method=='POST':
        my_form=AddCustomerForm(request.POST)
        if my_form.is_valid():
            first_name=my_form.cleaned_data['first_name']
            last_name=my_form.cleaned_data['last_name']
            email=my_form.cleaned_data['email']
            phone_number=my_form.cleaned_data['phone_number']
            address=my_form.cleaned_data['address']
            city=my_form.cleaned_data['city']
            country=my_form.cleaned_data['country']

            new_customer=Customer(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,address=address,city=city,country=country)
            new_customer.save()

            return redirect('customer')

        else:
         return render(request,'add_customer.html',{'add_customer':my_form})        



        







        




