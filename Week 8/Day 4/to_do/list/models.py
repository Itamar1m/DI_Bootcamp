from django.db import models

class ToDo(models.Model):
    title=models.CharField(max_length=30)
    details=models.TextField()
    date_creation=models.DateField(auto_now_add=True)
    deadline_date=models.DateField(null=True)

    def __str__(self):
        return f'{self.title}'

class Category(models.Model):
    name=models.CharField(max_length=30)
    img=models.URLField()
    todo=models.ManyToManyField(ToDo,related_name='category')    

    def __str__(self):
        return f'{self.name}'




