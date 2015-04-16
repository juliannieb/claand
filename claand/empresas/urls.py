from django.conf.urls import url, patterns
from empresas import views

urlpatterns = patterns('',
        url(r'^registrar/$', views.registrar_empresa, name='registrar_empresa'),
        url(r'^consultar/$', views.consultar_empresas, name='consultar_empresas'),
        url(r'^consultar/(?P<empresa_nombre_slug>[\w\-]+)/$', views.empresa, name='empresa'),
        )


