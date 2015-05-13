from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import date
from django.forms.util import ErrorList

from cotizaciones.models import Cotizacion, Venta, Pago
from principal.models import Vendedor
from contactos.models import Pertenece

from cotizaciones.forms import Contacto, CotizacionForm, VentaForm, PagoForm

def no_es_vendedor(user):
    """ Funcion para el decorador user_passes_test
    """
    return not user.groups.filter(name='vendedor').exists()

def obtener_contactos_list(vendedor):
    todos_los_contactos = Contacto.objects.all()
    contactos_list = []
    for contacto in todos_los_contactos:
        atiende_set = contacto.atiende_set.all()
        if atiende_set:
            ultimo_atiende = atiende_set[len(atiende_set) - 1]
            if ultimo_atiende.vendedor == vendedor:
                if contacto.is_active:
                    contactos_list.append(contacto)
    return contactos_list

def obtener_cotizaciones_list(contactos_list):
    todas_las_cotizaciones = Cotizacion.objects.all()
    cotizaciones_list = []
    for cotizacion in todas_las_cotizaciones:
        for contacto in contactos_list:
            atiende_set = contacto.atiende_set.all()
            if atiende_set:
                ultimo_atiende = atiende_set[len(atiende_set) - 1]
                if cotizacion.contacto == contacto and cotizacion.fecha_creacion >= ultimo_atiende.fecha:
                    if cotizacion.is_active:
                        cotizaciones_list.append(cotizacion)
    return cotizaciones_list

def obtener_ventas_list(cotizaciones_list):
    todas_las_ventas = Venta.objects.all()
    ventas_list = []
    for venta in todas_las_ventas:
        for cotizacion in cotizaciones_list:
            if venta.cotizacion == cotizacion:
                if venta.is_active:
                    ventas_list.append(venta)
    return ventas_list

def obtener_contactos_ids(contactos_list):
    contactos_ids = []
    for contacto in contactos_list:
        contactos_ids.append(contacto.id)
    return contactos_ids

@login_required
def consultar_cotizaciones(request):
    """ Vista para mostrar todas las cotizaciones de un usuario.
    """
    current_user = request.user
    if no_es_vendedor(current_user):
        cotizaciones_list = Cotizacion.objects.all()
    else:
        current_vendedor = Vendedor.objects.get(user=current_user)
        todos_los_contactos = Contacto.objects.all()
        contactos_list = obtener_contactos_list(current_vendedor)
        cotizaciones_list = obtener_cotizaciones_list(contactos_list)

    es_vendedor = no_es_vendedor(request.user)

    context = {}
    context['cotizaciones_list'] = cotizaciones_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'cotizaciones/cotizaciones.html', context)

@login_required
def cotizacion(request, id_cotizacion):
    """ Vista para mostrar el detalle de una cotizacion.
    """
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    contacto = cotizacion.contacto
    pertenece = Pertenece.objects.get(contacto=contacto)
    es_vendedor = no_es_vendedor(request.user)

    context = {}
    context['cotizacion'] = cotizacion
    context['contacto'] = contacto
    context['pertenece'] = pertenece
    context['no_es_vendedor'] = es_vendedor
    return render(request, "cotizaciones/cotizacion.html", context)

@login_required
def consultar_ventas(request):
    """ Vista para mostrar todas las ventas asociadas a un usuario.
    En el caso del director, se muestran todas las ventas globales.
    """
    current_user = request.user
    if no_es_vendedor(current_user):
        ventas_list = Venta.objects.all()
    else:
        current_vendedor = Vendedor.objects.get(user=current_user)
        todos_los_contactos = Contacto.objects.all()
        contactos_list = obtener_contactos_list(current_vendedor)
        cotizaciones_list = obtener_cotizaciones_list(contactos_list)
        ventas_list = obtener_ventas_list(cotizaciones_list)
    es_vendedor = no_es_vendedor(request.user)
    context = {}
    context['ventas_list'] = ventas_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'cotizaciones/ventas.html', context)

@login_required
def venta(request, id_venta):
    """ Vista para mostrar el detalle de una venta en particular.
    """
    venta = Venta.objects.get(id=id_venta)
    id_cotizacion = venta.cotizacion.id
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    contacto = cotizacion.contacto
    pertenece = Pertenece.objects.get(contacto=contacto)
    es_vendedor = no_es_vendedor(request.user)
    pagos_list = Pago.objects.filter(venta=venta)
    context = {}
    context['venta'] = venta
    context['cotizacion'] = cotizacion
    context['contacto'] = contacto
    context['pertenece'] = pertenece
    context['no_es_vendedor'] = es_vendedor
    context['pagos_list'] = pagos_list
    return render(request, 'cotizaciones/venta.html', context)


@login_required
def registrar(request):
    """ Vista para registrar una cotizacion.
    """
    current_user = request.user
    current_vendedor = Vendedor.objects.get(user=current_user)
    contactos_list = obtener_contactos_list(current_vendedor)
    contactos_list = obtener_contactos_ids(contactos_list)
    if request.method == 'POST':
        formCotizacion = CotizacionForm(request.POST)
        formCotizacion.fields["contacto"].queryset = Contacto.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor}
        if formCotizacion.is_valid():
            data = formCotizacion.cleaned_data
            contacto = data['contacto']
            monto = data['monto']
            descripcion = data['descripcion']
            Cotizacion(contacto=contacto, monto=monto, descripcion=descripcion).save()
            return render(request, 'principal/exito.html')
    else:
        formCotizacion = CotizacionForm()
        formCotizacion.fields["contacto"].queryset = Contacto.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor}
    return render(request, 'cotizaciones/registrar_cotizacion.html', forms)

@login_required
def registrar_venta(request, id_cotizacion):
    """ Vista para registrar una venta.
    En esta misma se cambia el status de una cotizacion a no pendiente.
    """
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    current_user = request.user
    if request.method == 'POST':
        formVenta = VentaForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'cotizacion' : cotizacion, 'no_es_vendedor':es_vendedor}
        if formVenta.is_valid():
            data = formVenta.cleaned_data
            monto_total = data['monto_total']
            cotizacion.is_pendiente = False
            cotizacion.save()
            contacto = cotizacion.contacto
            if contacto.is_cliente == False:
                contacto.is_cliente = True
                contacto.save()
            Venta(monto_total=monto_total, cotizacion=cotizacion).save()
            return render(request, 'principal/exito.html')
    else:
        formVenta = VentaForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'no_es_vendedor':es_vendedor, 'cotizacion' : cotizacion}
    return render(request, 'cotizaciones/registrar_venta.html', forms)


@login_required
def registrar_pago(request, id_venta):
    venta = Venta.objects.get(id=id_venta)
    current_user = request.user
    if request.method == 'POST':
        formPago = PagoForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formPago':formPago, 'venta' : venta, 'no_es_vendedor':es_vendedor}
        if formPago.is_valid():
            data = formPago.cleaned_data
            monto = data['monto']
            if venta.monto_acumulado + monto > venta.monto_total:
                formPago.errors['monto'] = ErrorList(['El monto acumulado no puede ser mayor al monto total de la venta.'])
                forms = {'formPago':formPago, 'venta' : venta, 'no_es_vendedor':es_vendedor}
                return render(request, 'cotizaciones/registrar_pago.html', forms)
            else:
                venta.monto_acumulado += monto
                if venta.monto_acumulado >= venta.monto_total:
                    venta.is_completada = True
                venta.save()
                Pago(monto=monto, venta=venta).save()
                return render(request, 'principal/exito.html')
    else:
        formPago = PagoForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formPago':formPago, 'no_es_vendedor':es_vendedor, 'venta' : venta}
    return render(request, 'cotizaciones/registrar_pago.html', forms)

@login_required
def eliminar_cotizacion(request, id_cotizacion):
    cotizacion = Cotizacion.objects.get(pk=id_cotizacion)
    cotizacion.is_active = False
    cotizacion.save()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})

@login_required
def eliminar_venta(request, id_venta):
    venta = Venta.objects.get(pk=id_venta)
    venta.is_active = False
    venta.save()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})

@login_required
def editar_cotizacion(request, id_cotizacion):
    """ Vista para editar una cotizacion.
    """
    cotizacion = Cotizacion.objects.get(pk=id_cotizacion)
    current_user = request.user
    current_vendedor = Vendedor.objects.get(user=current_user)
    contactos_list = obtener_contactos_list(current_vendedor)
    contactos_list = obtener_contactos_ids(contactos_list)
    if request.method == 'POST':
        formCotizacion = CotizacionForm(request.POST)
        formCotizacion.fields["contacto"].queryset = Contacto.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor, 'cotizacion':cotizacion}
        if formCotizacion.is_valid():
            data = formCotizacion.cleaned_data
            contacto = data['contacto']
            monto = data['monto']
            descripcion = data['descripcion']
            cotizacion.contacto = contacto
            cotizacion.monto = monto
            cotizacion.descripcion = descripcion
            cotizacion.save()
            return render(request, 'principal/exito.html')
    else:
        formCotizacion = CotizacionForm(instance=cotizacion)
        formCotizacion.fields["contacto"].queryset = Contacto.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor, 'cotizacion':cotizacion}
    return render(request, 'cotizaciones/editar_cotizacion.html', forms)

@login_required
def editar_venta(request, id_venta):
    """ Vista para editar una cotizacion.
    """
    venta = Venta.objects.get(pk=id_venta)
    current_user = request.user
    if request.method == 'POST':
        formVenta = VentaForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'no_es_vendedor':es_vendedor, 'venta':venta}
        if formVenta.is_valid():
            data = formVenta.cleaned_data
            monto_total = data['monto_total']
            venta.monto_total = monto_total
            venta.save()
            return render(request, 'principal/exito.html')
    else:
        formVenta = VentaForm(instance=venta)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'no_es_vendedor':es_vendedor, 'venta':venta}
    return render(request, 'cotizaciones/editar_venta.html', forms)