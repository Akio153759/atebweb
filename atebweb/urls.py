from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publicacion/<int:pk>', views.post_detail, name='post_detail'),
    path('equipos', views.equipos, name='equipos'),
    path('contacto', views.contacto, name='contacto'),
    path('galeria', views.galeria, name='galeria'),
    path('torneo', views.torneo, name='torneo'),
    path('categorias/<str:nombre_categoria>', views.noticias_x_categoria, name='noticias_x_categoria'),
]