from django.conf.urls import url, patterns
from principal import views
from django.conf.urls.static import static

urlpatterns = patterns('',
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^vendedor/$', views.vendedor_index, name='vendedor_index'),
        url(r'^consultar/$', views.consultar, name='consultar'),
        url(r'^director/$', views.director_index, name='director_index'),
        )


