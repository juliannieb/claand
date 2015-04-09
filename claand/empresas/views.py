from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def registrar_empresa(request):
	""" Funcion para manejar la vista de registrar empresa. """
	return HttpResponse("Registrar Empresa")

def consultar_empresas(request):
	""" mostrar todas las empresas """
	return render_to_response('Vendedor/Consultar/Empresas.html')

def empresa(request, empresa_id):
	""" mostrar una empresa """
	return HttpResponse("detalle empresa")
