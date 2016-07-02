from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
	usuario = models.OneToOneField(User)
	telefono = models.CharField(max_length=15, default="")