import time

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from empresas.forms import EmpresaForm, DireccionForm, NumeroTelefonicoForm, RedSocialForm

from empresas.models import Empresa, Direccion, EmpresaTieneDireccion
from cotizaciones.models import Cotizacion, Venta
from contactos.models import Contacto

def no_es_vendedor(user):
    """Funcion para el decorador user_passes_test
    """
    return not user.groups.filter(name='vendedor').exists()

@login_required
def consultar_empresas(request):
    """ mostrar todas las empresas """
    empresas_list = Empresa.objects.all()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'empresas/empresas.html', {'empresas_list': empresas_list, \
        'no_es_vendedor':es_vendedor})

@login_required
def empresa(request, empresa_nombre_slug):
    """ mostrar una empresa """
    context = {}
    empresa = Empresa.objects.get(slug=empresa_nombre_slug)
    empresa_tiene_direccion = EmpresaTieneDireccion.objects.filter(empresa=empresa)
    numeros_list = empresa.numerotelefonico_set.all()
    redes_list = empresa.redsocial_set.all()
    contactos_list = Contacto.objects.filter(empresa=empresa)
    cotizaciones_list = Cotizacion.objects.filter(contacto=contactos_list)
    
    xdata = list()
    ydata = list()
    for cotizacion in cotizaciones_list:
        xdata.append(time.mktime(cotizacion.fecha_creacion.timetuple()) * 1000)
        ydata.append(cotizacion.monto)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
        'color': '#a4c639'
    }

    chartdata = {'x': xdata,
                 'name1': 'Monto', 'y1': ydata, 'extra1': extra_serie1}

    charttype = "lineChart"
    chartcontainer = 'linechart_container'  # container name
    context = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }

    ventas_list = Venta.objects.filter(cotizacion=cotizaciones_list)
    es_vendedor = no_es_vendedor(request.user)
    context['empresa'] = empresa
    context['empresa_tiene_direccion'] = empresa_tiene_direccion
    context['numeros_list'] = numeros_list
    context['redes_list'] = redes_list
    context['contactos_list'] = contactos_list
    context['cotizaciones_list'] = cotizaciones_list
    context['ventas_list'] = ventas_list
    context['no_es_vendedor'] = es_vendedor

    return render(request, 'empresas/empresa.html', context)

@login_required
def registrar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        formDireccion = DireccionForm(request.POST)
        formNumeroTelefonico = NumeroTelefonicoForm(request.POST)
        formRedSocial = RedSocialForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'form':form, 'formDireccion':formDireccion, 'formNumeroTelefonico':formNumeroTelefonico, \
        'formRedSocial':formRedSocial, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if form.is_valid() and formDireccion.is_valid() and formNumeroTelefonico.is_valid() and formRedSocial.is_valid():
            # Save the new category to the database.
            empresa = form.instance
            empresa = form.save(commit=True)
            direccion = formDireccion.save(commit=True)

            EmpresaTieneDireccion(empresa=empresa, direccion=direccion).save()

            if formNumeroTelefonico.has_changed():
                numero_telefonico = formNumeroTelefonico.instance
                numero_telefonico.empresa = empresa
                numero_telefonico.save()
            if formRedSocial.has_changed():
                red_social = formRedSocial.instance
                red_social.empresa = empresa
                red_social.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/index_vendedor.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
            print (formDireccion.errors)
            print (formNumeroTelefonico.errors)
            print (formRedSocial.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = EmpresaForm()
        formDireccion = DireccionForm()
        formNumeroTelefonico = NumeroTelefonicoForm()
        formRedSocial = RedSocialForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'form':form, 'formDireccion':formDireccion, \
        'formNumeroTelefonico':formNumeroTelefonico, \
        'formRedSocial':formRedSocial, 'no_es_vendedor':es_vendedor}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'empresas/registrar_empresa2.html', forms)
