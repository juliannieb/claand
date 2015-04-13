from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from empresas.forms import EmpresaForm, DireccionForm
from empresas.models import Empresa, Direccion, EmpresaTieneDireccion

"""
@login_required
def registrar_empresa(request):
	""Funcion para manejar la vista de registrar empresa. ""
	return render_to_response('empresas/registrar_empresa.html', context_instance=RequestContext(request))
"""

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

@login_required
def registrar_empresa(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        formDireccion = DireccionForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid() and formDireccion.is_valid():
            # Save the new category to the database.
            direccion = formDireccion.save(commit=True)
            empresa = form.save(commit=True)
            EmpresaTieneDireccion(empresa=empresa, direccion=direccion).save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/index_vendedor.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = EmpresaForm()
        formDireccion = DireccionForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'empresas/registrar_empresa2.html', {'form':form, 'formDireccion':formDireccion})
