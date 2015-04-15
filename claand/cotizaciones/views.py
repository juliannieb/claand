from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cotizaciones.models import Cotizacion, Venta
from principal.models import Vendedor
from cotizaciones.forms import Contacto, CotizacionForm

@login_required
def consultar_cotizaciones(request):
    """ mostrar todas las cotizaciones """
    cotizaciones_list = Cotizacion.objects.all()
    return render(request, 'cotizaciones/cotizaciones.html', {'cotizaciones_list': cotizaciones_list})

@login_required
def cotizacion(request, id_cotizacion):
    """ mostrar detalle de una cotizacion """
    return render(request, "cotizaciones/cotizacion.html", {})

@login_required
def consultar_ventas(request):
    """ mostrar todas las ventas """
    return render(request, 'cotizaciones/ventas.html', {})

@login_required
def venta(request, id_venta):
    """ mostrar detalle de una venta """
    return HttpResponse("venta detalle")

@login_required
def registrar(request):
    """ registrar cotizacion """
    current_user = request.user
    current_vendedor = Vendedor.objects.get(user=current_user)
    contactos_list = Contacto.objects.filter(vendedor=current_vendedor)
    if request.method == 'POST':
        formCotizacion = CotizacionForm(request.POST)
        formCotizacion.fields["contacto"].queryset = contactos_list
        forms = {'formCotizacion':formCotizacion}

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
            return render(request, 'principal/index_vendedor.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formCotizacion.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formCotizacion = CotizacionForm()
        formCotizacion.fields["contacto"].queryset = contactos_list
        forms = {'formCotizacion':formCotizacion}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'cotizaciones/registrar_cotizacion.html', forms)


""" Falta todas las relacionadas con pago """
