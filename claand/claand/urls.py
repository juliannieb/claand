from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url='/principal/login/')),
    url(r'^principal/', include('principal.urls', namespace="principal")),
    url(r'^empresas/', include('empresas.urls', namespace="empresas")),
    url(r'^cotizaciones/', include('cotizaciones.urls', namespace="cotizaciones")),
    url(r'^contactos/', include('contactos.urls', namespace="contactos")),
    url(r'^oauth2callback', 'contactos.views.auth_return'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
