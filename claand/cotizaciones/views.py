from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

def consultar_cotizaciones(request):
	""" mostrar todas las cotizaciones """
	return HttpResponse("cotizaciones general")

def cotizacion(request, id_cotizacion):
	""" mostrar detalle de una cotizacion """
	return HttpResponse("cotizacion detalle")

def consultar_ventas(request):
	""" mostrar todas las ventas """
	return HttpResponse("ventas general")

def venta(request, id_venta):
	""" mostrar detalle de una venta """
	return HttpResponse("venta detalle")

def registrar(request):
	""" registrar cotizacion """
	return HttpResponse("registrar cotizacion")
