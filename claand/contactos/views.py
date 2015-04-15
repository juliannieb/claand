from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from contactos.models import Contacto, Pertenece, NumeroTelefonico, Calificacion, Atiende, Recordatorio, Nota
from principal.models import Vendedor
from cotizaciones.models import Cotizacion, Venta


@login_required
def consultar_contactos(request):
	""" mostrar todos los contactos """
	#Falta validar si el current_user es el Director, para mostrar todos los contactos
	current_user = request.user
	if current_user.is_superuser:
		contactos_list = Contacto.objects.all()
	else:
		current_vendedor = Vendedor.objects.get(user=current_user)
		contactos_list = Contacto.objects.filter(vendedor=current_vendedor)
	return render(request, 'contactos/contactos.html', {'contactos_list': contactos_list})

@login_required
def contacto(request, contacto_nombre_slug):
	""" mostrar detalle de un contacto """
	contacto = Contacto.objects.get(slug=contacto_nombre_slug)
	pertenece = Pertenece.objects.get(contacto=contacto)
	numeros_list = contacto.numerotelefonico_set.all()
	calificacion = Calificacion.objects.get(contacto=contacto)
	cotizaciones_list = Cotizacion.objects.filter(contacto=contacto)
	return render(request, 'contactos/contacto.html', {'contacto': contacto, 'pertenece': pertenece, 'numeros_list': numeros_list, 'calificacion': calificacion, 'cotizaciones_list': cotizaciones_list})

@login_required
def registrar_contactos(request):
	""" registrar un nuevo contacto """
	return render(request, 'contactos/registrar_contactos.html', {})

@login_required
def registrar_contacto(request):
	""" registrar un nuevo contacto """
	return render(request, 'contactos/registrar_contacto.html', {})

@login_required
def registrar_llamada(request):
	""" registrar una llamada """
	return render(request, 'contactos/registrar_llamada.html', {})

@login_required
def consultar_notas(request):
	""" mostrar todas las notas """
	return render(request, 'contactos/notas.html', {})

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
	recordatorios_list = Recordatorio.objects.all()
	return render(request, 'contactos/recordatorios.html', {'recordatorios_list': recordatorios_list})

@login_required
def recordatorio(request, recordatorio_id):
	""" mostrar detalle de un recordatorio """
	return HttpResponse("detalle recordatorio")

@login_required
def registrar_recordatorio(request):
	""" registrar un nuevo recordatorio """
	return HttpResponse("registrar un recordatorio")

