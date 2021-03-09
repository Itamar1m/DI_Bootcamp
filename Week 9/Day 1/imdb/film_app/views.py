from django.shortcuts import render,redirect
from .urls import *
from .models import *
from django.views.generic import CreateView,UpdateView,DeleteView
from .forms import *
from django.urls import reverse_lazy
from cprint import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def homepage(request):
    films=Film.objects.all()
    return render(request,'homepage.html',{'films':films})
# *__________________________________________

@method_decorator(login_required, name='dispatch')
class AddDirector(CreateView):
    form_class=AddDirectorForm
    template_name='add_director.html'
    success_url=reverse_lazy('home-page')
# *__________________________________________

@method_decorator(login_required, name='dispatch')
class AddFilm(CreateView):    
    form_class=AddFilmForm
    template_name='add_film.html'
    success_url=reverse_lazy('home-page')
# *__________________________________________

@login_required(login_url='login')
def change_director(request,pk):
    my_form=ChangeDirectorForm()

    if request.method=='GET':
        return render(request,'change_director.html',{'form':my_form})

    if request.method =='POST':
        my_form=ChangeDirectorForm(request.POST)

        if my_form.is_valid():
            directors=my_form.cleaned_data['director']
            
            this_film=Film.objects.get(pk=pk)
               
            for director in this_film.director.all():
                this_film.director.remove(director)
                this_film.save()
                
            for director in directors:
                this_film.director.add(director)
                this_film.save()

            return redirect ('home-page')
        else:
             return render(request,'change_director.html',{'form':my_form})    

# *__________________________________________

class EditFilm(UpdateView):
    model=Film
    fields='__all__'
    post='edit_film.html'
# *__________________________________________

@login_required(login_url='login')
def delete_film(request,pk):
    film=Film.objects.get(pk=pk)
    film.delete()
    return redirect('home-page')
# *__________________________________________

@login_required(login_url='login')
def like_film(request,pk,username):
    liked_film=Film.objects.get(pk=pk) 
    user1=User.objects.get(username=username)
    user1.liked_film.add(liked_film)

    return redirect('home-page')
# *__________________________________________

def dislike_film(request,pk,username):
    disliked_film=Film.objects.get(pk=pk)
    user1=User.objects.get(username=username)
    user1.liked_film.remove(disliked_film)
    
    return redirect('home-page')

def dislike_profile(request,pk,username):
    disliked_film=Film.objects.get(pk=pk)
    user1=User.objects.get(username=username)
    user1.liked_film.remove(disliked_film)
    
    return redirect('profile',pk)






    




