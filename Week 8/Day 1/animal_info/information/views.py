from django.shortcuts import render
from django.http import HttpResponse
import json

with open ('animals.json')as f:
    file=json.load(f)
    print(file)

def family(request):
    animal=[]
    family=[]
    for item in file['animals']:
        animal.append({item['name']:item['family']})
    for animal in animal:
        for family in file['families']:        
            if family['id'] in animal:
                family.append({animal:family['name']})
                     
    print=HttpResponse(animal)
    return print
    # return render(request,'family.html', context)
