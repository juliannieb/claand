from django.db import models


class Calificacion(models.Model):
	calificacion  = models.IntegerField(default=1)

class Contacto(models.Model):
	is_active = models.BooleanField(default=True)
	es_cliente = models.BooleanField(default=False)
	nombre = models.CharField(max_length=35)
	apellido = models.CharField(max_length=35)
	correo_electronico = models.EmailField(unique=True)
	calificaciones = models.ManyToManyField(Calificacion)

	def __str__(self):
		return self.nombre

class Nota(models.Model):
	is_active = models.BooleanField(default=True)
	descripcion = models.TextField()
	contacto = models.ForeignKey(Contacto)

	def __str__(self):
		return contacto, ":", self.descripcion[:30]

class Recordatorio(models.Model):
	is_active = models.BooleanField(default=True)
	descripcion = models.TextField()
	contacto = models.ForeignKey(Contacto)

	def __str__(self):
		return contacto, ":", self.descripcion[:30]

class Llamada(models.Model):
	is_active = models.BooleanField(default=True)
	descripcion = models.TextField()
	contacto = models.ForeignKey(Contacto)

	def __str__(self):
		return contacto, ":", self.descripcion[:30]

class TipoNumeroTelefonico(models.Model):
	nombre = models.CharField(max_length=30)

class NumeroTelefonico(models.Model):
	is_active = models.BooleanField(default=True)
	numero = models.IntegerField()
	tipo_numero = models.ForeignKey(TipoNumeroTelefonico)

	def __str__(self):
		return numero