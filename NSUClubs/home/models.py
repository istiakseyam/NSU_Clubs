from django.db import models
from django.forms import PasswordInput
from numpy import place

# Create your models here.
class Club(models.Model):
    cname= models.CharField(max_length=400)
    csname=models.CharField(max_length=10, unique=True)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    logo=models.ImageField(upload_to='images')

    def __str__(self):
        return self.csname

class User(models.Model):
    username=models.CharField(max_length=200, unique=True)
    password=models.CharField(max_length=50)
    email=models.EmailField()


class Event(models.Model):
    ename=models.CharField(max_length=400)
    eby=models.ForeignKey(Club,to_field='csname', on_delete=models.CASCADE)
    date=models.DateField()
    place=models.CharField(max_length=400)
    time=models.CharField(max_length=20)

    def __str__(self):
        return self.ename

class ClubMember(models.Model):
    mname=models.CharField(max_length=200)
    mposition=models.CharField(max_length=200)
    fclub=models.ForeignKey(Club,to_field='csname', on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return self.mname



