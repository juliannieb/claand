from django.contrib import admin

from contactos.models import *

admin.site.register(Contacto)
admin.site.register(Area)
admin.site.register(Calificacion)
admin.site.register(Nota)
admin.site.register(Recordatorio)
admin.site.register(Llamada)
admin.site.register(NumeroTelefonico)
admin.site.register(TipoNumeroTelefonico)
admin.site.register(Pertenece)
admin.site.register(Atiende)