from django.contrib import admin

from cotizaciones.models import Cotizacion, Venta, Pago

admin.site.register(Cotizacion)
admin.site.register(Venta)
admin.site.register(Pago)
