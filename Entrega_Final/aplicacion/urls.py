from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index),
    path('nosotros/',Nosotros, name= "nosotros"),
    path('servicios/',servicios, name= "servicios"),
    path('clientes/',clientes, name= "clientes"),
    path('oficinas/',oficinas, name= "oficinas"),
    path('eventos/', eventos, name= "eventos"),
    path('acerca_de_mi/',acerca_de_mi, name= "acerca_de_mi"),
    path('serviciosForm/',serviciosForm, name= "serviciosForm"),
    path('serviciosForm2/',serviciosForm2, name= "serviciosForm2"),
    path('updateClientes/<id_clientes>/',updateClientes, name= "updateClientes"),
    path('deleteClientes/<id_clientes>/',deleteClientes, name= "deleteClientes"),
    path('createClientes/',createClientes, name= "createClientes"),
    path('login/', loginRequest, name= "login"),
    path('logout/', LogoutView.as_view(template_name = 'aplicacion/logout.html'), name = 'logout'),
    path('register/', register, name = 'register'),
    path('updateServicios/<id_servicios>/',updateServicios, name= "updateServicios"),
    path('deleteServicios/<id_servicios>/',deleteServicios, name= "deleteServicios"),
    path('createServicios/',createServicios, name= "createServicios"),
    path('editarPerfil/',editarPerfil, name= "editarPerfil"),
    path('agregarAvatar/',agregarAvatar, name= "agregarAvatar"),
    path('updateOficinas/<id_oficinas>/',updateOficinas, name= "updateOficinas"),
    path('deleteOficinas/<id_oficinas>/',deleteOficinas, name= "deleteOficinas"),
    path('createOficinas/',createOficinas, name= "createOficinas"),
    path('updateEventos/<id_eventos>/',updateEventos, name= "updateEventos"),
    path('deleteEventos/<id_eventos>/',deleteEventos, name= "deleteEventos"),
    path('createEventos/',createEventos, name= "createEventos")]