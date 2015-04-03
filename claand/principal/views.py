from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
	return HttpResponse("Indexxxx")



def vendedor_index(request):
	return HttpResponse("Index vendedor")


def consultar(request):
	return HttpResponse("Consultar general")

"""
Aqui deben ir los permisos de login para el director.
"""
def director_index(request):
	return HttpResponse("Index director")