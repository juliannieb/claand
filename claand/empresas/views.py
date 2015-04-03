from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def registrar_empresa(request):
	""" Funcion para manejar la vista de registrar empresa. """
	return HttpResponse("Registrar Empresa")
