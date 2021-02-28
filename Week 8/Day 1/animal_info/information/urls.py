from django.urls import path
from . import views

urlpatterns=[
    path('family/',views.family,name='family')
]
