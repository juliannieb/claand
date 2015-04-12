from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def registrar_empresa(request):
	""" Funcion para manejar la vista de registrar empresa. """
	return render_to_response('empresas/registrar_empresa.html', context_instance=RequestContext(request))

@login_required
def consultar_empresas(request):
	""" mostrar todas las empresas """
	return render_to_response('empresas/empresas.html', context_instance=RequestContext(request))

@login_required
def empresa(request, empresa_id):
	""" mostrar una empresa """
	return render_to_response('empresas/empresa.html', context_instance=RequestContext(request))
