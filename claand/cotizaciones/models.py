from datetime import datetime

from django.db import models

from contactos.models import Contacto

class Cotizacion(models.Model):
    is_active = models.BooleanField(default=True)
    monto = models.FloatField(default=0)
    descripcion = models.TextField()
    is_pendiente = models.BooleanField(default=False)
    contacto = models.ForeignKey(Contacto)
    fecha_creacion = models.DateField(editable=False)
    fecha_modificacion = models.DateField()

    def save(self, *args, **kwargs):
        """ Override de save para que sólo haya una fecha de creación,
        y si dicha tupla se modifica, se guarde la fecha de modificación.
        """
        if not self.id:
            self.fecha_creacion = datetime.today()
        self.fecha_modificacion = datetime.today()
        return super(Cotizacion, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'

class Venta(models.Model):
    is_active = models.BooleanField(default=True)
    monto_total = models.FloatField(default=0)
    is_completada = models.BooleanField(default=False)
    cotizacion = models.OneToOneField(Cotizacion)

class Pago(models.Model):
    is_active = models.BooleanField(default=True)
    venta = models.ForeignKey(Venta)
    fecha_creacion = models.DateField(editable=False)
    fecha_modificacion = models.DateField()
    monto = models.FloatField()
    
    def save(self, *args, **kwargs):
        """ Override de save para que sólo haya una fecha de creación,
        y si dicha tupla se modifica, se guarde la fecha de modificación.
        """
        if not self.id:
            self.fecha_creacion = datetime.today()
        self.fecha_modificacion = datetime.today()
        return super(Pago, self).save(*args, **kwargs)  
