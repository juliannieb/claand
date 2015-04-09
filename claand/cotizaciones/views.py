from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def consultar_cotizaciones(request):
	""" mostrar todas las cotizaciones """
	return render_to_response('cotizaciones/cotizaciones.html')

def cotizacion(request, id_cotizacion):
	""" mostrar detalle de una cotizacion """
	return HttpResponse("cotizacion detalle")

def consultar_ventas(request):
	""" mostrar todas las ventas """
	return render_to_response('cotizaciones/ventas.html')

def venta(request, id_venta):
	""" mostrar detalle de una venta """
	return HttpResponse("venta detalle")

def registrar(request):
	""" registrar cotizacion """
	return render_to_response('cotizaciones/registrar_cotizacion.html')


""" Falta todas las relacionadas con pago """
