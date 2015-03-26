from datetime import datetime

from django.db import models


class Empresa(models.Model):
    is_active = models.BooleanField(default=True)
    nombre = models.CharField(max_length=30)
    rfc = models.CharField(primary_key=True, max_length=13)
    direcciones = models.ManyToManyField('Direccion', through='EmpresaTieneDireccion')

    def save(self, *args, **kwargs):
        self.rfc = self.rfc.upper()
        return super(Empresa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class EmpresaTieneDireccion(models.Model):
    fecha = models.DateField()
    empresa = models.ForeignKey(Empresa)
    direccion = models.ForeignKey('Direccion')

    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha = datetime.datetime.today()
        return super(EmpresaTieneDireccion, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Empresa tiene direcciones'

class TipoRedSocial(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Tipo Redes Sociales'

class RedSocial(models.Model):
    is_active = models.BooleanField(default=True)
    link = models.URLField()
    empresa = models.ForeignKey(Empresa)
    tipo_red_social = models.ForeignKey(TipoRedSocial)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = 'Redes Sociales'

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

    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'
