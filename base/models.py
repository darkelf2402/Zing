from operator import truediv
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

   
class category1(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Productd(models.Model):
    category = models.ForeignKey(category1,on_delete=models.CASCADE,null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=500)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name
    
    class Meta:
        ordering = ['created']
    
    
class Chatr(models.Model):

    chat_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    body = models.TextField()
    chadd = models.ForeignKey(Productd,on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body    
    
    class Meta:
        ordering = ['-created']
        