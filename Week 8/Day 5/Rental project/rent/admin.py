from django.contrib import admin
from .models import *

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'real_cost', 'size')

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Customer)
admin.site.register(VehicleType)
admin.site.register(VehicleSize)
admin.site.register(Rental)
admin.site.register(RentalRate)






