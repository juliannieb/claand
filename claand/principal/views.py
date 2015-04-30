import time

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.contrib.auth.models import User, Group

from principal.models import Vendedor
from contactos.models import Contacto, Llamada, Atiende
from cotizaciones.models import Cotizacion, Venta

from principal.forms import VendedorForm, SeleccionarVendedorForm

def no_es_vendedor(user):
    """Funcion para el decorador user_passes_test
    """
    return not user.groups.filter(name='vendedor').exists()

def user_login(request):
    """ esta vista maneja todo el proceso de login:
    en el caso de que sea un GET, muestra el template de login,
    y si es POST realiza la validacion y redireccionamiento. 
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                es_vendedor = no_es_vendedor(user)
                return HttpResponseRedirect('/principal/index/', {'no_es_vendedor':es_vendedor})
            else:
                return render(request, 'principal/login2.html', {'desactivada':True})
        else:
            return render(request, 'principal/login2.html', {'errors':True})
    else:
        return render(request, 'principal/login2.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/principal/login')

@login_required
def consultar(request):
    """ En esta vista se muestran las opciones de consulta para los usuarios.
    """
    es_vendedor = no_es_vendedor(request.user)
    context = {}
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'principal/consultar.html', context)

@login_required
def index(request):
    """ Vista para mostrar el index del usuario.
    """
    es_vendedor = no_es_vendedor(request.user)
    context = {}
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'principal/index.html', context)

@login_required
def consultar_vendedores(request):
    """ Vista para mostrar toda la lista de vendedores al director
    """
    es_vendedor = no_es_vendedor(request.user)
    vendedores_list = Vendedor.objects.all()
    context = {}
    xdata = list()
    ydata = list()
    for vendedor in vendedores_list:
        xdata.append(vendedor.user.first_name + " " +vendedor.user.last_name)

    print(xdata)
    for vendedor in vendedores_list:
        contactos_list = Contacto.objects.filter(vendedor=vendedor)
        cotizaciones_list = Cotizacion.objects.filter(contacto=contactos_list)
        ydata.append(cotizaciones_list.count())
    print(ydata)

    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    context = {
    'charttype': charttype,
    'chartdata': chartdata,
    'chartcontainer': chartcontainer,
    'extra': {
        'x_is_date': False,
        'x_axis_format': '',
        'tag_script_js': True,
        'jquery_on_ready': False,
        }
    }
    context['vendedores_list'] = vendedores_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'principal/consultar_vendedores.html', context)

@login_required
@user_passes_test(no_es_vendedor)
def vendedor(request, id_vendedor):
    """ Vista para mostrar el detalle de un contacto en particular
    """
    es_vendedor = no_es_vendedor(request.user)
    vendedor = Vendedor.objects.get(id=id_vendedor)
    contactos_list = Contacto.objects.filter(vendedor=vendedor)
    cotizaciones_list = Cotizacion.objects.filter(contacto=contactos_list)
    ventas_list = Venta.objects.filter(cotizacion=cotizaciones_list)
    llamadas_list = Llamada.objects.filter(contacto=contactos_list)

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

    x_data = sorted(xdata)
    ydata = []
    for x in x_data:
        ydata.append(x_dict[x])
    
    for venta in ventas_list:
        fecha_venta = time.mktime(venta.cotizacion.fecha_creacion.timetuple()) * 1000
        if fecha_venta in x_dict2:
            x_dict2[fecha_venta] += venta.monto_total
        else:
            xdata2.append(fecha_venta)
            x_dict2[fecha_venta] = venta.monto_total

    x_data2 = sorted(xdata2)
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
    context = {}
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
    context['vendedor'] = vendedor
    context['contactos_list'] = contactos_list
    context['cotizaciones_list'] = cotizaciones_list
    context['ventas_list'] = ventas_list
    context['llamadas_list'] = llamadas_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'principal/vendedor.html', context)

@login_required
@user_passes_test(no_es_vendedor)
def registrar_vendedor(request):
    """ Vista para registrar un nuevo vendedor en el sistema """
    current_user = request.user
    if request.method == 'POST':
        formVendedor = VendedorForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVendedor':formVendedor, 'no_es_vendedor':es_vendedor}
        if formVendedor.is_valid():
            data = formVendedor.cleaned_data
            nombre = data['nombre']
            apellido = data['apellido']
            correo_electronico = data['correo_electronico']
            usuario = data['usuario']
            password = data['password']

            user = User.objects.create_user(usuario, correo_electronico, password)
            user.first_name = nombre
            user.last_name = apellido
            user.save()
            Vendedor(user=user).save()
            return render(request, 'principal/exito.html')
        else:
            print (formVendedor.errors)
    else:
        formVendedor = VendedorForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVendedor':formVendedor, 'no_es_vendedor':es_vendedor, }

    return render(request, 'principal/registrar_vendedor.html', forms)

@login_required
@user_passes_test(no_es_vendedor)
def eliminar_vendedor(request, id_vendedor):
    """ Vista para registrar un nuevo vendedor en el sistema """
    vendedor = Vendedor.objects.get(pk=id_vendedor)
    if request.method == 'POST':
        formAsignarTodosLosContactos = SeleccionarVendedorForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formAsignarTodosLosContactos':formAsignarTodosLosContactos, 'vendedor':vendedor, 'no_es_vendedor':es_vendedor}

        if formAsignarTodosLosContactos.is_valid():
            data = formAsignarTodosLosContactos.cleaned_data
            nuevoVendedor = data['vendedor']
            todos_los_contactos = Contacto.objects.all()
            contactos_list = []
            for contacto in todos_los_contactos:
                if contacto.atiende_set.all():
                    if contacto.atiende_set.all()[len(contacto.atiende_set.all()) - 1].vendedor \
                    == vendedor:
                        contactos_list.append(contacto)
            for contacto in contactos_list:
                Atiende(contacto=contacto, vendedor=nuevoVendedor).save()
            vendedor.is_active = False
            vendedor.save()
            user = vendedor.user
            user.is_active = False
            user.save()
            return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})
    else:
        formAsignarTodosLosContactos = SeleccionarVendedorForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formAsignarTodosLosContactos':formAsignarTodosLosContactos, 'vendedor':vendedor, \
        'no_es_vendedor':es_vendedor, }

    return render(request, 'principal/eliminar_vendedor.html', forms)
