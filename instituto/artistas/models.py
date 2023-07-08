from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.

class AreaGaleria(models.Model):
    idArea          = models.AutoField(db_column='idArea', primary_key=True) 
    Descripcion     = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return str(self.Descripcion)


class Galeria(models.Model):
    codigo           = models.CharField(primary_key=True, max_length=6, verbose_name='codigo')
    nombre           = models.CharField(max_length=50, verbose_name='nombre')
    historia         = models.CharField(max_length=200, blank=True, null=True, verbose_name='historia')
    precio            = models.IntegerField(verbose_name='precio')  
    img              = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='img')
    
    def __str__(self):
        return str(self.nombre)
    class Meta:      
        ordering = ['nombre']

    def delete(self, using=None, keep_parents=False):
        self.img.storage.delete(self.img.name)
        return super().delete()

