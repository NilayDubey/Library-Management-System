from django.db import models
from django.shortcuts import render,HttpResponse,redirect
# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    picture=models.ImageField()
    author=models.CharField(max_length=50, default="Techvarsity")
    price=models.FloatField()
    description=models.TextField()

    def __str__(self):
        return self.name+" "+self.author+" "+str(self.price)


class Meta:
    db_table="Books"