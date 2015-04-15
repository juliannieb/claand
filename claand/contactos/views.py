from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from contactos.models import Contacto, Pertenece, NumeroTelefonico, Calificacion, Atiende, Recordatorio, Nota
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
	if no_es_vendedor(current_user):
		contactos_list = Contacto.objects.all()
	else:
		current_vendedor = Vendedor.objects.get(user=current_user)
		contactos_list = Contacto.objects.filter(vendedor=current_vendedor)
	return render(request, 'contactos/contactos.html', {'contactos_list': contactos_list})

@login_required
def contacto(request, contacto_nombre_slug):
	""" mostrar detalle de un contacto """
	contacto = Contacto.objects.get(slug=contacto_nombre_slug)
	pertenece = Pertenece.objects.get(contacto=contacto)
	numeros_list = contacto.numerotelefonico_set.all()
	calificacion = Calificacion.objects.get(contacto=contacto)
	cotizaciones_list = Cotizacion.objects.filter(contacto=contacto)
	return render(request, 'contactos/contacto.html', {'contacto': contacto, 'pertenece': pertenece, 'numeros_list': numeros_list, 'calificacion': calificacion, 'cotizaciones_list': cotizaciones_list})

@login_required
def registrar_contactos(request):
    """ registrar un nuevo contacto """
    return render(request, 'contactos/registrar_contactos.html', {})

@login_required
def registrar_contacto(request):
    if request.method == 'POST':
        formContacto = ContactoForm(request.POST)
        formNumeroTelefonico = NumeroTelefonicoForm(request.POST)
        forms = {'formContacto':formContacto, 'formNumeroTelefonico':formNumeroTelefonico}

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
            contacto = Contacto(nombre=nombre, apellido=apellido, correo_electronico=correo_electronico, is_cliente=is_cliente)
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
            return render(request, 'principal/index_vendedor.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formContacto.errors)
            print (formNumeroTelefonico.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formContacto = ContactoForm()
        formNumeroTelefonico = NumeroTelefonicoForm()
        forms = {'formContacto':formContacto, 'formNumeroTelefonico':formNumeroTelefonico}

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
        forms = {'formLlamada':formLlamada}

        # Have we been provided with a valid form?
        if formLlamada.is_valid():
            # Save the new category to the database.
            data = formLlamada.cleaned_data
            contacto = data['contacto']
            descripcion = data['descripcion']
            Llamada(contacto=contacto, descripcion=descripcion).save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/index_vendedor.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formLlamada.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formLlamada = LlamadaForm()
        formLlamada.fields["contacto"].queryset = contactos_list
        forms = {'formLlamada':formLlamada}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contactos/registrar_llamada.html', forms)

@login_required
@user_passes_test(no_es_vendedor)
def consultar_notas(request):
    """ mostrar todas las notas """
    return render(request, 'contactos/notas.html', {})

@login_required
@user_passes_test(no_es_vendedor)
def nota(request, nota_id):
    """ mostrar detalle de una nota """
    return HttpResponse("detalle nota")

@login_required
@user_passes_test(no_es_vendedor)
def registrar_nota(request):
    """ registrar una nueva nota """
    if request.method == 'POST':
        formNota = NotaForm(request.POST)
        forms = {'formNota':formNota}

        # Have we been provided with a valid form?
        if formNota.is_valid():
            # Save the new category to the database.
            data = formNota.cleaned_data
            contacto = data['contacto']
            descripcion = data['descripcion']
            Nota(contacto=contacto, descripcion=descripcion, clasificacion=clasificacion).save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/index_vendedor.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formNota.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formNota = NotaForm()
        forms = {'formNota':formNota}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contactos/registrar_nota.html', forms)

@login_required
@user_passes_test(no_es_vendedor)
def consultar_recordatorios(request):
	""" mostrar todos los recordatorios """
	recordatorios_list = Recordatorio.objects.all()
	return render(request, 'contactos/recordatorios.html', {'recordatorios_list': recordatorios_list})

@login_required
@user_passes_test(no_es_vendedor)
def recordatorio(request, recordatorio_id):
    """ mostrar detalle de un recordatorio """
    return HttpResponse("detalle recordatorio")

@login_required
@user_passes_test(no_es_vendedor)
def registrar_recordatorio(request):
    """ registrar un nuevo recordatorio """
    if request.method == 'POST':
        formRecordatorio = RecordatorioForm(request.POST)
        forms = {'formRecordatorio':formRecordatorio}

        # Have we been provided with a valid form?
        if formRecordatorio.is_valid():
            # Save the new category to the database.
            data = formRecordatorio.cleaned_data
            contacto = data['contacto']
            descripcion = data['descripcion']
            Nota(contacto=contacto, descripcion=descripcion, clasificacion=clasificacion).save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/index_vendedor.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formRecordatorio.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formRecordatorio = RecordatorioForm()
        forms = {'formRecordatorio':formRecordatorio}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contactos/registrar_recordatorio.html', forms)

