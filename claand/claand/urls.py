from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^principal/', include('principal.urls')),
	url(r'^empresas/', include('empresas.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
