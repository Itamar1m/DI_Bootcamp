from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    
     ]