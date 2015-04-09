from django.conf.urls import url, patterns
from principal import views
from django.conf.urls.static import static

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^vendedor/$', views.vendedor_index, name='vendedor_index'),
        url(r'^consultar/$', views.consultar, name='consultar'),
        url(r'^director/$', views.director_index, name='director_index'),
		)


