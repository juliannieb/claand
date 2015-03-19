from django.db import models

# Create your models here.


class Contacto(models.Model):
	esCliente = models.BooleanField(default=False)
	nombre = models.CharField(max_length=35)
	correoElectronico = models.EmailField()

	def __str__(self):
		return self.nombre
