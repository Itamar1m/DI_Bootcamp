from django.shortcuts import render
from django.http import HttpResponse
import json

with open ('animals.json')as f:
    file=json.load(f)

def family(request):
    context=file
    animal_id=[]
    for animal in file['animals']:
        animal_id.append( f'  {animal["family"]}')
    return HttpResponse(animal_id)
    # return render(request, 'family.html', context)