from django import forms
from .models import *

def movie_exists(title):
    film=Film.objects.filter(title=title) 
    if film:
        raise forms.ValidationError(f'This movie already exists in our database. ')


class AddFilmForm(forms.ModelForm):
    class Meta:
        model=Film
        exclude=('liked_film',)
    title=forms.CharField(validators=[movie_exists])

class AddDirectorForm(forms.ModelForm):
    class Meta:
        model=Director
        fields= '__all__'

class ChangeDirectorForm(forms.ModelForm):
    class Meta:
        model =Film
        fields=['director']
