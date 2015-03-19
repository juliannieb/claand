from datetime import datetime

from django.db import models

from contactos.models import Contacto

class Cotizacion(models.Model):
	is_active = models.BooleanField(default=True)
	monto = models.FloatField(default=0)
	descripcion = models.TextField()
	es_pendiente = models.BooleanField(default=False)
	contacto = models.ForeignKey(Contacto)
	fecha_creacion = models.DateField(editable=False)
	fecha_modificacion = models.DateField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.fecha_creacion = datetime.datetime.today()
		self.fecha_modificacion = datetime.datetime.today()		# siempre guardar fecha modificacion.
		return super(Pago, self).save(*args, **kwargs)

class Venta(models.Model):
	is_active = models.BooleanField(default=True)
	monto_total = models.FloatField(default=0)
	completada = models.BooleanField(default=False)
	cotizacion = models.OneToOneField(Cotizacion)

class Pago(models.Model):
	is_active = models.BooleanField(default=True)
	venta = models.ForeignKey(Venta)
	fecha_creacion = models.DateField(editable=False)
	fecha_modificacion = models.DateField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.fecha_creacion = datetime.datetime.today()
		self.fecha_modificacion = datetime.datetime.today()		# siempre guardar fecha modificacion.
		return super(Pago, self).save(*args, **kwargs)
