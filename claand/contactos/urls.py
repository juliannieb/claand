from django.conf.urls import url, patterns
from contactos import views

urlpatterns = patterns('',
        url(r'^registrar-contactos/', views.registrar_contactos, name='registrar_contactos'),
        url(r'^registrar-llamada/', views.registrar_llamada, name='registrar_llamada'),
        url(r'^registrar-contacto/', views.registrar_contacto, name='registrar_contacto'),

        url(r'^consultar-contactos/', views.consultar_contactos, name='consultar_contactos'),
        url(r'^consultar-contactos/(?<contacto_nombre_slug>)', views.consultar_contactos, name='consultar_contactos_slug'),

        url(r'^notas/', views.notas, name='notas'),
        url(r'^notas/(?<nota_id>)', views.notas_nota_id, name='notas_nota_id'),
        url(r'^registrar-nota/', views.registrar_nota, name='registrar_nota'),

        url(r'^recordatorios/', views.recordatorios, name='recordatorios'),
        url(r'^recordatorios/(?<recordatorio_id>)', views.recordatorios_recordatorio_id, name='recordatorios_recordatorio_id'),
        url(r'^registrar-recordatorio/', views.registrar_recordatorio, name='registrar_recordatorio'),

		)