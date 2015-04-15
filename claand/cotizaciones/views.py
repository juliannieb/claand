from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cotizaciones.models import Cotizacion, Venta
from contactos.models import Pertenece

@login_required
def consultar_cotizaciones(request):
    """ mostrar todas las cotizaciones """
    cotizaciones_list = Cotizacion.objects.all()
    return render(request, 'cotizaciones/cotizaciones.html', {'cotizaciones_list': cotizaciones_list})

@login_required
def cotizacion(request, id_cotizacion):
    """ mostrar detalle de una cotizacion """
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    contacto = cotizacion.contacto
    pertenece = Pertenece.objects.get(contacto=contacto)
    return render(request, "cotizaciones/cotizacion.html", {'cotizacion': cotizacion, 'contacto': contacto, 'pertenece': pertenece})

@login_required
def consultar_ventas(request):
    """ mostrar todas las ventas """
    ventas_list = Venta.objects.all()
    return render(request, 'cotizaciones/ventas.html', {'ventas_list': ventas_list})

@login_required
def venta(request, id_venta):
    """ mostrar detalle de una venta """
    venta = Venta.objects.get(id=id_venta)
    id_cotizacion = venta.cotizacion.id
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    contacto = cotizacion.contacto
    pertenece = Pertenece.objects.get(contacto=contacto)
    return render(request, 'cotizaciones/venta.html', {'venta': venta, 'cotizacion': cotizacion, 'contacto': contacto, 'pertenece': pertenece})

@login_required
def registrar(request):
    """ registrar cotizacion """
    return render(request, 'cotizaciones/registrar_cotizacion.html', {})


""" Falta todas las relacionadas con pago """
