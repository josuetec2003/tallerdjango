from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

class Ubicacion(models.Model):
	nombre = models.CharField(max_length=300)
	lat = models.CharField(max_length=30)
	lng = models.CharField(max_length=30)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre

class Fotos(models.Model):
	descripcion = models.CharField(max_length=400)
	foto = models.ImageField(upload_to='fotos')
	fecha = models.DateTimeField(auto_now_add=True)
	ubicacion = models.ForeignKey(Ubicacion)

	def __unicode__(self):
		return self.descripcion

class UbicacionForm(ModelForm):
	class Meta():
		model = Ubicacion
		exclude = ('user', )
		widgets = {
			'lat': TextInput(attrs={'readonly': 'readonly'}),
			'lng': TextInput(attrs={'readonly': 'readonly'}),
		}

