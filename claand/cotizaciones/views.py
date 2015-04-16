from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from cotizaciones.models import Cotizacion, Venta, Pago
from principal.models import Vendedor
from contactos.models import Pertenece

from cotizaciones.forms import Contacto, CotizacionForm, VentaForm, PagoForm

def no_es_vendedor(user):
    """Funcion para el decorador user_passes_test
    """
    return not user.groups.filter(name='vendedor').exists()

@login_required
def consultar_cotizaciones(request):
    """ mostrar todas las cotizaciones """
    current_user = request.user
    if no_es_vendedor(current_user):
        cotizaciones_list = Cotizacion.objects.all()
    else:
        current_vendedor = Vendedor.objects.get(user=current_user)
        contactos_list = Contacto.objects.filter(vendedor=current_vendedor)
        cotizaciones_list = Cotizacion.objects.filter(contacto=contactos_list)
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'cotizaciones/cotizaciones.html', {'cotizaciones_list': cotizaciones_list, \
        'no_es_vendedor':es_vendedor})

@login_required
def cotizacion(request, id_cotizacion):
    """ mostrar detalle de una cotizacion """
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    contacto = cotizacion.contacto
    pertenece = Pertenece.objects.get(contacto=contacto)
    es_vendedor = no_es_vendedor(request.user)
    return render(request, "cotizaciones/cotizacion.html", {'cotizacion': cotizacion, \
        'contacto': contacto, 'pertenece': pertenece, 'no_es_vendedor':es_vendedor})

@login_required
def consultar_ventas(request):
    """ mostrar todas las ventas """
    current_user = request.user
    if no_es_vendedor(current_user):
        ventas_list = Venta.objects.all()
    else:
        current_vendedor = Vendedor.objects.get(user=current_user)
        contactos_list = Contacto.objects.filter(vendedor=current_vendedor)
        cotizaciones_list = Cotizacion.objects.filter(contacto=contactos_list)
        ventas_list = Venta.objects.filter(cotizacion=cotizaciones_list)
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'cotizaciones/ventas.html', {'ventas_list': ventas_list, \
        'no_es_vendedor':es_vendedor})

@login_required
def venta(request, id_venta):
    """ mostrar detalle de una venta """
    venta = Venta.objects.get(id=id_venta)
    id_cotizacion = venta.cotizacion.id
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    contacto = cotizacion.contacto
    pertenece = Pertenece.objects.get(contacto=contacto)
    es_vendedor = no_es_vendedor(request.user)
    pagos_list = Pago.objects.filter(venta=venta)
    return render(request, 'cotizaciones/venta.html', {'venta':venta, 'cotizacion':cotizacion, \
        'contacto':contacto, 'pertenece':pertenece, 'pagos_list':pagos_list, 'no_es_vendedor':es_vendedor})

@login_required
def registrar(request):
    """ registrar cotizacion """
    current_user = request.user
    current_vendedor = Vendedor.objects.get(user=current_user)
    contactos_list = Contacto.objects.filter(vendedor=current_vendedor)
    if request.method == 'POST':
        formCotizacion = CotizacionForm(request.POST)
        formCotizacion.fields["contacto"].queryset = contactos_list
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formCotizacion.is_valid():
            # Save the new category to the database.
            data = formCotizacion.cleaned_data
            contacto = data['contacto']
            monto = data['monto']
            descripcion = data['descripcion']
            Cotizacion(contacto=contacto, monto=monto, descripcion=descripcion).save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formCotizacion.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formCotizacion = CotizacionForm()
        formCotizacion.fields["contacto"].queryset = contactos_list
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'cotizaciones/registrar_cotizacion.html', forms)


def registrar_venta(request, id_cotizacion):
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    current_user = request.user
    if request.method == 'POST':
        formVenta = VentaForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formVenta.is_valid():
            # Save the new category to the database.
            data = formVenta.cleaned_data
            monto_total = data['monto_total']
            cotizacion.is_pendiente = False
            cotizacion.save()
            Venta(monto_total=monto_total, cotizacion=cotizacion).save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formVenta.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formVenta = VentaForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'no_es_vendedor':es_vendedor, 'cotizacion' : cotizacion}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'cotizaciones/registrar_venta.html', forms)



def registrar_pago(request, id_venta):
    venta = Venta.objects.get(id=id_venta)
    current_user = request.user
    if request.method == 'POST':
        formPago = PagoForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formPago':formPago, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formPago.is_valid():
            # Save the new category to the database.
            data = formPago.cleaned_data
            monto = data['monto']
            venta.monto_acumulado += monto
            if venta.monto_acumulado >= venta.monto_total:
                venta.is_completada = True
            venta.save()
            Pago(monto=monto, venta=venta).save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formPago.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formPago = PagoForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formPago':formPago, 'no_es_vendedor':es_vendedor, 'venta' : venta}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'cotizaciones/registrar_pago.html', forms)
