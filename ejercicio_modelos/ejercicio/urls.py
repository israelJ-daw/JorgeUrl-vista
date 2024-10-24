from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ejercicio/listar', views.listar_proyectos, name='listar_proyectos')
]
