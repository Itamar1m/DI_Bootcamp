from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Country(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
# *________________________________________

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
# *________________________________________

class Film (models.Model):
    title=models.CharField(max_length=50)
    image_url=models.URLField(max_length=700,null=True)
    release_date=models.DateField(default=now,editable=True)
    created_in_countries=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    available_in_countries=models.ManyToManyField(Country,related_name='available_in_countries')
    category=models.ManyToManyField(Category,related_name='category')
    director=models.ManyToManyField('Director',related_name='director')
    liked_film=models.ManyToManyField(User,related_name="liked_film")
 

    def __str__(self):
        return self.title
# *________________________________________

class Director(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
# *________________________________________







   






