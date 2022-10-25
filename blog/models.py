from unittest.util import _MAX_LENGTH
from django.db import models

class Configuracion(models.Model):
    nombre_blog=models.CharField(max_length=14) 
    construido_por = models.CharField(max_length=30)  
    titulo_principal=models.CharField(max_length=30, default='', blank=False)
    subtitulo_principal=models.CharField(max_length=30, default='')


