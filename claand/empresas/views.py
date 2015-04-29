import time
import collections
import operator

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from empresas.forms import EmpresaForm, DireccionForm, NumeroTelefonicoForm, RedSocialForm

from principal.models import Vendedor
from empresas.models import Empresa, Direccion, EmpresaTieneDireccion, Municipio
from cotizaciones.models import Cotizacion, Venta
from contactos.models import Contacto

def no_es_vendedor(user):
    """Funcion para el decorador user_passes_test
    """
    return not user.groups.filter(name='vendedor').exists()


@login_required
def consultar_empresas(request):
    """ Vista para mostrar todas las empresas.
    """
    empresas_list = Empresa.objects.all()
    es_vendedor = no_es_vendedor(request.user)

    context = {}
    context['empresas_list'] = empresas_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'empresas/empresas.html', context)


@login_required
def empresa(request, empresa_nombre_slug):
    """ Vista para consultar la información de una empresa en particular.
    En esta, se realiza un gráfico de ventas y cotizaciones vs tiempo, utilizando 
    el app de nvd3.
    """
    context = {}
    empresa = Empresa.objects.get(slug=empresa_nombre_slug)
    es_vendedor = no_es_vendedor(request.user)
    # obtener info general
    empresa_tiene_direccion = EmpresaTieneDireccion.objects.filter(empresa=empresa)
    numeros_list = empresa.numerotelefonico_set.all()
    redes_list = empresa.redsocial_set.all()
    
    # obtener todos los contactos, o sólo los del vendedor dependiendo si
    # es director o vendedor.
    if es_vendedor: # si no es vendedor
        contactos_list = Contacto.objects.filter(empresa=empresa)
    else:
        current_user = request.user
        current_vendedor = Vendedor.objects.get(user=current_user)
        contactos_list = Contacto.objects.filter(vendedor=current_vendedor, empresa=empresa)
        
    cotizaciones_list = Cotizacion.objects.filter(contacto=contactos_list)
    ventas_list = Venta.objects.filter(cotizacion=cotizaciones_list)
    
    xdata = list()
    xdata2 = list()
    ydata = list()
    ydata2 = list()
    x_dict = {}
    x_dict2 = {}
    # obtener montos de cotizaciones para gráfico.
    for cotizacion in cotizaciones_list:
        fecha_cotizacion = time.mktime(cotizacion.fecha_creacion.timetuple()) * 1000
        if fecha_cotizacion in x_dict:
            x_dict[fecha_cotizacion] += cotizacion.monto
        else:
            xdata.append(fecha_cotizacion)
            x_dict[fecha_cotizacion] = cotizacion.monto

    print(x_dict)

    #ydata = list(x_dict.values())
    #x = list(x_dict.keys())

    x_data = sorted(xdata)
    print(x_data)
    ydata = []
    for x in x_data:
        ydata.append(x_dict[x])

    print(ydata)
    # obtener montos de ventas para el gráfico
    
    for venta in ventas_list:
        fecha_venta = time.mktime(venta.cotizacion.fecha_creacion.timetuple()) * 1000
        if fecha_venta in x_dict2:
            x_dict2[fecha_venta] += venta.monto_total
        else:
            xdata2.append(fecha_venta)
            x_dict2[fecha_venta] = venta.monto_total

    #x = list(x_dict2.keys())

    x_data2 = sorted(xdata2)
    print("x_data2")
    print(x_data2)
    ydata2 = []
    for x in x_data2:
        ydata2.append(x_dict2[x])

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
        'color': '#a4c639'
    }
    extra_serie2 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
        'color': '#FF8aF8'
    }
    chartdata = {'x': x_data,
                 'name1': 'Monto Cotizado', 'y1': ydata, 'extra1': extra_serie1,
                 'name2': 'Monto Vendido', 'y2': ydata2, 'extra2': extra_serie2}

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
    """ Vista para registrar una empresa.
    """
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
            return render(request, 'principal/exito.html')
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
    return render(request, 'empresas/registrar_empresa.html', forms)


@login_required
def get_municipio(request):
    """ Función para atender la petición GET AJAX para obtener el municipio de un estado
    """
    if request.is_ajax() and request.method == 'GET':
        estado_id = request.GET['estado_id']
        municipios = Municipio.objects.filter(estado=estado_id).order_by('nombre')
        return render_to_response('empresas/municipios_seleccionados.html', {'municipios': municipios})
    else:
        return HttpResponseRedirect(reverse('principal:index'))


def search_empresas(request):
    """Función para atender la petición GET AJAX para filtrar las empresas en la Vista
    empresas
    """
    if request.is_ajax() and request.method == 'GET':
        texto = request.GET['texto']
        empresas_list = Empresa.objects.filter(nombre__icontains=texto)
    return render_to_response('empresas/search_empresas.html', {'empresas_list': empresas_list})