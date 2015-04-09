from django.conf.urls import url, patterns
from cotizaciones import views

urlpatterns = patterns('',
        url(r'^cotizaciones/$', views.consultar_cotizaciones, name='consultar_cotizaciones'),
       	url(r'^cotizaciones/(?P<id_cotizacion>[\w\-]+)', views.cotizacion, name='cotizacion'),
       	url(r'^ventas/$', views.consultar_ventas, name='consultar_ventas'),
       	url(r'^ventas/(?P<id_venta>[\w\-]+)', views.venta, name='venta'),
       	url(r'^registrar/$', views.registrar, name='registrar_cotizacion'),
		)