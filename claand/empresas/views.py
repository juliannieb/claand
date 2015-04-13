from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from models.empresas import Empresa

@login_required
def registrar_empresa(request):
	""" Funcion para manejar la vista de registrar empresa. """
	return render_to_response('empresas/registrar_empresa.html', context_instance=RequestContext(request))

@login_required
def consultar_empresas(request):
	""" mostrar todas las empresas """
	empresas_list = Empresa.objects.all()
	#t = loader.get_template('empresas/empresas.html')
	#c = Context({'empresas_list': empresas_list})
	#return HttpResponse(t.render(c))
	return render(request, 'empresas/empresas.html', {'empresas_list': empresas_list})

@login_required
def empresa(request, empresa_id):
	""" mostrar una empresa """
	return render_to_response('empresas/empresa.html', context_instance=RequestContext(request))
