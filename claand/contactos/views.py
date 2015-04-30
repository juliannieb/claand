import time
import os
import logging
import httplib2

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from oauth2client.django_orm import Storage
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets

from claand import settings
from contactos.models import CredentialsModel
from contactos.models import Contacto, Pertenece, NumeroTelefonico, Calificacion, Atiende, Recordatorio, Nota, Llamada
from principal.models import Vendedor
from cotizaciones.models import Cotizacion, Venta
from empresas.models import Empresa
from contactos.models import Llamada

from contactos.forms import ContactoForm, LlamadaForm, NotaForm, RecordatorioForm, AtiendeForm
from empresas.forms import NumeroTelefonicoForm, RedSocialForm

def no_es_vendedor(user):
    """Funcion para el decorador user_passes_test
    """
    return not user.groups.filter(name='vendedor').exists()


CLIENT_SECRETS = os.path.join(os.path.dirname(__file__),  'client_secret.json')
FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/calendar',
    redirect_uri='http://localhost:8000/oauth2callback')

@login_required
def auth_return(request):
    ans = xsrfutil.validate_token(settings.SECRET_KEY, str(request.REQUEST['state']), request.user)
    if not ans:
        return HttpResponseBadRequest()
    credential = FLOW.step2_exchange(request.REQUEST)
    storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    storage.put(credential)
    return HttpResponseRedirect(reverse('contactos:registrar_recordatorio'))

@login_required
def consultar_contactos(request):
    """ Vista para mostrar toda la lista de contactos correspondiente
    al usuario que está loggeado.
    """
    current_user = request.user
    es_vendedor = no_es_vendedor(request.user)
    if no_es_vendedor(current_user):
        contactos_list = Contacto.objects.all()
    else:
        current_vendedor = Vendedor.objects.get(user=current_user)
        todos_los_contactos = Contacto.objects.all()
        contactos_list = []
        for contacto in todos_los_contactos:
            if contacto.atiende_set.all():
                if contacto.atiende_set.all()[len(contacto.atiende_set.all()) - 1].vendedor == current_vendedor:
                    contactos_list.append(contacto)
    context = {}
    context['contactos_list'] = contactos_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'contactos/contactos.html', context)

@login_required
def contacto(request, contacto_nombre_slug):
    """ Vista para mostrar todo el detalle de un contacto en particular.
    """
    contacto = Contacto.objects.get(slug=contacto_nombre_slug)
    pertenece = Pertenece.objects.get(contacto=contacto)
    numeros_list = contacto.numerotelefonico_set.all()
    calificacion = Calificacion.objects.get(contacto=contacto)
    cotizaciones_list = Cotizacion.objects.filter(contacto=contacto)
    ventas_list = Venta.objects.filter(cotizacion=cotizaciones_list)
    llamadas_list = Llamada.objects.all()
    es_vendedor = no_es_vendedor(request.user)
    notas_list = Nota.objects.filter(contacto=contacto)
    recordatorios_list = Recordatorio.objects.filter(contacto=contacto)
    context = {}
    context['contacto'] = contacto
    context['pertenece'] = pertenece
    context['numeros_list'] = numeros_list
    context['calificacion'] = calificacion
    context['cotizaciones_list'] = cotizaciones_list
    context['llamadas_list'] = llamadas_list
    context['no_es_vendedor'] = es_vendedor
    context['ventas_list'] = ventas_list
    context['notas_list'] = notas_list
    context['recordatorios_list'] = recordatorios_list
    return render(request, 'contactos/contacto.html', context)

@login_required
def registrar_contactos(request):
    """ En esta vista se presentan las alternativas entre registrar un contacto
    o una empresa
    """
    es_vendedor = no_es_vendedor(request.user)
    context = {}
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'contactos/registrar_contactos.html', context)

@login_required
def registrar_contacto(request):
    """ En esta vista se maneja el registro y validación de un contacto, dependiendo
    si la solicitud es POST o GET.
    """
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
    """ En esta vista, un vendedor registra una llamada y se valida la entrada de la misma.
    """
    current_user = request.user
    current_vendedor = Vendedor.objects.get(user=current_user)
    todos_los_contactos = Contacto.objects.all()
    contactos_list = []
    for contacto in todos_los_contactos:
        if contacto.atiende_set.all():
            if contacto.atiende_set.all()[len(contacto.atiende_set.all()) - 1].vendedor == current_vendedor:
                contactos_list.append(contacto.pk)
    if request.method == 'POST':
        formLlamada = LlamadaForm(request.POST)
        formLlamada.fields["contacto"].queryset = Contacto.objects.filter(pk__in=contactos_list)
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
            return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formLlamada.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formLlamada = LlamadaForm()
        formLlamada.fields["contacto"].queryset = Contacto.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formLlamada':formLlamada, 'no_es_vendedor':es_vendedor}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contactos/registrar_llamada.html', forms)

@login_required
@user_passes_test(no_es_vendedor)
def consultar_notas(request):
    """ En esta vista se muestran todas las notas del director 
    """
    notas_list = Nota.objects.all()
    es_vendedor = no_es_vendedor(request.user)
    context = {}
    context['notas_list'] = notas_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'contactos/notas.html', context)

@login_required
@user_passes_test(no_es_vendedor)
def nota(request, nota_id):
    """ En esta vista se muestra el detalle de una nota en particular.
    """
    nota = Nota.objects.get(id=nota_id)
    context = {}
    es_vendedor = no_es_vendedor(request.user)
    context['no_es_vendedor'] = es_vendedor
    context['nota'] = nota
    return render(request, "contactos/nota.html", context)

@login_required
@user_passes_test(no_es_vendedor)
def registrar_nota(request):
    """ En esta vista, se maneja el registro y validación de una nota dependiendo
    del tipo de solicitud.
    """
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
            clasificacion = data['clasificacion']
            Nota(contacto=contacto, descripcion=descripcion, clasificacion=clasificacion).save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})
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
    """ En esta vista se muestran todos los recordatorios del director
    """
    recordatorios_list = Recordatorio.objects.all()
    es_vendedor = no_es_vendedor(request.user)
    context = {}
    context['recordatorios_list'] = recordatorios_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'contactos/recordatorios.html', context)

@login_required
@user_passes_test(no_es_vendedor)
def recordatorio(request, recordatorio_id):
    """ En esta vista se muestra el detalle de un recordatorio
    """
    recordatorio = Recordatorio.objects.get(id=recordatorio_id)
    es_vendedor = no_es_vendedor(request.user)
    context = {}
    context['no_es_vendedor'] = es_vendedor
    context['recordatorio'] = recordatorio
    return render(request, "contactos/recordatorio.html", context)

# @login_required
# @user_passes_test(no_es_vendedor)
# def registrar_recordatorio(request):
#     """ En esta vista se registra y valida un nuevo recordatorio
#     """
#     storage = Storage(CredentialsModel, 'id', request.user, 'credential')
#     credential = storage.get()
#     if credential is None or credential.invalid == True:
#         FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY, request.user)
#         authorize_url = FLOW.step1_get_authorize_url()
#         return HttpResponseRedirect(authorize_url)
#     else:
#         http = httplib2.Http()
#         http = credential.authorize(http)
#         service = build("calendar", "v3", http=http)
#         formRecordatorio = RecordatorioForm()
#         es_vendedor = no_es_vendedor(request.user)
#         forms = {'formRecordatorio':formRecordatorio, 'no_es_vendedor':es_vendedor}
#     return render(request, 'contactos/registrar_recordatorio.html', forms)

@login_required
@user_passes_test(no_es_vendedor)
def registrar_recordatorio(request):
    """ En esta vista se registra y valida un nuevo recordatorio
    """
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
            urgencia = data['urgencia']
            fecha = data['fecha']
            Recordatorio(contacto=contacto, descripcion=descripcion, urgencia=urgencia, \
                fecha=fecha).save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})
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


@login_required
def search_contactos(request):
    """ Función para atender la petición GET AJAX para filtrar los contactos en la Vista
    contactos
    """
    if request.is_ajax() and request.method == 'GET':
        current_user = request.user
        es_vendedor = no_es_vendedor(request.user)
        if no_es_vendedor(current_user):
            contactos_list = Contacto.objects.all()
        else:
            current_vendedor = Vendedor.objects.get(user=current_user)
            contactos_list = Contacto.objects.filter(vendedor=current_vendedor)
        texto = request.GET['texto']
        contactos_list = contactos_list.filter(Q(nombre__icontains=texto) | \
            Q(apellido__icontains=texto) | Q(correo_electronico__icontains=texto))
    return render_to_response('contactos/search_contactos.html', {'contactos_list': contactos_list, \
        'no_es_vendedor':es_vendedor})

@login_required
@user_passes_test(no_es_vendedor)
def asignar_vendedor(request, contacto_id):
    """ En esta vista se asigna la atención de un vendedor a un contacto
    """
    contacto = Contacto.objects.get(id=contacto_id)
    if request.method == 'POST':
        formAtiende = AtiendeForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formAtiende':formAtiende, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formAtiende.is_valid():
            # Save the new category to the database.
            data = formAtiende.cleaned_data
            vendedor = data['vendedor']
            Atiende(contacto=contacto, vendedor=vendedor).save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formAtiende.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formAtiende = AtiendeForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formAtiende':formAtiende, 'no_es_vendedor':es_vendedor, \
        'contacto':contacto, }

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contactos/asignar_vendedor.html', forms)

@login_required
def eliminar_contacto(request, id_contacto):
    contacto = Contacto.objects.get(pk=id_contacto)
    contacto.is_active = False
    contacto.save()
    cotizaciones_list = Cotizacion.objects.filter(contacto=contacto)
    for cotizacion in cotizaciones_list:
        cotizacion.is_active = False
        try:
            venta = Venta.objects.get(cotizacion=cotizacion)
        except:
            venta = None
        if venta:
            venta.is_active = False
            venta.save()
        cotizacion.save()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})

@login_required
@user_passes_test(no_es_vendedor)
def eliminar_nota(request, id_nota):
    nota = Nota.objects.get(pk=id_nota)
    nota.is_active = False
    nota.save()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})

@login_required
@user_passes_test(no_es_vendedor)
def eliminar_recordatorio(request, id_recordatorio):
    recordatorio = Recordatorio.objects.get(pk=id_recordatorio)
    recordatorio.is_active = False
    recordatorio.save()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})