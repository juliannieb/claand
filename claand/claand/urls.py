from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^principal/', include('principal.urls', namespace="principal")),
    url(r'^empresas/', include('empresas.urls', namespace="empresas")),
    url(r'^cotizaciones/', include('cotizaciones.urls', namespace="cotizaciones")),
    url(r'^contactos/', include('contactos.urls', namespace="contactos")),
    url(r'^admin/', include(admin.site.urls)),
)
