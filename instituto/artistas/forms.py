#CREAR CLASES PARA FORMULARIOS
from django.forms import ModelForm
from django import forms
from .models import Galeria

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria 
        #fields = ['codigo', 'nombre', 'descripcion', 'idArea', 
         #         'modalidad', 'historia', 'precio', 'img'] 
   
        fields = '__all__' 


