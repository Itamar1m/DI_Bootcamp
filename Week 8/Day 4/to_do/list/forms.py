from django import forms
from .models import Category
from django.utils.functional import lazy

class DateInput(forms.DateInput):
    input_type='date'

def all_categories():
    cat_objects = Category.objects.all()
    cats = [(cat.id, cat.name) for cat in cat_objects]
    return cats

class ToDoList(forms.Form):
    list_item=forms.CharField(max_length=50)
    details=forms.CharField(max_length=200,widget=forms.Textarea)
    deadline_date =forms.DateField(widget=DateInput)  
    category=forms.MultipleChoiceField(choices=lazy(all_categories,tuple)())





