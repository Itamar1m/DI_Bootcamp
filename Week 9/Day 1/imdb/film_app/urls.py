from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='home-page'),
    path('addFilm/',views.AddFilm.as_view(),name='add-film'),
    path('addDirector',views.AddDirector.as_view(),name='add-director'),
    path('change_director/<int:pk>',views.change_director,name='change-director'),
    path('edit_film/<int:pk>',views.EditFilm.as_view(),name='edit-film'),
    path('delete_film/<int:pk>',views.delete_film,name='delete-film'),
    path('like_film/<int:pk>/<str:username>',views.like_film,name='like-film'),
    path('dislike_film/<int:pk>/<str:username>',views.dislike_film,name='dislike-film'),
    path('dislike_profile/<int:pk>/<str:username>',views.dislike_profile,name='dislike-film2')
    ]



