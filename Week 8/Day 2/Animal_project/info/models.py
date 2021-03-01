from django.db import models

class Family(models.Model):
    name=models.CharField(max_length=30,unique=True)   



class Animal(models.Model):
    name=models.CharField(max_length=30,default='')
    legs=models.IntegerField(default=0)
    weight=models.FloatField(default=0)
    height=models.FloatField(default=0)
    max_speed=models.FloatField(default=0)
    family=models.ForeignKey(Family,on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return f'{self.name}' 




