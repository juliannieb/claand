from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
	""" Funcion para manejar el index principal de la aplicación.
	TO DO: implementar todo ja.
	"""
	return HttpResponse("Indexxxx")

def vendedor_index(request):
	""" Funcion para manejar el index principal del vendedor.
	TO DO: implementar todo ja.
	"""
	return HttpResponse("Index vendedor")

def consultar(request):
	""" Funcion para manejar la vista principal de consultas.
	TO DO: implementar todo ja.
	"""
	return HttpResponse("Consultar general")

def director_index(request):
	""" Funcion para manejar el index principal del director.
	Aqui deben ir los permisos de login para el director.
	TO DO: implementar todo ja.
	"""
	return HttpResponse("Index director")