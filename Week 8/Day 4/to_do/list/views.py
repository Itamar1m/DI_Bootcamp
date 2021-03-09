from django.shortcuts import render,redirect
from .models import *
from .forms import *

def todo(request):
    if request.method=='GET':
        return render(request,'todo.html',{'todo_list':ToDoList()})
    if request.method=='POST':
        
        my_form=ToDoList(request.POST)

        if my_form.is_valid():
            title=my_form.cleaned_data['list_item']
            details=my_form.cleaned_data['details']
            deadline_date=my_form.cleaned_data['deadline_date']
            categories=my_form.cleaned_data['category']
            
            a1=ToDo(title=title,details=details,deadline_date=deadline_date)
            a1.save()


        for category in categories:
            category=Category.objects.get(id=category)
            category.todo.add(a1)
            category.save()
            # all_categories=Category.objects.all()
            # for item in categories:
            #         b1=all_categories.get(id=item)
            #         b1.todo.add(a1)
                    
            return redirect('todo')
        else:
            return render(request,'todo.html',{'todo_list':ToDoList()})

def display (request):
    todo_list=ToDo.objects.all()
    context={
     'todo_list':todo_list

    }

    return render(request,'display.html',context)
