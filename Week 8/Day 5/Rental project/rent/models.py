from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_group_by import GroupByMixin

class Customer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
# *________________________________________________________

class Vehicle(models.Model):
    vehicle_type=models.ForeignKey('VehicleType',on_delete=models.SET_NULL,null=True,related_name='type')
    date_creaeted=models.DateTimeField(auto_now_add=True)
    real_cost=models.FloatField()
    size=models.ForeignKey('VehicleSize',on_delete=models.SET_NULL,null=True,related_name='size')

    def __str__(self):
        return f'{str(self.vehicle_type)} Cost: {self.real_cost} $'
# *________________________________________________________

class VehicleType(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
# *_________________________________________________________

class VehicleSize(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
# *_________________________________________________________

class Rental(models.Model):
    rental_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField(null=False)
    customer=models.ForeignKey('Customer',on_delete=models.SET_NULL,null=True)
    vehicle=models.ForeignKey('Vehicle',on_delete=models.SET_NULL,null=True)

# *_________________________________________________________

class RentalRate(models.Model):
    daily_rate=models.FloatField(default=100)
    vehicle_type=models.ForeignKey('VehicleType',on_delete=models.SET_NULL,null=True)
    vehicle_size=models.ForeignKey('VehicleSize',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.vehicle_type} {self.daily_rate}'

# *_________________________________________________________
