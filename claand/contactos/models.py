from django.db import models


class Calificacion(models.Model):
	calificacion  = models.IntegerField(default=1)

class Contacto(models.Model):
	es_cliente = models.BooleanField(default=False)
	nombre = models.CharField(max_length=35)
	apellido = models.CharField(max_length=35)
	correo_electronico = models.EmailField()
	calificaciones = models.ManyToManyField(Calificacion)

	def __str__(self):
		return self.nombre

class Nota(models.Model):
	descripcion = models.TextField()
	contacto = models.ForeignKey(Contacto)

class Recordatorio(models.Model):
	descripcion = models.TextField()
	contacto = models.ForeignKey(Contacto)

class Llamada(models.Model):
	descripcion = models.TextField()
	contacto = models.ForeignKey(Contacto)

