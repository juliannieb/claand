from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from contactos.models import Contacto
from django.contrib.auth.decorators import login_required

@login_required
def consultar_contactos(request):
	""" mostrar todos los contactos """
	contactos_list = Contacto.objects.all()
	return render(request, 'contactos/contactos.html', {'contactos_list': contactos_list})

@login_required
def contacto(request, contacto_nombre_slug):
	""" mostrar detalle de un contacto """

	return render_to_response('contactos/contacto.html')

@login_required
def registrar_contactos(request):
	""" registrar un nuevo contacto """
	return render_to_response('contactos/registrar_contactos.html')

@login_required
def registrar_contacto(request):
	""" registrar un nuevo contacto """
	return render_to_response('contactos/registrar_contacto.html')

@login_required
def registrar_llamada(request):
	""" registrar una llamada """
	return render_to_response('contactos/registrar_llamada.html')

@login_required
def consultar_notas(request):
	""" mostrar todas las notas """
	return render_to_response('contactos/notas.html')

@login_required
def nota(request, nota_id):
	""" mostrar detalle de una nota """
	return HttpResponse("detalle nota")

@login_required
def registrar_nota(request):
	""" registrar una nueva nota """
	return HttpResponse("registrar una nota")

@login_required
def consultar_recordatorios(request):
	""" mostrar todos los recordatorios """
	return render_to_response('contactos/recordatorios.html')

@login_required
def recordatorio(request, recordatorio_id):
	""" mostrar detalle de un recordatorio """
	return HttpResponse("detalle recordatorio")

@login_required
def registrar_recordatorio(request):
	""" registrar un nuevo recordatorio """
	return HttpResponse("registrar un recordatorio")

