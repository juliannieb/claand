from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from empresas.forms import EmpresaForm, DireccionForm
from empresas.models import Empresa, Direccion, EmpresaTieneDireccion


@login_required
def consultar_empresas(request):
    """ mostrar todas las empresas """
    empresas_list = Empresa.objects.all()
    return render(request, 'empresas/empresas.html', {'empresas_list': empresas_list})

@login_required
def empresa(request, empresa_nombre_slug):
    """ mostrar una empresa """
    empresa = Empresa.objects.get(slug=empresa_nombre_slug)
    empresa_tiene_direccion = EmpresaTieneDireccion.objects.filter(empresa=empresa)
    numeros_list = empresa.numerotelefonico_set.all()
    redes_list = empresa.redsocial_set.all()
    return render(request, 'empresas/empresa.html', {'empresa': empresa, 'empresa_tiene_direccion': empresa_tiene_direccion,'numeros_list': numeros_list, 'redes_list': redes_list})

@login_required
def registrar_empresa(request):
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
