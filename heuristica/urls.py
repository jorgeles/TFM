from django.conf.urls import patterns, url

from heuristica import views

urlpatterns = patterns('',
											 url(r'^$', views.index, name='index'),
											 url(r'^registro', views.registro, name='registro'),
											 url(r'^logear', views.logear, name='logear'),
											 url(r'^facetas', views.facetas, name='facetas'),
											 url(r'^perfiles', views.perfiles, name='perfiles'),
											 url(r'^guardarPerfil', views.guardarPerfil, name='guardarPerfil'),
											 url(r'^cargarPerfil', views.cargarPerfil, name='cargarPerfil'),
											 url(r'^nuevoPerfil', views.nuevoPerfil, name='nuevoPerfil'),
											 url(r'^eliminarPerfil', views.eliminarPerfil, name='eliminarPerfil'),
											 url(r'^juegos', views.juegos, name='juegos'),
											 url(r'^nuevoJuego', views.nuevoJuego, name='nuevoJuego'),
											 url(r'^cargarJuego', views.cargarJuego, name='cargarJuego'),
											 url(r'^eliminarJuego', views.eliminarJuego, name='eliminarJuego'),
											 url(r'^guardarJuego', views.guardarJuego, name='guardarJuego'),
											 url(r'^mistest', views.mistest, name='mistest'),
											 url(r'^asignados', views.asignados, name='asignados'),
											 url(r'^guardar_Heuristica', views.guardar_Heuristica, name='guardar_Heuristica'),
											 url(r'^cargar_dato', views.cargar_dato, name='cargar_dato'),
											 url(r'^eliminar_dato', views.eliminar_dato, name='eliminar_dato'),
											 url(r'^cargarJugabilidad', views.cargarJugabilidad, name='cargarJugabilidad'),
											 url(r'^cargarTest', views.cargarTest, name='cargarTest'),
											 url(r'^nuevoTest', views.nuevoTest, name='nuevoTest'),
											 url(r'^cargarTablas', views.cargarTablas, name='cargarTablas'),
											 url(r'^guardarTest', views.guardarTest, name='guardarTest'),
											 url(r'^eliminarTest', views.eliminarTest, name='eliminarTest'),
											 url(r'^cargarUsuarios', views.cargarUsuarios, name='cargarUsuarios'),
											 url(r'^UsuarioExiste', views.UsuarioExiste, name='UsuarioExiste'),
											 url(r'^guardarIndividual', views.guardarEnviarIndividual, name='guardarIndividual'),
											 url(r'^guardarEnviar', views.guardarEnviar, name='guardarEnviar'),
											 url(r'^cargarAsignado', views.cargarAsignado, name='cargarAsignado'),
											 url(r'^eliminarAsignado', views.eliminarAsignado, name='eliminarAsignado'),
											 url(r'^cargarPreguntas', views.cargarPreguntas, name='cargarPreguntas'),
											 url(r'^guardarResultado', views.guardarResultado, name='guardarResultado'),
											 url(r'^enviarResultado', views.enviarResultado, name='enviarResultado'),
											 url(r'^cargarValoracion', views.cargarValoracion, name='cargarValoracion'),
											 url(r'^guardarComentarios', views.guardarComentarios, name='guardarComentarios'),

											 # Url para borrar mas adelante
											 url(r'^google', views.google, name='google'),
											 url(r'^mongo', views.mongo, name='mongo'),
											 url(r'^prueba', views.prueba, name='prueba'),
											 
											 

											 )