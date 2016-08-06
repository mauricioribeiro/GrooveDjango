from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artistas/$', views.artistas_listar, name='artistas_listar'),
    url(r'^artistas/(?P<nome_artista>[a-zA-Z0-9 ]+)$', views.artistas_detalhar, name='artistas_detalhar'),
]