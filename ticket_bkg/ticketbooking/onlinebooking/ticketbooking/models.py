from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class persons(models.Model):
    img=models.ImageField(upload_to='picture')
    heading=models.TextField(max_length=150)
    desc=models.TextField()

       #
       # def __str__(self):
       #   return self.name