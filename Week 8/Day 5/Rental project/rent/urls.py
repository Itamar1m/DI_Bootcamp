
from django.urls import path
from . import views
urlpatterns = [
    path('customer/', views.customer, name='customer'),

    path('add_customer/', views.add_customer, name='add_customer'),

    path('vehicle/', views.vehicle, name='vehicle'),

    path('add_vehicle/', views.add_vehicle, name='vehicle_add'),

  path('add_rental/', views.add_rental, name='add_rental'),

    ]