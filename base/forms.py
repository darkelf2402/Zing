from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Productd

class ProductForm(ModelForm):
    class Meta:
        model = Productd
        fields = '__all__'
        
