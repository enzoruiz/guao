from django import forms
from .models import Anuncio

class AnuncioForm(forms.ModelForm):
	class Meta:
		model = Anuncio
		fields = ('fecha_perdido', 'especie', 'raza', 'color', 'sexo', 'ultimo_lugar', 'mas_informacion', 'imagen', 'nombre_mascota')