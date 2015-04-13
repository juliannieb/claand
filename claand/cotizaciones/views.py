from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cotizaciones.models import Cotizacion, Venta

@login_required
def consultar_cotizaciones(request):
    """ mostrar todas las cotizaciones """
    cotizaciones_list = Cotizacion.objects.all()
    return render(request, 'cotizaciones/cotizaciones.html', {'cotizaciones_list': cotizaciones_list})

@login_required
def cotizacion(request, id_cotizacion):
    """ mostrar detalle de una cotizacion """
    return HttpResponse("cotizacion detalle")

@login_required
def consultar_ventas(request):
    """ mostrar todas las ventas """
    return render_to_response('cotizaciones/ventas.html')

@login_required
def venta(request, id_venta):
    """ mostrar detalle de una venta """
    return HttpResponse("venta detalle")

@login_required
def registrar(request):
    """ registrar cotizacion """
    return render_to_response('cotizaciones/registrar_cotizacion.html')


""" Falta todas las relacionadas con pago """
