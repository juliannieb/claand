from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

def consultar_contactos(request):
	""" mostrar todos los contactos """
	return HttpResponse("todos los contactosss")

def contacto(request, contacto_nombre_slug):
	""" mostrar detalle de un contacto """
	return HttpResponse("contacto en especifico")

def registrar_contactos(request):
	""" registrar un nuevo contacto """
	return HttpResponse("registrar contacto")

def registrar_llamada(request):
	""" registrar una llamada """
	return HttpResponse("registrar una llamada")

def consultar_notas(request):
	""" mostrar todas las notas """
	return HttpResponse("consultar todas las notas")

def nota(request, nota_id):
	""" mostrar detalle de una nota """
	return HttpResponse("detalle nota")

def registrar_nota(request):
	""" registrar una nueva nota """
	return HttpResponse("registrar una nota")

def consultar_recordatorios(request):
	""" mostrar todos los recordatorios """
	return HttpResponse("consultar todos los recordatorio")

def recordatorio(request, recordatorio_id):
	""" mostrar detalle de un recordatorio """
	return HttpResponse("detalle recordatorio")

def registrar_recordatorio(request):
	""" registrar un nuevo recordatorio """
	return HttpResponse("registrar un recordatorio")

