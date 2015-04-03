from django.conf.urls import url, patterns
from empresas import views

urlpatterns = patterns('',
        url(r'^registrar-empresa', views.registrar_empresa, name='registrar_empresa'),
		)


