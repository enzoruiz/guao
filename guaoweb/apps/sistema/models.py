from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Anuncio(models.Model):
	fecha_perdido = models.DateField()
	nombre_mascota = models.CharField(max_length=20)
	especie = models.CharField(max_length=25)
	raza = models.CharField(max_length=25)
	color = models.CharField(max_length=25)
	sexo = models.CharField(max_length=1)
	ultimo_lugar = models.TextField()
	mas_informacion = models.TextField()
	imagen = models.ImageField(upload_to='img-mascotas/')
	creador = models.ForeignKey(User)