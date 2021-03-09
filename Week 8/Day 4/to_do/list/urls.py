from django.urls import path
from . import views

urlpatterns=[
    path("",views.todo,name='todo'),
    path ("display_todos/",views.display,name='display_todos')
]