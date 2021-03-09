from django.db import models

class Gif(models.Model):
    title=models.CharField(max_length=20)
    url=models.URLField()
    uploader_name=models.CharField(null=True,max_length=50)
    cretaed_at=models.DateTimeField(max_length=200,auto_now_add=True)

    def __str__(self):
        return f' title: {self.title}'

class Category(models.Model):
    name=models.CharField(max_length=80)
    gif=models.ManyToManyField(Gif,related_name='all_gifs')

    def __str__(self):
        return f'gif name:{self.name}'

            
