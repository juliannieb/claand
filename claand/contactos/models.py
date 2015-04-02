from django.db import models
from empresas.models import Empresa
from principal.models import Vendedor

class Contacto(models.Model):
    is_active = models.BooleanField(default=True)
    is_cliente = models.BooleanField(default=False)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    correo_electronico = models.EmailField(unique=True)
    calificaciones = models.ManyToManyField('Calificacion')
    empresa = models.ManyToManyField(Empresa, through='Pertenece')
    vendedor = models.ManyToManyField(Vendedor, through='Atiende')

    def __str__(self):
        return self.nombre

class Pertenece(models.Model):
    contacto = models.ForeignKey(Contacto)
    empresa = models.ForeignKey(Empresa)
    fecha = models.DateField()
    area = models.ForeignKey('Area')

    class Meta:
        verbose_name_plural = 'Pertenecen'

class Area(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

class Atiende(models.Model):
    contacto = models.ForeignKey(Contacto)
    vendedor = models.ForeignKey(Vendedor)
    fecha = models.DateField()

    class Meta:
        verbose_name_plural = 'Atienden'


class Calificacion(models.Model):
    calificacion  = models.IntegerField(default=1)

    def __str__(self):
        return str(self.calificacion)

    class Meta:
        verbose_name_plural = 'Calificaciones'

class Nota(models.Model):
    is_active = models.BooleanField(default=True)
    clasificacion = models.IntegerField(default=1)
    descripcion = models.TextField()
    contacto = models.ForeignKey(Contacto)

    def __str__(self):
        return self.contacto, ":", self.descripcion[:30]

class Recordatorio(models.Model):
    is_active = models.BooleanField(default=True)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    urgencia = models.IntegerField(default=1)
    contacto = models.ForeignKey(Contacto)

    def __str__(self):
        return self.contacto, ":", self.descripcion[:30]

class Llamada(models.Model):
    is_active = models.BooleanField(default=True)
    descripcion = models.TextField()
    fecha = models.DateField()
    contacto = models.ForeignKey(Contacto)

    def __str__(self):
        return self.contacto, ":", self.descripcion[:30]

class TipoNumeroTelefonico(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class NumeroTelefonico(models.Model):
    contacto = models.ForeignKey(Contacto, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, null=True, blank=True)
    vendedor = models.ForeignKey(Vendedor, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    numero = models.BigIntegerField()
    tipo_numero = models.ForeignKey(TipoNumeroTelefonico)

    def __str__(self):
        return str(self.numero)

    class Meta:
        verbose_name_plural = 'Números Telefónicos'
        verbose_name = 'Número Telefónico'
