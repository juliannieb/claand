from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator

from contactos.models import Contacto

class Cotizacion(models.Model):
    is_active = models.BooleanField(default=True)
    monto = models.FloatField(default=0, validators=[MinValueValidator(0)])
    descripcion = models.TextField()
    is_pendiente = models.BooleanField(default=True)
    contacto = models.ForeignKey(Contacto)
    fecha_creacion = models.DateField(editable=True)
    fecha_modificacion = models.DateField()

    def save(self, *args, **kwargs):
        """ Override de save para que sólo haya una fecha de creación,
        y si dicha tupla se modifica, se guarde la fecha de modificación.
        """
        if not self.id:
            self.fecha_creacion = datetime.today()
        self.fecha_modificacion = datetime.today()
        return super(Cotizacion, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.contacto) + ": " + self.descripcion + ": $" + str(self.monto)

    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'

class Venta(models.Model):
    is_active = models.BooleanField(default=True)
    monto_total = models.FloatField(default=0, validators=[MinValueValidator(0)])
    monto_acumulado = models.FloatField(default=0)
    is_completada = models.BooleanField(default=False)
    cotizacion = models.OneToOneField(Cotizacion)
    fecha_creacion = models.DateField(editable=True)
    fecha_modificacion = models.DateField()

    def save(self, *args, **kwargs):
        """ Override de save para que sólo haya una fecha de creación,
        y si dicha tupla se modifica, se guarde la fecha de modificación.
        """
        if not self.id:
            self.fecha_creacion = datetime.today()
        self.fecha_modificacion = datetime.today()
        return super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.cotizacion.contacto) + ": " + self.cotizacion.descripcion + ": $" + \
        str(self.monto_total)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

class Pago(models.Model):
    is_active = models.BooleanField(default=True)
    venta = models.ForeignKey(Venta)
    fecha_creacion = models.DateField(editable=False)
    fecha_modificacion = models.DateField()
    monto = models.FloatField(validators=[MinValueValidator(0)])
    
    def save(self, *args, **kwargs):
        """ Override de save para que sólo haya una fecha de creación,
        y si dicha tupla se modifica, se guarde la fecha de modificación.
        """
        if not self.id:
            self.fecha_creacion = datetime.today()
        self.fecha_modificacion = datetime.today()
        return super(Pago, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + ": " + self.venta.cotizacion.descripcion + ": $" + \
        str(self.monto)