from django.db import models
from apps.adopcion.models import Persona

class Vacuna(models.Model):
	nombre = models.CharField(max_length=30)
	caducidad = models.DateField()

	def __str__(self):
		return '{}'.format(self.nombre)

# Create your models here.
class Mascota(models.Model):
	nombre = models.CharField(max_length = 50)
	tipo = models.CharField(max_length = 20)
	edad = models.IntegerField()
	fecha_rescate = models.DateField()

	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna, blank = True)