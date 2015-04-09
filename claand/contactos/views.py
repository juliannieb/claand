from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from contactos.models import Contacto

def consultar_contactos(request):
	""" mostrar todos los contactos """
	lista_contactos = Contacto.objects.all()
	context = {'contactos_list' : lista_contactos}
	return render_to_response('contactos/contactos.html', context)

def contacto(request, contacto_nombre_slug):
	""" mostrar detalle de un contacto """

	return render_to_response('contactos/contacto.html')

def registrar_contactos(request):
	""" registrar un nuevo contacto """
	return render_to_response('contactos/registrar_contactos.html')


def registrar_contacto(request):
	""" registrar un nuevo contacto """
	return render_to_response('contactos/registrar_contacto.html')

def registrar_llamada(request):
	""" registrar una llamada """
	return render_to_response('contactos/registrar_llamada.html')

def consultar_notas(request):
	""" mostrar todas las notas """
	return render_to_response('contactos/notas.html')

def nota(request, nota_id):
	""" mostrar detalle de una nota """
	return HttpResponse("detalle nota")

def registrar_nota(request):
	""" registrar una nueva nota """
	return HttpResponse("registrar una nota")

def consultar_recordatorios(request):
	""" mostrar todos los recordatorios """
	return render_to_response('contactos/recordatorios.html')

def recordatorio(request, recordatorio_id):
	""" mostrar detalle de un recordatorio """
	return HttpResponse("detalle recordatorio")

def registrar_recordatorio(request):
	""" registrar un nuevo recordatorio """
	return HttpResponse("registrar un recordatorio")

