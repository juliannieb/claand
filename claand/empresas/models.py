from django.db import models


class Empresa(models.Model):
	is_active = models.BooleanField(default=True)
	nombre = models.CharField(max_length=30)
	rfc = models.CharField(primary_key=True, max_length=13)

	def save(self, *args, **kwargs):
		self.rfc = self.rfc.upper()
		super(Empresa, self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre

class TipoRedSocial(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre

class RedSocial(models.Model):
	is_active = models.BooleanField(default=True)
	link = models.URLField()
	empresa = models.ForeignKey(Empresa)
	tipo_red_social = models.ForeignKey(TipoRedSocial)

	def __str__(self):
		return self.link

class Estado(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre

class Municipio(models.Model):
	nombre = models.CharField(max_length=30)
	estado = models.ForeignKey(Estado)

	def __str__(self):
		return self.nombre

class Direccion(models.Model):
	is_active = models.BooleanField(default=True)
	direccion = models.CharField(max_length=100)
	municipio = models.ForeignKey(Municipio)

	def __str__(self):
		return self.direccion
