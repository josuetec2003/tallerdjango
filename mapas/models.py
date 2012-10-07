from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Ubicacion(models.Model):
	nombre = models.CharField(max_length=300)
	lat = models.CharField(max_length=30)
	lng = models.CharField(max_length=30)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre

class UbicacionForm(ModelForm):
	class Meta():
		model = Ubicacion
		exclude = ('user', )

