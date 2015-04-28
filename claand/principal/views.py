from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.contrib.auth.models import User, Group

from principal.models import Vendedor
from contactos.models import Contacto, Llamada
from cotizaciones.models import Cotizacion, Venta

from principal.forms import VendedorForm

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
    context['vendedores_list'] = vendedores_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'principal/consultar_vendedores.html', context)

def vendedor(request, id_vendedor):
    """ Vista para mostrar el detalle de un contacto en particular
    """
    es_vendedor = no_es_vendedor(request.user)
    vendedor = Vendedor.objects.get(id=id_vendedor)
    contactos_list = Contacto.objects.filter(vendedor=vendedor)
    cotizaciones_list = Cotizacion.objects.filter(contacto=contactos_list)
    ventas_list = Venta.objects.filter(cotizacion=cotizaciones_list)
    llamadas_list = Llamada.objects.filter(contacto=contactos_list)
    context = {}
    context['vendedor'] = vendedor
    context['contactos_list'] = contactos_list
    context['cotizaciones_list'] = cotizaciones_list
    context['ventas_list'] = ventas_list
    context['llamadas_list'] = llamadas_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'principal/vendedor.html', context)

def registrar_vendedor(request):
    """ Vista para registrar un nuevo vendedor en el sistema """
    current_user = request.user
    if request.method == 'POST':
        formVendedor = VendedorForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVendedor':formVendedor, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formVendedor.is_valid():
            # Save the new category to the database.
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
            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formVendedor.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formVendedor = VendedorForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVendedor':formVendedor, 'no_es_vendedor':es_vendedor, }

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'principal/registrar_vendedor.html', forms)