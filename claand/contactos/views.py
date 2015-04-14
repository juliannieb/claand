from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from contactos.models import Contacto, Pertenece, NumeroTelefonico, Calificacion, Atiende
from principal.models import Vendedor
from empresas.models import Empresa

from contactos.forms import ContactoForm
from empresas.forms import NumeroTelefonicoForm, RedSocialForm

@login_required
def consultar_contactos(request):
	#Falta validar si el current_user es el Director, para mostrar todos los contactos
	current_user = request.user
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
    return render(request, 'contactos/contacto.html', {'contacto': contacto, 'pertenece': pertenece, 'numeros_list': numeros_list, 'calificacion': calificacion})

@login_required
def registrar_contactos(request):
    """ registrar un nuevo contacto """
    return render(request, 'contactos/registrar_contactos.html', {})

@login_required
def registrar_contacto(request):
    if request.method == 'POST':
        formContacto = ContactoForm(request.POST)
        formNumeroTelefonico = NumeroTelefonicoForm(request.POST)

        # Have we been provided with a valid form?
        if formContacto.is_valid():
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

            if formNumeroTelefonico.has_changed() and formNumeroTelefonico.is_valid():
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
        context = {'formContacto':formContacto, 'formNumeroTelefonico':formNumeroTelefonico}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contactos/registrar_contacto.html', context)

@login_required
def registrar_llamada(request):
    """ registrar una llamada """
    return render(request, 'contactos/registrar_llamada.html', {})

@login_required
def consultar_notas(request):
    """ mostrar todas las notas """
    return render(request, 'contactos/notas.html', {})

@login_required
def nota(request, nota_id):
    """ mostrar detalle de una nota """
    return HttpResponse("detalle nota")

@login_required
def registrar_nota(request):
    """ registrar una nueva nota """
    return HttpResponse("registrar una nota")

@login_required
def consultar_recordatorios(request):
    """ mostrar todos los recordatorios """
    return render('contactos/recordatorios.html')

@login_required
def recordatorio(request, recordatorio_id):
    """ mostrar detalle de un recordatorio """
    return HttpResponse("detalle recordatorio")

@login_required
def registrar_recordatorio(request):
    """ registrar un nuevo recordatorio """
    return HttpResponse("registrar un recordatorio")

