from django.shortcuts import render
from info.models import Family,Animal
from django.http import HttpResponse

def family(request,id):
    animals=Animal.objects.filter(family=id)
    context ={
        'content':animals   
    }
    return render(request,'family.html',context)
    
def animal(request,id):
    animals=Animal.objects.filter(id=id)

    context={
        'content':animals
    }
    return render(request,'animal.html',context)

def all_animals(request):
    all_animals=Animal.objects.all()
    print(all_animals[0])   
    for i in range (len(all_animals)):
        all_animals[i].link =(str(f'../animal/{all_animals[i].id}'))

    context={
        'content':all_animals,
           
    }
    print(all_animals[0].link)
    return render(request,'all_animals.html',context)
   

