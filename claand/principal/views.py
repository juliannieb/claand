from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
	""" Funcion para manejar el index principal de la aplicación.
	TO DO: implementar todo ja.
	"""
	return render_to_response('principal/login.html')

def vendedor_index(request):
	""" Funcion para manejar el index principal del vendedor.
	TO DO: implementar todo ja.
	"""
	return render_to_response('principal/index_vendedor.html')

def consultar(request):
	""" Funcion para manejar la vista principal de consultas.
	TO DO: implementar todo ja.
	"""
	return render_to_response('principal/consultar.html')

def director_index(request):
	""" Funcion para manejar el index principal del director.
	Aqui deben ir los permisos de login para el director.
	TO DO: implementar todo ja.
	"""
	return render_to_response('principal/index_director.html')