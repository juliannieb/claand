from django.conf.urls import url, patterns
from contactos import views

urlpatterns = patterns('',
        url(r'^registrar-contacto/$', views.registrar_contactos, name='registrar_contactos'),
        url(r'^registrar-llamada/$', views.registrar_llamada, name='registrar_llamada'),

        url(r'^contactos/$', views.consultar_contactos, name='consultar_contactos'),
        url(r'^contactos/(?P<contacto_nombre_slug>[\w\-]+)/$', views.contacto, name='contacto'),

        url(r'^notas/$', views.consultar_notas, name='consultar_notas'),
        url(r'^notas/(?P<nota_id>[\w\-]+)/$', views.nota, name='nota'),
        url(r'^registrar-nota/$', views.registrar_nota, name='registrar_nota'),

        url(r'^recordatorios/$', views.consultar_recordatorios, name='consultar_recordatorios'),
        url(r'^recordatorios/(?P<recordatorio_id>[\w\-]+)/$', views.recordatorio, name='recordatorio'),
        url(r'^registrar-recordatorio/$', views.registrar_recordatorio, name='registrar_recordatorio'),
		)