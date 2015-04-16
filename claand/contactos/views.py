import time

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from contactos.models import Contacto, Pertenece, NumeroTelefonico, Calificacion, Atiende, Recordatorio, Nota, Llamada
from principal.models import Vendedor
from cotizaciones.models import Cotizacion, Venta
from empresas.models import Empresa
from contactos.models import Llamada

from contactos.forms import ContactoForm, LlamadaForm, NotaForm, RecordatorioForm
from empresas.forms import NumeroTelefonicoForm, RedSocialForm



def no_es_vendedor(user):
    """Funcion para el decorador user_passes_test
    """
    return not user.groups.filter(name='vendedor').exists()

@login_required
def consultar_contactos(request):
    current_user = request.user
    es_vendedor = no_es_vendedor(request.user)
    if no_es_vendedor(current_user):
        contactos_list = Contacto.objects.all()
    else:
        current_vendedor = Vendedor.objects.get(user=current_user)
        contactos_list = Contacto.objects.filter(vendedor=current_vendedor)
    return render(request, 'contactos/contactos.html', {'contactos_list': contactos_list, \
        'no_es_vendedor':es_vendedor})

@login_required
def contacto(request, contacto_nombre_slug):
    """ mostrar detalle de un contacto """
    contacto = Contacto.objects.get(slug=contacto_nombre_slug)
    pertenece = Pertenece.objects.get(contacto=contacto)
    numeros_list = contacto.numerotelefonico_set.all()
    calificacion = Calificacion.objects.get(contacto=contacto)
    cotizaciones_list = Cotizacion.objects.filter(contacto=contacto)
    llamadas_list = Llamada.objects.all()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'contactos/contacto.html', {'contacto':contacto, 'pertenece':pertenece, \
        'numeros_list':numeros_list, 'calificacion':calificacion, \
        'cotizaciones_list':cotizaciones_list, 'llamadas_list':llamadas_list, \
        'no_es_vendedor':es_vendedor})

@login_required
def registrar_contactos(request):
    """ registrar un nuevo contacto """
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'contactos/registrar_contactos.html', {'no_es_vendedor':es_vendedor})

@login_required
def registrar_contacto(request):
    if request.method == 'POST':
        formContacto = ContactoForm(request.POST)
        formNumeroTelefonico = NumeroTelefonicoForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formContacto':formContacto, 'formNumeroTelefonico':formNumeroTelefonico, \
        'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formContacto.is_valid() and formNumeroTelefonico.is_valid():
            # Save the new category to the database.
            data = formContacto.cleaned_data
            nombre = data['nombre']
            apellido = data['apellido']
            correo_electronico = data['correo_electronico']
            empresa = data['empresa']
            area = data['area']
            is_cliente = data['is_cliente']
            calificacion = data['calificacion']
            contacto = Contacto(nombre=nombre, apellido=apellido, correo_electronico=correo_electronico, \
                calificacion=calificacion, is_cliente=is_cliente)
            contacto.save()
            
            
            Pertenece(contacto=contacto, empresa=empresa, area=area).save()

            current_user = request.user
            current_vendedor = Vendedor.objects.get(user=current_user)
            Atiende(vendedor=current_vendedor, contacto=contacto).save()

            if formNumeroTelefonico.has_changed():
                numero_telefonico = formNumeroTelefonico.instance
                numero_telefonico.contacto = contacto
                numero_telefonico.save()
            

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formContacto.errors)
            print (formNumeroTelefonico.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formContacto = ContactoForm()
        formNumeroTelefonico = NumeroTelefonicoForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formContacto':formContacto, 'formNumeroTelefonico':formNumeroTelefonico, \
        'no_es_vendedor':es_vendedor}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contactos/registrar_contacto.html', forms)

@login_required
def registrar_llamada(request):
    """ registrar una llamada """
    current_user = request.user
    current_vendedor = Vendedor.objects.get(user=current_user)
    contactos_list = Contacto.objects.filter(vendedor=current_vendedor)
    if request.method == 'POST':
        formLlamada = LlamadaForm(request.POST)
        formLlamada.fields["contacto"].queryset = contactos_list
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formLlamada':formLlamada, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formLlamada.is_valid():
            # Save the new category to the database.
            data = formLlamada.cleaned_data
            contacto = data['contacto']
            descripcion = data['descripcion']
            Llamada(contacto=contacto, descripcion=descripcion).save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formLlamada.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formLlamada = LlamadaForm()
        formLlamada.fields["contacto"].queryset = contactos_list
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formLlamada':formLlamada, 'no_es_vendedor':es_vendedor}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contactos/registrar_llamada.html', forms)

@login_required
@user_passes_test(no_es_vendedor)
def consultar_notas(request):
    """ mostrar todas las notas """
    notas_list = Nota.objects.all()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'contactos/notas.html', {'notas_list': notas_list, \
        'no_es_vendedor':es_vendedor})

@login_required
@user_passes_test(no_es_vendedor)
def nota(request, nota_id):
    """ mostrar detalle de una nota """
    nota = Nota.objects.get(id=nota_id)
    return render(request, "contactos/nota.html", {'nota': nota})

@login_required
@user_passes_test(no_es_vendedor)
def registrar_nota(request):
    """ registrar una nueva nota """
    if request.method == 'POST':
        formNota = NotaForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formNota':formNota, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formNota.is_valid():
            # Save the new category to the database.
            data = formNota.cleaned_data
            contacto = data['contacto']
            descripcion = data['descripcion']
            Nota(contacto=contacto, descripcion=descripcion, clasificacion=clasificacion).save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formNota.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formNota = NotaForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formNota':formNota, 'no_es_vendedor':es_vendedor}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contactos/registrar_nota.html', forms)

@login_required
@user_passes_test(no_es_vendedor)
def consultar_recordatorios(request):
    """ mostrar todos los recordatorios """
    recordatorios_list = Recordatorio.objects.all()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'contactos/recordatorios.html', {'recordatorios_list': recordatorios_list, \
        'no_es_vendedor':es_vendedor})

@login_required
@user_passes_test(no_es_vendedor)
def recordatorio(request, recordatorio_id):
    """ mostrar detalle de un recordatorio """
    recordatorio = Recordatorio.objects.get(id=recordatorio_id)
    return render(request, "contactos/recordatorio.html", {'recordatorio': recordatorio})

@login_required
@user_passes_test(no_es_vendedor)
def registrar_recordatorio(request):
    """ registrar un nuevo recordatorio """
    if request.method == 'POST':
        formRecordatorio = RecordatorioForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formRecordatorio':formRecordatorio, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formRecordatorio.is_valid():
            # Save the new category to the database.
            data = formRecordatorio.cleaned_data
            contacto = data['contacto']
            descripcion = data['descripcion']
            Nota(contacto=contacto, descripcion=descripcion, clasificacion=clasificacion).save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formRecordatorio.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formRecordatorio = RecordatorioForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formRecordatorio':formRecordatorio, 'no_es_vendedor':es_vendedor}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contactos/registrar_recordatorio.html', forms)

def demo_piechart(request):
    claand = Empresa.objects.get(nombre="Claand")
    contactos_claand = Contacto.objects.filter(empresa=claand)
    cotizaciones = Cotizacion.objects.filter(contacto=contactos_claand)
    xdata = list()
    ydata = list()
    for cotizacion in cotizaciones:
        xdata.append(time.mktime(cotizacion.fecha_creacion.timetuple()) * 1000)
        ydata.append(cotizacion.monto)

    # start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    # nb_element = 150
    # xdata = range(nb_element)
    # xdata = list(map(lambda x: start_time + x * 1000000000, xdata))
    # ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    # ydata2 = list(map(lambda x: x * 2, ydata))

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
        'color': '#a4c639'
    }
    # extra_serie2 = {
    #     "tooltip": {"y_start": "", "y_end": " cal"},
    #     "date_format": tooltip_date,
    #     'color': '#FF8aF8'
    # }
    chartdata = {'x': xdata,
                 'name1': 'Monto', 'y1': ydata, 'extra1': extra_serie1}

    charttype = "lineChart"
    chartcontainer = 'linechart_container'  # container name
    data = {
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
    return render_to_response('contactos/linechart.html', data)


