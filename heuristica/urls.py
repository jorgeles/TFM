from django.conf.urls import patterns, url

from heuristica import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^registro', views.registro, name='registro'),
                       url(r'^logear', views.logear, name='logear'),
                       url(r'^inicio', views.inicio, name='inicio'),
                       url(r'^perfiles', views.perfiles, name='perfiles'),
                       url(r'^guardarPerfil', views.guardarPerfil, name='guardarPerfil'),
                       url(r'^cargarPerfil', views.cargarPerfil, name='cargarPerfil'),
                       url(r'^nuevoPerfil', views.nuevoPerfil, name='nuevoPerfil'),
                       
                       # Url para borrar mas adelante
                       url(r'^google', views.google, name='google'),
                       url(r'^mongo', views.mongo, name='mongo'),

                       )