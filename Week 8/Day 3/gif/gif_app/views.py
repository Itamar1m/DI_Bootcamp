from django.shortcuts import render
from .models import *

def gif(request,id):
    

    return render(request,'gif.html',{"gifs":Gif.objects.filter(id=id)})

def category(request):
    return render(request,'categories.html',{"categories":Category.objects.all()})
    

def all_gifs(request):   
    return render(request,'all.html',{'all_gifs':Gif.objects.all()})

def gif_by_cat(request,id):
    categories=Category.objects.filter(name=sport)
    sport=categories.filter(name='sport')
    politics=categories.filter(name='politics')
    emotion=categories.filter(name='emotion')
  
    context={
        'sport':sport,
        "politics":politics,
        "emotion":emotion
    }
    return render(request,'gif_by_cat.html',context)
   
    

# categories=Category.objects.filter(name='sport')
# categories=Category.objects.all()
# sport=categories[0]
# print(sport.gif.all())

# politics=categories.filter(name='politics')
# emotion=categories.filter(name='emotion')
