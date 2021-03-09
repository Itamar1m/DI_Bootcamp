from django.urls import path 
from . import views

urlpatterns=[
    path('gif/<int:id>',views.gif,name='gif'),
    path('category/',views.category,name='category'),
    path('',views.all_gifs,name='all_gifs'),
    path('gif_by_cat/<int:id>',views.gif_by_cat,name='gif_by_cat')

]