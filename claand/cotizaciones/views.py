from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def consultar_cotizaciones(request):
	""" mostrar todas las cotizaciones """
	return render_to_response('cotizaciones/cotizaciones.html')

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
